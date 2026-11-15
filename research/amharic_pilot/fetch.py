import concurrent.futures,json,sys,hashlib
from pathlib import Path
from datetime import datetime,timezone
import requests
from bs4 import BeautifulSoup
BASE=Path(__file__).parent
def fetch(item):
    name,url=item
    d={'id':name,'url':url,'accessed_at':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get(url,timeout=50,verify='/etc/ssl/cert.pem',headers={'User-Agent':'Mozilla/5.0'})
        d.update(status=r.status_code,final_url=r.url,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest())
        if r.content.startswith(b'%PDF'):
            (BASE/(name+'.pdf')).write_bytes(r.content)
            from pypdf import PdfReader
            reader=PdfReader(BASE/(name+'.pdf'))
            pages=[p.extract_text() or '' for p in reader.pages]
            (BASE/(name+'_pages.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2))
            (BASE/(name+'.txt')).write_text('\n\n'.join(f'PDF PAGE {i+1}\n{t}' for i,t in enumerate(pages)))
            d.update(format='pdf',pages=len(pages))
        else:
            (BASE/(name+'.html')).write_text(r.text)
            s=BeautifulSoup(r.content,'html.parser')
            for el in s(['script','style']):el.decompose()
            (BASE/(name+'.txt')).write_text(s.get_text(' ',strip=True))
            (BASE/(name+'_links.json')).write_text(json.dumps([(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]')],ensure_ascii=False,indent=2))
            d.update(format='html',title=s.title.get_text() if s.title else '')
    except Exception as e:d['error']=str(e)
    (BASE/(name+'_source.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
    print(json.dumps(d,ensure_ascii=False),flush=True)
    return d
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(fetch,json.loads(sys.argv[1])))
