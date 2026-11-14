"""Read-only checks for document links and the 2026-11-13 move inventory."""
from pathlib import Path
import ast
import hashlib
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)')


def main():
    report = json.loads((ROOT / 'research/维护/整理记录_20261113.json').read_text())
    allowed = set(report['intentionally_updated']) | {'README.md'}
    missing = []
    changed = []
    for row in report['file_inventory']:
        p = ROOT / row['new']
        if not p.is_file():
            missing.append(row['new'])
            continue
        if row['new'] not in allowed:
            h = hashlib.sha256()
            with p.open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    h.update(block)
            if h.hexdigest() != row['sha256']:
                changed.append(row['new'])

    broken = []
    docs = []
    links = 0
    for p in ROOT.rglob('*.md'):
        if any(part in p.relative_to(ROOT).parts for part in
               ['.git', '.venv', '.project_backups', 'bivaltyp-master']):
            continue
        docs.append(p)
        for match in LINK.finditer(p.read_text()):
            raw = match.group(1).strip().removeprefix('<').removesuffix('>')
            if re.match(r'^[A-Za-z][\w+.-]*:', raw) or raw.startswith('#'):
                continue
            raw = unquote(raw.partition('#')[0])
            links += 1
            if not (p.parent / raw).resolve().exists():
                broken.append({'document': str(p.relative_to(ROOT)), 'target': raw})

    scripts = ['research/finnish_pilot/build_pilot.py', 'research/turkish_pilot/build_pilot.py',
               'research/global_sample/build_examples.py', 'research/第三轮/build_corpus.py']
    for relative in scripts:
        ast.parse((ROOT / relative).read_text())
    result = {'original_files_checked': len(report['file_inventory']),
              'missing_originals': missing, 'unexpected_content_changes': changed,
              'markdown_documents_checked': len(docs), 'local_links_checked': links,
              'broken_local_links': broken, 'generator_syntax_checked': scripts}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if missing or changed or broken:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
