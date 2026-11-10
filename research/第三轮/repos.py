import requests,json,pathlib
s=requests.Session();s.verify='/etc/ssl/cert.pem'
p=pathlib.Path('research/第三轮')
def get(u):
 r=s.get(u,timeout=35);r.raise_for_status();return r.json()
x=json.loads(pathlib.Path('research/ergative/newar_or_search.html').read_text())
for o in x['_embedded']['searchResult']['_embedded']['objects']:
 i=o['_embedded']['indexableObject'];print(i['id'],i['name']);
 if 'intentional' in i['name']:
  bs=get(i['_links']['bundles']['href']);(p/'newar_bundles.json').write_text(json.dumps(bs));
  for b in bs.get('_embedded',{}).get('bundles',[]):
   if b['name']=='ORIGINAL':
    files=get(b['_links']['bitstreams']['href']);(p/'newar_bitstreams.json').write_text(json.dumps(files));
    for f in files.get('_embedded',{}).get('bitstreams',[]):print('DOWNLOAD',f['name'],f['_links']['content']['href'])
x=get('https://scholarsbank.uoregon.edu/server/api/discover/search/objects?query=Valenzuela&size=30');(p/'shipibo_author.json').write_text(json.dumps(x))
for o in x.get('_embedded',{}).get('searchResult',{}).get('_embedded',{}).get('objects',[]):
 i=o['_embedded']['indexableObject'];print('SHIP',i['id'],i['name'])
