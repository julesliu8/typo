"""Attested Turkish psychological predicates; quotations and supplied Leipzig glosses."""
import json
import re
from pathlib import Path
BASE = Path(__file__).parent
ROOT = BASE.parent.parent
SOURCES = {
 'BIV': dict(title='Ovsjannikova, Maria. 2020. Bivalent patterns in Turkish. BivalTyp. Consultant: Enes Taştan.', url='https://bivaltyp.info/languages/descriptions/Turkish.html', kind='elicited_database', file='bivaltyp_selected.json'),
 'GK': dict(title='Göksel, Aslı & Celia Kerslake. 2005. Turkish: A Comprehensive Grammar. Routledge.', url='https://doi.org/10.4324/9780203340769', kind='reference_grammar', file='goksel_kerslake2005.txt', pdf='goksel_kerslake2005.pdf'),
 'K': dict(title='Kornfilt, Jaklin. 1997. Turkish. Routledge (Descriptive Grammars).', url='https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Turkic/Turkish%20%28Kornfilt%29.pdf', kind='reference_grammar', file='kornfilt1997.txt', pdf='kornfilt1997.pdf'),
 'ETG': dict(title='Demir, Halit. 2025-10-04. Turkish Verb Conjugation: Hoşuna Gitmek. Easy Turkish Grammar.', url='https://www.easyturkishgrammar.com/post/turkish-verb-conjugation-ho%C5%9Funa-gitmek', kind='teaching', file='etg_hosuna.txt'),
 'EL': dict(title='Elon.io. Likes, Dislikes, and Hobbies.', url='https://elon.io/grammar/turkish/expressions/likes-hobbies', kind='teaching_secondary', file='elon_like.txt'),
 'TF': dict(title='Le Roux, Nicolas. 2026-01 (updated). How to Introduce Yourself in Turkish. TurkishFluent.', url='https://turkishfluent.com/blog/how-to-introduce-yourself-in-turkish/', kind='teaching_secondary', file='introductions.txt'),
 'SU': dict(title='gazeteSU, Sabancı Üniversitesi. Öğretim Üyemiz Raha Akhavan, ABD’deki yüzme başarısını gazeteSU’ya anlattı.', url='https://gazetesu.sabanciuniv.edu/tr/ogretim-uyemiz-raha-akhavan-abddeki-yuzme-basarisini-gazetesuya-anlatti', kind='native_interview', file='sabanci_bayil.txt'),
}
ROWS=[]
def add(lexeme,content,realization,y_flag,original,segmentation,gloss,translation,source,location,note='',e_flag='NOM',quote=None):
 assert len(segmentation.split())==len(gloss.split()),(original,segmentation,gloss)
 group=y_flag if y_flag not in ['NONE'] else realization
 ROWS.append(dict(id=f'T{len(ROWS)+1:02}',lexeme=lexeme,content=content,realization=realization,e_flag=e_flag,y_flag=y_flag,frame_group=f'E:{e_flag}|Y:{group}',original=original,segmentation=segmentation,gloss=gloss,translation=translation,source=source,location=location,note=note,source_quote=quote or original))

add('sevmek','ENTITY','NP','ACC','Mehmet Filizi seviyor.','Mehmet Filiz-i sev-iyor','PN.NOM PN-ACC love-IPFV','梅赫梅特爱菲利兹。','BIV','#46','来源专名与格尾间不写撇号；不改正文。')
add('sevmek','ENTITY','NP','ZERO_OBJECT','Mehmet çay sever.','Mehmet çay sev-er','PN.NOM tea love-AOR','梅赫梅特喜欢茶。','BIV','#119','数据库概括栏为 ACC／TR，但本句 çay 没有格尾；按实际表面形式记零标记宾语。茶记普通实体。')
add('sevmek','ENTITY','NP','ZERO_OBJECT','Ayten şapka seviyor.','Ayten şapka sev-iyor','PN.NOM hat like-IPFV','艾滕喜欢帽子。','GK','p.332, §22.4.3, (64); PDF p.357')
add('sevmek','ENTITY','NP','ACC','Ayten şapkayı seviyor.','Ayten şapka-yı sev-iyor','PN.NOM hat-ACC like-IPFV','艾滕喜欢那顶帽子。','GK','p.332, §22.4.3, (65); PDF p.357','与 T03 对照，体现宾语差异标记；不据此拆成两个心理义项。')
add('sevmek','EVENT','NMLZ_NP','ACC','En çok kim-(in)-le şakalaşmayı seviyorsun?','en çok kim-(in)-le şakalaş-ma-yı sev-iyor-sun','most much who-(GEN)-COM joke-NMLZ-ACC like-IPFV-2SG','你最喜欢和谁开玩笑？','GK','p.260, §19.2.1.1, (45); PDF p.285','保留来源可选属格括号。COM 属于事件内部的共同参与者；外层 Y 是 şakalaşmayı-ACC。şakalaş- 作为词汇词干，不是被动或使役。')
add('sevmek','EVENT','NMLZ_NP','ACC','Ahmet araba kullanmasını sever.','Ahmet araba kullan-ma-sı-n-ı sev-er','PN.NOM car drive-NMLZ-POSS.3SG-LNK-ACC like-AOR','艾哈迈德喜欢开车。','GK','p.361, §24.4.1.2, (55); PDF p.386','前页 p.360 说明：口语 sev- 等可用 -mAsInI 代替通常的 -mAyI；这里第三人称领属形式不代表另一个第三人称动作主体。')
add('beğenmek','ENTITY','NP','ACC','Mehmet bu gömleği beğeniyor.','Mehmet bu gömleğ-i beğen-iyor','PN.NOM this shirt-ACC like-IPFV','梅赫梅特喜欢这件衬衫。','BIV','#58')
add('beğenmek','CONTENT_UNRESOLVED','HEADLESS_RELATIVE_NP','ACC','Sizin söylediklerinizi beğendim.','siz-in söyle-dik-ler-iniz-i beğen-di-m','2PL-GEN say-PTCP-PL-POSS.2PL-ACC like-PST-1SG','我喜欢你们说的话。','GK','p.161, §14.3.3.6, (108); PDF p.186','无头关系名词短语；本轮不强行把“说的话／内容”判成事件。该例不能代替明确的“喜欢做某事”用例。')
add('hoşlanmak','ENTITY','NP','ABL','Kız benden hoşlanmamış.','kız ben-den hoşlan-ma-mış','girl.NOM 1SG-ABL like-NEG-EVID','那个姑娘似乎没有喜欢上我。','ETG','第二节的 hoşuna gitmek／hoşlanmak 对照','来源篇章中的 girl 指某个姑娘，不添加实体背后的事件。')
add('hoşlanmak','STATE_NP','LEXICAL_STATE_NP','ABL','Gürcan yağmurlu havalardan hoşlanır.','Gürcan yağmur-lu hava-lar-dan hoşlan-ır','PN.NOM rain-ADJ weather-PL-ABL like-AOR','居尔詹喜欢阴雨天气。','GK','p.159, §14.3.3.5, (92); PDF p.184','保留天气／状态 NP 标签；与普通人物实体分列，暂缓八节点语义归入。')
add('hoşlanmak','EVENT','NMLZ_NP','ABL','okumaktan hoşlanırım','oku-mak-tan hoşlan-ır-ım','read-NMLZ-ABL like-AOR-1SG','我喜欢阅读。','EL','The -mAyI severim pattern 小节','补充教学例；形式与 GK §24.4.1.3 的 -mAktAn 斜格名物化分析一致。原文小写短例。')
add('hoşuna gitmek','ENTITY','NP_SUBJECT','NOM','Film (bizim) hoşumuza gitmedi.','film (biz-im) hoş-umuz-a git-me-di','film.NOM (1PL-GEN) liking-POSS.1PL-DAT go-NEG-PST','我们不喜欢这部电影。','ETG','例句 Film (bizim)...','E 可由 bizim-GEN 出现并在 hoş 上以领属词尾表示；DAT 属于整个 hoş-umuz-a，不把 E 本身误标 DAT。',e_flag='GEN/POSS')
add('hoşuna gitmek','ENTITY','NP_SUBJECT','NOM','Sen çok hoşuma gidiyorsun.','sen çok hoş-um-a gid-iyor-sun','2SG.NOM very liking-POSS.1SG-DAT go-IPFV-2SG','我很喜欢你。','ETG','例句 Sen çok...','Y 是 sen，谓语 -sun 与 Y 的第二人称一致；E 是 hoş 上第一人称领属词尾。',e_flag='GEN/POSS')
add('hoşuna gitmek','ENTITY','NP_SUBJECT','NOM','Ben kızın hoşuna gitmemişim.','ben kız-ın hoş-u-n-a git-me-miş-im','1SG.NOM girl-GEN liking-POSS.3SG-LNK-DAT go-NEG-EVID-1SG','那个姑娘似乎不喜欢我。','ETG','例句 Ben kızın...','显式 E＝kız-ın GEN；Y＝ben NOM。保留与 T09 的取向对照。',e_flag='GEN/POSS')
add('istemek','ENTITY','NP','ZERO_OBJECT','Mehmet yeni telefon istiyor.','Mehmet yeni telefon isti-yor','PN.NOM new phone want-IPFV','梅赫梅特想要一部新手机。','BIV','#121','来源标 TR／ACC，但实际 telefon 为无格尾对象，不补造 ACC。')
add('istemek','EVENT','NMLZ_NP','ZERO_OBJECT','Sokağa çıkmak istiyorum.','sokağ-a çık-mak isti-yor-um','street-DAT go.out-NMLZ want-IPFV-1SG','我想出去。','GK','p.358, §24.4.1, (39); PDF p.383','外层 -mAk 为无格尾的事件名词性补语；sokağa 的 DAT 是事件内部去向。按本研究约定，名物化实现记 NP，内容仍为 EVENT。')
add('istemek','EVENT','NMLZ_NP','ACC','Sokağa çıkmanı istiyorum.','sokağ-a çık-ma-n-ı isti-yor-um','street-DAT go.out-NMLZ-POSS.2SG-ACC want-IPFV-1SG','我想让你出去。','GK','p.358, §24.4.1, (40); PDF p.383','中文“让”不表示原文使用 CAUS：原文为主动 iste- 加 -mA 领属名物化；与 T16 同主语／异主语的分布有关。')
add('istemek','EVENT','NMLZ_NP','ACC','Turgutun gelmesini istiyorum.','Turgut-un gel-me-si-n-i isti-yor-um','PN-GEN come-NMLZ-POSS.3SG-LNK-ACC want-IPFV-1SG','我希望图尔古特来。','GK','p.161, §14.3.3.6, (106); PDF p.186','Turgut-GEN 是嵌入事件的主语；外层 Y-ACC 在 gelmesini 上。原文 Turgut-un 的边界改为整词，撇号未增补。')
add('istemek','EVENT','KI_FINITE','NONE','İstiyorum ki Ali üniversiteye gitsin.','isti-yor-um ki Ali üniversite-ye git-sin','want-IPFV-1SG COMP PN.NOM university-DAT go-OPT.3SG','我希望阿里上大学。','K','p.14, (60); PDF p.46','有限 ki 从句单列，不把内部大学-DAT 当外层格；-sIn 跟随来源标 OPT。OCR 的 ii 已按原书土耳其字母 ü 校正。')
add('istemek','EVENT','BARE_FINITE_OPT','NONE','Bu kitabı okuyasın istiyorum.','bu kitab-ı oku-yasın isti-yor-um','this book-ACC read-OPT.2SG want-IPFV-1SG','我希望你读这本书。','K','p.373, §2.1.3.4.4, (1291a); PDF p.405','来源将此类完全有限的嵌入形式称少见。与常见 -mA 名物化 T21 对照；不是把所有裸动词补语都标为有限。')
add('istemek','EVENT','NMLZ_NP','ACC','Bu kitabı okumanı istiyorum.','bu kitab-ı oku-ma-n-ı isti-yor-um','this book-ACC read-NMLZ-POSS.2SG-ACC want-IPFV-1SG','我希望你读这本书。','K','p.373, §2.1.3.4.4, (1291b); PDF p.405','kitabı-ACC 是嵌入“读”的对象；okumanı-ACC 才是外层 Y。')
add('sevinmek','ENTITY','NP','DAT','Mehmet mektuba sevindi.','Mehmet mektub-a sevin-di','PN.NOM letter-DAT rejoice-PST','梅赫梅特为那封信高兴。','BIV','#83','按用户约定，信直接记实体，不推断读信／收到信。')
add('sevinmek','EVENT','NMLZ_NP','DAT','Ayşenin geleceğine sevindik.','Ayşe-nin gel-eceğ-i-n-e sevin-di-k','PN-GEN come-NMLZ.FUT-POSS.3SG-LNK-DAT rejoice-PST-1PL','我们为艾谢将要来而高兴。','GK','p.157, §14.3.3.3, (76); PDF p.182','外层 DAT 在未来名物化上；Ayşe-GEN 是事件内部主语。原文以 Ayşe’nin 写撇号，此处只合并格边界。')
add('sevinmek','EVENT','NMLZ_NP','DAT','Mehmetin geleceğine seviniyorum.','Mehmet-in gel-eceğ-i-n-e sevin-iyor-um','PN-GEN come-NMLZ.FUT-POSS.3SG-LNK-DAT rejoice-IPFV-1SG','我很高兴梅赫梅特将要来。','GK','p.291, §21.3.3, (37b); PDF p.316','同页 (37a) sevindim 使用同样 DAT 内容；时体不同不另建 flagging 框架。')
add('sevinmek','EVENT','NMLZ_NP','DAT','Tanıştığımıza sevindim.','tanış-tığ-ımız-a sevin-di-m','meet-NMLZ-POSS.1PL-DAT rejoice-PST-1SG','我很高兴我们认识了。','TF','§2.2 Nice to meet you / Me too','教学补例，用 -DIK 名物化，与未来 -AcAK 名物化同归 DAT；保留后缀种类差异。')
add('memnun (olmak)','ENTITY','NP','ABL','Mehmet oğlundan memnun.','Mehmet oğl-u-n-dan memnun','PN.NOM son-POSS.3SG-LNK-ABL satisfied','梅赫梅特对他的儿子满意。','BIV','#112','形容词述谓、第三人称零系词；不擅自补 ol-。')
add('memnun (olmak)','EVENT','NMLZ_NP','DAT','Tanıştığıma memnun oldum.','tanış-tığ-ım-a memnun ol-du-m','meet-NMLZ-POSS.1SG-DAT pleased be-PST-1SG','很高兴认识你。','TF','§1 Nice to meet you','这条实证为 DAT，不是 ABL；不可因词条实体例为 ABL 而将事件式也预设为 ABL。原句嵌入领属为 1SG，译文自然表达为认识你。')
add('memnun (olmak)','EVENT','LEXICAL_EVENT_NP','ABL','Ne yabancılar ne (de) mahalle halkı otobüs turlarından memnunlar.','ne yabancı-lar ne (de) mahalle halk-ı otobüs tur-lar-ı-n-dan memnun-lar','neither foreigner-PL.NOM nor (also) neighborhood population-CMPD bus tour-PL-CMPD-LNK-ABL satisfied-3PL','外国游客和当地居民都对巴士游览不满意。','GK','p.276, §20.4, (37); PDF p.301','游览为明确活动 NP；土耳其语 ne...ne 表达否定，并非被动。外层 ABL 位于复合名词 turlarından。')
add('bayılmak','ENTITY','NP','DAT','Herkes piyaniste bayıldı.','herkes piyanist-e bayıl-dı','everyone.NOM pianist-DAT adore-PST','人人都很喜欢那位钢琴家。','GK','p.128, §13.1.2.2, (15); PDF p.153','保留 adore 义项；不同于昏倒义。')
add('bayılmak','EVENT','NMLZ_NP','DAT','Türkiye’nin her yerinde yüzmeye bayılıyorum!','Türkiye-nin her yer-i-n-de yüz-me-ye bayıl-ıyor-um','PN-GEN every place-POSS.3SG-LNK-LOC swim-NMLZ-DAT adore-IPFV-1SG','我特别喜欢在土耳其各地游泳！','SU','采访末尾，关于下一步游泳计划的回答','母语采访原句；以不含使役的 yüz- 事件补齐 DAT 两侧。地点内部 GEN／LOC 不计入外层心理框架。')
add('âşık olmak','ENTITY','NP','DAT','Mehmet Filize âşık oldu.','Mehmet Filiz-e âşık ol-du','PN.NOM PN-DAT enamoured become-PST','梅赫梅特爱上了菲利兹。','BIV','#113','主动状态变化表达；不是被动或 CAUS。事件式本轮未取得合格例证。')

# Search validation ignores spaces, morphological separators and case, never silently changes wording.
def norm(s):
 return ''.join(c for c in s.casefold() if c.isalnum())

def verify():
 for r in ROWS:
  if r['source']=='BIV':
   x=next(x for x in json.loads((BASE/'bivaltyp_selected.json').read_text()) if '#'+x['predicate_no']==r['location'])
   assert norm(r['source_quote'])==norm(x['sentence']),r['id']
  elif r['source']!='K':
   assert norm(r['source_quote']) in norm((BASE/SOURCES[r['source']]['file']).read_text()),(r['id'],r['source_quote'])
  # Kornfilt is image OCR: its three cited examples are verified from rendered source pages.

INTRO='''# 土耳其语心理谓词：实体／事件构式与逐例标注

采集日期：2026-11-12。接续日语、芬兰语，先记录 LIKE／LOVE／WANT／HAPPY 周围的词项和构式，细分语义及八节点最终编码暂缓。这里有 **9 个词项／词汇构式、31 条有出处的例句**。语法书为主要来源，数据库和教学／实际用例补充语法书未覆盖的一侧。

普通实体（人、茶、帽子、衬衫、信、手机）直接记实体；活动、事件名词和显式事件名物化另记 EVENT。**事件名物化在句法实现上记 NP，同时保留事件内容标签。排除被动和 CAUS 构式。** 没有找到的一侧记 `?`，不等于不合语法。

## 1. 构式汇总

|词项|实体侧已见|事件侧已见|主要对照|
|---|---|---|---|
|sevmek 喜欢／爱|Y-ACC；Y-Ø 对象|V-mA-ACC；口语 V-mA-POSS.3SG-ACC|ACC 可跨实体／事件；实体另有零标记宾语|
|beğenmek 喜欢／认可|Y-ACC|语法书明确允许 -mA-ACC，但本轮未取得该式心理谓词完整原句；另有“说的话”无头关系 NP-ACC|不把内容关系 NP 直接当事件正例|
|hoşlanmak 喜欢|人物 Y-ABL；天气状态 NP-ABL|V-mAk-ABL|ABL 可跨实体／事件|
|hoşuna gitmek 合意／喜欢|Y-NOM 主语；E-GEN／POSS|?|与多数 E-NOM 构式取向不同|
|istemek 想要|Y-Ø 对象|V-mAk-Ø；V-mA-POSS-ACC；ki＋有限 OPT 从句；裸有限 OPT 从句|同一词有多种事件补语，不能只按 want 译词取一式|
|sevinmek 高兴|Y-DAT|V-AcAK-POSS-DAT；V-DIK-POSS-DAT|DAT 可跨实体／事件|
|memnun (olmak) 满意／高兴|Y-ABL|活动 NP-ABL；V-DIK-POSS-DAT|实际事件例同时见 ABL 和 DAT；不是恒定单一格|
|bayılmak 极喜欢|Y-DAT|V-mA-DAT|DAT 可跨实体／事件|
|âşık olmak 爱上|Y-DAT|?|主动状态变化式，单列保留|

除 hoşuna gitmek 外，这些正例的 E 按 NOM 框架记录；省略的体验者由人称词尾体现，不人为补入主语。hoşuna gitmek 的 E 是显式 GEN 或领属索引：如 kız-ın hoş-u-n-a 中，**GEN 在姑娘上，DAT 在“合意／喜好”这个领属名词短语上**；Y 是控制谓语人称一致的主语。

## 2. 编码规则与语法依据

- **同一外层格合组，实际实现分存。** NP-ACC 和事件名物化-ACC 可同归 `E:NOM|Y:ACC`，DAT／ABL 同理；名物化种类记录在实现及逐词标注中。ki 有限从句和裸有限从句分别成组。这个规则接续芬兰语当前粒度，不主张不同实现句法完全相同。
- **无格尾对象单列 ZERO_OBJECT。** GK pp.128、332–333 和 BIV 语法说明支持土耳其语宾语差异标记：T03 şapka 与 T04 şapkayı 是同词不同对象形式。不能只读取数据库 ACC 总括栏；也不能把无格尾对象一概标成句法 NOM。
- **-mAk 是事件名词性实现。** GK pp.358–361 讨论其作为主语、述语和对象的用途，并指出 iste- 经常取无格尾 -mAk 对象；其他及物词通常要求 -mAyI。按本研究约定记 `NMLZ_NP`，书中常见的 infinitive／verbal noun 称呼在此对应 NMLZ，不误等同于日语连用型或芬兰语 A 不定式。
- **内外层格分开。** T18 Turgut-un 是事件的主语 GEN，gelmesini 才是外层内容 ACC；T16 的 sokağa 是出去的去向，不是 want 支配 DAT。
- **保留同一词的多个框架。** T27 的 memnun 事件式实际用 DAT，T28 的游览活动名词用 ABL，二者都保留。不要根据实体侧的一个格预测事件侧只有该格。
- **语法描述与完整原句不同级。** GK p.366 §24.4.2.2(d) 明确把 beğen- 列为可取 -mA 对象的态度词，但紧接完整例句用的是 affet-。因此本轮记录这项描述性证据，不编造 beğen-＋-mA 的句子。T08 单独保留为无头关系 NP，不充当该缺例。

## 3. 来源

'''
TAIL='''
## 5. 本轮得到的初步分布与待补项目

已有三组直接的跨实体／事件格框架：ACC（sevmek）、DAT（sevinmek、bayılmak）、ABL（hoşlanmak，事件一侧当前为补充教学例）。memnun 另提示，同一词的事件表达可以有不止一个格框架。hoşuna gitmek 的 Y 主语取向也说明不能只为每种词义记录一个 Y 格尾而忽略 E 的实现。

这些是构式覆盖的证据，还不能据此提出 WANT→LIKE→HAPPY 的蕴含共性。后续需在语义判定后，分别以格框架及具体词项作为观察单位作图；实体侧受宾语差异标记影响，零标记与 ACC 两式要保留，不能当作取样误差删除。

下一轮优先补：beğenmek 的明确活动／事件 -mA 原句；hoşuna gitmek 的非被动、非使役事件原句；âşık olmak 的事件对应式；mutlu、arzu etmek、dilemek 等更多词项。本轮没有为这些空白按直觉造句。ETG 的事件对照用 vakit geçirmek “花时间”；为避免其中 geçir- 的词形派生干扰当前排除 CAUS 的口径，该句暂不进入例句集。

缩写：NOM 主格；ACC 宾格；DAT 与格；ABL 离格；GEN 属格；LOC 方位格；COM 共伴；POSS 领属；NMLZ 名物化；NMLZ.FUT 未来名物化；PTCP 关系／分词形式；IPFV 未完成体（BIV 原文将 -yor 标 PRS，GK 将它标 IMPF，此处统一）；AOR 一般／习惯形式；PST 过去；EVID 传闻／间接证据形式；OPT 祈愿（跟随 K 的术语）；NEG 否定；COMP 补语连词；LNK 无独立语义的连接辅音；CMPD 复合标记；PN 专名。缓冲 y 与元音后格尾合写（如 -yı），领属后的 n 单独标 LNK；不从这些连接辅音推导额外论元。

逐词切分与缩写由本研究统一提供，不冒充各来源完全一致的原注。第三人称单数零人称标记通常不另写；零格尾对象不补 -Ø。原句去除书中分析用的连字符／中括号，个别保留的可选成分照录。K 的图像 OCR 有字母错误，已核读原页再规范化。原始资料、来源记录、结构化例句与构建脚本保存于 research/turkish_pilot/。
'''

def render():
 text=INTRO
 for key,s in SOURCES.items():text+=f"- **{key}**：{s['title']} [来源]({s['url']})；类型 `{s['kind']}`。\n"
 text+='\n书页均为印刷页码；另列 PDF 文件的 1 起算页码。网页访问日期 2026-11-12。补充教学例不等同于母语者判断实验，明确保留来源类型。\n\n### 当前归并框架\n\n|框架组|词项|例号|\n|---|---|---|\n'
 groups={}
 for r in ROWS:groups.setdefault(r['frame_group'],[]).append(r)
 for group,rs in groups.items():text+=f"|{group}|{'、'.join(dict.fromkeys(r['lexeme'] for r in rs))}|{'、'.join(r['id'] for r in rs)}|\n"
 text+='\n## 4. 原句、切分和莱比锡标注\n'
 for r in ROWS:
  text+=f"\n### {r['id']} · {r['lexeme']} · {r['content']}\n\n原句：**{r['original']}**\n\n```text\n{r['segmentation']}\n{r['gloss']}\n```\n\n“{r['translation']}”\n\n框架 `{r['frame_group']}`；实现 `{r['realization']}`。来源 **{r['source']}**，{r['location']}。\n"
  if r['note']:text+='\n'+r['note']+'\n'
 text+=TAIL
 (ROOT/'02_语言材料/已移出样本/土耳其语/土耳其语心理谓词_实体事件构式_例句与标注.md').write_text(text)
 (BASE/'examples.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2)+'\n')
 (BASE/'sources.json').write_text(json.dumps(SOURCES,ensure_ascii=False,indent=2)+'\n')
 (BASE/'frame_groups.json').write_text(json.dumps({g:[r['id'] for r in rs] for g,rs in groups.items()},ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
 verify();render();print(f'Saved {len(ROWS)} examples across {len(set(r["lexeme"] for r in ROWS))} lexemes/constructions.')
