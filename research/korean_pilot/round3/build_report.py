"""Nominal-only Korean comparison and verification of formerly missing cells."""
import json,re,sys
from pathlib import Path
from bs4 import BeautifulSoup
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent))
from romanization import romanize,annotate_markdown,aligned_rows
from comparison_scope import annotate_scope
ROOT=B.parents[2]
OUT=ROOT/'02_语言材料/韩语/韩语心理谓词_名词框架与缺例复核_第三轮.md'
EX=[]
def add(lex,source,original,morph,gloss,zh,content,frame,e,y,note,full=None,locator='正文例句',kind='来源原句连续摘录',relation='名词内容形式；保留实际格，不据此判定默认频率'):
 x=dict(id=f'K{60+len(EX)}',lexeme=lex,source=source,original=original,morphemes=morph,gloss=gloss,translation_zh=zh,content_type=content,realization='NP' if content in {'ENTITY','ENTITY_APPEARANCE','EVENT_REPORT','LEXICAL_EVENT'} else 'NMLZ_NP',frame_group=frame,experiencer_flagging=e,y_flagging=y,note=note,full_original=full,locator=locator,evidence_type=kind,relation_status=relation,final_semantic_node=None)
 EX.append(annotate_scope(x))
add('반갑다','entry_속간','속간이 반갑네.',
 '속간-이 반갑-네','resumption.of.publication-NOM be.glad-FIN',
 '复刊真让人高兴啊。','LEXICAL_EVENT','NOM','省略','NOM',
 '词典将 속간 定义为中断发行的报刊重新继续出版，明确是词汇事件名词；无需非名物化分句即可填 EVENT-NOM。反问、假设或语用补出的事件都不涉及本例。',
 '응. 즐겨 읽던 잡지라 속간이 반갑네.',kind='官方词典对话原句中的连续分句')
add('기뻐하다','news_기뻐_선물ACC','선물을 기뻐했다.',
 '선물-을 기뻐하-였-다','gift-ACC rejoice-PST-DECL',
 '为礼物感到高兴。','ENTITY','ACC','摘录省略；载句为 임원희-TOP','ACC',
 '报道前文明确礼物是花；按普通实体处理，不重释成收到花的事件。载句中的引述并非 Y 的实现。已证实普通实体也有 ACC，而不只是第一轮的胜利等事件名词。',
 '임원희는 "진짜 예쁘다"며 선물을 기뻐했다.',locator='2024-10-28，Sports Chosun，送花段落')
add('기뻐하다','news_기뻐_선물','유재석에게 받은 선물에 기뻐 했다.',
 '유재석-에게 받-은 선물-에 기뻐하-였-다','PN-DAT receive-ADN gift-LOC rejoice-PST-DECL',
 '为刘在锡送的礼物感到高兴。','ENTITY','EY','摘录省略；载句为 그-TOP','에',
 '礼物为前文所说的洗衣机。内部赠送者-DAT 不是 E；外层礼物-에 才是本例所查形式。받다 为词汇“收到”，不是语法被动。来源把 기뻐 했다 分写，原文保留；词素行按同一词 기뻐하다 切分。',
 locator='2022-10-29，Newsen，洗衣机礼物段落')
add('즐겁다','news_즐겁_그림책','아이들은 이 그림책이 즐겁다.',
 '아이-들-은 이 그림책-이 즐겁-다','child-PL-TOP this picture.book-NOM be.pleasant-DECL',
 '孩子们觉得这本绘本很有趣／愉快。','ENTITY','NOM','TOP','NOM',
 '实际实体是绘本，E 为孩子们-TOP；不把它补写成阅读绘本的事件。来源前面解释读者反应，但所选句的外层 Y 明确为绘本-NOM。具体义素和最终 LIKE／HAPPY 归属仍不在本轮裁决。',
 locator='2013-07-07，京乡新闻，绘本评论正文',kind='报道正文完整独立句')
add('흐뭇하다','news_흐뭇_네가','나에겐 지금의 네가 흐뭇해.',
 '나-에게-는 지금-의 네-가 흐뭇하-여','1SG-DAT-TOP now-GEN 2SG-NOM be.pleased-FIN',
 '对我而言，现在的你令我欣慰。','ENTITY','NOM','DAT＋TOP','NOM',
 '来自母亲对女儿说的话。나에겐 是 나에게는 的缩合；E 为我-DAT-TOP，Y 为你-NOM，两者不能互换。指人实体按实体保留；不把“现在的你”扩写成成长事件。此例也补足第二轮尚未取得的真实人称代词例。',
 locator='NewsTNT，〈突然飞来的40年前的照片〉，母女对话引语',kind='公开文章中的完整引语句')
add('흐뭇하다','daum_examples_흐뭇_4','자기만 잠을 깼다는 사실이 흐뭇하기까지 하다.',
 '자기-만 잠-을 깨-었-다는 사실-이 흐뭇하-기-까지 하-다',
 'self-ONLY sleep-ACC wake-PST-ADN.QUOT fact-NOM be.pleased-NMLZ-EVEN do-DECL',
 '甚至对只有自己醒来了这一事实感到欣慰。','EVENT','NOM','摘录内省略；反身词指回感受者','NOM',
 '事件经 -다는 사실 名词化，外层事实-NOM；不计为裸引述分句。心理谓词后的 -기까지 하다 是强调辅助形式，不是它的 Y 实现。잠을 깨다 是醒来，韩语原文没有语法使役。',
 '모두들 아직 잠결에 있는데 자기만 잠을 깼다는 사실이 흐뭇하기까지 하다.',locator='Daum 词典用例 kke001241909；交叉词条 잠결')
add('행복하다','news_행복_노래','노래하는 게 행복하다.',
 '노래하-는 것-이 행복하-다','sing-ADN NMLZ-NOM be.happy-DECL',
 '唱歌让我感到幸福。','EVENT','NOM','句内省略；引语说话者为歌手','NOM',
 '正文直接引语，不只出现在标题里。게＝것이，事件名物化-NOM，不能继续说 행복하다 只有连接分句。E 没有显现，不能据此填 E-NOM。',
 locator='2018-03-11，MK Sports，歌手自述',kind='报道正文中的完整引语句')
add('기쁘다','news_기쁘_소식','대통령 표창 소식이 기쁘다',
 '대통령 표창 소식-이 기쁘-다','president commendation news-NOM be.glad-DECL',
 '总统表彰的消息让我高兴。','EVENT_REPORT','NOM','引语句内省略','NOM',
 '已取得信息名词 소식-NOM 的实证，不等于取得礼物等具体物体-NOM 的实证。沿用第一轮 EVENT_REPORT 元数据，实体／事件最终节点仍不赋值；现行表明确显示这一细分。原文在引号内无句号，此处不添加。',
 locator='2026-08-17，蔚山每日，受表彰者家属的引语',kind='报道正文中的完整引语句')
add('행복하다','daum_examples_행복_40','나는 우리 딸 민애만으로도 행복한데',
 '나-는 우리 딸 민애-만-으로-도 행복하-ㄴ데',
 '1SG-TOP 1PL daughter PN-ONLY-INST-ADD be.happy-CVB.BACKGROUND',
 '仅有我们女儿敏爱，我就已经很幸福了，可是……','ENTITY','MAN_URO_TO','TOP','만으로도',
 '女儿是普通实体，外层为 -만으로도。这里不是女儿-NOM；-으로 的形式与 ONLY／ADD 分开保存。心理谓词自身末尾 -ㄴ데 接续后话，不是前置 Y 的分句形式，不能因此把已显现的实体 NP 排除。',
 '나는 우리 딸 민애만으로도 행복한데 시어머니께서는 계속 아들 타령을 하신다.',locator='Daum 词典用例 kke000218233；交叉词条 타령',relation='名词性根据／原因表达；未证明为词汇选定补语')
add('행복하다','daum_examples_행복_34','그녀가 기뻐하는 모습을 보는 것만으로도 나는 행복했다.',
 '그녀-가 기뻐하-는 모습-을 보-는 것-만-으로-도 나-는 행복하-였-다',
 '3SG.F-NOM rejoice-ADN scene-ACC see-ADN NMLZ-ONLY-INST-ADD 1SG-TOP be.happy-PST-DECL',
 '仅仅看到她高兴的样子，我就觉得幸福。','EVENT','MAN_URO_TO','TOP','만으로도',
 '事件名物化 NP＋만으로도，与 K68 的普通女儿实体实现相同的完整标记序列。그녀-NOM 是嵌入高兴的感受者；外层幸福的 E 是 나-TOP。此形式有“仅凭……就足够”的限定／标量意义，不叫中性默认表达。',
 locator='Daum 词典用例 kke000034994；交叉词条 기뻐하다',kind='词典完整独立句',relation='名词性根据／原因表达；未证明为词汇选定补语')
add('즐겁다','standard_content_즐겁다','문태석은 경채를 만나기가 즐거웠다.',
 '문태석-은 경채-를 만나-기-가 즐겁-었-다',
 'PN-TOP PN-ACC meet-NMLZ-NOM be.pleasant-PST-DECL',
 '文泰锡很乐于见京彩。','EVENT','NOM','TOP','NOM',
 '《标准国语大辞典》明列 【…이】【-기가】；此为 -기-NOM 的直接文学例，不需要依赖第二轮的反问例。-기 与 -는 것 仍保留为内部实现变体，外层同组 NOM。',
 locator='义项例句，原标出处：채만식，돼지',kind='官方词典引用的文学完整句')
add('흐뭇하다','daum_examples_흐뭇_3','그는 학사모를 쓴 아들의 모습이 흐뭇하고 대견스러웠다.',
 '그-는 학사모-를 쓰-ㄴ 아들-의 모습-이 흐뭇하-고 대견스럽-었-다',
 '3SG-TOP graduation.cap-ACC wear-ADN son-GEN appearance-NOM be.pleased-COORD be.proud-PST-DECL',
 '他对儿子戴着学士帽的样子感到欣慰和骄傲。','ENTITY_APPEARANCE','NOM','TOP','NOM',
 '词典补强：感受者直接用他-TOP，外层为儿子的样子-NOM，无 마음。这里记录外貌／样态名词，不擅自扩写成毕业事件；与 K64 指人的 ENTITY 分开保留子类。',
 locator='Daum 词典用例 kke000243006；交叉词条 흐뭇하다',kind='词典完整独立句')
add('기쁘다','daum_examples_기쁘_15','너의 합격 소식에 다들 얼마나 기쁜지 모른다.',
 '너-의 합격 소식-에 다들 얼마나 기쁘-ㄴ지 모르-ㄴ다',
 '2SG-GEN passing news-LOC everyone how.much be.glad-INT.EMB not.know-DECL',
 '大家对你考上的消息高兴极了。','EVENT_REPORT','EY','다들，零格','에',
 '又见信息 NP-에。얼마나…-ㄴ지 모른다 为高程度表达；它在心理谓词外层，消息仍以 NP-에 实现，不是把该嵌入疑问当心理刺激分句。普通具体物体仍未获证。',
 locator='Daum 词典用例 kke000081420；交叉词条 모르다',kind='词典完整独立句',relation='名词性原因／根据；与词典明列的 NOM 配价分开存储')

HEAD='''# 韩语心理谓词：名词框架与缺例复核（第三轮）

核查：2026-11-14。按用户新要求，**除 -고 싶다 外，不讨论外层内容以非名物化分句实现的构式**。条件愿望 -었으면 싶다、条件引述 -었으면 하고 바라다，以及原因、条件、先后、伴随分句全部排除。事件名词及事件名物化 NP 继续保留。

排除针对的是 **Y 的外层实现**：名物化 NP 内部的谓词／定语结构不是本次要排除的裸分句；若心理谓词已有明确的 NP 内容，其载句另有引语、原因说明或后续连接，不能据此删除 NP 证据。第一、二轮原文与例号保留，均增加 `comparison_eligible` 与排除原因；以本稿表格为当前阅读入口。

本轮补 **13例，K60—K72**，主要新增来源是韩国国立国语院《표준국어대사전》、Daum 收录的韩国语词典用例，以及可回查正文的报刊实例。原文、罗马转写、莱比锡式标注、中文译文和内容细分逐条保留。没有用自造句补空格。

## 1. 收窄后的比较表

本表记录可见的 **Y 形式**；完整 E／Y 框架必须再读逐例的 E 标记。`NOM` 不预设都是相同句法主语关系。实体、信息实体、样态实体和事件的细分保留；本轮不作最终八节点词义归并。

|词项|实体侧：经核对的名词形式|事件侧：经核对的名词形式／保留例外|复核结果|
|---|---|---|---|
|좋아하다|ACC K01|ACC K02—03|两侧已有；K04 条件式退出|
|좋다|NOM／TOP K05、39—40|NOM K41|K06 普通工作／任务仍不算事件|
|사랑하다|ACC K07—09|ACC K42|热爱活动的事件用法已有，保留义项差别|
|아끼다，珍爱义|ACC K10|**仍未证实**|两部官方词典的珍爱义释义均指人／物；节省／不吝惜义不能补到此处|
|원하다|ACC K11—12|ACC，可不显现 K13—14|保留实际省格，不补写外层 ACC|
|바라다|ACC K15|ACC K16|K17 条件引述退出|
|싶다，WANT 义|**结构上不适用：辅助谓词，不独立接实体 NP**|**仅 -고 싶다 K18—20**|K21 条件愿望退出；内部所看／所喝的对象不算 싶다 的直接实体补足|
|기쁘다|信息 NP-NOM K67；信息 NP-에 K72；**具体物体仍未证实**|词汇事件-NOM K22；事件名物化-NOM K44|信息名词沿用 EVENT_REPORT 元数据；不把消息和具体物体的证据混在一起|
|기뻐하다|**普通礼物-ACC K61；普通礼物-에 K62**|词汇事件-ACC K24；事件名物化-ACC K47|这次补齐了普通实体，而且同一名词类有两种格形式|
|즐겁다|**绘本-NOM K63**|名物化-NOM K48；**-기-NOM K70**|官方词典另有明确 -기가 配价与文学例；一天 K26 仍作内容待定|
|즐기다|ACC K28|词汇事件／事件名物化-ACC K29—31|两侧已有|
|행복하다|**普通女儿 NP-만으로도 K68**；直接具体物体-NOM 未证|**事件名物化-NOM K66；事件名物化-만으로도 K69**；事实名词-만으로 K59|完整 -만으로도 在实体／事件两侧都有；此为带标量意义的名词根据／原因式，尚非词汇选定配价的证明|
|만족하다|职业-에 K34|事件名物化-에 K43|两侧同为 에；结果 K33 内容仍待定|
|반갑다|朋友-NOM K35|**复刊-NOM K60**|缺事件的问题已解决；是词汇事件名词|
|흐뭇하다|**你-NOM K64；儿子的样子-NOM K71**|**事实名词化-NOM K65**|实体／事件两侧均补到；E 可见 DAT-TOP 或人称 TOP，不要求 마음|
|마음에 들다|实体-NOM／TOP K38、58|事件名物化-NOM K57|两侧已有；마음-에 属惯用构式内部，不是刺激 LOC|

**最清楚的新补齐项**是 기뻐하다、즐겁다、반갑다、흐뭇하다 的实体／事件对应；행복하다 还取得相同完整标记 -만으로도 的两侧实例。具体是否把名词根据／原因式与所选补足式并入同一地图构式，数据先保留区别，不凭 LOC／INST 字面直接合并。

## 2. 问号查证的依据与限度

### 아끼다：珍爱义事件形式仍未取得正例

《표준국어대사전》[아끼다，第2义](https://stdict.korean.go.kr/search/searchView.do?word_no=216488)释义明确提到把“物或人”视为珍贵而照料、爱护；第1义是不随便消耗钱、物、时间。第一轮官方基础词典也分这两个义项。检查 Daum 中取得的115条不同用例以及事件名物化检索，未得到珍爱义的可靠 EVENT-NP 正例。

努力、支持、称赞等名词后“不吝惜”的用法，以及节省时间的用法，不能仅因有活动相关名词便移入珍爱义。**这支持“目前有义项限制证据”，还不支持把所有事件名词／名物化一律标为不合语法。** 此格保持未证，不造星号句。

### 기쁘다：信息 NP 已取得，普通具体物体仍未取得

[《标准国语大辞典》기쁘다](https://stdict.korean.go.kr/search/searchView.do?word_no=405464)明列 NOM 框架，例子主要为归来、考上等事件；另说明可出现连接形式，但这部分现按用户要求退出。K67 的消息-NOM、K72 的消息-에 是真实的名词证据，分别存信息实体／事件报告子类。

在 Daum 该词检出的用例集中，含礼物的例子多为收到礼物后高兴，或礼物使人高兴。前者的 Y 是分句，后者有 CAUS，均未用来补普通具体实体格。**具体物体未取到正例，与“NP-NOM 整体不存在”完全不同。**

### 싶다：不再作为普通缺例格

[官方词典的싶다第1义](__SIPHTA_URL__)将其标为辅助形容词，并明确接在动词后使用 -고 싶다。因此独立“想要一个实体”的 NP 格子不再简单打问号；记为该辅助构式的结构不适用。K18—20 中 ACC／NOM 的东西仍属嵌入动词的对象。这里不排除整个韩语 WANT 的实体表达，원하다 的实体 ACC 已有 K11—12。

## 3. 新增例句与标注

标注由本稿补配。`ADN.QUOT` 引述式定语，`INT.EMB` 嵌入疑问，`LOC` 暂标 에 的可见形式，`INST` 标 으로，`ONLY` 限定，`ADD` 添加／标量焦点，`FIN` 句末，`CVB.BACKGROUND` 后接背景／转折；其余同第一轮。句末的非终结形式或外部程度结构不改变其前方 NP 的外层格。
'''

def norm(t):return re.sub(r'\s+','',t)
def build():
 sources={}
 for x in EX:
  raw=(B/(x['source']+'.txt')).read_text()
  assert norm(x['full_original'] or x['original']) in norm(raw),(x['id'],x['full_original'] or x['original'])
  if x['full_original']:assert norm(x['original']) in norm(x['full_original']),x['id']
  assert len(x['morphemes'].split())==len(x['gloss'].split()),x['id']
  for m,g in zip(x['morphemes'].split(),x['gloss'].split()):assert m.count('-')==g.count('-'),(x['id'],m,g)
  for f in ['lexeme','original','morphemes','full_original']:x[f+'_romanized']=romanize(x[f]) if x[f] else None
  s=json.loads((B/(x['source']+'_source.json')).read_text());assert s.get('status')==200,x['source']
  sources[x['source']]=s
 # Verify links against fetched lemma entries, rather than guessing entry identifiers.
 siphta=json.loads((B.parent/'dict_싶다_source.json').read_text())
 head=HEAD.replace('__SIPHTA_URL__',siphta['url'])
 sources['dict_싶다']=siphta
 for name in ['standard_content_아끼다','standard_content_기쁘다','standard_content_흐뭇하다','standard_content_반갑다','standard_content_행복하다','daum_entry_기쁘다','daum_entry_행복하다']:
  sources[name]=json.loads((B/(name+'_source.json')).read_text())
 body=[head]
 for x in EX:
  s=sources[x['source']];url=s.get('public_entry_url') or s.get('final_url') or s['url']
  body.append(f"\n### {x['id']} {x['lexeme']}：{x['content_type']}／{x['frame_group']}\n\n证据：{x['evidence_type']}。原文：**{x['original']}**\n\n")
  body.append('```text\n'+aligned_rows([x['morphemes'],x['morphemes_romanized'],x['gloss']])+'\n```\n\n')
  body.append(f"“{x['translation_zh']}”\n\n")
  if x['full_original']:body.append(f"完整载句：{x['full_original']}\n\n")
  body.append(f"来源：[{x['locator']}]({url})。E：{x['experiencer_flagging']}；Y：{x['y_flagging']}。\n\n{x['note']}\n")
 body.append('''
## 4. 当前数据入口

- [本轮13例](../../research/korean_pilot/round3/examples.json)：完整保留来源和切分；本轮正例的目标均为名词形式。
- [当前允许形式的合并记录](../../research/korean_pilot/round3/current_comparison_examples.json)：第一至三轮合并，滤去所有被排除的非名物化分句形式；内容待定的名词记录仍标待定，不当成最终地图节点。
- [已排除记录与原因](../../research/korean_pilot/round3/excluded_examples.json)：保留证据和旧例号，以免误用旧表恢复分句。
- [实际引证来源](../../research/korean_pilot/round3/sources.json)：官方词典动态正文的请求参数、Daum 用例编号、报刊实际地址均可回查。搜索结果只作找例线索，未当作最终引文。
- [缺例格逐项检索记录](../../research/korean_pilot/round3/search_audit.json)：记录每个原问号格的结论、检索入口，以及下载用例按来源 ID 去重后的数量；这不是随机频率样本，不能据数量推断默认构式。

第一轮 K22／24 的胜利仍是事件／结果名词；K06 工作／任务仍按用户复核不计事件。本轮不新增 NSM 定义，不改变 Mouton 正文尚待落实的来源状态。
''')
 OUT.write_text(annotate_markdown(''.join(body)))
 all_ex=[]
 for p in [B.parent/'examples.json',B.parent/'round2/examples.json']:
  all_ex.extend(annotate_scope(x) for x in json.loads(p.read_text()))
 all_ex+=EX
 assert len({x['id'] for x in all_ex})==len(all_ex)
 included=[x for x in all_ex if x['comparison_eligible']]
 excluded=[x for x in all_ex if not x['comparison_eligible']]
 groups={}
 for x in included:groups.setdefault(x['frame_group'],[]).append(x['id'])
 (B/'current_frame_groups.json').write_text(json.dumps({'status':'仅当前允许形式的外层Y分组；须继续核对E标记及词义，不是最终地图输入','groups':groups},ensure_ascii=False,indent=2)+'\n')
 for name,data in [('examples',EX),('current_comparison_examples',included),('excluded_examples',excluded),('sources',sources)]:
  (B/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(f'Wrote {len(EX)} new examples; {len(all_ex)} total, {len(included)} in current formal scope, {len(excluded)} excluded. Sources and gloss boundaries checked.')
if __name__=='__main__':build()
