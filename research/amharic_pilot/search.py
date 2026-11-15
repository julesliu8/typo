import concurrent.futures, json, sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).parent
def search(q):
    try:
        r=requests.get('https://search.yahoo.co.jp/search', params={'p':q}, timeout=40, verify='/etc/ssl/cert.pem')
        s=BeautifulSoup(r.content,'html.parser')
        d={'query':q,'status':r.status_code,'text':s.get_text(' ',strip=True),'links':[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]') if a['href'].startswith('http')]}
    except Exception as e: d={'query':q,'error':str(e)}
    print(json.dumps(d,ensure_ascii=False)[:20000],flush=True)
    return d
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: data=list(ex.map(search,json.loads(sys.argv[2])))
    (BASE/sys.argv[1]).write_text(json.dumps(data,ensure_ascii=False,indent=2))
