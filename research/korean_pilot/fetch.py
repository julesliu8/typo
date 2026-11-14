import requests,json,pathlib,concurrent.futures,sys
from bs4 import BeautifulSoup
from pypdf import PdfReader
BASE=pathlib.Path(__file__).resolve().parent

def fetch(item):
 name,url=item
 record={'name':name,'url':url,'accessed':'2026-11-13'}
 try:
  r=requests.get(url,verify='/etc/ssl/cert.pem',timeout=25)
  record.update(status=r.status_code,final_url=r.url,bytes=len(r.content))
  if r.content.startswith(b'%PDF'):
   p=BASE/(name+'.pdf');p.write_bytes(r.content)
   p.with_suffix('.txt').write_text('\n'.join('[PDF PAGE '+str(i+1)+']\n'+(pg.extract_text() or '') for i,pg in enumerate(PdfReader(p).pages)))
   record['kind']='pdf'
  else:
   s=BeautifulSoup(r.content,'html.parser');(BASE/(name+'.html')).write_bytes(r.content);(BASE/(name+'.txt')).write_text(s.get_text(' ',strip=True))
   (BASE/(name+'_links.json')).write_text(json.dumps([(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]')],ensure_ascii=False,indent=2));record['title']=s.title.get_text() if s.title else ''
 except Exception as e:record['error']=str(e)
 (BASE/(name+'_source.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
 print(record,flush=True)
 return record
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:list(p.map(fetch,json.loads(sys.argv[1])))
