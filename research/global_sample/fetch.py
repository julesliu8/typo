import requests,bs4,pathlib,concurrent.futures,json,sys
S=requests.Session();S.verify='/etc/ssl/cert.pem'
def fetch(pair):
 name,url=pair;p=pathlib.Path('research/global_sample')
 try:
  r=S.get(url,timeout=40);r.raise_for_status()
  if r.content.startswith(b'%PDF'):
   (p/(name+'.pdf')).write_bytes(r.content)
   from pypdf import PdfReader
   rd=PdfReader(p/(name+'.pdf'));(p/(name+'.txt')).write_text('\n'.join('[PDF PAGE %s]\n%s'%(i+1,pg.extract_text()) for i,pg in enumerate(rd.pages)))
   return name,'PDF',len(rd.pages)
  r.encoding='utf8';sp=bs4.BeautifulSoup(r.text,'html.parser');(p/(name+'.html')).write_text(r.text)
  for x in sp(['style','script','header','footer','nav']):x.decompose()
  (p/(name+'.txt')).write_text(sp.get_text(' ',strip=True))
  links=[(a.get_text(' ',strip=True),a['href']) for a in sp.select('a[href]')];(p/(name+'_links.json')).write_text(json.dumps(links,ensure_ascii=False))
  return name,r.status_code,sp.get_text(' ',strip=True)[:450],[(n,u) for n,u in links if any(t in (n+u).lower() for t in ['pdf','download','bitstream'])][:12]
 except Exception as e:return name,str(e)
if __name__=='__main__':
 for o in concurrent.futures.ThreadPoolExecutor(max_workers=5).map(fetch,json.loads(sys.argv[1])):print(o,flush=True)
