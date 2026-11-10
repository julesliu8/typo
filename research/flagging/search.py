import requests,concurrent.futures,json,pathlib
s=requests.Session();s.verify='/etc/ssl/cert.pem'
qs=['"experiencer" "semantic map"','"psych" "case" "implicational"','"want" "like" "case marking"','"happy" "experiencer" "typology"','"emotion" "valency" "hierarchy"','"Experiencer coding and transitivity"','"Case Marking and the Semantics of Mental Verbs"','"Experiencer coding in Nakh-Daghestanian"']
def f(q):
 try:
  r=s.get('https://api.openalex.org/works',params={'search':q,'per-page':5},timeout=30);r.raise_for_status();return q,r.json()['results']
 except Exception as e:return q,str(e)
rs=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs));pathlib.Path('research/flagging/search1.json').write_text(json.dumps(rs,ensure_ascii=False))
for q,rr in rs:
 print('\nQUERY',q)
 if isinstance(rr,list):
  for x in rr:
   print(x['title'],x.get('doi'),x['publication_year']);print([(z.get('pdf_url'),z.get('landing_page_url')) for z in x['locations']][:3])
 else:print(rr)
