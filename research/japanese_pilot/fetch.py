import requests,bs4,pathlib,concurrent.futures,json,sys
BASE=pathlib.Path('research/japanese_pilot')
def f(z):
 name,url=z
 try:
  r=requests.get(url,verify='/etc/ssl/cert.pem',timeout=40);r.raise_for_status()
  if r.content.startswith(b'%PDF'):
   (BASE/(name+'.pdf')).write_bytes(r.content)
   from pypdf import PdfReader
   p=PdfReader(BASE/(name+'.pdf'))
   (BASE/(name+'.txt')).write_text('\n'.join('[PDF PAGE %d]\n%s'%(i+1,x.extract_text()) for i,x in enumerate(p.pages)))
   return name,len(p.pages),'PDF'
  s=bs4.BeautifulSoup(r.content,'html.parser');(BASE/(name+'.html')).write_text(r.text);(BASE/(name+'.txt')).write_text(s.get_text(' ',strip=True));links=[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]')];(BASE/(name+'_links.json')).write_text(json.dumps(links,ensure_ascii=False));return name,r.status_code,s.get_text(' ',strip=True)[:100],[(n,u) for n,u in links if any(t in u.lower() for t in ['pdf','file','download'])][:8]
 except Exception as e:return name,str(e)
for a in concurrent.futures.ThreadPoolExecutor(max_workers=6).map(f,json.loads(sys.argv[1])):print(a,flush=True)
