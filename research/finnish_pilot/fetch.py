import concurrent.futures
import json
import pathlib
import sys

import bs4
import requests

BASE = pathlib.Path(__file__).parent


def fetch(item):
    name, url = item
    record = {"name": name, "url": url}
    try:
        response = requests.get(url, verify="/etc/ssl/cert.pem", timeout=35)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        (BASE / (name + ".html")).write_text(str(soup))
        (BASE / (name + ".txt")).write_text(soup.get_text(" ", strip=True))
        links = [(a.get_text(" ", strip=True), a["href"]) for a in soup.select("a[href]")]
        (BASE / (name + "_links.json")).write_text(json.dumps(links, ensure_ascii=False, indent=2))
        record.update(status=response.status_code, title=soup.title.get_text() if soup.title else "")
    except Exception as error:
        record["error"] = str(error)
    (BASE / (name + "_source.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2))
    return record


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for record in pool.map(fetch, json.loads(sys.argv[1])):
            print(json.dumps(record, ensure_ascii=False), flush=True)
