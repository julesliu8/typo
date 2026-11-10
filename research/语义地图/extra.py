exec(open('research/语义地图/search.py').read().split('queries=')[0])
qs=['"want" "like" "happy" semantic','"perception" "valency" "semantic map"','"Phenomenon-based perception verbs"','"love" "want" "polysemy" typology']
def f(q):
 try:
  r=s.get('https://api.openalex.org/works',params={'search':q,'per-page':6},timeout=25);r.raise_for_status();its=r.json()['results'];return q,[{k:x.get(k) for k in ['title','doi','publication_year','locations','abstract_inverted_index']} for x in its]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs));pathlib.Path('research/语义地图/oa_extra.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for q,x in r:
 print(q)
 if isinstance(x,list):
  for z in x:print(z['title'],z['doi'],z['publication_year'],[(l.get('pdf_url'),l.get('landing_page_url')) for l in z['locations']][:2])
 else:print(x)
