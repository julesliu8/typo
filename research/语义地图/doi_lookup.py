exec(open('research/语义地图/search.py').read().split('queries=')[0])
dois=['10.1515/zfs-2021-2039','10.1038/s41598-023-48922-8','10.2307/417135','10.1515/ling.1983.21.1.123','10.1515/lingty-2021-2088','10.1515/zfs-2021-2044','10.1111/lnc3.12270','10.1515/stuf-2024-2003']
def f(d):
 try:
  r=s.get('https://api.openalex.org/works/https://doi.org/'+d,timeout=25);r.raise_for_status();x=r.json();pathlib.Path('research/语义地图/doi_'+d.replace('/','_')+'.json').write_text(json.dumps(x,ensure_ascii=False,indent=2))
  abstract=x.get('abstract_inverted_index') or {};seq={i:w for w,ii in abstract.items() for i in ii}
  return d,x.get('title'),x.get('publication_year'),[a['author']['display_name'] for a in x['authorships']],[(l.get('pdf_url'),l.get('landing_page_url')) for l in x['locations']],' '.join(seq[i] for i in sorted(seq))
 except Exception as e:return d,str(e)
for x in concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,dois):print(json.dumps(x,ensure_ascii=False))
