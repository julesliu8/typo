exec(open('research/flagging/search_more.py').read().split('qs=')[0])
qs=['"psych" "implicational"','"experiencer" "hierarchy"','"emotion" "flagging"','"bivalent" "semantic map"','"want" "like" "valency"','"experiencer" "coding"','"Case Pattern Splits, Verb Types and Construction Competition"','"A paradigm of psych-predicates"']
exec(open('research/flagging/search_more.py').read().split('def f(q):')[1].split('rs=')[0].join(['def f(q):','']))
rs=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,qs));pathlib.Path('research/flagging/target.json').write_text(json.dumps(rs,ensure_ascii=False))
for q,rr in rs:
 print('\nQUERY',q)
 if isinstance(rr,list):
  for x in rr:print(x['title'],x.get('doi'),x['publication_year']);print([(z.get('pdf_url'),z.get('landing_page_url')) for z in x['locations']][:2])
 else:print(rr)
