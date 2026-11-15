# 阿姆哈拉语第一轮采集

2026-11-15。阅读入口：[例句与标注](../../02_语言材料/阿姆哈拉语/阿姆哈拉语心理谓词_实体事件构式_例句与标注.md)；[NSM／Mouton核读](../../03_文献笔记/NSM/阿姆哈拉语心理谓词_NSM与Mouton正文核读.md)。

- `examples.json`：A01–A27，共27条证据记录；派生词清单／人称变体合并记，不视为27个独立自然句或词项。
- `current_comparison_examples.json`：19条当前NP形式范围记录，8实体、11事件。`background_and_excluded_examples.json`：8条背景／范围外记录及原因。
- `frame_groups.json`：仅Y表面形式分组；`coverage.json`记录缺口。所有`final_semantic_node=null`、`native_speaker_verified=false`。语义标签允许重叠，形式合格不等于已确立语义节点。
- `sources.json`：书目、实际核读范围、出版者及本轮作用。单次下载响应、访问时间和SHA256保存在对应`*_source.json`。`heart_crossref.json`／`heart_openalex.json`只用于书目及开放状态，不当正文。
- `verified_pages/`：目标原页图，`*_small.png`为阅读缩图。FSI印刷页＋19＝PDF页；love2026印刷页＝PDF页＋8；Baker2014例43印刷152＝PDF13；Amberber章35–37＝预览PDF41–43；Kozicki页码两者相同。
- `fsiv1_clean.txt`是Internet Archive OCR，定位用，不能直接复制当作核准文本。`*_pages.json`是抽取文本。原图为最终校对依据。
- `leslau1969.pdf`题名页为1969 ERIC版本；曾按网络文件标签误命名为1995，核查后已改正；不与引用的Leslau1995混用。
- `search.py`、`fetch.py`、`ocr.swift`是检索辅助；有些200／202响应实际为空或错误页。文件存在不代表正文已读。`build_materials.py`只生成本轮报告与数据，后续人工编辑前先比较差异，勿运行旧脚本覆盖人工补例。

当前主要缺口：HAPPY实体外部刺激、afäqqärä独立NP句、LOVE事件的独立语义证据、däss alä显性E NP、名物化格交替条件、Mouton后续正文。没有找到不编码为不存在。
