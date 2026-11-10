import requests,concurrent.futures,json,pathlib,bs4
s=requests.Session();s.verify='/etc/ssl/cert.pem'
qs=[('oa_perception','https://api.openalex.org/works?search=semantic%20maps%20perception&per-page=8'),('oa_desire','https://api.openalex.org/works?search=semantic%20maps%20desire&per-page=8'),('cr_viberg','https://api.crossref.org/works?query.title=The%20verbs%20of%20perception&rows=3'),('cr_evans','https://api.crossref.org/works?query.title=In%20the%20mind%20of%20the%20tongue&rows=2'),('cr_emotion','https://api.crossref.org/works?query.title=Emotion%20semantics%20show%20both%20cultural%20variation%20and%20universal%20structure&rows=2')]
def f(x):
 n,u=x
 try:
  r=s.get(u,timeout=30);r.raise_for_status();j=r.json();pathlib.Path('research/语义地图/'+n+'.json').write_text(json.dumps(j,ensure_ascii=False,indent=2))
  if 'results' in j:return n,[{k:z.get(k) for k in ['title','doi','publication_year','primary_location','open_access']} for z in j['results']]
  return n,[{k:z.get(k) for k in ['title','DOI','published','link','author','container-title','page','abstract']} for z in j['message']['items']]
 except Exception as e:return n,str(e)
for z in concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs):print(json.dumps(z,ensure_ascii=False))
