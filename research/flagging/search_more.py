import requests,concurrent.futures,json,pathlib
s=requests.Session();s.verify='/etc/ssl/cert.pem'
qs=['experiencer coding typology','psych predicates typology','emotion predicates typology','experiencer semantic maps','desiderative case marking','emotive predicates case frames','case pattern splits verb types','want like transitivity hierarchy','psychological predicates implicational hierarchy','experiencer flagging valency','semantic map emotion case marking','Le marquage de l experient']
def f(q):
 try:
  r=s.get('https://api.openalex.org/works',params={'search':q,'per-page':8},timeout=30);r.raise_for_status();return q,r.json()['results']
 except Exception as e:return q,str(e)
rs=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs));pathlib.Path('research/flagging/search_more.json').write_text(json.dumps(rs,ensure_ascii=False))
for q,rr in rs:
 print('\nQUERY',q)
 if isinstance(rr,list):
  for x in rr:print(x['title'],x.get('doi'),x['publication_year']);print([(z.get('pdf_url'),z.get('landing_page_url')) for z in x['locations']][:2])
 else:print(rr)
