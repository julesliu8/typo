import requests,json,concurrent.futures,pathlib
qs=['"natural semantic metalanguage" "Madura"','"natural semantic metalanguage" "Kayardild"','"natural semantic metalanguage" "Lezgian"','"natural semantic metalanguage" "Lango"','"natural semantic metalanguage" "Fongbe"','"natural semantic metalanguage" "Kambera"','"natural semantic metalanguage" "Kilivila"','"natural semantic metalanguage" "Baba Malay"']
def f(q):
 try:
  r=requests.get('https://api.openalex.org/works',params={'search':q,'per-page':10},verify='/etc/ssl/cert.pem',timeout=25);r.raise_for_status();j=r.json();print('\nQUERY',q,'count',j.get('meta',{}).get('count'),flush=True)
  for x in j.get('results',[])[:6]:print(x.get('title'),x.get('doi'),x.get('open_access'),flush=True)
  return {'q':q,'data':j}
 except Exception as e:return {'q':q,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:out=list(p.map(f,qs))
pathlib.Path('research/nsm/openalex_intersection1.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
