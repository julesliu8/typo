import requests,bs4,json,concurrent.futures,sys
from pathlib import Path
qs=json.loads(sys.argv[2])
def f(q):
 try:
  r=requests.get('https://search.yahoo.co.jp/search',params={'p':q,'ei':'UTF-8'},headers={'User-Agent':'Mozilla/5.0'},verify='/etc/ssl/cert.pem',timeout=30)
  s=bs4.BeautifulSoup(r.content,'html.parser')
  d=dict(q=q,status=r.status_code,text=s.get_text(' ',strip=True),links=[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]') if a['href'].startswith('http')])
  print(json.dumps(d,ensure_ascii=False)[:14000],flush=True);return d
 except Exception as e:return {'q':q,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rs=list(ex.map(f,qs))
Path(sys.argv[1]).write_text(json.dumps(rs,ensure_ascii=False,indent=2))
