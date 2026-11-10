import requests,concurrent.futures,pathlib,bs4,json
s=requests.Session();s.verify='/etc/ssl/cert.pem'
queries=['"Newar" "Hargreaves" "afraid"','"Shipibo" "rake" "keen"','"Lezgian" "Ganenkov" "experiencer"','"Kathmandu" "Newar" "dative" "know"']
def run(q):
 try:
  r=s.get('https://www.google.com/search',params={'q':q},timeout=25)
  soup=bs4.BeautifulSoup(r.text,'html.parser')
  for x in soup(['script','style','header','footer']):x.decompose()
  return q,r.status_code,soup.get_text(' ',strip=True),[(a.get_text(' ',strip=True),a.get('href')) for a in soup.select('a[href]')]
 except Exception as e:return q,str(e)
for i,r in enumerate(concurrent.futures.ThreadPoolExecutor().map(run,queries)):
 pathlib.Path('research/第三轮/websearch'+str(i)+'.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(str(r)[:9000])
