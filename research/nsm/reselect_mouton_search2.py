import requests,json,pathlib,concurrent.futures
qs=[('korean_maum_metadata',{'query.bibliographic':'Yoon maum Korean','rows':12}),('korean_psych_mouton',{'filter':'prefix:10.1515','query.bibliographic':'Korean psychological experiencer predicates','rows':12}),('korean_case_mouton',{'filter':'prefix:10.1515','query.bibliographic':'Korean psych adjectives case nominative dative','rows':8}),('ewe_psych_mouton',{'filter':'prefix:10.1515','query.bibliographic':'Ameka Ewe experiences emotion','rows':8}),('koromu_grammar_book',{'query.bibliographic':'Koromu Kesawai Grammar Information Structure Priestley','rows':2})]
def f(x):
 n,params=x
 try:
  r=requests.get('https://api.crossref.org/works',params=params,verify='/etc/ssl/cert.pem',timeout=25);r.raise_for_status();j=r.json();pathlib.Path('research/nsm/'+n+'.json').write_text(json.dumps(j,ensure_ascii=False,indent=2));print('\nQUERY',n,flush=True)
  for w in j['message']['items'][:12]:print(w.get('title'),w.get('DOI'),w.get('publisher'),str(w.get('abstract',''))[:350],flush=True)
 except Exception as e:print(n,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:list(p.map(f,qs))
