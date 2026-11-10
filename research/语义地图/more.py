exec(open('research/语义地图/search.py').read().split('queries=')[0])
queries=['The semantic map model State of the art and future avenues for linguistic research','Semantic maps and the typology of colexification Intertwining polysemous networks across languages','Towards a Typology of Transitivity Splits','A semantic map of perception verbs','A semantic map of emotion verbs','Polysemy of love and want','semantic maps desire volition']
def run(q):
 try:
  r=s.get('https://api.crossref.org/works',params={'query.title':q,'rows':3},timeout=25);r.raise_for_status()
  return q,[{k:x.get(k) for k in ['title','author','DOI','published','container-title','page','abstract','link']} for x in r.json()['message']['items']]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(run,queries));pathlib.Path('research/语义地图/crossref2.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for q,items in r:
 print(q)
 if isinstance(items,list):
  for i in items:print(i['title'],i['DOI'],i['published'])
 else:print(items)
