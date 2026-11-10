import requests,concurrent.futures,json,pathlib,time
s=requests.Session();s.verify='/etc/ssl/cert.pem'
queries=['semantic map perception verbs','semantic map causative perception','semantic map love like want','semantic map emotion desire pleasure','Viberg verbs of perception typological study','Evans Wilkins knowing hearing Australian']
def run(q):
 try:
  r=s.get('https://api.crossref.org/works',params={'query.bibliographic':q,'rows':5},timeout=30);r.raise_for_status()
  return q,[{k:x.get(k) for k in ['title','author','DOI','published','container-title','page','abstract','link']} for x in r.json()['message']['items']]
 except Exception as e:return q,str(e)
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(run,queries))
pathlib.Path('research/语义地图/crossref1.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
for q,items in r:
 print('\nQUERY',q)
 if isinstance(items,list):
  for i in items:print(i['title'],i['DOI'],i['published'])
 else:print(items)
