# 韩语第一轮采集

采集日期：2026-11-13。

- 阅读入口：[例句稿](../../02_语言材料/韩语/韩语心理谓词_实体事件构式_例句与标注.md)、[NSM 核读笔记](../../03_文献笔记/NSM/韩语心理谓词_NSM定义与文献核读.md)。
- `examples.json`：40 条、16 词项（含惯用语）。保留原句、完整句上下文、证据类型、韩文／作者罗马字切分、gloss、内容类型及 E／Y 实际标记；新增 `lexeme_romanized`、`romanization`、`morphemes_romanized`、`full_original_romanized` 字段。语义节点待复核，未填最终值。
- `frame_groups.json`：按外层 Y 形式初分；不是完整 E／Y 框架合并结果，不直接作最终地图输入。
- `sources.json`：本轮实际使用的官方词典词条和 Yoon 2003 论文来源。`dict_마음에들다`（dict_maumeytulta）（dict_maumeytulta） 的 ParaWordNo 指向 마음（maum） 母词条，惯用语附在该条目下。
- `dict_词项.html/.txt`：官方词典原始网页与可读抽取文本。`dict_search_*` 为搜索页，不等同于词条全文。
- `yoon2003_repository_fulltext.txt`：ANU DSpace 提供的完整抽取文本，保留分页符。它由 `yoon2003_text_api.html` 原始响应无改动复制；原响应实际上为纯文本，扩展名源自通用抓取器。相关访问记录见同名前缀的 `_source.json`。
- `yoon2003_full_source.json` 等：大体积原扫描 PDF 的超时记录，**文件名不表示已经下载到全文 PDF**。部分 OCR 损坏段落没有用于逐字释义引用。
- `schutze_*`：Mouton 格叠加文章的检索和访问尝试；挑战页／404 不是论文内容。
- `happiness_chapter.pdf`、`want_reply.pdf`：检索期间取得的通论补充文献，未用作韩语目标词完整 NSM 定义的证据。
- `build_report.py`：输出本轮例句稿和三个 JSON；执行时核验所有原句存在于来源文本，并检查切分／gloss 的词数及连字符对应。不会重新下载来源。人工修改例句后应同步生成器，以免再生时丢失修订。

尚缺：LOVE＋事件名物化等互补构式，若干 HAPPY 词的直接实体／事件补语，喜欢／爱／高兴各词项现成 NSM explication，以及实际可核读的 Mouton 相关正文。缺例均不作为不合语法证据。

罗马转写由 `romanization.py` 按 Yale 式拼写规则生成，不代替来源原文，不应用语流音变。阅读稿中的词项、表格、例句、释义与说明均附转写；原始网页及论文抽取文本按原样保存。
