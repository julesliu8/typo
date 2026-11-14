"""One-time, non-destructive reorganization with a byte-level inventory."""
from pathlib import Path
from collections import Counter
import ast
import hashlib
import json
import os
import re
import shutil
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
MOVES = {
    '心理谓词_按NSM与Mouton来源重新筛选.md': '01_研究方案/心理谓词_按NSM与Mouton来源重新筛选.md',
    '心理谓词_八节点研究_语义判定与构式编码试行稿.md': '01_研究方案/心理谓词_八节点研究_语义判定与构式编码试行稿.md',
    '日语心理谓词_八节点试采_例句与构式.md': '02_语言材料/日语/日语心理谓词_八节点试采_例句与构式.md',
    '日语心理谓词_实体事件互补构式_第二轮.md': '02_语言材料/日语/日语心理谓词_实体事件互补构式_第二轮.md',
    '芬兰语心理谓词_实体事件构式_例句与标注.md': '02_语言材料/芬兰语/芬兰语心理谓词_实体事件构式_例句与标注.md',
    '土耳其语心理谓词_实体事件构式_例句与标注.md': '02_语言材料/已移出样本/土耳其语/土耳其语心理谓词_实体事件构式_例句与标注.md',
    'NSM心理谓词研究_土耳其语_检索补记.md': '02_语言材料/已移出样本/土耳其语/NSM心理谓词研究_土耳其语_检索补记.md',
    'Hasada2000_日语心理谓词_全文核读与八节点启示.md': '03_文献笔记/NSM/Hasada2000_日语心理谓词_全文核读与八节点启示.md',
    'NSM心理谓词研究_日语芬兰语_文献与方法笔记.md': '03_文献笔记/NSM/NSM心理谓词研究_日语芬兰语_文献与方法笔记.md',
    '心理谓词_两篇PDF精读_欲望喜好愉悦.md': '03_文献笔记/语义地图与比较方法/心理谓词_两篇PDF精读_欲望喜好愉悦.md',
    '心理谓词_WANT_LIKE_HAPPY_flagging蕴含_专项检索.md': '03_文献笔记/语义地图与比较方法/心理谓词_WANT_LIKE_HAPPY_flagging蕴含_专项检索.md',
    '心理谓词_选题1与3_语义地图前人研究.md': '03_文献笔记/语义地图与比较方法/心理谓词_选题1与3_语义地图前人研究.md',
    '心理谓词_第一轮材料与粗特征.md': '90_历史方案/01_作通格阶段/心理谓词_第一轮材料与粗特征.md',
    '作通格语言_心理谓词分布_初步材料.md': '90_历史方案/01_作通格阶段/作通格语言_心理谓词分布_初步材料.md',
    '作通格语言_第二轮_羌语及新增样本.md': '90_历史方案/01_作通格阶段/作通格语言_第二轮_羌语及新增样本.md',
    '心理谓词_前人研究与比较方法.md': '90_历史方案/01_作通格阶段/心理谓词_前人研究与比较方法.md',
    '心理谓词_五点位及亲缘语言_莱比锡例句库.md': '90_历史方案/01_作通格阶段/心理谓词_五点位及亲缘语言_莱比锡例句库.md',
    '心理谓词_重新选样_WANT_LIKE_HAPPY.md': '90_历史方案/02_扩样阶段/心理谓词_重新选样_WANT_LIKE_HAPPY.md',
    '心理谓词_全球扩样_非洲巴新澳大利亚美洲.md': '90_历史方案/02_扩样阶段/心理谓词_全球扩样_非洲巴新澳大利亚美洲.md',
    '心理谓词_全球扩样_莱比锡例句库.md': '90_历史方案/02_扩样阶段/心理谓词_全球扩样_莱比锡例句库.md',
    'MGL五语言硬性要求_来源核查清单.md': '90_历史方案/03_MGL来源筛选/MGL五语言硬性要求_来源核查清单.md',
    '心理谓词_按NSM与MGL交集重新筛选.md': '90_历史方案/03_MGL来源筛选/心理谓词_按NSM与MGL交集重新筛选.md',
    '心理谓词_构式对照矩阵.csv': '04_数据/历史数据/心理谓词_构式对照矩阵.csv',
}
PATTERN = re.compile(r'(!?\[[^\]\n]*\]\()(<[^>\n]+>|[^)\n]+)(\))')


def included(p):
    return not any(x in p.relative_to(ROOT).parts for x in ['.git', '.venv', '.project_backups', '__pycache__'])


def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def moved(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel in MOVES:
        return ROOT / MOVES[rel]
    if rel.startswith('tmp/'):
        return ROOT / 'research/页面核查' / rel[4:]
    return path


def local_target(raw, owner):
    value = raw.strip().removeprefix('<').removesuffix('>')
    if re.match(r'^[A-Za-z][\w+.-]*:', value) or value.startswith('#'):
        return None
    path, sep, fragment = value.partition('#')
    resolved = (owner.parent / unquote(path)).resolve()
    return resolved, sep + fragment


def broken(text, owner):
    issues = []
    for match in PATTERN.finditer(text):
        target = local_target(match.group(2), owner)
        if target and not target[0].exists():
            issues.append({'document': str(owner.relative_to(ROOT)), 'target': match.group(2)})
    return issues


def main():
    for old, new in MOVES.items():
        if not (ROOT / old).is_file() or (ROOT / new).exists():
            raise RuntimeError(f'Move precondition failed: {old} -> {new}')
    backup = ROOT / '.project_backups/整理前_20261113'
    if backup.exists():
        raise RuntimeError('Backup already exists; migration must not run twice.')
    original_files = sorted(p for p in ROOT.rglob('*') if p.is_file() and included(p))
    inventory = [{'old': str(p.relative_to(ROOT)), 'new': str(moved(p).relative_to(ROOT)),
                  'sha256': digest(p), 'bytes': p.stat().st_size} for p in original_files]
    documents = {p: p.read_text() for p in original_files if p.suffix == '.md' and 'bivaltyp-master' not in p.parts}
    preexisting = [issue for p, content in documents.items() for issue in broken(content, p)]
    backup.mkdir(parents=True)
    mutable = list(documents) + [ROOT / p for p in [
        '.gitignore', 'research/finnish_pilot/build_pilot.py',
        'research/turkish_pilot/build_pilot.py', 'research/global_sample/build_examples.py',
        'research/第三轮/build_corpus.py']]
    for p in mutable:
        dest = backup / p.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
    (backup / '整理前文件清单.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
    for old, new in MOVES.items():
        target = ROOT / new
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(ROOT / old), str(target))
    if (ROOT / 'tmp').exists():
        shutil.move(str(ROOT / 'tmp'), str(ROOT / 'research/页面核查'))

    modified = set()
    for old, content in documents.items():
        dest = moved(old)

        def replace(match):
            target = local_target(match.group(2), old)
            if not target:
                return match.group(0)
            path, fragment = target
            try:
                path.relative_to(ROOT)
            except ValueError:
                return match.group(0)
            path = moved(path)
            value = os.path.relpath(path, dest.parent) + fragment
            return match.group(1) + ('<' + value + '>' if ' ' in value else value) + match.group(3)

        updated = PATTERN.sub(replace, content)
        # Turn named cross-references into portable links without altering source quotations.
        for name, location in MOVES.items():
            for literal in ['《' + name + '》']:
                updated = updated.replace(literal, '《[' + name + '](' + os.path.relpath(ROOT / location, dest.parent) + ')》')
        updated = updated.replace('`tmp/pdfs/hasada2000/`', '`research/页面核查/pdfs/hasada2000/`')
        if str(dest.relative_to(ROOT)).startswith('90_历史方案/'):
            lines = updated.splitlines(keepends=True)
            lines.insert(1, '\n> 历史研究记录：保留当时材料与判断；当前选样及来源规则以[现行方案](../../01_研究方案/当前方案.md)为准。\n')
            updated = ''.join(lines)
        if '/已移出样本/' in str(dest):
            lines = updated.splitlines(keepends=True)
            lines.insert(1, '\n> 土耳其语已移出当前样本；本文件保留为已有采集／方法参考。\n')
            updated = ''.join(lines)
        if updated != content:
            dest.write_text(updated)
            modified.add(str(dest.relative_to(ROOT)))

    # Keep generators pointing at their relocated reports; do not regenerate research text.
    for relative in ['research/finnish_pilot/build_pilot.py', 'research/turkish_pilot/build_pilot.py',
                     'research/global_sample/build_examples.py', 'research/第三轮/build_corpus.py']:
        p = ROOT / relative
        source = p.read_text()
        for name, target in MOVES.items():
            source = source.replace("ROOT/'" + name + "'", "ROOT/'" + target + "'")
            source = source.replace('ROOT / "' + name + '"', 'ROOT / "' + target + '"')
            source = source.replace("root/'" + name + "'", "root/'" + target + "'")
        source = source.replace("root=Path('/Users/jessicac/Documents/FU!DAN!!/学习/typology')", 'root=Path(__file__).resolve().parents[2]')
        ast.parse(source)
        p.write_text(source)
        modified.add(relative)
    ignore = ROOT / '.gitignore'
    text = ignore.read_text()
    if '.project_backups/' not in text:
        ignore.write_text(text.rstrip() + '\n\n# Local recovery snapshots from project organization\n.project_backups/\n')
    modified.add('.gitignore')

    failures = []
    for row in inventory:
        dest = ROOT / row['new']
        if not dest.is_file():
            failures.append({'missing': row['new']})
        elif row['new'] not in modified and digest(dest) != row['sha256']:
            failures.append({'changed_unexpectedly': row['new']})
    report = {'date': '2026-11-13', 'file_inventory': inventory,
              'moved_documents_and_data': MOVES, 'moved_preview_directory': ['tmp', 'research/页面核查'],
              'intentionally_updated': sorted(modified), 'preexisting_broken_links': preexisting,
              'integrity_failures': failures, 'backup': '.project_backups/整理前_20261113'}
    (ROOT / 'research/维护/整理记录_20261113.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'original_files': len(inventory), 'moved_documents_and_data': len(MOVES),
                      'preexisting_broken_links': len(preexisting), 'integrity_failures': failures}, ensure_ascii=False))
    if failures:
        raise RuntimeError('Integrity check failed')


if __name__ == '__main__':
    main()
