"""Keep attested examples, source locations, and supplied glosses together."""
import json
import pathlib
import re

BASE = pathlib.Path(__file__).parent
ROOT = BASE.parent.parent
SOURCES = {
    "BIV": ("Shagal 2021, Bivalent patterns in Finnish, BivalTyp", "https://bivaltyp.info/languages/descriptions/Finnish.html", None),
    "K-RAK": ("Kielitoimiston ohjepankki, Rektioita: rakastaa uuden kokeilemista vai rakastaa kokeilla uutta?", "https://kielitoimistonohjepankki.fi/ohje/rektioita-rakastaa-uuden-kokeilemista-vai-rakastaa-kokeilla-uutta/", "kotus_rakastaa"),
    "K-TYY": ("Kielitoimiston ohjepankki, Rektioita: tyytyväinen asiaan vai asiasta?", "https://kielitoimistonohjepankki.fi/ohje/rektioita-tyytyvainen-asiaan-vai-asiasta/", "kotus_tyytyvainen"),
    "K-SE": ("Kielitoimiston ohjepankki, Pronominit: se ja sivulause", "https://kielitoimistonohjepankki.fi/ohje/pronominit-se-ja-sivulause-tarkeinta-on-se-etta-yritamme/", "kotus_se_clause"),
    "UK-L": ("Uusi kielemme, Tykätä and Pitää – Saying You Like Things in Finnish", "https://uusikielemme.fi/finnish-grammar/syntax/rections/tykata-and-pitaa-saying-you-like-things-in-finnish", "uk_like"),
    "UK-M": ("Uusi kielemme, Fourth Infinitive Verb Rections -Minen Rektiot", "https://uusikielemme.fi/finnish-grammar/syntax/constructions/fourth-infinitive-verb-rections", "uk_minen"),
    "UK-I": ("Uusi kielemme, Infinitive Verb Rections – Rektiot Infinitiivi", "https://uusikielemme.fi/finnish-grammar/syntax/rections/infinitive-verb-rections-rektiot-perusmuoto", "uk_infinitive"),
    "UK-E": ("Uusi kielemme, Verb Rections with Että – Siihen että, Siitä että", "https://uusikielemme.fi/finnish-grammar/syntax/rections/verb-rections-with-etta-siihen-etta-siita-etta", "uk_etta"),
    "UK-A": ("Uusi kielemme, Adjective Rections – Vihainen sinulle – Ylpeä sinusta", "https://uusikielemme.fi/finnish-grammar/syntax/rections/adjective-rections-vihainen-sinulle-ylpea-sinusta", "uk_adjectives"),
    "JK": ("Jukka K. Korpela, Suomen sanojen rektioita", "https://jkorpela.fi/rektio/all.html", "jk_rections"),
    "WEB-ONN": ("Tietoisuusakatemia，网站所引学员反馈", "https://www.tietoisuusakatemia.com", "native_onnellinen"),
}
ROWS = []


def add(lexeme, content, realization, flag, original, segmentation, gloss, translation, source, location, note=""):
    assert len(segmentation.split()) == len(gloss.split()), (original, segmentation, gloss)
    frame_group = flag if flag != "NONE" else "BARE_ETTA" if realization == "FINITE" else realization
    ROWS.append(dict(id=f"F{len(ROWS)+1:02}", lexeme=lexeme, content=content,
                     realization=realization, y_flag=flag, frame_group=frame_group, original=original,
                     segmentation=segmentation, gloss=gloss, translation=translation,
                     source=source, location=location, note=note))


add("pitää", "ENTITY", "NP", "ELA", "Pekka pitää tästä paidasta.",
    "Pekka pit-ää tä-stä paida-sta", "PN.NOM like-PRS.3SG this-ELA shirt-ELA",
    "佩卡喜欢这件衬衫。", "BIV", "#58")
add("pitää", "EVENT", "NMLZ_NP", "ELA", "Pidän uimisesta.",
    "pidä-n ui-mise-sta", "like-PRS.1SG swim-NMLZ-ELA",
    "我喜欢游泳。", "UK-L", "§3 Tykätä and Pitää with Verbs")
add("pitää", "EVENT", "LEXICAL_ACTIVITY_NP", "ELA", "Pidän uinnista.",
    "pidä-n uinni-sta", "like-PRS.1SG swimming-ELA",
    "我喜欢游泳。", "UK-L", "§3", "uinti 是词汇性活动名词；与生产性的 uiminen 分列。")
add("pitää", "EVENT", "PRONOUN_+_FINITE", "ELA", "Pidän siitä, että työni on vaihtelevaa.",
    "pidä-n siitä että työ-ni on vaihteleva-a",
    "like-PRS.1SG DEM.ELA COMP work.NOM-POSS.1SG be.PRS.3SG varied-PART",
    "我喜欢我的工作富于变化这一点。", "UK-E", "§2 Mistä Rections", "ELA 出现在关联代词 siitä 上；不是从句谓语 vaihtelevaa 的 PART。")

add("tykätä", "ENTITY", "NP", "ELA", "Minä tykkään sinusta.",
    "minä tykkää-n sinu-sta", "1SG.NOM like-PRS.1SG 2SG-ELA",
    "我喜欢你。", "UK-L", "§2.2 Simple sentences")
add("tykätä", "EVENT", "NMLZ_NP", "ELA", "En tykkää tiskaamisesta.",
    "en tykkää tiskaa-mise-sta", "NEG.1SG like.CNG wash.dishes-NMLZ-ELA",
    "我不喜欢洗碗。", "UK-M", "Mistä 表，tykätä 行", "否定例句保留 NEG 标签；不是被动。")
add("tykätä", "EVENT", "A_INFINITIVE", "NONE", "Tykkään uida.",
    "tykkää-n ui-da", "like-PRS.1SG swim-INF1",
    "我喜欢游泳。", "UK-L", "§3", "K-RAK 的 Tiesitkö? 小节另明确支持 tykätä 的不定式／名物化两种形式。")
add("tykätä", "EVENT", "PRONOUN_+_FINITE", "ELA", "Tykkään siitä, että rutiinit säilyvät.",
    "tykkää-n siitä että rutiini-t säily-vät", "like-PRS.1SG DEM.ELA COMP routine-PL.NOM remain-PRS.3PL",
    "我喜欢日常惯例保持不变。", "UK-E", "§2 Mistä Rections", "säilyvät 为主动不及物形式；来源英语 maintained 的被动译法不决定芬兰语语态。")
add("tykätä", "EVENT", "FINITE", "NONE", "Tykkään, että se on hyvä idea.",
    "tykkää-n että se on hyvä idea", "like-PRS.1SG COMP DEM.NOM be.PRS.3SG good.NOM idea.NOM",
    "我觉得这是个好主意。", "JK", "tykätä 词条，että-lause 行", "保留来源的裸 että 从句用例；具体义项暂不与 F05–F08 合并判定。")

add("rakastaa", "ENTITY", "NP", "PART", "Pekka rakastaa Mattia.",
    "Pekka rakasta-a Matti-a", "PN.NOM love-PRS.3SG PN-PART",
    "佩卡爱马蒂。", "BIV", "#46")
add("rakastaa", "ENTITY+EVENT", "COORDINATED_NPS", "PART", "Rakastan kirjoja ja lukemista.",
    "rakasta-n kirjo-j-a ja luke-mis-ta", "love-PRS.1SG book-PL-PART and read-NMLZ-PART",
    "我爱书，也爱阅读。", "K-RAK", "Koko ohje 开头", "一个原句并列普通实体名词和事件名物化；二者均为 PART，是直接的跨内容形式证据。")
add("rakastaa", "EVENT", "NMLZ_NP", "PART", "Rakastan runojen lukemista.",
    "rakasta-n runo-j-en luke-mis-ta", "love-PRS.1SG poem-PL-GEN read-NMLZ-PART",
    "我热爱读诗。", "K-RAK", "Ohje lyhyesti", "runo-j-en 是名物化内部的 GEN；外层 Y 是 luke-mis-ta。")
add("rakastaa", "EVENT", "A_INFINITIVE", "NONE", "rakastan kokeilla erilaisia kasvisruokia",
    "rakasta-n kokeil-la erilais-i-a kasvisruok-i-a", "love-PRS.1SG try-INF1 different-PL-PART vegetable.dish-PL-PART",
    "我热爱尝试不同的素菜。", "K-RAK", "Koko ohje，不定式用法说明", "原文小写列举表达，未补句尾。官方指南将 rakastaa + A 不定式列为 yleiskielen rajatapaus（标准语边缘用法）；不改写成无标记或不合语法。菜后的 PART 属于 try 的内部对象。")
add("rakastaa", "EVENT", "PRONOUN_+_FINITE", "PART", "Rakastan sitä, että vihaan sinua.",
    "rakasta-n sitä että vihaa-n sinu-a", "love-PRS.1SG DEM.PART COMP hate-PRS.1SG 2SG-PART",
    "我爱我恨你这件事。", "UK-E", "§1 Partitive Rections", "外层 PART 在 sitä 上；sinua 是内部 hate 的对象。")
add("rakastua", "ENTITY", "NP", "ILL", "Pekka rakastui Mattiin.",
    "Pekka rakastu-i Matti-in", "PN.NOM fall.in.love-PST.3SG PN-ILL",
    "佩卡爱上了马蒂。", "BIV", "#113", "主动状态变化谓词，单列于 rakastaa；不是 CAUS 或被动。事件对应式本轮未核实。")

add("haluta", "ENTITY", "NP", "GEN", "Pekka haluaa uuden kännykän.",
    "Pekka halua-a uude-n kännykä-n", "PN.NOM want-PRS.3SG new-GEN mobile.phone-GEN",
    "佩卡想要一部新手机。", "BIV", "#121", "GEN 是本句名词单数全量宾语的表面形态；不是 haluta 恒定的词汇支配格。")
add("haluta", "ENTITY", "NP", "PART", "Haluan karkkeja.",
    "halua-n karkke-j-a", "want-PRS.1SG candy-PL-PART",
    "我想要糖果。", "JK", "haluta 词条，objekti 行")
add("haluta", "EVENT", "A_INFINITIVE", "NONE", "Minä haluan nukkua ikuisesti.",
    "minä halua-n nukku-a ikuisesti", "1SG.NOM want-PRS.1SG sleep-INF1 eternally",
    "我想永远睡下去。", "UK-I", "haluta 行")
add("haluta", "EVENT", "FINITE", "NONE", "Haluan, että kokous loppuu pian.",
    "halua-n että kokous loppu-u pian", "want-PRS.1SG COMP meeting.NOM end-PRS.3SG soon",
    "我希望会议快点结束。", "JK", "haluta 词条，että-lause 行")
add("haluta", "ENTITY", "NP", "PART", "en halua omenaa",
    "en halua omena-a", "NEG.1SG want.CNG apple-PART",
    "我不想要苹果。", "JK", "引言，haluta 的一般宾语规则示例", "原文小写片段。否定构式另标 NEG，不把 PART 当作另一种心理义项的证明。")

add("tahtoa", "ABSTRACT_NP", "NP", "PART", "Hän tahtoi itselleen lisää etuja.",
    "hän tahto-i itse-lle-en lisää etu-j-a", "3SG.NOM want-PST.3SG self-ALL-POSS.3 more benefit-PL-PART",
    "他／她想给自己争取更多好处。", "JK", "tahtoa 词条，objekti 行", "好处为抽象 NP；实体／事件精细归类暂不处理。")
add("tahtoa", "EVENT", "A_INFINITIVE", "NONE", "Me tahdomme olla rauhassa.",
    "me tahdo-mme ol-la rauha-ssa", "1PL.NOM want-PRS.1PL be-INF1 peace-INE",
    "我们想安安静静地待着。", "UK-I", "tahtoa 行", "INE 在不定式内部的 rauhassa 上。")
add("toivoa", "ENTITY", "NP", "PART", "Toivoin isältä tuliaiseksi suklaata.",
    "toivo-i-n isä-ltä tuliaise-ksi suklaa-ta", "hope-PST-1SG father-ABL souvenir-TRA chocolate-PART",
    "我希望父亲带巧克力作伴手礼。", "JK", "toivoa 词条", "所希望的 NP 为巧克力-PART；father-ABL 是来源／请求对象，另留记录。")
add("toivoa", "EVENT", "FINITE", "NONE", "Toivon, että hän suostuu.",
    "toivo-n että hän suostu-u", "hope-PRS.1SG COMP 3SG.NOM agree-PRS.3SG",
    "我希望他／她同意。", "JK", "toivoa 词条，että-lause 行")

add("nauttia", "ENTITY", "NP", "ELA", "Pekka nauttii teestä.",
    "Pekka nautti-i tee-stä", "PN.NOM enjoy-PRS.3SG tea-ELA",
    "佩卡享受茶。", "BIV", "#120", "按约定茶记实体。来源英语回译有 hot，芬兰语原句没有对应修饰词，不在原句中添加。")
add("nauttia", "EVENT", "NMLZ_NP", "ELA", "Nautin saunomisesta.",
    "nauti-n sauno-mise-sta", "enjoy-PRS.1SG take.sauna-NMLZ-ELA",
    "我享受蒸桑拿。", "UK-M", "Mistä 表，nauttia 行")
add("nauttia", "EVENT", "PRONOUN_+_FINITE", "ELA", "Nautin siitä, että voin auttaa muita.",
    "nauti-n siitä että voi-n autta-a mu-i-ta", "enjoy-PRS.1SG DEM.ELA COMP can-PRS.1SG help-INF1 other-PL-PART",
    "我享受能够帮助别人这一点。", "UK-E", "§2 Mistä Rections")

add("olla iloinen", "ENTITY", "NP", "ELA", "Pekka oli iloinen kirjeestä.",
    "Pekka ol-i iloinen kirjee-stä", "PN.NOM be-PST.3SG glad.NOM letter-ELA",
    "佩卡因那封信而高兴。", "BIV", "#83", "信直接记实体。")
add("olla iloinen", "EVENT", "LEXICAL_EVENT_NP", "ELA", "Olen iloinen palkankorotuksesta.",
    "ole-n iloinen palkankorotukse-sta", "be-PRS.1SG glad.NOM pay.raise-ELA",
    "我因加薪而高兴。", "UK-A", "§1，iloinen 行")
add("olla iloinen", "EVENT", "PRONOUN_+_FINITE", "ELA", "Olen iloinen siitä, että olet olemassa.",
    "ole-n iloinen siitä että ole-t ole-ma-ssa", "be-PRS.1SG glad.NOM DEM.ELA COMP be-PRS.2SG be-INF3-INE",
    "我因你的存在而高兴。", "UK-E", "§2.2 Adjectives with Rections", "olemassa 的 INF3-INE 在从句内部；外层 Y 的 ELA 在 siitä 上。")
add("olla iloinen", "EVENT", "FINITE", "NONE", "Olen iloinen, että pääsitte kaikki paikalle.",
    "ole-n iloinen että pääs-i-tte kaikki paika-lle", "be-PRS.1SG glad.NOM COMP arrive-PST-2PL all.NOM place-ALL",
    "我很高兴你们都能到场。", "JK", "iloinen 词条，että-lause 行")
add("iloita", "RESULT_NP", "LEXICAL_NP", "ELA", "iloitsi tuloksesta",
    "iloit-si tulokse-sta", "rejoice-PST.3SG result-ELA",
    "为结果而高兴。", "JK", "iloita 词条", "来源是未明说 E 的片段；不补造主语。结果名词另留子标签。")
add("iloita", "EVENT", "PRONOUN_+_FINITE", "ELA", "Iloitsin siitä, että posti saapui ajoissa.",
    "iloit-si-n siitä että posti saapu-i ajoissa", "rejoice-PST-1SG DEM.ELA COMP mail.NOM arrive-PST.3SG on.time",
    "我因邮件及时到达而高兴。", "UK-E", "§2 Mistä Rections")
add("onnellinen", "RESULT_NP", "LEXICAL_NP", "ELA", "onnellinen saavutuksestaan",
    "onnellinen saavutukse-sta-an", "happy.NOM achievement-ELA-POSS.3",
    "为自己的成就感到幸福／高兴。", "JK", "onnellinen 词条", "原文为形容词短语，没有补入 olla 或 E；普通实体和完整事件从句的对应例本轮尚缺。")

add("olla tyytyväinen", "ENTITY", "NP", "ILL", "Pekka on tyytyväinen poikaansa.",
    "Pekka on tyytyväinen poika-ansa", "PN.NOM be.PRS.3SG satisfied.NOM son-ILL.POSS.3SG",
    "佩卡对自己的儿子满意。", "BIV", "#112", "依来源将 -ansa 记为 ILL 与第三人称领属形式的融合。")
add("olla tyytyväinen", "ENTITY", "NP", "ILL", "Asiakkaat ovat tyytyväisiä tuotteisiin.",
    "asiakkaa-t ovat tyytyväis-i-ä tuotte-i-siin", "customer-PL.NOM be.PRS.3PL satisfied-PL-PART product-PL-ILL",
    "顾客对产品满意。", "K-TYY", "Ohje lyhyesti", "满意述谓自身为复数 PART；Y 的格在 tuotteisiin 上，是 ILL。")
add("olla tyytyväinen", "EVENT", "LEXICAL_EVENT_NP", "ELA", "Pelaajat olivat tyytyväisiä voitosta.",
    "pelaaja-t ol-i-vat tyytyväis-i-ä voito-sta", "player-PL.NOM be-PST-3PL satisfied-PL-PART victory-ELA",
    "球员们为胜利而满意。", "K-TYY", "Ohje lyhyesti")
add("olla tyytyväinen", "EVENT", "PRONOUN_+_FINITE", "ILL", "Yhtiö on tyytyväinen siihen, että myynti kasvoi.",
    "yhtiö on tyytyväinen siihen että myynti kasvo-i", "company.NOM be.PRS.3SG satisfied.NOM DEM.ILL COMP sales.NOM grow-PST.3SG",
    "公司对销售增长感到满意。", "K-TYY", "Koko ohje，Tavallisin ilmaisemassa kohdetta")
add("olla tyytyväinen", "EVENT", "PRONOUN_+_FINITE", "ELA", "Olen tyytyväinen siitä, että se on ohi.",
    "ole-n tyytyväinen siitä että se on ohi", "be-PRS.1SG satisfied.NOM DEM.ELA COMP DEM.NOM be.PRS.3SG over",
    "我对这件事已经结束感到满意。", "UK-E", "§2.2 Adjectives with Rections", "ELA 用法另有 K-TYY 的明确说明；不因 BIV 只列 ILL 就排除 ELA。")

add("onnellinen", "ENTITY", "NP", "ELA", "Oon niin onnellinen sinusta",
    "oon niin onnellinen sinu-sta", "be.PRS.1SG so happy.NOM 2SG-ELA",
    "有你，我真幸福。", "WEB-ONN", "Satu 的反馈，Oon niin onnellinen... 句的前半", "原文口语形式 oon 保留，未标准化为 olen。节选后原句有呼语 Johanna 及 että 从句；本记录只分析人称代词 Y-ELA。")
add("onnellinen", "EVENT", "FINITE", "NONE", "Olin tosi onnellinen, että minulla oli aikaa ja mahdollisuus pysähtyä näitten asioiden äärelle.",
    "ol-i-n tosi onnellinen että minu-lla ol-i aika-a ja mahdollisuus pysähty-ä näi-tten asio-i-den ääre-lle",
    "be-PST-1SG very happy.NOM COMP 1SG-ADE be-PST.3SG time-PART and opportunity.NOM stop-INF1 this-PL.GEN matter-PL-GEN proximity-ALL",
    "我很高兴自己有时间和机会停下来面对这些事情。", "WEB-ONN", "Satu 的反馈，Olin tosi onnellinen... 句", "完整原句，保留口语 näitten。minulla 的 ADE 属于事件从句内部的领有结构，不是外层心理体验者的格。")


def norm(text):
    return re.sub(r"[^\w]", "", text.lower())


def verify_quotes():
    from bs4 import BeautifulSoup
    source_text = {}
    for key, (_, _, name) in SOURCES.items():
        if name:
            soup = BeautifulSoup((BASE / (name + ".html")).read_text(), "html.parser")
            source_text[key] = norm(soup.get_text("", strip=True))
    for row in ROWS:
        if row["source"] != "BIV":
            assert norm(row["original"]) in source_text[row["source"]], (row["id"], row["original"])
    raw = json.loads((BASE / "bivaltyp_selected.json").read_text())
    for row in ROWS:
        if row["source"] == "BIV":
            record = next(x for x in raw if row["location"] == "#" + x["predicate_no"])
            assert norm(row["original"]) == norm(record["sentence"]), row["id"]


INTRO = """# 芬兰语心理谓词：实体／事件表达第一轮采集

整理日期：2026-11-11；框架归类更新：2026-11-12。接续日语样本，范围为 LIKE／LOVE／WANT／HAPPY 及原来已纳入采集的相关词项。本轮先记录形式，不做新的细分语义裁决或最终八节点编码。

**排除被动与 CAUS 句式，包含事件内部从句中的被动也不选作本轮正例。** 主动的状态变化谓词 rakastua 单独记录。例句中的普通实体名词（如茶、书、信、手机、人）按实体处理；明确的活动名词和 -minen 事件名物化分别记录。名物化事件在内容上仍是事件，在句法实现上是 NP。缺例记 `?`，不等于不合语法。

## 1. 构式汇总

格标签记整个 Y 的外层标记；表中 E 的 NOM 框架由 BIV 语法说明与相关例句支持。省略 E 的人称屈折例句没有人为补入代词。具体主语性诊断留待下一阶段。

|词项|普通实体／抽象 NP|事件表达：已核实形式|记录号|
|---|---|---|---|
|pitää|实体 NP-ELA|活动名词-ELA；V-NMLZ-ELA；siitä（ELA）＋että 从句|F01–F04|
|tykätä|实体 NP-ELA|V-NMLZ-ELA；A 不定式；siitä（ELA）＋että；裸 että 从句|F05–F09|
|rakastaa|实体 NP-PART|V-NMLZ-PART；sitä（PART）＋että；A 不定式〔标准语边缘用法〕|F10–F14|
|rakastua|实体 NP-ILL|?|F15|
|haluta|实体 NP：GEN／PART；来源概括还允许其他一般宾语形式|A 不定式；裸 että 从句|F16–F20|
|tahtoa|抽象 NP-PART|A 不定式|F21–F22|
|toivoa|实体 NP-PART|裸 että 从句|F23–F24|
|nauttia|实体 NP-ELA|V-NMLZ-ELA；siitä（ELA）＋että|F25–F27|
|olla iloinen|实体 NP-ELA|事件名词-ELA；siitä（ELA）＋että；裸 että 从句|F28–F31|
|iloita|结果 NP-ELA；普通实体例尚缺|siitä（ELA）＋että|F32–F33|
|onnellinen|成就 NP-ELA；人称代词 NP-ELA|裸 että 从句；另存成就名词短语|F34、F40–F41|
|olla tyytyväinen|实体 NP-ILL|事件名词-ELA；siihen（ILL）＋että；siitä（ELA）＋että|F35–F39|

**2026-11-12 归类规则**：按本研究当前采用的 flagging 粒度，带格 se 代词＋että 从句并入对应格框架：siitä＋että 归 ELA，sitä＋että 归 PART，siihen＋että 归 ILL。普通 NP、活动／事件名词、名物化 NP 与这些带格从句在格相同时归同一类。裸 että 从句统一另归 `BARE_ETTA`；A 不定式另归 `A_INFINITIVE`。实际实现形式仍保存在 realization 字段中，供回查。此处是研究编码层面的合并，不等于断言所有实现形式句法结构完全相同。

### että 从句与带格 se 代词

芬兰语语法中的 `että-lause` 是由补语连词 **että** 引出的有限从句。它本身保留从句的谓语、主语等内部句法；不能将它当成一个本身带 ELA/PART/ILL 的 NP。若主句谓词要求特定格，而补充内容用有限 että 从句表达，常见形式是在从句前放代词 **se**，并让它承担要求的格，再由后面的从句展开其内容：

|类型|例子|外层形式|
|---|---|---|
|支配 ELA 的喜欢／享受词|`Pidän siitä, että työni on vaihtelevaa.` “我喜欢工作富于变化这一点。”|`siitä`＝`se-ELA`；että 从句说明内容|
|支配 ELA 的喜欢词|`Tykkään siitä, että rutiinit säilyvät.` “我喜欢日常惯例保持不变。”|`siitä`＝`se-ELA`|
|PART 对象式爱|`Rakastan sitä, että vihaan sinua.` “我爱我恨你这件事。”|`sitä`＝`se-PART`；不是把从句内部的 `sinua-PART` 当外层 Y|
|ILL 形式的满意|`Yhtiö on tyytyväinen siihen, että myynti kasvoi.` “公司对销售增长感到满意。”|`siihen`＝`se-ILL`|
|HAPPY 形容词|`Olen iloinen siitä, että olet olemassa.` “我因你的存在而高兴。”|`siitä`＝`se-ELA`|
|裸从句|`Olen iloinen, että pääsitte kaikki paikalle.` “我很高兴你们都到场了。”|无显式 se；Y 内容没有显式外层格尾|

**代词不总是可省。** Uusi kielemme 的教学语法将这一结构概括为“格支配由代词 se 承接，后接 että 从句”，并指出对许多动词该代词必需；但更细的官方语言指南说明，带格代词在结构上“常常必需”，某些情况也可选。该指南以 `Olimme iloisia (siitä), että tulitte ajoissa` 为例，指出 *iloinen* 等状态形容词可有无 `siitä` 两式。实现形式仍分别记 `PRONOUN_+_FINITE` 与 `FINITE`；框架分组中前者并入可见的格，后者单列 `BARE_ETTA`。不给裸从句补标一个未实现的 ELA。

Kielitoimiston ohjepankki 还说，`se + että` 整体可形成类似名词短语的组合；裸 `että` 从句则是从句。带 `se` 有时使内容显得较明确、作为一个既存事实／命题提出；但指南同时提醒，这种语篇差异并非每处都稳定。这里先只编码可见句法形式，不把它们预判为两个不同心理义项。

## 2. 来源

"""

TAIL = """
## 4. 编码注意事项与剩余空白

- **GEN 不等于所有对象统一 ACC**：F16 的手机与修饰词是表面 GEN；F17、F20 是 PART。BIV 对 haluta 的总括是一般及物宾语范式（GEN／PART／NOM 等），不能只取一个正面例句建立恒定 GEN 框架。此轮没有为未给出具体实例的 NOM 补造正例。
- **格在代词上**：siitä＝DEM.ELA、sitä＝DEM.PART、siihen＝DEM.ILL。`带格代词＋että 从句` 的实现形式独立记录；框架分组并入对应格。裸 että 从句单列。该归类不声称 että 自己带格或所有实现的句法性质完全相同。
- **从句内部的格另记**：F12 诗的 GEN、F13 素菜的 PART、F14 你的 PART，都不代表外层 Y 的格。F36 形容词的 PART 也不是 Y 的标记。
- **A 不定式与 NP 名物化分列**：名物化用 NMLZ 标注；Uusi kielemme 称其 fourth infinitive 的教学名称保留在书目标题里，不因此把 -minen 与不带格的 A 不定式混为一类。
- **体裁／规范信息保留**：rakastaa＋A 不定式已由官方指南列举，但标为标准语边缘用法；tykätä 的不定式另有指南明确支持。Korpela 的概括不能覆盖掉官方指南更细的体裁说明。
- **tyytyväinen 不止 ILL**：官方指南明确同时承认 ILL 和 ELA，并说明所呈现关系的差别。本轮只保存这种来源分析，不据此展开新的语义分类。官方页面的一个 ELA＋että 例句含内部被动，已排除，选用 F39 的主动例句。
- **保留空白**：rakastua 的事件式、iloita 的普通实体式仍待补查；tahtoa 的具体实体例也可继续补。onnellinen 的普通实体和完整事件从句已由网站实际用例补上，来源类型与教学例分开。此处 `?` 不是语法否定判断。没有核实的 -minen／不定式对应式不按直觉生成。
- **未冒充已读研究**：先前书目中的 Siiroinen 2003 专章没有在本轮获得全文，不能当作以上例句出处；VISK 若干页面本轮访问受限，未把搜索或转引当成直接核读。来源不限 Mouton，按当前授权使用官方语言指南、数据库及教学资料。

缩写：ELA＝出格，ILL＝入格，PART＝部分格，GEN＝属格，NOM＝主格，INE＝内格，ALL＝向格，ABL＝离格，ADE＝外格，TRA＝变格；NMLZ＝名物化，INF1＝A 不定式，INF3＝MA 不定式，COMP＝补语连词，DEM＝指示代词，POSS＝领属，PRS＝现在，PST＝过去，CNG＝否定结构中不带人称的配合形式，NEG＝否定助动词，PN＝人名。

原网页、抽取文本、来源访问记录与结构化例句保存在 `research/finnish_pilot/`。网页访问日期：2026-11-11。例句用于确认形式存在，不作频率样本或母语者可接受度实验。
"""


def render():
    grouped = {}
    for row in ROWS:
        grouped.setdefault(row["frame_group"], []).append(row)
    group_table = "### 按当前口径合并后的框架\n\n|框架组|词项／构式|记录|\n|---|---|---|\n"
    for group, examples in grouped.items():
        lexemes = list(dict.fromkeys(r["lexeme"] for r in examples))
        group_table += f"|{group}|{'、'.join(lexemes)}|{'、'.join(r['id'] for r in examples)}|\n"
    sections = [INTRO.replace("## 2. 来源\n", group_table + "\n## 2. 来源\n")]
    sections.append("|代号|来源|用途与证据性质|\n|---|---|---|\n")
    for key, (title, url, _) in SOURCES.items():
        kind = ("芬兰语格系统说明与编号问卷；2017 年提供数据、2021 年经母语者校核。" if key == "BIV"
                else "官方语言指南；包含形式、体裁或规范说明。" if key.startswith("K-")
                else "教学语法网页；核对原例与表格位置。" if key.startswith("UK-")
                else "实际网页中所引的个人反馈；用于补充形式存在，非可接受性实验。" if key.startswith("WEB-")
                else "个人整理的芬兰语支配关系参考；按词条定位，与官方指南交叉核查。")
        sections.append(f"|{key}|[{title}]({url})|{kind}|\n")
    sections.append("\n## 3. 逐条例句与 Leipzig 标注\n\n原来源中的芬兰语词形、词序保留；BIV 的词内分析连字符恢复为正常拼写。标点统一不影响词形。切分和 gloss 由本稿补配／统一，不声称全部照录来源。例句之间的 1SG/3SG、时态、肯否定差异都有标注，不当作严格最小对照。\n")
    for row in ROWS:
        segments, glosses = row["segmentation"].split(), row["gloss"].split()
        widths = [max(len(a), len(b)) for a, b in zip(segments, glosses)]
        line1 = "  ".join(x.ljust(w) for x, w in zip(segments, widths)).rstrip()
        line2 = "  ".join(x.ljust(w) for x, w in zip(glosses, widths)).rstrip()
        sections.append(f"\n### {row['id']}　{row['lexeme']}：{row['content']}／{row['realization']}\n\n")
        sections.append(f"原文：{row['original']}\n\n```text\n{line1}\n{line2}\n```\n\n“{row['translation']}”\n\n")
        title, url, _ = SOURCES[row["source"]]
        sections.append(f"来源：[{row['source']}]({url})，{row['location']}。外层 Y：**{row['y_flag']}**；框架组：**{row['frame_group']}**。")
        if row["note"]:
            sections.append(" " + row["note"])
        sections.append("\n")
    sections.append(TAIL)
    (ROOT / "02_语言材料/芬兰语/芬兰语心理谓词_实体事件构式_例句与标注.md").write_text("".join(sections))
    (BASE / "examples.json").write_text(json.dumps(ROWS, ensure_ascii=False, indent=2))
    (BASE / "frame_groups.json").write_text(json.dumps({group: [r["id"] for r in examples] for group, examples in grouped.items()}, ensure_ascii=False, indent=2))
    (BASE / "sources.json").write_text(json.dumps({key: {"title": title, "url": url, "local": name, "accessed": "2026-11-11"} for key, (title, url, name) in SOURCES.items()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    verify_quotes()
    render()
    print(f"Saved {len(ROWS)} source-checked examples across {len(set(r['lexeme'] for r in ROWS))} lexemes/constructions.")
