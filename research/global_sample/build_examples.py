from pathlib import Path
import json
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(__file__).resolve().parent
out = []
count = 0

def add(label, words, glosses, translation, source, frame, note=''):
    global count
    count += 1
    w, g = words.split(), glosses.split()
    assert len(w) == len(g), (label, len(w), len(g))
    display_width = lambda x: sum(0 if unicodedata.combining(c) else 2 if unicodedata.east_asian_width(c) in ('W','F') else 1 for c in x)
    widths = [max(display_width(a), display_width(b)) + 2 for a,b in zip(w,g)]
    line = lambda xs: ''.join(t + ' '*(n-display_width(t)) for t,n in zip(xs,widths)).rstrip()
    out.append(f'### G{count:02d}　{label}\n\n```text\n{line(w)}\n{line(g)}\n```\n\n“{translation}”\n\n出处：{source}。\n\n编码：{frame}。' + (f'\n\n注意：{note}' if note else '') + '\n')

intro = '''# WANT—LIKE—HAPPY 全球扩样：莱比锡标注例句库

更新：2026-11-08。共 COUNT 条可溯源实例，覆盖 17 种语言；Mapudungun 仅作候选，未在本库补造例句。配套分析见《心理谓词_全球扩样_非洲巴新澳大利亚美洲》。

## 标注和证据约定

- 每例给出原作者的语素分析、规范化 gloss、中文意译、出处、编码及必要限制。没有为凑齐三项而自行翻译、拼造句子。原句多词释义中的下划线改为点号，语法缩写统一大写；不硬拆来源未拆解的融合形式。
- E = Experiencer；Y = 想要／喜欢／高兴所针对的对象。身体部位、情绪／状态名词及名词化事件另说明。主宾语、格、索引不是同一层次。
- Ø 表示没有显性关系标记；“E 未独立表达”表示例句没有独立 E 短语，两者不相等。ABS 等没有独立语素时可作词汇形式的分析属性，不凭空加 `-Ø`。
- 某些地方只摘录连续的原文分句，明确标“节录”，不当作新造的完整句子。语义解读依作者语境，不把 feel.good／taste.good 自动并入一般 HAPPY／LIKE。
- 非洲条目的编号是 BivalTyp 问卷号：58 LIKE、83 BE GLAD、121 WANT。ValPaL 的括号编号是数据库例号，非语法书例号。
- 本库有些数据用于说明分析困难，**不全都是能进入三义地图的有效观察值**；每例限制应与原句一起引用。

## 非洲
'''

raw = json.loads((DATA/'africa_bivaltyp_raw.json').read_text())
years = {'Bafut':'Lum 2024', 'Tswana':'Creissels 2025', 'Khoekhoe':'Witzlack-Makarevich & Job 2024', 'Oromo_West_Central':'Gobena 2023', 'Bambara':'Vydrin 2023', 'Wolof':'Creissels 2024', 'Mano':'Khachaturyan 2023'}
translations = {
'Bafut': ['Ambe 喜欢这件衬衫。','Ambe 因那封信而高兴。','Ambe 想要一部新手机。'],
'Tswana': ['Mpho 喜欢这件衬衫。','我因那件礼物而高兴。','我想要这条裙子。'],
'Khoekhoe': ['Peter 喜欢这件衬衫。','Peter 因那封信而高兴。','Peter 想要一部新手机。'],
'Oromo_West_Central': ['Obsa 喜欢这件衬衫。','Obsa 因那封信而高兴。','Obsa 想要一部新手机。'],
'Bambara': ['Seku 喜欢这条裤子。','那封信使 Seku 高兴。','Seku 想要一辆摩托车。'],
'Wolof': ['我喜欢你的衬衫；直译：你的衬衫使我愉快。','我为你们和好而高兴。','我想要的是这个芒果。'],
'Mano': ['我喜欢他／她；直译：他／她抓住我的心。','我为你高兴；直译：我的肚子因你而变好。','他／她想要一些米饭。']}
frames = {
'Bafut':['EØ／YØ；E-SBJ、Y-DO','EØ／mbᵼ́ʔᵼ́ Y','EØ／YØ；E-SBJ、Y-DO'],
'Tswana':['EØ／YØ；普通主宾语框架','EØ／YØ；带 REFL、APPL.PRF 的派生动词','EØ／YØ；普通主宾语框架'],
'Khoekhoe':['EØ／Y xa；谓词含 APPL-PASS','EØ／Y ǃaroma','EØ／Y-OBL（-a）'],
'Oromo_West_Central':['E-NOM／Y-ABS','E-NOM／Y-LOC','E-NOM／Y-ABS'],
'Bambara':['E-ye／YØ；Y 为 pleasant 的主语','EØ／YØ；Y 为 gladden 主语，E 为宾语','EØ／Y-fɛ；非动词性构式'],
'Wolof':['E-OBJ／Y-SBJ；全名词主宾语无格，这句 E 以 ma 形式出现','E-SBJ／Y-ci','E-SBJ／Y-OBJ；Y 被焦点化'],
'Mano':['E 以心的领有者形式出现，整个 zò kṵ̄ 也可作为复杂谓词分析','E 为 stomach 的领有者；Y-píé','E 由 3SG.IPFV 辅助成分体现；Y-ká']}
notes = {
('Tswana','58'):'Ø-hempe 中 Ø 是来源给出的名词单数前缀零形式，不是本库另加的零宾格；CL 类别不是关系格。',
('Tswana','83'):'来源将 -ets- 合并标为 APPL.PRF；此处保留，不自行拆成两个来源未独立给出的语素。',
('Khoekhoe','58'):'-b／-s 是人称性数形式；本例的 Y 用 xa。不要将被动式去掉后仍声称这是同一个表面框架。',
('Oromo_West_Central','83'):'sana-tti 中的 -tti 承载 LOC；来源将 letter 一词标作 ABS，但整个宾语性对象短语有 LOC，不据此改成纯 ABS 框架。',
('Bambara','58'):'yé 是后置词；不是下例的 PFV.TR。源表另列 bɛ́／tɛ́＋fɛ̀ 的替代 LIKE，故本例不能证明 WANT／LIKE 完全不共享框架。',
('Bambara','83'):'问卷英语回译为 Seku is glad about the letter，实际给出的构式是 gladden；与非使动 HAPPY ABOUT 分列。ART 是声调性的，反斜线按非串接形态标注保留。',
('Bambara','121'):'fɛ̀ 来源字面释义为 by。不能因为英语译成 want 就将 bɛ́ 单独认定为一个普通及物欲望动词。',
('Wolof','58'):'ma 与主语人称形式的区别不能直接外推为全名词的格差别。flagging 与 indexing 分列。',
('Mano','58'):'Khachaturyan 2017 说明不可分领有者与直接宾语形式重合；须保留 NP 内部结构与复杂谓词两层分析可能。',
('Mano','83'):'BivalTyp 因 E 是 NP 内部成分而未将此条纳入主统计。这是结构排除，不是没有 HAPPY 表达。条目还列 ŋwɛ́ŋ̀、mɔ̀ 替代后置词，但未附本库可核的完整例句。'}
repl = {'PN':'PN','PRN(1)':'PN(CL1)','sI:cl1-like-FV':'SBJ.CL1-like-FV','SG-shirt(9)':'SG-shirt(CL9)','cl9.DEM':'CL9.DEM','sI:1SG-REFL-accept-APPL.PRF-FV':'SBJ.1SG-REFL-accept-APPL.PRF-FV','SG-gift(9)':'SG-gift(CL9)','sI:1SG-want-FV':'SBJ.1SG-want-FV','SG-dress(3)':'SG-dress(CL3)','cl3.DEM':'CL3.DEM','3SG.IPFV':'3SG.IPFV','PRF.sI:3SG':'PRF.SBJ.3SG','oI:1SG':'OBJ.1SG','FocV.sI:1SG':'FOC.V.SBJ.1SG','FocO/X.sI:1SG':'FOC.O/X.SBJ.1SG','clB-DEF':'CL.B-DEF','clB-DEM':'CL.B-DEM','POSS:2PL':'POSS.2PL'}
for lang in years:
    rows = [next(r for r in raw[lang] if r['predicate_no']==str(k)) for k in [58,83,121]]
    for j,r in enumerate(rows):
        gloss = ' '.join(repl.get(t,t.replace('_','.')) for t in r['glosses_en'].split())
        name = {'58':'LIKE','83':'BE GLAD','121':'WANT'}[r['predicate_no']]
        add(f'{lang.replace("_"," ")}：{name}',r['sentence'],gloss,translations[lang][j],f"{years[lang]}，BivalTyp，条目 {r['predicate_no']}；https://bivaltyp.info/languages/descriptions/{lang}.html",frames[lang][j],notes.get((lang,r['predicate_no']),''))

add('Mandinka：WANT','kew-ó lafí-ta kód-oo la','man-DEF want-PF.POS money-DEF OBL','那男人想要钱。','Creissels 2013，ValPaL 例 (31)，https://valpal.info/values/mand1436-want-1','EØ／Y-la')
add('Mandinka：LIKE，与 WANT 同词同框架','kew-ó lafí-ta kambaan-óo la','man-DEF like-PF.POS boy-DEF OBL','那男人喜欢那男孩。','同上，例 (30)','EØ／Y-la')
add('Mandinka：另一种 LIKE','súŋkút-oo yé ñiŋ báy-oo kanu','girl-DEF PF.POS DEM cloth-DEF like','那女孩喜欢这块布。','Creissels 2013，ValPaL 例 (34)，https://valpal.info/values/mand1436-like-2','EØ／YØ；yé 为谓语标记，不是后置词')
add('Mandinka：pleasant 型 LIKE','ñiŋ báy-oo díyáa-ta mus-óo ye','DEM cloth-DEF be.pleasant-PF.POS woman-DEF BEN','那女人喜欢这块布。','Creissels 2013，ValPaL 例 (264)，https://valpal.info/values/mand1436-like-3','E-ye／YØ','网页微角色摘要与实际例句有冲突。本条据实际句子和作者注释记录角色；不要把 woman 错写成 liked entity。')

out.append('## 澳大利亚\n')
add('Dalabon：WANT NP（原例分句节录）','loli kardu ka-h-djare dohkardu mey','lollies maybe 3SG-R-like/want or food','他也许想要糖果，或食物。','Ponsonnet 2013，p.184，例 (31) 的第一句','E-S（独立 E 未表达，由前缀索引）；YØ','djare 形态上不及物，不能因它带所欲物 NP 就直接认定 E-A／Y-O。')
add('Dalabon：WANT 的 GEN 替代构式','beka-kun nga-h-kakku-djare-ninj','tobacco-GEN 1SG-R-really-like/want-PI','我当时非常想要烟草。','Ponsonnet 2013，p.189，例 (46)','E-S（由前缀索引）；Y-GEN','上下文为前一天烟草用完。这里 GEN 确实出现于 WANT，不应把 GEN 只分配给 HAPPY。')
add('Dalabon：LIKE NP，应用式','nunh kanh naddo nga-h-marnu-djare','DEM DEM bush.peanuts 1SG>3-R-BEN-like/want','我喜欢灌木花生。','Ponsonnet 2013，p.183，例 (29)','E-A／Y-O 由及物索引建立；本例 Y 无关系标记','BEN 是动词上的应用式标记，不是 Y 名词上的“与格”。作者特别指出无生 Y 可见于词汇化的 marnu-djare。')
add('Dalabon：WANT 也可用应用式（原例分句节录）','nah-ngan nga-h-marnu-djare','mother-1SG.POSS 1SG>3-R-BEN-like/want','我想要妈妈。','Ponsonnet 2013，p.184，例 (33) 引语分句','E-A／Y-O；YØ','语境为孩子想回到被迫分离的母亲身边。不能把 marnu-djare 绝对限定为偏好而排除欲望。')
add('Dalabon：feel good about（原例后半分句）','ka-h-lng-yolh-mon njing-kun','3SG-R-SEQ-feelings-good 2SG-GEN','他现在对你感觉好了／与你和好了。','Ponsonnet 2013，p.173，例 (8) 后半分句','E-S（前缀索引）；Y-GEN','作者置于争执后的语境；可作愉悦／良好感受关于某人的证据，但不将其无条件等同于所有因事件高兴的读法。论文还说明应用式可引入对象。')

add('Jaminjung：LIKE','majani malara ngunthug gan-angga-m majani yani-ba malara','maybe frog like 3SG.A:3SG.P-get/handle-PRS maybe IRR:3SG.A:3SG.P-bite frog','也许它们（鱼）喜欢青蛙（作鱼饵），也许会咬青蛙。','Schultze-Berndt 2013，ValPaL 例 (14)，https://valpal.info/values/djam1255-like-1','数据库所给一般框架为 E-ERG／Y-ABS；本例 E 未独立表达，Y 无显性 ABS 后缀','来源说明低有生度名词用单数一致。ERG 框架来自作者分析，不能声称本句显示了一个显性的 ERG 体验者。')
add('Jaminjung：WANT VP','gurrany ngunthug nga-ngu waga','NEG like 1SG.A:3SG.P-get/handle.PST.PFV sit','我不想坐在那里／不想留下来。','Schultze-Berndt 2013，ValPaL 例 (132)，https://valpal.info/values/djam1255-want-1','E 由动词索引；所欲内容为 sit 的 VP／小句','尽管注释说此复合谓词也可表示 want something，这个具体例句不能当作 WANT NP 与 LIKE NP 同框架的完整配对证据。')

out.append('## 巴布亚新几内亚\n')
add('Nen：LIKE NP','ärtog-am mleg mñte-ba y-aka-t-e','boy-ERG girl sweetness-COM 3SG.U:α-look.at-ND:B.IPF-3SG.A','那男孩喜欢／爱那女孩。','Evans 2013，ValPaL 例 (94)，https://valpal.info/values/nenn1238-like-1','E-ERG／Y-ABS；COM 附着在 sweetness 上','不能误读成“喜欢的对象 girl 是 COM”。情感／方式成分与真正的偏好对象分开记录。')
add('Nen：WANT VP／名词化事件','bä mñte y-m ungi-s-t','3SG.ABS desirous 3SG.U:α-be:ND stand.up-NMLZ-ALL','他想站起来。','Evans 2013，ValPaL 例 (179)，https://valpal.info/values/nenn1238-want-1','E-ABS／名词化所欲事件-ALL','此 ALL 例证来自事件名词化，不是普通实体 NP；HAPPY ABOUT 尚缺，不能将三项地图填满。')
add('Nen：状态名词作施事的对照','zän ak-äm y-ram-t-e','dog.ABS thirst-ERG 3SG.U:α-do-B.IPF:ND-3SG.A','那狗渴了；直译：口渴作用于那狗。','Evans 2025，p.29，例 (19)','E-ABS／状态名词-ERG','这是状态名词 thirst 作 ERG，不是“想喝的水”作 ERG。不作为 WANT NP／LIKE NP 的直接同义实例。')

add('Komnzo：WANT 名词化事件','zena keke miyo wo\\rä/ ruga mgthk-si … znsä t-tüfr','today NEG desire 1SG.SBJ.NPST.IPFV.be pig feed-NMLZ … work REDUP-plenty','今天我不想喂猪，太多活了。','Döhler 2018，p.320，§9.3.3，例 (21)','E 为系词 S，由动词索引；所欲内容为 pig feeding 名词化短语，作者分析为 ABS','原作者用反斜线和正斜线标示动词形态组合，下同；这里不是普通实体 WANT NP。')
add('Komnzo：be happy towards 的对照','kwa nm weto wo\\rä/r o keke','FUT maybe joy 2|3SG.SBJ>1SG.OBJ.NPST.IPFV.do or NEG','也许他会对我高兴，也许不会？','Döhler 2018，p.310，例 (77)','E 以 do 的主语索引出现；对向对象以 1SG.OBJ 索引出现','独立 E、Y 名词短语均未出现，不能单凭这个例子给二者各添一个显性格后缀；作者的一般构式说明需与实例分列。LIKE 尚未补齐。')

add('Koromu：想喝／想要水','I ya oru-se-r-a','1SG water feel.like-OBJ.1SG-PRS-3SG','我想喝水／想要水。','Priestley 2008，p.409，例 (11.8)；已对扫描页','独立 E 为无显性格形式 I，动词另有 E 宾语后缀；Y 为无标记 ya','作者将消费对象视为 adjunct，不能据英语 water makes me want it 就将其强记为主语。oru 被 OCR 误成 oni，已据页图纠正。')
add('Koromu：feel good inside','oru nokonoko-se-r-a','inside good-OBJ.1SG-PRS-3SG','我心里感觉很好。','Priestley 2008，p.409，例 (11.7)；已对扫描页','E 由 OBJ.1SG 索引；inside 是内部状态／身体部位成分，没有表达外部 Y','这是 feel.good，不足以填入 HAPPY ABOUT NP。此 oru 的 inside 释义与上一例动词同形，不根据表面同形擅自建立历时派生。')

add('Mauwake：LIKE NP','mua eliwa nain kookal-i-yem','man good that1 like-NP-PRS.1SG','我喜欢那个好人。','Berghäll 2015，p.357，例 (170)','E 由动词 1SG 索引；Y 为未标记 NP','NP 是原作者的 non-past 形态标签，不是“名词短语”标签；本文叙述中的 NP 与 gloss 内的 NP 区分。原句也可分析作“我喜欢那个是好人的人”。p.366 注31 明说此动词还涵盖 love／desire。')
add('Kalam：味觉良好，方法对照','yp ydk g-p','1SG.ACC good.tasting do-PFV.3SG','它对我来说很好吃。','Pawley 2006，p.98，例 (21)；ACC 由同页语法说明补明','E-ACC；good.tasting 为 condition 成分','来源逐词只译 me，正文明确此类代词为 ACC，故将分析信息补入 gloss。不是一般偏好 LIKE，更不是 HAPPY，不能直接占据地图节点。')

out.append('## 美洲\n')
add('Kakataibo：同根 WANT','paën-xun kana ‘ë=n ‘atsa kwëën-i-n','get.drunk-S/A>A NAR.1SG 1SG=A manioc.ABS want-IPFV-1/2','我喝醉时会想要／馋木薯。','Zariquiey 2011，p.381，例 (460)','E-A／ERG，Y-ABS','保留作者的代词 A 标记，不假称本例中的 =n 已是普通全名词的独立格后缀；该节正文给出一般 ERG 分析。')
add('Kakataibo：同根裸 HAPPY','paën-ax kana ‘ë=x kwëën-i-n','get.drunk-S/A>S NAR.1SG 1SG=S like-IPFV-1/2','我喝醉时很高兴。','Zariquiey 2011，p.381，例 (461)','E-S；没有表达 Y','gloss 的 like 是原作者此例的词汇标签，句子读法是 happy；不据词根 gloss 偷换为一般偏好。')
add('Kakataibo：同根 LIKE／ENJOY','paën-ax kana ‘ë=x ‘atsa=n kwëën-i-n','get.drunk-S/A>S NAR.1SG 1SG=S manioc=INS like-IPFV-1/2','我喝醉时喜欢／享受木薯。','Zariquiey 2011，p.382，例 (462)','E-S／ABS，Y-INS','作者说有此工具格对象才有该 LIKE 读法；以专有的第三人称工具格代词 anun 辅证，不能因 =n 同形就误标为 ERG。作者提出 happy with → like 的可能发展，尚非已完成的历史重建。')

add('Yucatec Maya：WANT','in kiik-o’ hun-p’éel xa’n-il nah u k’áat','POSS.1SG elder.sister-D2 one-CL.INAN palm-REL house SBJ.3 want','我姐姐想要一间棕榈叶顶的房子。','Lehmann 2013，ValPaL 例 (101)，https://valpal.info/values/yuca1254-want-1','E 为姐姐，与谓词前 u 有人称联系；Y 为所欲房屋 NP','in 是姐姐这一 NP 内部的领有者“我”，不是本句欲望体验者本身。k’áat 的关系名词／verboid 分析见 Lehmann 等 2004 pp.34–35；不将 u 的 SBJ 与 POSS 两种分析强行统一。')
add('Yucatec Maya：LIKE 的眼睛构式','le xibpal-o’ uts t-u y-ich u tumben baaxal','DEM boy-D2 good LOC-POSS.3 0-eye POSS.3 new toy','那个男孩喜欢他的新玩具；直译：他的新玩具对他的眼睛来说是好的。','Lehmann 2013，ValPaL 例 (9)，https://valpal.info/values/yuca1254-like-1','E 为 eye 的领有者，整个身体部位短语置于 LOC；Y 为被评价为 good 的玩具','不简写为“E-DAT”。0 是来源对 y- 的 gloss 标签，保留其呈现，不等同于此处的 Ø flagging。两处 u 各自所属的 NP 也须区分。')
add('Yucatec Maya：HAPPY ABOUT 的心构式','le máak-o’ ki’imak u y-óol yéetel le tsikbal-o’','DEF person-D2 happy POSS.3 0-mind with DEF story-D2','那个人因那个故事而高兴；直译：那个人的心对／因那个故事高兴。','Rott, Verhoeven & Fritz-Huechante 2020，p.412，例 (26a)','E 为 mind 的领有者；Y 由 yéetel 引入','该文还给出使动对应式 (26b)。与 ValPaL 的 LIKE、WANT 来自不同材料，保留各来源的方言与采集说明，不能未经核查就假定全属于一个完全相同的方言点。')

end = '''
## 缩写与来源提示

ABS = absolutive；ACC = accusative；ALL = allative；APPL = applicative；ART = article；A = transitive actor；BEN = benefactive；CL = noun/agreement class；COM = comitative；D2 = 作者的远指／篇章指示标签；DEF = definite；DEM = demonstrative；ERG = ergative；FOC = focus；FV = final vowel；GEN = genitive；INAN = inanimate；INDEF = indefinite；IPF/IPFV = imperfective；IRR = irrealis；LOC = locative；NAR = narrative；ND = non-dual；NEG = negative；NMLZ = nominalizer；NOM = nominative；NP（仅 Mauwake gloss）= non-past；NPST = non-past；OBJ = object；OBL = oblique；PASS = passive；PF.POS = 作者标作 positive perfective 的形式；PFV = perfective；PI = past imperfective；PN = proper name；POSS = possessive；PRF = perfect；PRS = present；PST = past；QUAL = qualitative predicate marker；R = realis（Dalabon）；REFL = reflexive；REL = relational；SEQ = sequential；SG = singular；SM = subject marker；S = intransitive subject；SBJ = subject；TR = transitive；U = undergoer。

P2 保留 Bafut 来源中的第二过去时标签；不凭本例确定其具体时间距离。Kakataibo 的 S/A>A、S/A>S 保留作者的同主语／枢轴标注，箭头后是主句相应论元地位；1/2 是来源的第一／第二人称后缀标签。Nen 的 α 表示需与其他形态联合解释的前缀系列，不是独立时态。Komnzo 的 2|3 表示第二或第三人称的形式合并。

本库标注按莱比锡规则尽量规范，但来源特有的融合分析、A/S/U 系统与存在争议的句法分析均保留；规范化呈现不等于已经解决其理论分析。

完整书目、语言采样与缺口见配套分析文件。PDF 原文和数据库原始记录保留在 research/global_sample/，早期 Kakataibo 与相关 Panoan 材料在 research/ergative/。所有中文翻译为本次据来源英语回译及上下文所作的意译。
'''

target = ROOT/'90_历史方案/02_扩样阶段/心理谓词_全球扩样_莱比锡例句库.md'
target.write_text(intro.replace('COUNT',str(count))+'\n'.join(out)+end)
print(f'{count} examples -> {target}')
