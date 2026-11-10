exec(open('research/第三轮/lookup.py').read().split('queries=')[0])
queries=['"Transitivity in Shipibo-Konibo grammar" pdf','"Agency and intentional action" Newar pdf','"Ganenkov" "Experiencer coding" pdf']
def run(q):
 try:
  r=s.get('https://www.bing.com/search',params={'q':q},timeout=25)
  soup=bs4.BeautifulSoup(r.text,'html.parser')
  return q,r.status_code,[(x.get_text(' ',strip=True),[(a.get_text(' ',strip=True),a.get('href')) for a in x.select('a[href]')]) for x in soup.select('li.b_algo')]
 except Exception as e:return q,str(e)
for i,r in enumerate(concurrent.futures.ThreadPoolExecutor().map(run,queries)):
 pathlib.Path('research/第三轮/bing'+str(i)+'.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(str(r)[:16000])
