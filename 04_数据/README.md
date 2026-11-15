# 数据入口

原有数据按采集来源保留，以下链接是统一入口。**目前没有完成语义复核和五语采集的最终八节点合并表。** 不将历史例句库或旧矩阵自动当作语义地图输入。

|数据|位置|用途／限制|
|---|---|---|
|阿姆哈拉语当前比较范围|[current_comparison_examples.json](../research/amharic_pilot/current_comparison_examples.json)|第一轮27条证据中19条NP形式（8实体、11事件）；HAPPY_ENTITY等仍未知，最终语义节点为空|
|阿姆哈拉语全部与范围外记录|[examples.json](../research/amharic_pilot/examples.json)、[background_and_excluded_examples.json](../research/amharic_pilot/background_and_excluded_examples.json)|全部27条；8条代词索引、派生词、感受内容、非名物化分句及NEED等背景／范围外材料|
|阿姆哈拉语形式与来源|[frame_groups.json](../research/amharic_pilot/frame_groups.json)、[sources.json](../research/amharic_pilot/sources.json)、[coverage.json](../research/amharic_pilot/coverage.json)|Y表面标记分组；多数E NP省略，不能当完整E/Y共享构式；Mouton部分正文已用、目标外部Y框架待补|
|英语释义与待测草案|[inventory.json](../research/nsm/elicitation_20261115/inventory.json)|57条Q/T/P/H记录；不是57个确立定义；无最终节点|
|韩语试测情境与成分|[scenarios.json](../research/nsm/elicitation_20261115/scenarios.json)、[component_probes.json](../research/nsm/elicitation_20261115/component_probes.json)|32个自拟情境、16组成分检查；允许重叠；不是已采自然语料，尚无答案|
|芬兰语当前比较范围|[current_comparison_examples.json](../research/finnish_pilot/round2/current_comparison_examples.json)|两轮58条中保留45条名词形式／单列A不定式；最终语义节点尚未赋值|
|芬兰语暂存从句|[deferred_clauses.json](../research/finnish_pilot/round2/deferred_clauses.json)|13条从句保留，按2026-11-14用户要求暂不处理；原格合并编码留档|
|芬兰语逐轮数据|[第一轮](../research/finnish_pilot/examples.json)、[第二轮](../research/finnish_pilot/round2/examples.json)、[带范围合并表](../research/finnish_pilot/round2/all_examples_with_scope.json)|41＋17条，新增例句均经原文核对并附莱比锡式标注|
|芬兰语当前形式分组|[current_frame_groups.json](../research/finnish_pilot/round2/current_frame_groups.json)|ELA、PART、ILL、GEN与不定式等；不含搁置从句，非最终完整E／Y构式|
|芬兰语来源表|[sources.json](../research/finnish_pilot/sources.json)|网页和文献的访问记录|
|韩语当前比较范围|[current_comparison_examples.json](../research/korean_pilot/round3/current_comparison_examples.json)|三轮共72条，按用户范围留下54条名词形式／ko siphta记录；最终语义节点尚未赋值，内容待定记录仍待定|
|韩语退出当前比较的记录|[excluded_examples.json](../research/korean_pilot/round3/excluded_examples.json)|18条非名物化分句形式，保留原例号和排除原因|
|韩语逐轮采集|[第一轮](../research/korean_pilot/examples.json)、[第二轮](../research/korean_pilot/round2/examples.json)、[第三轮](../research/korean_pilot/round3/examples.json)|40＋19＋13条；逐例 comparison_eligible 标记现行范围，历史采集不直接作最终图输入|
|韩语形式分组与来源|[frame_groups.json](../research/korean_pilot/frame_groups.json)、[sources.json](../research/korean_pilot/sources.json)|连接分句、VP 与格 NP 分开；形式组不是最终完整 E／Y 共享构式|
|日语 BivalTyp 摘录|[bivaltyp_selected.json](../research/japanese_pilot/bivaltyp_selected.json)|只覆盖该数据库的摘录，完整试采例句以[两轮稿件](../02_语言材料/README.md)为准|
|NSM 书目与阅读状态|[sources.json](../research/nsm/sources.json)|并非穷尽书目；未读全文与已核读区分记录|
|土耳其语逐例数据|[examples.json](../research/turkish_pilot/examples.json)、[框架分组](../research/turkish_pilot/frame_groups.json)、[来源表](../research/turkish_pilot/sources.json)|已移出当前样本，保留参考|
|早期五点位例句|[corpus.json](../research/第三轮/corpus.json)|作通格阶段的历史数据，含当前规则排除的构式|
|早期五点位矩阵|[构式对照矩阵.csv](历史数据/心理谓词_构式对照矩阵.csv)|与早期例句库配套；不是当前八节点矩阵|
|旧问卷摘录|[核心五语及亲缘问卷](../research/reselection/核心五语及亲缘_问卷原始摘录.json)|旧选样阶段材料|

生成器保留在相应采集目录。整理时只修改其报告输出位置，未运行生成器覆盖人工修订。若需要再生成，请先与现有阅读稿比较。
