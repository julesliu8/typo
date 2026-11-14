import requests,bs4,json,concurrent.futures
from pathlib import Path
qs=['site:nsm-approach.net Hasada 2000','site:nsm-approach.net Finnish emotions happy love','site:nsm-approach.net Japanese suki ureshii tanoshii','Hasada Rie 2000 An Exploratory Study Expression Emotions Japanese']
def f(q):
 r=requests.get('https://search.yahoo.co.jp/search',params={'p':q},verify='/etc/ssl/cert.pem',timeout=30);s=bs4.BeautifulSoup(r.content,'html.parser');d=dict(q=q,text=s.get_text(' ',strip=True),links=[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]') if a['href'].startswith('http')]);print(json.dumps(d,ensure_ascii=False),flush=True);return d
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:r=list(e.map(f,qs))
Path('research/nsm/search1.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
