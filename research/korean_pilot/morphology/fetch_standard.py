import requests,concurrent.futures,json
from pathlib import Path
from bs4 import BeautifulSoup
B=Path(__file__).resolve().parent
ITEMS=[('하다',363685),('-하다',498072),('좋아하다',477134),('즐기다1',483119),('즐기다2',313760),('사랑하다',166266),('원하다1',253825),('원하다2',465643),('만족하다',423287)]
def f(x):
 n,i=x
 try:
  url='https://stdict.korean.go.kr/search/contentViewOne.do';r=requests.post(url,data={'word_no':str(i)},verify='/etc/ssl/cert.pem',timeout=25)
  p=B/('std_'+n);p.with_suffix('.html').write_bytes(r.content);s=BeautifulSoup(r.content,'html.parser');p.with_suffix('.txt').write_text(s.get_text(' ',strip=True))
  (B/(p.name+'_source.json')).write_text(json.dumps({'url':url,'method':'POST','data':{'word_no':i},'status':r.status_code,'accessed':'2026-11-14','public_entry_url':'https://stdict.korean.go.kr/search/searchView.do?word_no='+str(i)},ensure_ascii=False,indent=2))
  print(n,r.status_code)
 except Exception as e:print(n,str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:list(p.map(f,ITEMS))
