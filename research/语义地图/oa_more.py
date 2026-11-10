exec(open('research/语义地图/search.py').read().split('queries=')[0])
qs=['"semantic map" "perception" linguistic','"semantic map" "love"','"semantic map" "like" "want"','"colexification" "want" "love"','"perception" "Viberg" "1983"','"mind’s ear"']
def f(q):
 try:
  r=s.get('https://api.openalex.org/works',params={'search':q,'per-page':10},timeout=30);r.raise_for_status();its=r.json()['results'];return q,[{k:x.get(k) for k in ['title','doi','publication_year','locations','abstract_inverted_index','authorships']} for x in its]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs));pathlib.Path('research/语义地图/oa_more.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for q,x in r:
 print('\nQUERY',q)
 if isinstance(x,list):
  for z in x:print(z['title'],z['doi'],z['publication_year'])
 else:print(x)
