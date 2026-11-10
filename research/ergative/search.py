import requests,concurrent.futures,json,pathlib,sys,bs4
S=requests.Session(); S.verify='/etc/ssl/cert.pem'
def search(q):
 try:
  j=S.get('https://api.openalex.org/works',params={'search':q,'per-page':6},timeout=25).json(); out=[]
  for d in j.get('results',[]):
   a=d.get('abstract_inverted_index')or{}; words={i:w for w,ps in a.items() for i in ps}
   out.append({'title':d.get('title'),'doi':d.get('doi'),'year':d.get('publication_year'),'authors':[a['author']['display_name'] for a in d.get('authorships',[])],'locations':[(x.get('landing_page_url'),x.get('pdf_url')) for x in d.get('locations',[])],'abstract':' '.join(words[i] for i in sorted(words))})
  pathlib.Path('research/ergative/'+q.replace(' ','_').replace('/','_')+'.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));return q,out
 except Exception as e:return q,str(e)
if __name__=='__main__':
 for q,o in concurrent.futures.ThreadPoolExecutor().map(search,json.loads(sys.argv[1])):print(q,json.dumps(o,ensure_ascii=False))
