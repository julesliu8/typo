# 数据入口

原有数据按采集来源保留，以下链接是统一入口。**目前没有完成语义复核和五语采集的最终八节点合并表。** 不将历史例句库或旧矩阵自动当作语义地图输入。

|数据|位置|用途／限制|
|---|---|---|
|芬兰语逐例数据|[examples.json](../research/finnish_pilot/examples.json)|例句、词项、形式、来源等采集记录；正文稿可能包含生成后的人工作业|
|芬兰语框架分组|[frame_groups.json](../research/finnish_pilot/frame_groups.json)|按既定规则归并 ELA、PART、ILL、裸 että 等|
|芬兰语来源表|[sources.json](../research/finnish_pilot/sources.json)|网页和文献的访问记录|
|韩语逐例数据|[examples.json](../research/korean_pilot/examples.json)|40 条、16 词项，原文、切分、gloss、E／Y 标记与证据类型；最终语义节点尚未赋值|
|韩语形式分组与来源|[frame_groups.json](../research/korean_pilot/frame_groups.json)、[sources.json](../research/korean_pilot/sources.json)|连接分句、VP 与格 NP 分开；形式组不是最终完整 E／Y 共享构式|
|日语 BivalTyp 摘录|[bivaltyp_selected.json](../research/japanese_pilot/bivaltyp_selected.json)|只覆盖该数据库的摘录，完整试采例句以[两轮稿件](../02_语言材料/README.md)为准|
|NSM 书目与阅读状态|[sources.json](../research/nsm/sources.json)|并非穷尽书目；未读全文与已核读区分记录|
|土耳其语逐例数据|[examples.json](../research/turkish_pilot/examples.json)、[框架分组](../research/turkish_pilot/frame_groups.json)、[来源表](../research/turkish_pilot/sources.json)|已移出当前样本，保留参考|
|早期五点位例句|[corpus.json](../research/第三轮/corpus.json)|作通格阶段的历史数据，含当前规则排除的构式|
|早期五点位矩阵|[构式对照矩阵.csv](历史数据/心理谓词_构式对照矩阵.csv)|与早期例句库配套；不是当前八节点矩阵|
|旧问卷摘录|[核心五语及亲缘问卷](../research/reselection/核心五语及亲缘_问卷原始摘录.json)|旧选样阶段材料|

生成器保留在相应采集目录。整理时只修改其报告输出位置，未运行生成器覆盖人工修订。若需要再生成，请先与现有阅读稿比较。
