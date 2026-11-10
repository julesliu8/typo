import requests,bs4,pathlib,concurrent.futures,sys,json
s=requests.Session();s.verify='/etc/ssl/cert.pem';s.headers['User-Agent']='Mozilla/5.0'
def get(url,name):
 try:
  r=s.get(url,timeout=40);r.raise_for_status();p=pathlib.Path('research')
  if r.content[:4]==b'%PDF':(p/(name+'.pdf')).write_bytes(r.content);return name,'PDF '+str(len(r.content))
  (p/(name+'.html')).write_text(r.text)
  soup=bs4.BeautifulSoup(r.text,'html.parser')
  for x in soup(['script','style','header','footer','nav']):x.decompose()
  txt=soup.get_text(' ',strip=True);(p/(name+'.txt')).write_text(txt)
  links=[(x.get_text(' ',strip=True),x.get('href')) for x in soup.select('a[href]')]
  (p/(name+'_links.json')).write_text(json.dumps(links,ensure_ascii=False,indent=2))
  return name,txt[-45000:]
 except Exception as e:return name,str(e)
if __name__=='__main__':
 for a,b in concurrent.futures.ThreadPoolExecutor().map(lambda x:get(*x),json.loads(sys.argv[1])): print(a,b,'\n')
