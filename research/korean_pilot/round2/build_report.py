"""Reviewed follow-up: source-attested excerpts, not acceptability judgments."""
import sys,json,re
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent))
from romanization import romanize,annotate_markdown,aligned_rows
from comparison_scope import annotate_scope
ROOT=B.parents[2]
OUT=ROOT/'02_语言材料/韩语/韩语心理谓词_补例与连接词尾核查_第二轮.md'
EX=[]
def add(lex,source,original,morph,gloss,zh,content,frame,e,note,full=None):
 nominal=frame in {'NOM','ACC','EY','MIND_EY_Y_NOM','NOMINAL_FACT_MAN_URO'}
 y={'NOM':'NOM','ACC':'ACC','EY':'에','MIND_EY_Y_NOM':'NOM','NOMINAL_FACT_MAN_URO':'만으로'}.get(frame,'无外层格；连接词尾另记')
 realization=('ADN_LEXICAL_FACT_NP' if frame=='NOMINAL_FACT_MAN_URO' else 'NP' if content=='ENTITY' else 'NMLZ_NP') if nominal else 'ADVERBIAL_CLAUSE'
 EX.append(dict(id=f'K{41+len(EX)}',lexeme=lex,source='entry_'+source,original=original,morphemes=morph,gloss=gloss,translation_zh=zh,content_type=content,realization=realization,frame_group=frame,experiencer_flagging=e,y_flagging=y,relation_status='名词内容形式；是否选定仍需结合词条配价' if nominal else '副词分句关系；未证明为选定补语',note=note,full_original=full,evidence_type='词典原句连续摘录' if full else '词典完整句／对话话轮',final_semantic_node=None))
add('좋다','문예반','나는 글을 쓰는 것이 좋아',
 '나-는 글-을 쓰-는 것-이 좋-아','1SG-TOP writing-ACC write-ADN NMLZ-NOM like-CVB.REASON',
 '我喜欢写作，所以……','EVENT','NOM','TOP',
 '明确的偏好义事件-NP-NOM；后接加入文学社的结果。不是“应该写作”的适宜／建议义。心理谓词自身的 -아 引出后果，与它前面的事件名物化补语分层。',
 '나는 글을 쓰는 것이 좋아 고등학교 때에는 문예반에 들어가 활동하기도 했다.')
add('사랑하다','동인','시 짓기와 읽기를 사랑하는 동인',
 '시 짓-기-와 읽-기-를 사랑하-는 동인','poem compose-NMLZ-CONJ read-NMLZ-ACC love-ADN fellow.member',
 '热爱写诗和读诗的同好','EVENT','ACC','定语从句内省略；关系中心语为感受者',
 '并列活动名物化，末项显现 ACC。原词“爱／热爱”保留，不擅自并入最终 LOVE 或 LIKE 节点。外层中心名词同好不是 E-NOM 的例证。',
 '그 모임은 시 짓기와 읽기를 사랑하는 동인끼리의 모임이었다.')
add('만족하다','대충대충','그는 대충대충 공부하면서 중간 정도의 성적을 유지하는 것에 만족했다.',
 '그-는 대충대충 공부하-면서 중간 정도-의 성적-을 유지하-는 것-에 만족하-였-다',
 '3SG-TOP carelessly study-CVB.SIM middle level-GEN grade-ACC maintain-ADN NMLZ-LOC be.satisfied-PST-DECL',
 '他随便学学，满足于维持中等成绩。','EVENT','EY','TOP',
 '事件名物化 NP-에；不是只有原因连接式。中间的成绩-ACC 属于维持的宾语；정도의 保留词典原有表达。')
add('기쁘다','떠오르다','유민이는 내가 온 것이 별로 기쁘지 않은가 봐.',
 '유민이-는 내-가 오-ㄴ 것-이 별로 기쁘-지 않-은가 보-아',
 'PN-TOP 1SG-NOM come-ADN NMLZ-NOM particularly be.glad-LINK NEG-INT.EMB seem-FIN',
 '有敏似乎对我来并不怎么高兴。','EVENT','NOM','TOP',
 '外层感受者是有敏-TOP；我-NOM 属于来这个事件。否定和推测不取消事件 NP-NOM 的证据。봐 是 보아 的缩合，末尾是推测辅助结构。')
add('기쁘다','접하다','결혼 소식을 접하니 나도 기쁘구나.',
 '결혼 소식-을 접하-니 나-도 기쁘-구나','marriage news-ACC encounter-CVB.REASON 1SG-ADD be.glad-EXCL',
 '听到结婚的消息，我也很高兴啊。','EVENT','REASON_NI','ADD',
 '-니 为事态接触后产生感受的根据／原因，兼有得知事实后的反应。消息-ACC 属于接触，不是高兴的直接 ACC。')
add('기쁘다','상쇄되다','합격하니까 정말 기쁘다.',
 '합격하-니까 정말 기쁘-다','pass.exam-CVB.REASON really be.glad-DECL',
 '考上了，真高兴。','EVENT','REASON_NIKKA','省略',
 '完整独立句摘自词典对话；只收这一句，不收后面含被动形态的句子。与第一轮 K23 的 -어서 对照，同词可用多种原因词尾。',
 '합격하니까 정말 기쁘다. 그동안 힘들었던 게 이걸로 다 상쇄됐어.')
add('기뻐하다','개국하다','당시 백성들은 새 나라가 개국한 것을 매우 기뻐했다고 합니다.',
 '당시 백성-들-은 새 나라-가 개국하-ㄴ 것-을 매우 기뻐하-였-다-고 하-ㅂ니다',
 'then commoner-PL-TOP new country-NOM be.founded-ADN NMLZ-ACC very rejoice-PST-DECL-QUOT say-DECL.POL',
 '据说，当时百姓对新国家的建立非常高兴。','EVENT','ACC','TOP',
 '事件名物化 NP-ACC。개국하다 是原文主动不及物形式；英文 be.founded 只为表达建国，不表示韩语有 PASS。对话前一话轮的被动例句不纳入。',
 '네, 당시 백성들은 새 나라가 개국한 것을 매우 기뻐했다고 합니다.')
add('즐겁다','주다','그 임무를 당신에게 주는 것이 즐거울 것 같습니까?',
 '그 임무-를 당신-에게 주-는 것-이 즐겁-을 것 같-습니까',
 'that task-ACC 2SG-DAT give-ADN NMLZ-NOM be.pleasant-PROS NMLZ seem-Q.POL',
 '把那个任务交给你，难道会让我愉快吗？','EVENT','NOM','摘录内省略；原话用 나라고',
 '反问语境的事件 NP-NOM 正例，不是肯定喜欢该事件的语义证据。것 같- 是推测结构；末尾 것 的名词形式与前面事件名物化分开。词干 즐겁- 有 ㅂ 不规则变化。',
 '이 대리. 나라고 그 임무를 당신에게 주는 것이 즐거울 것 같습니까?')
add('흐뭇하다','딸아이','아버지는 어느새 훌쩍 자란 딸아이를 보니 새삼 대견스럽고 흐뭇했다.',
 '아버지-는 어느새 훌쩍 자라-ㄴ 딸아이-를 보-니 새삼 대견스럽-고 흐뭇하-였-다',
 'father-TOP before.one.knows markedly grow-ADN daughter-ACC see-CVB.REASON anew be.proud-COORD be.pleased-PST-DECL',
 '父亲看到不知不觉长大了的女儿，顿时又骄傲又欣慰。','EVENT','REASON_NI','指人名词-TOP',
 '足以否定“只能用心作可见名词”的猜测：这里直接是父亲-TOP，无心名词。不单凭 TOP 判定所有主格替换都成立。女儿-ACC 是看的宾语。')
add('흐뭇하다','끔찍이','두 사람이 서로를 끔찍이 위하는 모습을 보면 흐뭇해요.',
 '두 사람-이 서로-를 끔찍이 위하-는 모습-을 보-면 흐뭇하-여요',
 'two person-NOM each.other-ACC dearly care.for-ADN scene-ACC see-COND be.pleased-POL',
 '看见两人如此爱护彼此的样子，就觉得欣慰。','EVENT','COND_MYEN','省略',
 '一般／反复条件，不能当成已经发生事件的中性原因式。두 사람-NOM 是嵌入照顾事件的参与者，不是外层 E。',
 '맞아요. 두 사람이 서로를 끔찍이 위하는 모습을 보면 흐뭇해요.')
add('흐뭇하다','벙긋벙긋하다','아버지는 아이의 재롱을 보고 흐뭇해서 벙긋벙긋했다.',
 '아버지-는 아이-의 재롱-을 보-고 흐뭇하-여서 벙긋벙긋하-였-다',
 'father-TOP child-GEN antics-ACC see-CVB.SEQ be.pleased-CVB.REASON smile.repeatedly-PST-DECL',
 '父亲看了孩子逗趣的表现，心里欣慰，笑眯眯的。','EVENT','SEQ_KO','指人名词-TOP',
 '入接 흐뭇하다 的是 보-고：先看到，随后产生感受，语境可推因果；-해서 是“欣慰→微笑”的出接原因，不能反过来编码为 Y 的形式。')
add('행복하다','효심','부부는 효심이 극진한 자녀를 두어 행복했다.',
 '부부-는 효심-이 극진하-ㄴ 자녀-를 두-어 행복하-였-다',
 'couple-TOP filial.piety-NOM be.deep-ADN child-ACC have-CVB.REASON be.happy-PST-DECL',
 '夫妇有极其孝顺的子女，感到幸福。','EVENT','REASON_E','TOP',
 '直接回答：裸 -어 不限于 있어。这里 두다“有／养育”＋-어；子女-ACC 属于 두다。它仍是拥有状态，其他词汇事件的 -어서 见 K53。')
add('행복하다','열애','남자 친구가 무척 잘해 줘서 행복해.',
 '남자 친구-가 무척 잘하-여 주-어서 행복하-여',
 'male friend-NOM very treat.well-LINK BEN-CVB.REASON be.happy-FIN',
 '男朋友对我很好，所以很幸福。','EVENT','CAUSE_ESEO','省略',
 '잘해 주다 是待人好／为对方做好的受益表达，不是语法使役；줘서＝주어서。证明幸福前的原因式不局限于存在句。男朋友-NOM 是嵌入施事。')
add('행복하다','다정스레','아기가 태어나니 정말 행복하지요?',
 '아기-가 태어나-니 정말 행복하-지요','baby-NOM be.born-CVB.REASON really be.happy-Q.POL',
 '孩子出生了，您一定很幸福吧？','EVENT','REASON_NI','省略',
 '태어나다 为词典普通不及物词“出生”，不是生产性的被动／使役句式。아기-NOM 是嵌入主语。')
add('행복하다','도란거리다','오랜만에 집에서 도란거리니까 너무 행복해.',
 '오랜만-에 집-에서 도란거리-니까 너무 행복하-여',
 'long.interval-LOC house-LOC chat.quietly-CVB.REASON very be.happy-FIN',
 '久违地在家闲聊，太幸福了。','EVENT','REASON_NIKKA','省略',
 '-니까 明说原因／根据；与 K52—54 构成同一谓词多个原因词尾的实证，不能再给该词只配一个 -e 框架。')
add('행복하다','배시시','난 초콜릿을 먹으면 행복해.',
 '나-는 초콜릿-을 먹-으면 행복하-여','1SG-TOP chocolate-ACC eat-COND be.happy-FIN',
 '我吃巧克力就觉得幸福。','EVENT','COND_MYEN','TOP',
 '난＝나는；条件／反复情境。巧克力-ACC 是吃的对象，不是幸福的直接实体 ACC。')
add('마음에 들다','깔끔히','생선을 아주 깔끔히 손질하시는 게 마음에 들어요.',
 '생선-을 아주 깔끔히 손질하-시-는 것-이 마음-에 들-어요',
 'fish-ACC very neatly prepare-HON-ADN NMLZ-NOM mind-LOC enter-POL',
 '我喜欢他把鱼处理得非常干净这一点。','EVENT','MIND_EY_Y_NOM','省略',
 '게＝것이；事件名物化 NP-NOM，不是只见原因式。마음-에 是惯用构式内部成分；此处不能将它算作刺激的 LOC。',
 '네. 생선을 아주 깔끔히 손질하시는 게 마음에 들어요.')
add('마음에 들다','들다','나는 네가 준 선물이 제일 마음에 들어.',
 '나-는 네-가 주-ㄴ 선물-이 제일 마음-에 들-어',
 '1SG-TOP 2SG-NOM give-ADN gift-NOM most mind-LOC enter-FIN',
 '我最喜欢你送的礼物。','ENTITY','MIND_EY_Y_NOM','TOP',
 '普通礼物按实体记录；不因定语“你给的”而改成收到礼物事件。与 K57 的事件-NOM 实现直接对应。')
add('행복하다','주경야독하다','공부를 한다는 사실만으로 행복했어요.',
 '공부-를 하-ㄴ다는 사실-만-으로 행복하-였-어요',
 'study-ACC do-ADN.QUOT fact-ONLY-INST be.happy-PST-POL',
 '仅仅因为自己在学习这一事实，就觉得幸福。','EVENT','NOMINAL_FACT_MAN_URO','省略',
 '事实名词名物化＋만으로“仅凭／单因……”。说明幸福也可有名词形式的事件根据；标记包含限定焦点，不把它当无标记 로 配价或直接合并到普通 NP-LOC。',
 '주경야독하는 생활이지만 공부를 한다는 사실만으로 행복했어요.')

HEAD='''# 韩语心理谓词：第二轮补例与连接词尾核查

**范围更新：用户已排除 -고 싶다 以外的非名物化分句形式。本稿的连接词尾讨论仅保留为历史核查，不再进入当前比较。现行表及问号核查见[第三轮](韩语心理谓词_名词框架与缺例复核_第三轮.md)；名物化 NP 继续保留。**

核读：2026-11-14。承接[第一轮40例](韩语心理谓词_实体事件构式_例句与标注.md)，本轮新增19例（K41—K59），逐例回查韩国国立国语院《한국어기초사전》实际词条。原文、摘录边界、完整上下文与分析分别保存；gloss 和中文译文由本稿补配。**不使用自造句，也不把搜索无结果当不合语法。** 所有阅读用谚文附 Yale 式拼写转写；原始来源按原样保存。

## 1. 对用户清单的核查结果

本表的“名词框架”与“分句关联”分列：前者记录内容 NP 的外层格，后者首先记录实际语义关系，暂不声称都是选定补语。`?`＝缺少足够正例。实体名词不因常见语用关联而自动重释为事件；事件名物化仍是 EVENT＋NP。

|词项|ENTITY 外层形式|EVENT 的名词形式|已见分句形式／修订|
|---|---|---|---|
|좋아하다|ACC K01|ACC K02—03|-면 K04 是下雪条件；-며 是四处跳跑的同时伴随，不宜写成专属 EVENT-mye；且 K04 是“表现高兴”义|
|좋다|NOM／TOP K05、39—40|**NOM K41**|K06 工作／任务不计 EVENT；排除“最好做……”建议义|
|사랑하다|ACC K07—09|**ACC K42**|已补热爱写诗和读诗；恋爱／珍爱／热爱义仍分存|
|아끼다|ACC K10|?|仍未找到珍爱义的可靠事件正例；节省金钱／少说话等不填此格|
|원하다|ACC K11—12|ACC 可省 K13—14|不能将嵌入对象 ACC 再算作外层实体|
|바라다|ACC K15|ACC K16|K17 是 -었으면 하고 条件愿望＋引述，不宜缩成一般 QUOT|
|싶다|直接实体 ?|不据内部名词填此栏|-고 싶다 为辅助愿望结构；-었으면 싶다 条件愿望另列，两者非同一普通原因 CVB|
|기쁘다|普通实体 ?|胜利-NOM K22；**事件名物化-NOM K44**|-어서 K23，-니 K45，-니까 K46 都有；不能限定为 -ese|
|기뻐하다|信息实体“消息”-에 K25；普通具体实体 ?|胜利-ACC K24；**事件名物化-ACC K47**|胜利是事件／结果名词，不能单因它是 NP 就改记 ENTITY|
|즐겁다|普通实体 ?；一天-NOM K26 待定|**事件名物化-NOM K48**|-니 K27 是原因／遭遇后的反应；K48 为反问，不抹去结构但也不作正向偏好证据|
|즐기다|酒-ACC K28|ACC K29—31|原有两边都已证实；习惯偏好与享受分义|
|행복하다|直接刺激 NP ?|**事件事实名词＋만으로 K59**|-어 K32、52；-어서 K53；-니 K54；-니까 K55；-면 K56。不能概括为只接 있어|
|만족하다|职业-에 K34|**事件名物化-에 K43**|名词补足的两边已齐；结果 K33 的内容判断另留|
|반갑다|朋友-NOM K35|?| -어서 K36、-니 K27；现有两个原因／情境词尾，不等于已经证明名词事件补语不存在|
|흐뭇하다|直接刺激 NP ?|?|**指人名词-TOP K49、51**；-니 K37、49；-면 K50；-고 K51。不要求一定出现 마음|
|마음에 들다|衣服-TOP K38；**礼物-NOM K58**|**事件名物化-NOM K57**|K38 同时有实体话题和原因分句，不应删去实体只记 event-CVB；心-에 为构式内部成分|

第一轮 K22／24“胜利”按词汇 EVENT／RESULT NP 保存；K25“消息”保留 EVENT_REPORT，亦可在后续内容规则明确后纳入信息实体。它们的**语法形式**与**内容类型**须分别读；这与普通礼物坚持 ENTITY 的规则一致。

## 2. 连接词尾究竟表达什么

以下依据官方词尾词条的明列义项，不是从英译倒推。表内标签是本项目方便比较的分析标签，CVB 并非唯一理论分类。

|形式|词典所列功能／本批读法|本项目建议|实际来源|
|---|---|---|---|
|-아／-어／-여|多义：先后／手段，原因，辅助连接，句末形式；K52 是原因|原因时 CVB.REASON；句末时 FIN；辅助连接时 LINK；不能见到 어 一律当原因|[-어¹ 义2](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=86094)|
|-아서／-어서／-여서|多义：先后，原因，手段；情绪例 K23、53 为原因|CVB.REASON／CVB.CAUSAL，同一原因关系；两个实际形式仍保存|[-어서 义2](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80215)、[-아서 义2](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80220)|
|-니／-으니|原因／根据／前提；也可接续相关或新发现事实；本批“见到→欣慰”有遭遇／发现背景|先记 CVB.REASON；说明具体语境，不能断定每例只有纯因果|[-니¹ 义1—2](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80144)|
|-니까／-으니까|原因／根据／前提；可突出理由|CVB.REASON，并保留形式子组|[-니까](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80139)|
|-면／-으면|假设、条件、反复条件，也可用于希望的非现实事态|COND；K50／56 是一般条件；K21 的愿望结构另列|[-면 义1—4](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80259)|
|-며／-으며|列举或动作／状态同时发生|COORD 或 CVB.SIM；K04 属同时伴随|[-며 义1—2](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=80253)|
|-고|并列、先后、持续结果状态等，也有辅助谓词连接专门用法|K51 看后欣慰＝CVB.SEQ；-고 싶다＝LINK.DESID，不与序列式合并|[-고¹，尤其义2与6](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=78583)|

**행복하다 的 -어 并不限于 있어。** K52 有 두어；K53 有 잘해 줘서。这里的 있어 是 있다＋-어，“存在／拥有”；韩语系词是 이다，不是 있다。来源：[있다¹](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=68796)。裸 -어 与 -어서 都可表达原因，不意味着在每一语体、时态和词序中可自由互换。

**흐뭇하다 可以直接出现人的话题 NP。** K49、51 明确是 아버지는，没有 마음；K37 的 마음이 则是“心／感受部位”名词。现有证据回答了“是不是只能有心”“能不能 TOP”，但尚未用同一语境的人称代词-NOM／TOP 最小对证明完整替换范围。

## 3. 什么能叫默认用法

目前能确认的是**构式可用**，还不能确认哪个在自然语料中最常用。词典选择的例句不构成随机频率样本；“词典先列”也不能自动叫默认。

1. 先提取谓词可记录的名词补足框架：如 좋아하다 的实体／事件 ACC，좋다 的实体／事件 NOM，만족하다 的实体／事件 에，마음에 들다 的实体／事件 NOM。
2. 对事件分句先区分**已发生原因／根据**、**一般或假设条件**、**先后反应**、**同时伴随**。不要将这些不同语义内容互相替换后仍算相同八节点表达。
3. -고 싶다 是特定辅助愿望结构；-었으면 싶다 是条件愿望结构。一般情绪前的 -어서／-니／-니까／-면 等跨多个谓词出现，有一般副词分句功能，**本批证据不够把它们一律当词汇选定的 Stimulus 补语**。
4. 绘图时建议先保留两份视图：一份只比较有直接名词框架证据的形式；另一份单列事件分句及关系。是否最终合并，应等全语言采用相同的“原因分句是否算八节点构式”规则；不能韩语用一般条件、芬兰语用事实补语而直接比较。

若后续要判“默认”，需另外取得描写语法的中性构式说明，或在相同人称、极性、事实性、语体下比较实际语料频率；目前不填一个想当然的唯一 CVB。

## 4. 新增例句与莱比锡式标注

切分采用词典词干或可恢复的底层形式；缩合／不规则变化逐例说明。`NMLZ` 名物化，`ADN` 定语，`ADN.QUOT` 引述式定语，`PROS` 前瞻，`LOC` 暂用于 에／에서 的可见格组，`DAT` 에게，`INST` 으로，`CONJ` 名词并列，`COORD` 谓词并列，`BEN` 受益辅助成分，`FIN` 句末，`EXCL` 感叹，`INT.EMB` 嵌入疑问，`NEG` 否定，`Q.POL` 礼貌疑问，其余同第一轮。CVB.REASON 与 CVB.CAUSAL 都表示原因连接，**不是 CAUS 使役**。只核入下列选中句／片段；未将来源网页中的其他被动或使役例句引入样本。
'''

def norm(t):return re.sub(r'\s+','',t)
def build():
 sources={}
 for x in EX:
  annotate_scope(x)
  raw=(B/(x['source']+'.txt')).read_text()
  assert norm(x['full_original'] or x['original']) in norm(raw),x['id']
  if x['full_original']:assert norm(x['original']) in norm(x['full_original']),x['id']
  assert len(x['morphemes'].split())==len(x['gloss'].split()),x['id']
  for m,g in zip(x['morphemes'].split(),x['gloss'].split()):assert m.count('-')==g.count('-'),(x['id'],m,g)
  for field in ['lexeme','original','morphemes','full_original']:
   x[field+'_romanized']=romanize(x[field]) if x[field] else None
  sources[x['source']]=json.loads((B/(x['source']+'_source.json')).read_text())
 body=[HEAD]
 for x in EX:
  body.append(f"\n### {x['id']} {x['lexeme']}：{x['content_type']}／{x['frame_group']}\n\n")
  body.append(f"证据：{x['evidence_type']}。原文：**{x['original']}**\n\n")
  body.append('```text\n'+aligned_rows([x['morphemes'],x['morphemes_romanized'],x['gloss']])+'\n```\n\n')
  body.append(f"“{x['translation_zh']}”\n\n")
  if x['full_original']:body.append(f"完整原句／相邻句：{x['full_original']}\n\n")
  body.append(f"来源：[官方词典：{x['source'].removeprefix('entry_')}]({sources[x['source']]['url']})，例句栏；E：{x['experiencer_flagging']}。\n\n{x['note']}\n")
 body.append('''
## 5. 留白与证据边界

- 珍爱义 아끼다 的事件形式、기쁘다／기뻐하다 的普通具体实体直接补足、반갑다／흐뭇하다 的事件名物化框架、행복하다 的普通实体直接刺激框架，本轮仍没有足够可靠正例。时间／生活类名词作幸福或愉快的主语，可能是在评价时段／生活，不能自动填成双价 E／Stimulus 框架。
- [본심词条](https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&nationCode=6&ParaWordNo=59944)还见“亲切／善意”-NOM＋기쁘다；该名词可能指品质或行为，暂不拿来补“普通具体实体”缺口，避免未经语义裁决补齐格子。
- 本轮以官方词典核对可用结构，没有新增可核读的 Mouton 正文，也未新增 NSM explication。不能因此把韩语的 Mouton 来源要求标为完成。
- 结构化例句及来源：[第二轮数据](../../research/korean_pilot/round2/examples.json)、[实际引证词条](../../research/korean_pilot/round2/sources.json)。搜索页仅作找例线索，以上19例均回到实际词条核对。
''')
 OUT.write_text(annotate_markdown(''.join(body)))
 (B/'examples.json').write_text(json.dumps(EX,ensure_ascii=False,indent=2)+'\n')
 for p in B.glob('ending_*_source.json'):sources[p.stem.removesuffix('_source')]=json.loads(p.read_text())
 sources['있다1']=json.loads((B/'있다1_source.json').read_text())
 sources['entry_본심']=json.loads((B/'entry_본심_source.json').read_text())
 (B/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
 print('Wrote',OUT,';',len(EX),'examples; literal source matching and gloss boundaries verified.')
if __name__=='__main__':build()
