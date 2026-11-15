# 芬兰语采集材料

当前阅读入口：[用户复核与补例（第二轮）](../../02_语言材料/芬兰语/芬兰语心理谓词_用户复核与补例_第二轮.md)。2026-11-14依据用户《芬兰.txt》复核：从句留档暂不处理，附件所列A不定式继续单列；普通实体与事件名物化NP按实际用例记录。

- 第一轮：`examples.json`，41例；`build_pilot.py`是原报告生成器。第一轮`frame_groups.json`包括当时合并的带格代词＋että，仅作历史记录。
- 第二轮：`round2/examples.json`，新增17例，均核对原始来源文字并附形态分析。
- 当前范围：`round2/current_comparison_examples.json`，45条；`round2/deferred_clauses.json`，13条仅留档。
- 合并留档：`round2/all_examples_with_scope.json`；每条保留原号及是否进入当前形式范围。
- 当前形式分组：`round2/current_frame_groups.json`，不含暂存从句，不是最终语义地图输入。
- 用户原清单：`round2/user_review.txt`。
- 新增原文：`round2/ks_*_api.json`为官方词典；`round2/korp_*.json`为Kielipankki公开新闻语料查询；`round2/yle_*.html/.txt`为逐篇核对的报道。同名source记录保存URL与访问日期。

用项目环境运行`round2/build_report.py`可重建第二轮稿和当前范围数据；生成前自动检查每个新例的引用文字、gloss词数及适用的语料句号定位。先核对现有阅读稿，避免覆盖后续人工编辑。

目前词义节点未最终裁决；官方词典、新闻与教学来源不等于已经完成Mouton来源要求。

**开放问题：toivoa 的 PART／GEN 条件尚未研究清楚。** 实体两种格均有实例，不等于已证明自由交替；事件名物化仍只有PART正例。需补同一义项和相近语境的对照，检验义项、有界性及数量等因素。F57–F58所证明的是GEN可见，不能单独说明分布规则。
