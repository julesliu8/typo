# 韩语采集：三轮72条记录，当前形式范围54条

采集日期：2026-11-13、14。

**当前以[第三轮名词框架与缺例复核](../../02_语言材料/韩语/韩语心理谓词_名词框架与缺例复核_第三轮.md)为阅读入口。** ko siphta 以外的非名物化分句均退出；72条历史记录中54条在当前形式范围内，18条排除。名物化事件继续保留。

- 当前合并数据：`round3/current_comparison_examples.json`；排除清单：`round3/excluded_examples.json`；各轮原始记录均有 `comparison_eligible`。
- `round3/`：本轮13条新例、官方标准词典正文、Daum词典用例、报刊原文和查询记录；`search_audit.json` 对每个原缺例格记录结论，`reviewed_*_examples.json` 按来源用例ID去重保存检索材料。
- 生成顺序：`build_report.py`、`round2/build_report.py`、`round3/build_report.py`；`comparison_scope.py` 保存当前范围及历史例号排除列表。

- 历史第二轮阅读入口：[第二轮补例与连接词尾核查](../../02_语言材料/韩语/韩语心理谓词_补例与连接词尾核查_第二轮.md)。新增 K41—K59，原始网页、结构化数据及生成器位于 `round2/`；第一轮例号保持不变。

- 阅读入口：[例句稿](../../02_语言材料/韩语/韩语心理谓词_实体事件构式_例句与标注.md)、[NSM 核读笔记](../../03_文献笔记/NSM/韩语心理谓词_NSM定义与文献核读.md)。
- `examples.json`：40 条、16 词项（含惯用语）。保留原句、完整句上下文、证据类型、韩文／作者罗马字切分、gloss、内容类型及 E／Y 实际标记；新增 `lexeme_romanized`、`romanization`、`morphemes_romanized`、`full_original_romanized` 字段。语义节点待复核，未填最终值。
- `frame_groups.json`：按外层 Y 形式初分；不是完整 E／Y 框架合并结果，不直接作最终地图输入。
- `sources.json`：本轮实际使用的官方词典词条和 Yoon 2003 论文来源。`dict_마음에들다`（dict_maumeytulta）（dict_maumeytulta） 的 ParaWordNo 指向 마음（maum） 母词条，惯用语附在该条目下。
- `dict_词项.html/.txt`：官方词典原始网页与可读抽取文本。`dict_search_*` 为搜索页，不等同于词条全文。
- `yoon2003_repository_fulltext.txt`：ANU DSpace 提供的完整抽取文本，保留分页符。它由 `yoon2003_text_api.html` 原始响应无改动复制；原响应实际上为纯文本，扩展名源自通用抓取器。相关访问记录见同名前缀的 `_source.json`。
- `yoon2003_full_source.json` 等：大体积原扫描 PDF 的超时记录，**文件名不表示已经下载到全文 PDF**。部分 OCR 损坏段落没有用于逐字释义引用。
- 2026-11-15来源更新：用户另提供了原扫描，现位于`/Users/jessicac/Downloads/Constructing a Korean Natural Semantic Metalanguage -Yoon_K..pdf`。pp.42–44、251、282、308已核图；不据此声称WANT/GOOD全部章节均已图像核页。前一项的下载超时记录继续保留为历史记录。
- `schutze_*`：Mouton 格叠加文章的检索和访问尝试；挑战页／404 不是论文内容。
- `happiness_chapter.pdf`、`want_reply.pdf`：检索期间取得的通论补充文献，未用作韩语目标词完整 NSM 定义的证据。
- `build_report.py`：输出本轮例句稿和三个 JSON；执行时核验所有原句存在于来源文本，并检查切分／gloss 的词数及连字符对应。不会重新下载来源。人工修改例句后应同步生成器，以免再生时丢失修订。

第三轮又补礼物-ACC／LOC、绘本-NOM、指人实体及事实名物化-NOM、复刊-NOM，以及幸福的实体／事件-만으로도（manuloto）。尚缺：珍爱义的事件形式、普通具体物体＋高兴形容词的直接形式，喜欢／爱／高兴各词项现成 NSM explication，以及实际可核读的 Mouton 相关正文。缺例均不作为不合语法证据。

罗马转写由 `romanization.py` 按 Yale 式拼写规则生成，不代替来源原文，不应用语流音变。阅读稿中的词项、表格、例句、释义与说明均附转写；原始网页及论文抽取文本按原样保存。

2026-11-15新增[母语者试测说明](../../02_语言材料/韩语/母语者测试/研究者说明与测试表.md)与[离线问卷](../../02_语言材料/韩语/母语者测试/韩语心理词_离线测试表.html)。自拟英文情境、韩语词义草案和将来的诱导句与本目录自然／词典例句分开；未新增K例号，未填最终节点。
