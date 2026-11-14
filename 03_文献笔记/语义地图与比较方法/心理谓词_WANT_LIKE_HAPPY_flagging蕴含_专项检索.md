# WANT—LIKE—HAPPY：论元 flagging 框架覆盖与蕴含研究

检索与核读日期：2026-11-07。

## 核心结论

**存在直接研究“哪些谓词意义共享论元编码框架”的文献，也存在把编码框架分布作为蕴含等级加以统计检验的研究。** 因此，不能说此前没人从题元标记研究这些动词。但本轮尚未核实到专门确立 **WANT—LIKE—HAPPY 三义严格 flagging 蕴含关系**的论文。

最接近的两项先行研究是：Say（2018）§2.3 的论元编码相似性网络，以及 Aldai & Wichmann（2018）的编码框架蕴含等级检验。前者不是词汇共词化地图；后者是 De Gruyter Mouton 文献。Say 的 2026 年已接收稿又提供了更大样本的相关结果。

这些研究的总体提示是：心理谓词不一定在论元编码上形成统一簇，不能因为 WANT、LIKE、HAPPY 在词义或共词化上接近，就预设三者构成单一的格标记等级。

## 1. Say 2018：直接依据共享框架，把谓词意义放进网络

Сай, С. С. [Sergey Say]. 2018. **Маркирование актантов двухместных предикатов: предварительные итоги типологического исследования** [二价谓词的论元标记：类型学研究的初步结果]. In С. С. Сай (ed.), *Валентностные классы двухместных предикатов в разноструктурных языках*, 557–616. Санкт-Петербург: ИЛИ РАН.

- [开放整书](https://bivaltyp.info/docs/Say_ed_20018_Valentnostnye.pdf)（网址中的 `20018` 为原站拼写）。
- [本地全文](../../research/ergative/say2018book.pdf)。已核读相关章节，尤其 pp. 563、566–575，并查看 p. 568 图 1。
- 俄语出版物；不是 Mouton 来源。

### 方法为什么直接相关

§2.3（pp. 566–572）问的是：**两个谓词意义在各语言中是否归入相同的配价类，即是否具有相同的论元编码。**

作者对每对意义计算相对 Hamming 距离：在同时有可用材料的语言中，两个意义使用不同编码类的语言所占比例。该部分使用 37 种语言的子样本。例如 FEAR 和 AVOID：14 种语言编码不同、16 种相同、7 种缺项，距离为 14/30 ≈ 0.47。作者不是比较词根是否相同，也不要求跨语言的格词缀形式相同。

之后，作者用 NeighborNet 将距离可视化。p. 568 图 1 保留 74 个及物性指数不超过 0.5 的意义，并排除及物编码来重新计算距离。

### 对 WANT—LIKE—HAPPY 的实际发现

| 意义 | 网络中的近邻／所在区域 | 原文位置 |
|---|---|---|
| LIKE | HAVE、NEED、LACK、HAVE ENOUGH、FEEL PAIN、DREAM | p. 570 |
| BE GLAD / REJOICE | BE SURPRISED、BE ANGRY、TAKE OFFENCE；附近还有 ATTACK、LOOK、INFLUENCE | p. 569 |
| ENJOY / BE CONTENT | 工具／原因区域，与 HAVE ILLNESS、CUT ONESELF、WAVE 等接近 | p. 569 |

**重要限制：WANT 的及物性指数是 0.76（p. 563），因此不在图 1 的低及物性子集中。** 该图不能被引用为已经同时检验 WANT、LIKE、HAPPY 三义的地图。

pp. 570–571 明确指出：带有 Experiencer 和 Stimulus 的谓词没有形成统一簇；情绪、感知、思维内部的编码聚合也很弱。作者给出的是框架共享的相似性网络，**不是证明严格连通限制的经典语义地图，更不是单向蕴含等级**。

此外，原研究对象是 argument coding / valency classes；若论文只研究 flagging，需明确剥离或另记 indexing 等信息，不能把所有“编码类”直接等同于格标记框架。

## 2. Aldai & Wichmann 2018：直接检验编码框架的蕴含等级

Aldai, Gontzal & Søren Wichmann. 2018. **Statistical observations on hierarchies of transitivity.** *Folia Linguistica* 52(2): 249–281. **De Gruyter Mouton**.

- [DOI](https://doi.org/10.1515/flin-2018-0006)
- [开放全文](https://scholarlypublications.universiteitleiden.nl/download/1887/71830/1?col=81522199570002711)
- [本地全文](../../research/ergative/transitivity2018.pdf)。已核读研究设计、§4.1、相关讨论及 p. 267 表 (14)。

### 方法

以 ValPaL 中 36 种语言、38 个二价意义为样本，分别研究四类抽象框架：

- 1–2：普通及物编码；
- 1–3：斜格宾语编码；
- 1–3LOC：处所宾语编码；
- 3–1：倒置编码，如 DAT–NOM、OBL–ABS 等。

这里的数字是作者的抽象编码类别，不应直接当作 E、Stimulus 或某个语言的句法关系。作者用 Guttman scaling 检验谓词意义能否排成蕴含等级，再用矩阵随机化判断这种有序性是否高于偶然水平。随后也给出按跨语言实例比例排列的等级；**频率排列与严格蕴含检验必须分开理解**。

### 与心理谓词有关的结果

p. 266 的倒置编码等级 (13) 开头是：

> LIKE > HEAR > SEE > KNOW > MEET, FEAR, LOOK AT > …

但 **p. 267 表 (14) 中，倒置编码的随机化检验 p = 0.4967，不显著**。虽然 Guttman 系数高达 99.27，但这种框架非常稀少，矩阵中仅 1.3% 的非空单元为“有”；稀疏本身就会造成很高的表面有序性。其余三类框架在该检验中显著。

因此，这篇证明了“框架覆盖哪些意义→检验蕴含等级”是已有研究路线，**不能说它已经证实心理谓词的倒置编码等级**。其意义清单也不含 WANT、HAPPY，不能直接作为目标三义的结论。

## 3. Say 已接收稿：更大样本下，情绪谓词的编码仍高度分散

Say, Sergey. **Cross-linguistic argument-coding predictability and the lexical meaning of the verb.** *Linguistic Typology at the Crossroads*, 已接收稿。

- [BivalTyp 书目页](https://bivaltyp.info/project/publications/)列接收日期为 **2026-07-13**。
- [开放稿件](https://bivaltyp.info/docs/Say_accepted_Cross_linguistic.pdf)
- [本地全文](../../research/ergative/say2026predictability.pdf)。已核读研究范围、§5.4–5.5、稿件 p. 30 表 8。以下页码均为稿件页码；不假定已有最终出版卷期。

比较 149 种语言、130 个二价谓词，研究一个谓词的论元编码能否由其他谓词的编码预测。它不是严格蕴含研究，但与“哪些意义共享框架”直接相关。

§5.4 表 8 的一个小片段如下。表格保持原作 X–Y 次序；这些条目中 X 为体验者、Y 为刺激／对象。

| 意义 | Georgian | Mingrelian | Laz | Svan |
|---|---|---|---|---|
| BE CONTENT | NOM–INS | NOM–INS | NOM–ABL | DAT–NOM |
| BE SURPRISED | DAT–NOM | DAT–INS | NOM–DAT | DAT–NOM |
| ENJOY | NOM–INS | ERG–INS | TR | DAT–NOM |

TR 为原作的及物编码标签，不是某个具体格的名称。这些是编码概括，不能代替带语境的原语言例句。

表 8 的九个情绪谓词在每种 Kartvelian 语言中分成 5–8 个配价类，且各语言的分组方式不同。这说明：即使是亲缘很近、格系统相近的语言，也不能仅凭“情绪”或“E–Stimulus”语义预测具体框架。它同时支持用亲属语言检验点位内部稳定性的做法，但不支持直接构拟一个全家族统一框架。

## 4. 可直接利用的数据：BivalTyp

[谓词清单](https://bivaltyp.info/predicates/)和[问卷](https://bivaltyp.info/project/questionnaire/)包含所需的核心意义，且提供统一语境：

| 比较意义 | 问卷语境的中文概括 |
|---|---|
| WANT | P 想要一部新手机 |
| LIKE | P 喜欢这件衬衫 |
| LOVE (tea) | P 爱喝茶／喜欢茶 |
| BE GLAD | P 收到一封信，对这封信感到高兴 |
| ENJOY | P 从冷水中出来，享受热茶 |

**HAPPY 宜操作化为二价 BE GLAD ABOUT Y，而非只有体验者的一价“高兴”。** 否则，WANT／LIKE 的对象与 HAPPY 中根本未设的刺激论元无法比较。

同样，WANT NP 与 WANT VP／从句需要分开：前者直接观察名词性对象标记，后者还涉及补语策略、控制／同主语等问题。问卷给出的核心 WANT 是 NP 语境。

问卷中的英文标签只是比较概念，不能据此认定某语言只有一个对应词项或一种构式。数据库缺项也不等于该语言没有相应构式。

## 5. 必须区分：路径连通与单向等级

假设 F 为某语言中的一个具体 flagging 框架，如 E-DAT / Stimulus-ABS。分别判断 F 能否表达 WANT、LIKE、BE GLAD ABOUT。

### 假设 A：经典地图的连通限制

若假设线形地图为 `WANT — LIKE — BE GLAD ABOUT`，连通限制只排除：

> F 覆盖 WANT 和 BE GLAD ABOUT，却不覆盖 LIKE。

即：`F(WANT) ∧ F(BE GLAD) ⇒ F(LIKE)`。

它允许 F 只覆盖任意单个节点，也允许 F 覆盖 WANT+LIKE 或 LIKE+BE GLAD。**这不推出“F 用于 HAPPY，就也用于 WANT”。**

### 假设 B：单向蕴含等级

更强的假设是：

> `F(BE GLAD) ⇒ F(LIKE) ⇒ F(WANT)`。

这只允许覆盖 ∅、WANT、WANT+LIKE、三义全部。它连“只覆盖 HAPPY”也排除。若提出这种等级，必须另给方向的语义动机和经验依据，不能从地图的节点顺序直接读出来。

### 对这份 term paper 的建议

可以把核心问题写成：

> **欲望、喜好与愉悦谓词的论元标记是否共享框架？五种非印欧语言中的框架覆盖与连通性检验。**

先记录各点位的真实分布，再比较三种可能：WANT—LIKE—BE GLAD 的线形连通、其他节点次序，以及三者不适合排成单一路径。只有三个节点时，完整三角形对非空覆盖组合没有连通性排除力，因此不可仅凭“三者都有联系”就说发现了有预测力的地图。

编码时至少保留：

1. 语言、方言、资料及页码、词项、具体语境；
2. WANT NP／LIKE NP／BE GLAD ABOUT NP；必要时将 LOVE、ENJOY、BE CONTENT 作为扩展节点；
3. E 与 Stimulus 的完整 flagging 有序对；E 单独的标记另列，不能混成同一指标；
4. indexing 另列；词类、系词／轻动词结构另列；
5. 基本框架和可用交替；“任一构式可用”与“默认构式”两种统计口径分开；
6. 有例证、明确排除、未知三种证据状态。资料未记录时不能写“不允许”。

跨语言比较的起点是**同一语言内部，哪些意义共享 F**，而不是把所有语言中名称为 DAT 的标记视为同一实体。作通格语言保留 ERG／ABS 等实际标签，不统一改写成 NOM。

五个主点位适合检验局部连通假设、发现反例和提出后续调查问题，不能单独确立全球严格共性。亲属语言可以帮助确认结构稳定性、补充覆盖，但不应当作完全独立样本重复计算；构拟还需要对应形式、分布与历史证据，不能仅凭共同格标签完成。

## 6. 与前轮词汇地图材料及课程要求的关系

Georgakopoulos & Polis（2022）研究的是词汇共表达，其 WANT／LIKE／LOVE／HAPPY 地图只能作为意义选择的依据，不能替代 flagging 证据。Khanina（2008）确有欲望表达的形态句法材料，但没有建立目标三义的 flagging 蕴含地图。详见[此前两篇精读笔记](心理谓词_两篇PDF精读_欲望喜好愉悦.md)。

本轮新找到的 Say（2018）补上了更直接的“框架共享网络”先行研究；Aldai & Wichmann（2018）补上了“编码框架蕴含检验”的统计先例。

Aldai & Wichmann（2018）符合 Mouton 出版来源，但理论论文不能代替课程要求的至少五种非印欧语言的描述／分析材料。若课程严格限定 Mouton Grammar Library，期刊文献也只作为补充；Basque、Lezgian、Ronghong Qiang、Kakataibo、Dolakha Newar 的来源资格仍须逐项落实。
