import requests,bs4,json,concurrent.futures,sys
from pathlib import Path
qs=json.loads(sys.argv[2])
def f(q):
 try:
  r=requests.get('https://www.bing.com/search',params={'q':q,'setlang':'en'},headers={'User-Agent':'Mozilla/5.0'},verify='/etc/ssl/cert.pem',timeout=35)
  s=bs4.BeautifulSoup(r.content,'html.parser');parts=s.select('li.b_algo')
  d=dict(q=q,status=r.status_code,results=[{'text':p.get_text(' ',strip=True),'links':[(a.get_text(' ',strip=True),a['href']) for a in p.select('h2 a[href]')]} for p in parts],fallback=s.get_text(' ',strip=True)[:1000] if not parts else '')
  print(json.dumps(d,ensure_ascii=False)[:18000],flush=True);return d
 except Exception as e:print(q,str(e),flush=True);return {'q':q,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rs=list(ex.map(f,qs))
Path(sys.argv[1]).write_text(json.dumps(rs,ensure_ascii=False,indent=2))
