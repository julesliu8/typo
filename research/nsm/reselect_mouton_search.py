import requests,json,pathlib,concurrent.futures
outdir=pathlib.Path('research/nsm');qs=[('emotion2001_contents',{'filter':'isbn:9783110880168','rows':100}),('psych2001_contents_alt',{'query.container-title':'Emotions in Crosslinguistic Perspective','rows':25}),('korean_mouton_nsm',{'query.bibliographic':'Yoon Korean maum natural semantic metalanguage Mouton','rows':8}),('amharic_mouton_nsm',{'query.bibliographic':'Amberber testing emotional universals Amharic','rows':8}),('yankun_mouton_nsm',{'query.bibliographic':'Goddard Yankunytjatjara emotions Mouton','rows':10}),('finnish_mouton_psych',{'query.bibliographic':'Finnish emotion verbs experiencer constructions Mouton','rows':10})]
def f(x):
 n,params=x
 try:
  r=requests.get('https://api.crossref.org/works',params=params,verify='/etc/ssl/cert.pem',timeout=25);r.raise_for_status();j=r.json();(outdir/(n+'.json')).write_text(json.dumps(j,ensure_ascii=False,indent=2));print('\nQUERY',n,flush=True)
  for w in j['message']['items'][:20]:print(w.get('title'),w.get('DOI'),w.get('publisher'),flush=True)
 except Exception as e:print(n,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:list(p.map(f,qs))
