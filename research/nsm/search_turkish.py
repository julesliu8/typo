import requests,bs4,json,concurrent.futures
from pathlib import Path
qs=['site:nsm-approach.net Turkish emotions','site:nsm-approach.net Turkish sevmek istemek','Turkish "Natural Semantic Metalanguage" emotions love','Turkish "NSM" "happy" semantics','"Turkish" "Natural Semantic Metalanguage" want']
def f(q):
 r=requests.get('https://search.yahoo.co.jp/search',params={'p':q},verify='/etc/ssl/cert.pem',timeout=30);s=bs4.BeautifulSoup(r.content,'html.parser');d=dict(q=q,text=s.get_text(' ',strip=True),links=[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]') if a['href'].startswith('http')]);print(q,d['text'][:6500],d['links'][2:9],flush=True);return d
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:r=list(e.map(f,qs))
Path('research/nsm/turkish_search1.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
