import requests,pathlib,json,concurrent.futures
items=[('nsm1994_book','https://jbe-platform.com/deliver/fulltext/9789027285782.pdf'),('nsm2002_v2_book','https://jbe-platform.com/deliver/fulltext/9789027281869.pdf'),('nsm2008_book','https://jbe-platform.com/deliver/fulltext/9789027291370.pdf'),('mpi_lao_search','https://pure.mpg.de/rest/items/search?q=Combinatoric%20Properties%20of%20Natural%20Semantic%20Metalanguage%20Expressions%20in%20Lao&format=json')]
def f(x):
 n,u=x
 try:
  r=requests.get(u,verify='/etc/ssl/cert.pem',timeout=30);is_pdf=r.content.startswith(b'%PDF');p=pathlib.Path('research/nsm/'+n+('.pdf' if is_pdf else '.response'));p.write_bytes(r.content);d={'name':n,'url':u,'final_url':r.url,'status':r.status_code,'content_type':r.headers.get('content-type'),'bytes':len(r.content),'is_pdf':is_pdf};pathlib.Path('research/nsm/'+n+'_source.json').write_text(json.dumps(d,indent=2));return d
 except Exception as e:return {'name':n,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:
 for d in p.map(f,items):print(d,flush=True)
