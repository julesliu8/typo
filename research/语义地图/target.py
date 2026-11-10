exec(open('research/语义地图/search.py').read().split('queries=')[0])
queries=['Viberg perception typological','In the mind s ear semantic extensions perception verbs Australian','Jackson emotion semantics cultural variation universal structure','Georgakopoulos Polis semantic map model','François semantic maps colexification','Desideratives and Person Constructing a Semantic Map']
def f(q):
 try:
  r=s.get('https://api.openalex.org/works',params={'search':q,'per-page':3},timeout=25);r.raise_for_status();its=r.json()['results'];pathlib.Path('research/语义地图/oa_'+q.split()[0]+'.json').write_text(json.dumps(its,ensure_ascii=False,indent=2))
  return q,[{k:x.get(k) for k in ['title','doi','publication_year','authorships','locations','abstract_inverted_index']} for x in its]
 except Exception as e:return q,str(e)
for q,x in concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,queries):
 print('\n',q)
 if isinstance(x,list):
  for z in x:print(z['title'],z['doi'],z['publication_year'],[(l.get('pdf_url'),l.get('landing_page_url')) for l in z['locations']])
 else:print(x)
