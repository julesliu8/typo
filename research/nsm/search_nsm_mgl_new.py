import requests,json,concurrent.futures,pathlib
qs=['Kilivila natural semantic metalanguage emotion Senft','Kuuk Thaayorre natural semantic metalanguage emotion','Gurindji natural semantic metalanguage want emotion','Ngardi natural semantic metalanguage emotion','Kolyma Yukaghir natural semantic metalanguage want','Wardaman natural semantic metalanguage emotion','Semantic analysis of body parts in emotion terminology Enfield','Linguistic evidence for a Lao perspective on facial expression of emotion']
def f(q):
 try:
  r=requests.get('https://api.crossref.org/works',params={'query.bibliographic':q,'rows':7},verify='/etc/ssl/cert.pem',timeout=40); r.raise_for_status(); data=r.json()
  print('\nQUERY',q,flush=True)
  for x in data['message']['items'][:5]:print(x.get('title'),x.get('DOI'),str(x.get('abstract',''))[:300],flush=True)
  return {'q':q,'data':data}
 except Exception as e:return {'q':q,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:
 out=list(p.map(f,qs))
pathlib.Path('research/nsm/intersection_crossref5.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
