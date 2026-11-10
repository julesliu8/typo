exec(open('research/语义地图/websearch.py').read().split('qs=')[0])
qs=['perception verbs semantic map','want like love semantic map','emotion semantic map pleasure desire']
def f(q):
 try:
  r=s.get('https://html.duckduckgo.com/html/',params={'q':q},timeout=30);sp=bs4.BeautifulSoup(r.text,'html.parser');return q,r.status_code,[(a.get_text(' ',strip=True),a.get('href')) for a in sp.select('.result__a')],sp.get_text(' ',strip=True)[:1500]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,qs));pathlib.Path('research/语义地图/ddg.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for x in r:print(str(x)[:18000])
