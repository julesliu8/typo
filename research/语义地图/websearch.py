import requests,bs4,concurrent.futures,pathlib,json
s=requests.Session();s.verify='/etc/ssl/cert.pem'
qs=['"perception" "semantic map" verbs','"want" "like" "semantic map"','"love" "semantic map"','"causative" "perception" "semantic map"']
def f(q):
 try:
  r=s.get('https://www.google.com/search',params={'q':q,'udm':'14'},timeout=30);sp=bs4.BeautifulSoup(r.text,'html.parser')
  for x in sp(['script','style','header','footer']):x.decompose()
  return q,r.status_code,sp.get_text(' ',strip=True),[(a.get_text(' ',strip=True),a.get('href')) for a in sp.select('a[href]')]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,qs));pathlib.Path('research/语义地图/google.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for x in r:print(str(x)[:14000])
