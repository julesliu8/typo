"""Build the reviewed Korean pilot; never replace original source downloads."""
import json
import re
import pathlib
from romanization import romanize, annotate_markdown, aligned_rows

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = ROOT / '02_语言材料/韩语/韩语心理谓词_实体事件构式_例句与标注.md'
EX = []
SOURCES = {}
for p in B.glob('dict_*_source.json'):
    d = json.loads(p.read_text())
    if d.get('status') == 200 and not p.stem.startswith('dict_search'):
        SOURCES[p.stem.removesuffix('_source')] = d
SOURCES['YOON03'] = {
    'title': 'Yoon, Kyung-Joo. 2003. Constructing a Korean natural semantic metalanguage. ANU PhD.',
    'url': 'https://doi.org/10.25911/5d5158f90d84d',
    'fulltext_url': 'https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/d0ab13cc-a341-442c-81fc-8e9c6f281fe3/content',
    'local': 'research/korean_pilot/yoon2003_repository_fulltext.txt',
    'accessed': '2026-11-13',
    'read_status': '机构库提供的全文抽取文本，已核读指定章节；原扫描 PDF 未成功取得，未完成图像核页',
}
(B / 'yoon2003_repository_fulltext.txt').write_bytes((B / 'yoon2003_text_api.html').read_bytes())


def add(lex, sense, original, morph, gloss, zh, content, realization, frame,
        e_flag, y_flag, note='', kind='词典搭配短语', source=None, locator=None, full=None):
    source = source or 'dict_' + lex
    EX.append(dict(id=f'K{len(EX)+1:02}', lexeme=lex, sense=sense, original=original,
                   morphemes=morph, gloss=gloss, translation_zh=zh,
                   content_type=content, realization=realization, frame_group=frame,
                   experiencer_flagging=e_flag, y_flagging=y_flag,
                   source=source, locator=locator or f'义项 {sense}', evidence_type=kind,
                   note=note, full_original=full, final_semantic_node=None,
                   lexeme_romanized=romanize(lex), romanization=romanize(original),
                   morphemes_romanized=romanize(morph),
                   full_original_romanized=romanize(full) if full else None,
                   romanization_system='Yale-style spelling transliteration; author romanization retained for YOON03'))


add('좋아하다','1','꽃을 좋아하다.','꽃-을 좋아하-다','flower-ACC like-DECL','喜欢花。','ENTITY','NP','ACC','省略','ACC')
add('좋아하다','3','그림 그리기를 좋아하다.','그림 그리-기-를 좋아하-다','picture draw-NMLZ-ACC like-DECL','喜欢画画。','EVENT','NMLZ_NP','ACC','省略','ACC','-기 名物化后带外层 ACC；그림 是嵌入活动内部的名词。')
add('좋아하다','3','책 보는 것을 좋아하다.','책 보-는 것-을 좋아하-다','book read-ADN NMLZ-ACC like-DECL','喜欢看书。','EVENT','ADN_KES_NP','ACC','省略','ACC','把 -는 것 作为名物化构造标记；不把内部 책 当外层 Y。')
add('좋아하다','5','우리 집 강아지는 눈이 오면 이리저리 뛰어 다니며 너무 좋아한다.',
    '우리 집 강아지-는 눈-이 오-면 이리저리 뛰-어 다니-며 너무 좋아하-ㄴ다',
    '1PL house puppy-TOP snow-NOM come-COND here.and.there jump-CVB go.around-CVB very rejoice-DECL',
    '我家的小狗一下雪，就四处蹦跳，特别高兴。','EVENT','CONDITIONAL_CLAUSE','COND_MYEON','TOP','无外层格；-면连接',
    '此为词典第5义“表现高兴”，词典框架只有 1이 좋아하다。不能沿用第1／3义 ACC 配价；-면 是条件／情境连接。',kind='词典完整例句')
add('좋다','10','나는 이 드라마가 정말 좋아요.','나-는 이 드라마-가 정말 좋-아요',
    '1SG-TOP this drama-NOM really like-POL','我真的喜欢这部电视剧。','ENTITY','NP','NOM','TOP','NOM',
    '词典框架 1이 2가 좋다；本例实际 E 为 TOP。只取第10义，不能把所有 좋다 都算 LIKE。',kind='词典完整例句')
add('좋다','10','하는 일이 좋다.','하-는 일-이 좋-다','do-ADN work-NOM like-DECL','喜欢所做的工作／事情。',
    'UNRESOLVED','ADN_LEXICAL_NOUN_NP','NOM','省略','NOM',
    '일 可指工作、任务或事情，暂不把它强制判为 EVENT；也不同于专门名物化的 -는 것。')
add('사랑하다','2','동물을 사랑하다.','동물-을 사랑하-다','animal-ACC love-DECL','爱护动物。','ENTITY','NP','ACC','省略','ACC','第2义含珍爱、照护，和第1义性爱／恋爱情感分存。')
add('사랑하다','4','음악을 사랑하다.','음악-을 사랑하-다','music-ACC love-DECL','热爱音乐。','ENTITY','NP','ACC','省略','ACC','音乐按抽象实体记录；不补出听音乐事件。')
add('사랑하다','4','평화를 사랑하다.','평화-를 사랑하-다','peace-ACC love-DECL','热爱和平。','ENTITY','NP','ACC','省略','ACC','抽象实体／状态名词；是否纳入最终 ENTITY 比较概念仍可复核。')
add('아끼다','2','친구를 아끼다.','친구-를 아끼-다','friend-ACC cherish-DECL','珍爱朋友。','ENTITY','NP','ACC','省略','ACC','只收珍爱义；第1义“节省”排除。')
add('원하다','1','돈을 원하다.','돈-을 원하-다','money-ACC want-DECL','想要钱。','ENTITY','NP','ACC','省略','ACC')
add('원하다','WANT','na-nun i kes-ul wenha-n-ta.','na-nun i kes-ul wenha-n-ta','1SG-TOP this thing-ACC want-PRS-DECL',
    '我想要这个东西。','ENTITY','NP','ACC','TOP','ACC','作者原文为罗马字；韩文转写为 나는 이것을 원한다。统一原文 TC→TOP、AC→ACC、IN→PRS、DC→DECL。',
    kind='NSM文献作者例句',source='YOON03',locator='p.138，§3.7.2.3 (12)')
add('원하다','WANT','na-nun i kes-ul po-ki(-lul) wenha-n-ta.',
    'na-nun i kes-ul po-ki(-lul) wenha-n-ta','1SG-TOP this thing-ACC see-NMLZ(-ACC) want-PRS-DECL',
    '我想看这个。','EVENT','NMLZ_NP','ACC','TOP','ACC，可省略',
    '保留作者括号：外层 ACC 可不显现。i kes-ul 是嵌入“看”的对象，po-ki(-lul) 才是 WANT 的事件补语。',
    kind='NSM文献作者例句',source='YOON03',locator='p.126，§3.7.1.3 (15)b')
add('원하다','WANT','na-nun ney-ka cikum i il-ul ha-ki-lul wenha-n-ta.',
    'na-nun ney-ka cikum i il-ul ha-ki-lul wenha-n-ta','1SG-TOP 2SG-NOM now this work-ACC do-NMLZ-ACC want-PRS-DECL',
    '我希望你现在做这件事。','EVENT','NMLZ_NP','ACC','TOP','ACC',
    '非同主语事件；嵌入主语 ney-ka-NOM 与外层 E-TOP 分开。愿望内容是他人行动，不是 CAUS 句式。',
    kind='NSM文献作者例句',source='YOON03',locator='p.128，§3.7.1.3 (18)a')
add('바라다','2','돈을 바라다.','돈-을 바라-다','money-ACC desire-DECL','想得到钱。','ENTITY','NP','ACC','省略','ACC','第2义为想拥有；第3义“朝……看”排除。')
add('바라다','1','건강하기를 바라다.','건강하-기-를 바라-다','be.healthy-NMLZ-ACC hope-DECL','希望身体健康。','EVENT','NMLZ_NP','ACC','省略','ACC','状态补语也归 EVENT 内容；与 ENTITY 钱分义存储。')
add('바라다','1','지수는 빨리 승진해서 돈을 조금만 더 벌었으면 하고 바랐다.',
    '지수-는 빨리 승진하-여서 돈-을 조금-만 더 벌-었-으면 하-고 바라-았-다',
    'PN-TOP quickly get.promoted-CVB.CAUSAL money-ACC a.little-ONLY more earn-PST-COND do-QUOT hope-PST-DECL',
    '智秀希望能早些晋升，再多赚一点钱。','EVENT','CONDITIONAL_QUOTATIVE_CLAUSE','COND_QUOT','TOP','无外层格；-었으면 하고',
    '词典明确记此替代结构。“CAUSAL”是原因连接标签，不是 CAUS 使役；本例无语法使役。-었- 在愿望条件中不简单译为过去已发生。',kind='词典完整例句')
add('싶다','WANT','na-nun i kes-ul po-ko·siph-ta.','na-nun i kes-ul po-ko siph-ta',
    '1SG-TOP this thing-ACC see-CVB want-DECL','我想看这个。','EVENT','VP_KO_SIPHTA','KO_SIPHTA','TOP','无外层格；V-고',
    'i kes-ul-ACC 是“看”的宾语，不是“想要实体”的直接框架。此例与 K13 是作者的同内容对照。',
    kind='NSM文献作者例句',source='YOON03',locator='p.126，§3.7.1.3 (15)a')
add('싶다','1','좀 쉬고 싶어서요.','좀 쉬-고 싶-어서-요','a.little rest-CVB want-CVB.CAUSAL-POL',
    '因为想稍微休息一下。','EVENT','VP_KO_SIPHTA','KO_SIPHTA','省略','无外层格；V-고',
    '对话答句以 -어서요 结尾；保留原形，不擅改为完整陈述句。',kind='词典对话答句')
add('싶다','1','나는 시원한 게 마시고 싶어서',
    '나-는 시원하-ㄴ 것-이 마시-고 싶-어서',
    '1SG-TOP cool-ADN thing-NOM drink-CVB want-CVB.CAUSAL',
    '因为我想喝点凉的东西，……','EVENT','VP_KO_SIPHTA','KO_SIPHTA','TOP','无外层格；内部对象-NOM',
    '从完整原句摘录前半分句；게＝것이。“凉的东西”是嵌入“喝”的对象，不能据其 NOM 把整个 WANT 内容标为 ENTITY-NOM。',
    kind='词典原句的连续分句摘录',full='나는 시원한 게 마시고 싶어서 편의점에 맥주를 사러 갔다.')
add('싶다','4','저는 피자를 먹었으면 싶어요.','저-는 피자-를 먹-었-으면 싶-어요',
    '1SG.HUM-TOP pizza-ACC eat-PST-COND wish-POL','我希望吃比萨。','EVENT','CONDITIONAL_SIPHTA','MYEON_SIPHTA','TOP','无外层格；-었으면',
    'Yoon 不把 -(으)면 싶다 与 WANT 基元的两形式直接并为同一 allolex；本稿分组保留。',kind='词典完整例句')
add('기쁘다','1','승리가 기쁘다.','승리-가 기쁘-다','victory-NOM be.glad-DECL','为胜利高兴。','EVENT','LEXICAL_EVENT_NP','NOM','省略','NOM','胜利为词汇事件／结果 NP。普通实体一侧仍缺例。')
add('기쁘다','1','나는 이번 시험에서 일 등을 해서 매우 기뻤다.',
    '나-는 이번 시험-에서 일 등-을 하-여서 매우 기쁘-었-다',
    '1SG-TOP this.time exam-LOC one rank-ACC do-CVB.CAUSAL very be.glad-PST-DECL',
    '我这次考试得了第一名，非常高兴。','EVENT','CAUSAL_CLAUSE','CAUSE_EOSEO','TOP','无外层格；-어서连接',
    '明确因果连接分句，不等同于带 NOM 的事件 NP；尚未据此证明它是所选补语。',kind='词典完整例句')
add('기뻐하다','1','승리를 기뻐하다.','승리-를 기뻐하-다','victory-ACC rejoice-DECL','为胜利高兴。','EVENT','LEXICAL_EVENT_NP','ACC','省略','ACC',
    '词典框架同时记录 1이 2에／2를 기뻐하다。기뻐하다 的 -어하다 不作使役；不是 기쁘게 하다“使高兴”。')
add('기뻐하다','1','어머니는 딸의 합격 소식에 매우 기뻐하셨다.',
    '어머니-는 딸-의 합격 소식-에 매우 기뻐하-시-었-다',
    'mother-TOP daughter-GEN passing news-LOC very rejoice-HON-PST-DECL',
    '母亲因女儿考上的消息非常高兴。','EVENT_REPORT','NP','EY','TOP','에',
    '소식“消息”为信息实体，内容报告一个事件。独立记 EVENT_REPORT，暂不强塞入实体／事件八节点；에 的具体论元关系待语法正文核查。',kind='词典完整例句')
add('즐겁다','1','하루가 즐겁다.','하루-가 즐겁-다','day-NOM be.pleasant-DECL','一天过得愉快。','UNRESOLVED','NP','NOM','省略','NOM','时段名词是否与感受者共同经历的事件有关，暂不裁决。')
add('즐겁다','1','오랜만에 친구를 만나니 너무 반갑고 즐거웠다.',
    '오랜만-에 친구-를 만나-니 너무 반갑-고 즐겁-었-다',
    'long.interval-LOC friend-ACC meet-CVB.REASON very be.glad.to.see-COORD be.joyful-PST-DECL',
    '久别后见到朋友，特别高兴愉快。','EVENT','REASON_CLAUSE','REASON_NI','省略','无外层格；-니连接',
    '同一个分句背景关联 반갑다 和 즐겁다；不把 친구를-ACC 当这两个心理谓词的外层 Y。',kind='词典完整例句')
add('즐기다','2','술을 즐기다.','술-을 즐기-다','alcohol-ACC enjoy-DECL','喜欢酒／好酒。','ENTITY','NP','ACC','省略','ACC','按用户规则不重释为喝酒事件；词典该义含“喜欢而常做”的习惯性。')
add('즐기다','2','산책을 즐기다.','산책-을 즐기-다','walk-ACC enjoy-DECL','喜欢散步。','EVENT','LEXICAL_EVENT_NP','ACC','省略','ACC','산책 是词汇活动名词，没有在本例中生产性添加名物化后缀。')
add('즐기다','2','저는 매주 가족들과 산에 오르는 걸 즐깁니다.',
    '저-는 매주 가족-들-과 산-에 오르-는 것-을 즐기-ㅂ니다',
    '1SG.HUM-TOP every.week family-PL-COM mountain-LOC climb-ADN NMLZ-ACC enjoy-DECL.POL',
    '我喜欢每周和家人登山。','EVENT','ADN_KES_NP','ACC','TOP','ACC','걸＝것을；山的 에 为嵌入登山事件内部处所标记。',kind='词典对话完整句')
add('즐기다','1','우리는 바닷가에서 여름휴가를 즐겼다.',
    '우리-는 바닷가-에서 여름휴가-를 즐기-었-다',
    '1PL-TOP beach-LOC summer.vacation-ACC enjoy-PST-DECL','我们在海边享受了暑假。','EVENT','LEXICAL_EVENT_NP','ACC','TOP','ACC',
    '第1义为充分体验／享受，第2义为习惯性爱好，分义记录；不自动同归 LIKE。',kind='词典完整例句')
add('행복하다','1','나는 사랑스러운 자녀들이 있어 늘 행복하다고 느낀다.',
    '나-는 사랑스럽-은 자녀-들-이 있-어 늘 행복하-다-고 느끼-ㄴ다',
    '1SG-TOP lovable-ADN child-PL-NOM exist-CVB always be.happy-DECL-QUOT feel-DECL',
    '我因有可爱的孩子，总觉得很幸福。','EVENT','EXISTENTIAL_BACKGROUND_CLAUSE','BACKGROUND_EO','TOP','无外层格；있어连接',
    '행복하다 的词典框架为 1이 행복하다，一价。子女 NOM 是 있- 的论元，不能当作幸福谓词的直接刺激 NOM；末尾感到的宾语是引述内容。',kind='词典完整例句')
add('만족하다','1','결과에 만족하다.','결과-에 만족하-다','result-LOC be.satisfied-DECL','对结果满意。','UNRESOLVED','NP','EY','省略','에','词典为 동사 满足义；结果名词不足以独自判 ENTITY／EVENT。')
add('만족하다','1','지수는 자기 직업에 만족하지 못해서',
    '지수-는 자기 직업-에 만족하-지 못하-여서',
    'PN-TOP self job-LOC be.satisfied-LINK NEG.ABIL-CVB.CAUSAL',
    '因为智秀对自己的职业不满意，……','ENTITY','NP','EY','TOP','에',
    '抽象实体“职业”不补成从事该职业事件。保留否定；-지 是否定结构连接成分，记 LINK，不作事件名物化。',
    kind='词典原句的连续分句摘录',full='지수는 자기 직업에 만족하지 못해서 항상 직업을 바꿀 생각을 한다.')
add('반갑다','1','나는 오랜만에 만난 고향 친구가 너무나 반가워서',
    '나-는 오랜만-에 만나-ㄴ 고향 친구-가 너무나 반갑-어서',
    '1SG-TOP long.interval-LOC meet-ADN hometown friend-NOM very be.glad.to.see-CVB.CAUSAL',
    '因为我见到久别的故乡朋友特别高兴，……','ENTITY','NP','NOM','TOP','NOM',
    '词义含相逢背景，但 Y 的可见形式是普通人称实体“朋友”；不因背景而改记事件。반갑다 为 ㅂ 不规则，底层词干切分保留 반갑-。',
    kind='词典原句的连续分句摘录',full='나는 오랜만에 만난 고향 친구가 너무나 반가워서 한참 동안이나 손을 붙잡고 놓지 않았다.')
add('반갑다','1','그동안 누군지 한번 꼭 보고 싶었는데 이렇게 만나게 되어 반갑습니다.',
    '그동안 누구-이-ㄴ지 한번 꼭 보-고 싶-었-는데 이렇게 만나-게 되-어서 반갑-습니다',
    'meanwhile who-COP-INT.EMB once certainly see-CVB want-PST-CVB.BACKGROUND like.this meet-ADV become-CVB.CAUSAL be.glad.to.see-DECL.POL',
    '一直想见见您是谁，能这样见面很高兴。','EVENT','CAUSAL_CLAUSE','CAUSE_EOSEO','省略','无外层格；-게 되어서',
    '-게 되다 为事态形成／变化，不是 -게 하다 使役，也不是被动。原句可见的多个事件结构逐层分开。',kind='词典对话完整句')
add('흐뭇하다','1','열심히 공부하는 동생을 보니 마음이 흐뭇했다.',
    '열심히 공부하-는 동생-을 보-니 마음-이 흐뭇하-였-다',
    'diligently study-ADN younger.sibling-ACC see-CVB.REASON mind-NOM be.pleased-PST-DECL',
    '看到认真学习的弟弟／妹妹，心里很欣慰。','EVENT','REASON_CLAUSE','REASON_NI','省略；内部心-NOM','无外层格；-니连接',
    'NOM 的 마음“心”是感受部位／内部状态，不是 Stimulus。不能根据词典 1이 2가 的数字框架把它误编码为 Y-NOM。',kind='词典完整例句')
add('마음에들다','惯用语','이 옷은 디자인도 예쁘고, 값도 싸고, 나하고 잘 어울리기까지 해서 아주 마음에 든다.',
    '이 옷-은 디자인-도 예쁘-고 값-도 싸-고 나-하고 잘 어울리-기-까지 하-여서 아주 마음-에 들-ㄴ다',
    'this clothing-TOP design-ADD pretty-COORD price-ADD cheap-COORD 1SG-COM well suit-NMLZ-EVEN do-CVB.CAUSAL very mind-LOC enter-DECL',
    '这件衣服设计漂亮、价格便宜，还很适合我，十分合我心意。','ENTITY','NP','MIND_EY_CONSTRUCTION','省略；内部适合事件有1SG-COM','TOP',
    '词典惯用语附在 마음 词条下，列 1이 2가 마음에 들다。实际例中的 Y 是 옷-TOP，마음-에 是构式内部成分；나-하고 属 어울리다，不据它给外层 E 标 COM。',kind='词典完整例句',locator='마음词条附录：惯用语 마음에 들다')
add('좋다','心理吸引义','na-nun i kes-un coh-ta.','na-nun i kes-un coh-ta','1SG-TOP this thing-TOP like-DECL',
    '我喜欢这个东西。','ENTITY','NP','Y_TOP','TOP','TOP',
    '作者用双话题句讨论 GOOD／LIKE 多义。本例只支持实际 TOP 实现；不从 TOP 反推未显现的 NOM。',
    kind='NSM文献作者例句',source='YOON03',locator='p.113，§3.5.1 (7)')
add('좋다','心理吸引义','na-nun i mas-i coh-ta.','na-nun i mas-i coh-ta','1SG-TOP this taste-NOM like-DECL',
    '我喜欢这个味道。','ENTITY','NP','NOM','TOP','NOM',
    '统一作者原 gloss：实际 -nun 记 TOP，即使原行标签有 NM 的不一致。与“这个东西味道好”的非心理评价义分开。',
    kind='NSM文献作者例句',source='YOON03',locator='p.113，§3.5.1 (9)')


def norm(t):
    return re.sub(r'\s+', '', t)


def validate():
    for x in EX:
        assert len(x['morphemes'].split()) == len(x['gloss'].split()), x['id']
        # Word-level alignment, plus segment counts; abbreviations use '.' for fusion.
        for m, g in zip(x['morphemes'].split(), x['gloss'].split()):
            assert m.count('-') == g.count('-'), (x['id'], m, g)
        p = B / ('yoon2003_repository_fulltext.txt' if x['source'] == 'YOON03' else x['source'] + '.txt')
        raw = norm(p.read_text())
        target = x['full_original'] or x['original']
        assert norm(target) in raw, (x['id'], target)
        if x['full_original']:
            assert norm(x['original']) in norm(x['full_original']), x['id']


HEADER = '''# 韩语心理谓词：实体／事件构式、例句与标注

采集与核读：2026-11-13。第一轮按词项、义项、内容类型与可见形式记录，**尚不作最终八节点语义裁决**。原句来自韩国国立国语院《한국어기초사전》及 Yoon（2003）的 NSM 论文；本轮没有用自造句填补缺口。共计 **{count} 条记录、16 个词项（含惯用语）**；其中含完整句、对话句、原句连续分句摘录和词典明确给出的搭配短语，证据类型逐条注明。

## 1. 构式与词项概览

`?`＝本轮未取得相应实例，不表示不能使用。ENTITY 包括普通抽象实体；词汇事件名词、生产性名物化和连接分句分别标记。`EVENT_REPORT`／`UNRESOLVED` 不直接投入八节点图。表中的“框架”首先是目标内容的外层实现；**相同 Y 格还不足以证明完整 E／Y 框架相同**。

|词项／义项|实体侧|事件侧或相关结构|注意|
|---|---|---|---|
|좋아하다 1／3，喜欢|NP-ACC|V-기-ACC；V-는 것-ACC|名物化事件与实体同为 ACC；第5义高兴单列|
|좋다 10，喜欢／合意|NP-NOM|하는 일-NOM 记录，内容待定|实际 E-TOP；词典列 1이 2가；不能混入“适宜做……”义|
|마음에 들다，合心意|衣服-NP-TOP；词典框架 Y-NOM|?|마음-에 为内部“心”成分，不直接标 E-DAT|
|사랑하다 2／4，珍爱／热爱|动物、音乐、和平-ACC|?|恋爱、珍爱、热爱分义；事件名物化一侧仍缺例|
|아끼다 2，珍爱|人-NP-ACC|?|排除节省义|
|원하다，想要|NP-ACC|V-기(-ACC)，同主语／异主语均见|事件有 NP 形式；外层格可省有作者说明|
|바라다 1／2，希望／想得到|NP-ACC|V-기-ACC；V-었으면 하고|条件引述式另列，不能补标 ACC|
|V-고 싶다，想做|直接实体 NP 框架 ?|V-고 싶다|内部实体对象可见 ACC／NOM；不当作外层 WANT flagging|
|V-었으면 싶다，愿望|?|条件结构|与 -고 싶다 分组，Yoon 指出意义差别|
|기쁘다，高兴|普通实体 ?|胜利-NOM；V-어서连接|事件 NP 的格与原因分句分开|
|기뻐하다，为……高兴|普通实体 ?|胜利-ACC；事件消息-에|에 例为“消息”；其八节点内容类型暂缓|
|즐겁다，愉快|普通实体 ?；一天-NOM 内容待定|V-니连接|不从“日子愉快”直接推导双价心理刺激框架|
|즐기다 1／2，享受／爱好|酒-NP-ACC|活动名词-ACC；V-는 것-ACC|习惯性爱好与当下享受分义|
|행복하다，幸福|直接 Y ?|存在背景分句＋幸福状态|词典列一价；不把内部子女-NOM 当 Y|
|만족하다¹，满意|职业-NP-에|事件补语 ?；结果-NP-에 内容待定|另有 에게／로／로서 框架说明，未取得这些正例|
|반갑다，见到……高兴|朋友-NP-NOM|相见-게 되어서|实体保留实体编码；变化式不是使役式|
|흐뭇하다，欣慰|直接 Y ?|V-니连接；内部 마음-NOM|心-NOM 不是刺激 NOM|

本轮可以先检验 **ACC** 在 좋아하다／원하다／바라다／즐기다 的跨词项分布，以及 **NOM** 在 좋다／기쁘다／반갑다 的分布。但这些词的义项不同、E 的可见标记也不齐全，**目前不能据表宣称已有 LIKE→WANT→HAPPY 的蕴含或确定连边**。

## 2. 编码与标注约定

- 排除被动、语法使役构式；普通愿望句里“想让某人做某事”的中文译法不等于韩语 CAUS 构式。기뻐하다、좋아하다 的 -어하다 不据形式直接判 CAUS；-게 되다 与 -게 하다 分开。
- 保留 E 的实际 TOP／省略，不用词典的数字配价框架将所有 E 改标 NOM。词典 `1이 2가` 也不能单凭数字判题元，须核对实际名词角色。
- `에` 暂记为可见形式组 `EY`，gloss 用常规格标签 LOC；它在情感句中的具体关系另记。**不把所有 에 自动等同于 E-DAT 或同一种语义关系**。
- 谚文后附 **Yale 式拼写转写**，不标长音、不应用连读、收音中和等音变；这是拼写转写，不是语音转写。`e／ey／ay／u／wu` 分别对应 ㅓ／ㅔ／ㅐ／ㅡ／ㅜ；ㅜ 在唇音后省写 w，ㄹ 写 l。例句切分块依次为韩文词素、罗马字词素、英文 gloss 三行；Yoon 原本已用罗马字的例子保持作者写法，两行呈现。不规则变化、融合词形在说明中交代。`-고 싶다` 拆作连接形式和辅助谓词，不宣称 CVB 是唯一理论分析。
- `CVB.CAUSAL` 为“原因连接”，**不同于 CAUS（使役）**。连接分句是否为所选补语本轮未作统一分析；在数据中独立成组，不能直接与格补语合并。
- `ADD` 添加焦点，`ONLY` 限定焦点，`EVEN` 递进焦点，`COORD` 并列，`COP` 系词；韩语词典用的“形容词”是可直接屈折作谓词的类别，不套用英语系词句结构。
- `ADN` 定语形式；`NMLZ` 名物化；`TOP` 话题；`ACC` 宾格；`NOM` 主格；`LOC` 处所／에类标记；`COM` 共格；`GEN` 属格；`COND` 条件；`QUOT` 引述；`HON` 主体尊敬；`HUM` 谦称；`POL` 礼貌；`DECL` 陈述；`PRS` 现在；`PST` 过去；`NEG.ABIL` 否定能力；`LINK` 连接；`INT.EMB` 嵌入疑问。融合标签用点，切分边界用连字符。

## 3. 逐例记录

标注与中文译文由本稿补配，不冒称作者原标注。词典搭配本身常为 E 省略短语；未添加词典没有的主语。摘录分句保留可回查的完整原句。
'''


def build():
    validate()
    body = [HEADER.format(count=len(EX))]
    for x in EX:
        s = SOURCES[x['source']]
        body.append(f"\n### {x['id']}　{x['lexeme']}：{x['content_type']}／{x['realization']}\n\n")
        body.append(f"证据类型：{x['evidence_type']}。原文：**{x['original']}**\n\n")
        rows = [x['morphemes']]
        if x['morphemes_romanized'] != x['morphemes']:
            rows.append(x['morphemes_romanized'])
        rows.append(x['gloss'])
        body.append('```text\n' + aligned_rows(rows) + '\n```\n\n')
        body.append(f"“{x['translation_zh']}”\n\n")
        if x['full_original']:
            body.append(f"完整原句：{x['full_original']}\n\n")
        body.append(f"来源：[{x['source']}]({s['url']})，{x['locator']}。E：{x['experiencer_flagging']}；Y：{x['y_flagging']}；形式组：`{x['frame_group']}`。\n\n{x['note']}\n")
    body.append('''
## 4. 已有框架说明但不能当正例填表的项目

1. **만족하다**：词典列 `1이 2에/에게 만족하다, 1이 2로 만족하다`，另列 `2로서`。本轮只有 에 的实际例；에게／로／로서 保留为配价说明，不编造例句、不按意义填格。
2. **좋다、즐겁다、기쁘다、반갑다、흐뭇하다**：词典都有相似的数字框架，但第二个 NOM 可能是刺激、时段、心情部位等，不能据形式自动视为同一关系。
3. **사랑하다／아끼다＋事件名物化**、**기쁘다／기뻐하다＋普通实体**、**행복하다＋明确外层 Y**：仍需补证。未找到不等于不存在。
4. **마음에 들다**：K38 的 Y 实现为 TOP，词典另列 Y-NOM 框架；事件一侧仍缺例。不能仅凭字面“进入心里”直接宣称有 E-DAT。

## 5. NSM 与 Mouton 来源状态

详见 [韩语 NSM 核读笔记](../../03_文献笔记/NSM/韩语心理谓词_NSM定义与文献核读.md)。Yoon（2003）对 WANT／FEEL 有直接分析，但 **WANT 是基元，不是由更简单成分定义出来的词项**；其完整情感释义主要针对愤怒类词，本轮尚未取得喜欢、爱、高兴各词项的现成 NSM explication。词典释义不可改名为 NSM 定义。

Mouton 的 Schütze（2001）格叠加论文 DOI 已定位；全文访问仍未成功，本稿未抄录其中例号，也未把当前韩语记作已完成 Mouton 正文证据验收。当前直接例句证据是官方词典及 ANU 论文。要计入“五种语言使用 Mouton 分析来源”，还须落实该文或替代文献中的实际相关正文。

结构化材料：[逐例数据](../../research/korean_pilot/examples.json)、[形式组](../../research/korean_pilot/frame_groups.json)、[来源](../../research/korean_pilot/sources.json)。
''')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(annotate_markdown(''.join(body)))
    (B / 'examples.json').write_text(json.dumps(EX, ensure_ascii=False, indent=2) + '\n')
    (B / 'sources.json').write_text(json.dumps(SOURCES, ensure_ascii=False, indent=2) + '\n')
    frames = {}
    for x in EX:
        frames.setdefault(x['frame_group'], []).append(x['id'])
    (B / 'frame_groups.json').write_text(json.dumps({'status':'形式分组，尚非最终语义地图输入；须同时核对E标记和词义', 'groups':frames}, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {OUT.relative_to(ROOT)}: {len(EX)} examples, {len(set(x["lexeme"] for x in EX))} lexemes; source and gloss alignment verified.')


if __name__ == '__main__':
    build()
