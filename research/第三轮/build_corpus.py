from pathlib import Path
import json,csv,re,collections
root=Path(__file__).resolve().parents[2]
D=[]
def a(id,lang,topic,form,gloss,trans,src,loc,frame,note='',status='已核全文'):
 D.append(dict(id=id,language=lang,topic=topic,form=form,gloss=gloss,translation=trans,source=src,location=loc,frame=frame,note=note,status=status))
# Basque: direct Mouton journal source
a('B01','Basque','仇恨：动词','Jon-ek hau gorrota-tzen du','Jon-ERG this.ABS hate-IPFV have.3SG.ABS.3SG.ERG','Jon 恨这个。','B2020','p. 649, (2a)','E-ERG / St-ABS')
a('B02','Basque','担忧：Stimulus 作格','Hon-ek Jon kezka-tzen du','this-ERG Jon[ABS] worry-IPFV have.3SG.ABS.3SG.ERG','这个使 Jon 担忧。','B2020','p. 649, (2b)','E-ABS / St-ERG','原文表2把 kezkatu 写成 fear，但本例的动词释义和译文均为 worry；这里依例句。')
a('B03','Basque','喜欢：Experiencer 与格','Jon-i hau gusta-tzen zaio','Jon-DAT this.ABS please-IPFV be.3SG.ABS.3SG.DAT','这个让 Jon 喜欢。','B2020','p. 649, (2c)','E-DAT / St-ABS')
a('B04','Basque','名词／形容词性 atsegin：与格 E','Jon-i hau atsegin zaio','Jon-DAT this.ABS pleasant be.3SG.ABS.3SG.DAT','Jon 觉得这个令人愉快。','B2020','p. 650, (3b)','E-DAT / St-ABS','atsegin 的源释义是 pleasure/pleasant；此处用 pleasant 作简洁词汇释义，不据此裁定其词类。')
a('B05','Basque','同一 atsegin：作格 E','Jon-ek hau atsegin du','Jon-ERG this.ABS pleasant have.3SG.ABS.3SG.ERG','Jon 从这个获得愉悦。','B2020','p. 650, (4)','E-ERG / St-ABS','与 B04 构成有出处的构式对照；不假定两者完全同义。')
a('B06','Basque','忠诚：与格 Stimulus','Jon horr-i leiala da','Jon[ABS] that-DAT loyal be.3SG.ABS','Jon 对那个忠诚。','B2020','p. 650, (5)','E-ABS / St-DAT','这是关系／态度形容词；严格心理谓词样本可将其列为边缘项。原例不拆 leiala。')
a('B07','Basque','恐惧名词：作格—与格','Jon-ek horr-i beldur dio','Jon-ERG that-DAT fear have.3SG.ABS.3SG.DAT.3SG.ERG','Jon 害怕那个。','B2020','p. 651, (6)','E-ERG / St-DAT','助动词含默认3SG.ABS形式；不能由此补设第三个指称性论元。')
a('B08','Basque','在意／关切：与格—作格','Horr-ek Jon-i ardura dio','that-ERG Jon-DAT care have.3SG.ABS.3SG.DAT.3SG.ERG','那个对 Jon 很重要／让 Jon 挂心。','B2020','p. 651, (7)','E-DAT / St-ERG','同样不能把助动词的默认 ABS 形式当作一个隐含心理名词论元。')
a('B09','Basque（东北部）','感兴趣：ABS—DAT','1920–1950 urte-etako margolari-a-k bereziki baiones-a-k zer-i interesa-tzen ote ziren','1920–1950 year-PL.REL painter-DET-PL[ABS] especially Bayonnais-DET-PL[ABS] what-DAT interest-IPFV Q be.PST.3PL.ABS','1920至1950年的画家，尤其是巴约讷的画家，对什么感兴趣？','B2020','p. 688, (73b)','E-ABS / St-DAT','原例来自 Oyharçabal 的词典。urte-etako 中 PL.REL 保留融合标注；助动词无 DAT 索引。不是所有 Basque 方言的默认框架。')
a('B10','Basque（东北部）','引起兴趣：ERG Stimulus','Okupazio garai-ko istorio-ek ez zaituzte interesa-tzen','occupation time-REL story-DET.PL.ERG NEG have.2.ABS.3PL.ERG interest-IPFV','关于占领时期的故事不能引起你的兴趣。','B2020','p. 689, (77)','E-ABS / St-ERG','2 的数值依原释义不另补 SG；与 B09 存在“对……感兴趣／吸引……”的意义差异。')
a('B11','Basque（西南部）','interest：DAT E（原例首个主句）','Kixote-a dio Menar-ek izugarri interesa-tzen zait','Quixote-DET[ABS] say.3SG.ABS Menard-ERG enormously interest-IPFV be.1SG.DAT.3SG.ABS','“《堂吉诃德》非常吸引我，”Menard 说。','B2020','p. 688, (74), 首个主句','E-省略（AUX.1SG.DAT）/ St-ABS','保留原句插入语 dio Menar-ek；未录后面的“但是……”主句。Menar-ek 是“说”的论元，不能编码成 interest 的 E。')
# Lezgian: secondary quotations of Haspelmath
a('L01','Lezgian','爱','Za-z wun k’an-zawa','1SG-DAT 2SG.ABS love-IPFV','我爱你。','LSV2004','p. 79, E129b；引 Haspelmath 1993:137','E-DAT / St-ABS',status='已核转引；原书页码待复核')
a('L02','Lezgian','恐惧：空间来源格 St','Za-z wa-qʰaj kič’e-zwa','1SG-DAT 2SG-POEL afraid-IPFV','我怕你。','LSV2004','p. 79, E129d；引 Haspelmath 1993:138','E-DAT / St-POEL','POEL=postelative；将原上标 h 转写为 ʰ，不能简化成泛称 DAT。',status='已核转引；原书页码待复核')
a('L03','Lezgian','生气：情绪名词＋来','I kardi-kaj aslandi-z gzaf qʰel ata-na','this thing.OBL-SBEL lion.OBL-DAT much anger come-AOR','狮子对此非常生气。','LSV2004','p. 79, E129c；引 Haspelmath 1993:282','E-DAT / St-SBEL','qʰel 是“怒气”；E 是 aslandi-z。不要把 anger 的语义角色等同于 St。SBEL=subelative。',status='已核转引；原书页码待复核')
a('L04','Lezgian','变得高兴','Šičanbikedi-z gzaf šad x̂a-na','Šičanbike.OBL-DAT much glad be-AOR','Šičanbike 变得非常高兴。','LSV2004','p. 79, E129a；引 Haspelmath 1993:282','E-DAT / St-未表达',status='已核转引；原书页码待复核')
a('L05','Lezgian','高兴状态（原例首句）','Idris q̃e šad tir','Idris[ABS] today glad COP.PST','Idris 今天很高兴。','LSV2004','p. 79, E129e；引 Haspelmath 1993:112','E-ABS / St-未表达','与 L04 不是控制其他条件的最小对立：谓词、时体及变化／状态意义都有差别。',status='已核转引；原书页码待复核')
a('L06','Lezgian','遗忘：E 为“心”的领属者','Č’ul q̃aču-z či rik’e-laj alat-na','belt take-INF 1PL.GEN heart.OBL-SREL fall.off-AOR','我们忘了带上腰带。','LSV2004','p. 88, E155a；引 Haspelmath 1993:295','E-GEN（领属者）/ 内容-INF短语','直译“带腰带这件事从我们的心上掉下去了”。SREL=superelative；不是 E 的格，而是 heart 的空间格。',status='已核转引；原书页码待复核')
# Lezgic close relative + one more distant control
a('A01','Agul（Huppuq）','看见','za-s we ruš agu-ne','1SG-DAT 2SG.GEN daughter[ABS] see-PST','我看见了你的女儿。','GMM2008','p. 174, (3)','E-DAT / St-ABS','Lezgic 内部近亲对照；we 的原释义 your，这里规范为 2SG.GEN。')
a('A02','Agul（Huppuq）','听见','dad.a-s wuri unxu-ne','father-DAT everything[ABS] hear-PST','父亲听见了一切。','GMM2008','p. 187, (39a)','E-DAT / St-ABS','保留原转写 dad.a 中的词干内部点，不将其补拆为新语素。')
a('A03','Agul（Huppuq）','使某人听见：迂回使动','baw.a dad.a-s wuri unx.a-s q’u-ne','mother.ERG father-DAT everything[ABS] hear-INF do-PST','母亲使父亲听见了一切。','GMM2008','p. 187, (39b)','Causer-ERG / E-DAT / St-ABS','心理谓词位于不定式补语。作格母亲是上层使动者；E 父亲仍保留 DAT。不能把该例编码成“hear 的 E-ERG”。')
a('Z01','Bezhta','爱：远亲参照','di-l kid y-ac-ca','1SG-LAT girl[II.ABS] II-love-PRS','我（男性说话人）爱这个女孩。','CFK2013','p. 34, (6)','E-LAT / St-ABS','Tsezic 支，非 Lezgic 近亲。仅用于更高层级对照；y- 索引 II 类 ABS Stimulus。')
# Qiang public manuscript, visually checked
a('Q01','Qiang（Ronghong）','喜欢','qɑ khumtsi topu-ɑ','1SG Khumtsi like-1SG','我喜欢 Khumtsi。','LH稿','p. 77, (3.77b)','E-Ø / St-Ø','保留作者 actor 范畴；Ø=没有显性关系标记，不自动重标 ABS。')
a('Q02','Qiang（Ronghong）','不相信他的话','qɑ theː-tɕ-ʐəwɑ me-ɕtɕɑ','1SG 3SG-GEN-word NEG-believe.1SG','我不相信他说的话。','LH稿','p. 78, (3.78)','E-Ø / 内容NP-Ø','GEN 在内容NP内部，标记“他”；不是 St-NP 的论元格。相信词形按页面转写；原文词根另列 ɕtɕe。')
a('Q03','Qiang（Ronghong）','听见孩子的声音','qɑ tɕymi-tɕ-qəi ə-mɑ','1SG child-GEN-voice DIR-hear.1SG','我听见了孩子的声音。','LH稿','p. 83, (3.98)','E-Ø / St-NP-Ø','GEN 只标记声音的领属者 child；听见词形含融合的1SG。')
a('Q04','Qiang（Ronghong）','恐惧（去掉时间话题的节录）','… ʂkup-teː mo-qu-ɑ','… orangutan-DEF.CL NEG-be.afraid-1SG','……（我）不怕这只猩猩。','LH稿','p. 83, (3.102), 末尾主句','E-省略（V.1SG）/ St-Ø','原句句首是“今晚”。省略号只用于标明节录；不能把没有显现的 E-NP 判作 ABS。')
a('Q05','Qiang（Ronghong）','恼怒：反身 Stimulus','ʔiʔi-ɳɑ tɕe-khue','2SG.REFL-COM PROH-upset','别生自己的气。','LH稿','p. 96, (3.153)','E-命令句省略 / St-COM','反身命令句；证明 COM 可标记此构式的对象，但不足以确定所有普通陈述句的框架。原 NEG.IMP 规范为 PROH。')
# Southern Qiang relative
a('P01','Qiang（Puxi）','恐惧','tʰala ɕe-tɕi la mi-qu','3SG who-INDF also NEG-afraid.3','他／她不怕任何人。','H2004','p. 68, (60)','E-Ø / St-Ø','ɕe-tɕi 与 la、否定合用为“任何人”；这里无 AGT。')
a('P02','Qiang（Puxi）','喜欢','tʰala ɲi-tɕi la mi-mɑ','3SG what-CL also NEG-like.3','他／她什么也不喜欢。','H2004','p. 68, (61)','E-Ø / St-Ø','what-CL 依原标注保留，不因它与上一例形式相近就统一改为 INDF。')
a('P03','Qiang（Puxi）','听见：小句内容','ŋa no tsʰuə-n te-no-si','1SG.TP 2SG.TP cough-2 DIR-hear-CSM.1','我听见你在咳嗽。','H2004','p. 107, (141)','E-Ø / 内容小句-无显性从属标记','原文将 no tsʰuə-n 置于方括号。TP=topical pronoun form；并非附加在代词后的 TOP 后缀。CSM.1 沿用作者人称精度。')
a('P04','Qiang（Puxi）','认识：face＋know','tʰala kue ɕe sə bɑ','3SG 2SG.NTP face know.3 PRT','他／她认识你吗？（猜测）','H2004','p. 225, (436a)','E-Ø / 对象-代词NTP形','原词末元音按图为 bɑ；NTP=non-topical pronoun form。“face know”的内部论元结构仍需详查，不能直接当作简单 know 的双宾语例句。')
# Kakataibo
a('K01','Kakataibo','害怕：名词 Stimulus','‘ë=x kana rakwët-i-n ‘inu=mi','1SG=S NAR.1SG be.scared.of-IPFV-1/2 jaguar=IMPR.LOC','我怕美洲豹。','Z2011','p. 366, (442)','E-S / St-IMPR.LOC','代词 =x 标 S；不是本库重标的 ABS。1/2 指第一或第二人称，非复数。')
a('K02','Kakataibo','害怕：名词化内容','‘ë=x kana rakwët-i-n ‘inu=n pi-ti=mi','1SG=S NAR.1SG be.scared.of-IPFV-1/2 jaguar=ERG eat-NMLZ=IMPR.LOC','我怕美洲豹会吃掉我。','Z2011','p. 366, (443)','E-S / 内容-NMLZ=IMPR.LOC','原文 [‘inu=n pi-ti]=mi：整个名词化小句带 =mi。ERG 是嵌入小句的美洲豹，不是恐惧主句的 St 格；“我”在嵌入小句中无独立形式。')
a('K03','Kakataibo','思考：及物','a kana ‘ë=n sinan-i-n','this.O NAR.1SG 1SG=A think-IPFV-1/2','这个，我想。','Z2011','p. 380, (459), transitive use','E-A / 内容-O','按原句短译；不把 this 自动改写成自由的命题补语。')
a('K04','Kakataibo','想念：完整原例','‘ë=n bëchikë kwan-an kana tsót-i ‘ë=x a=mi sinan-i-n','1SG=GEN son[ABS] go-DS/A/O.PE NAR.1SG sit.down-A/S>S.SE 1SG=S 3SG=IMPR.LOC miss-NPST-1/2','儿子离开后，我坐着想念他。','Z2011','p. 380, (459), intransitive use','E-S / St-IMPR.LOC','switch-reference 的 DS/A/O.PE、A/S>S.SE 为作者特定缩写，见术语表；保留其分类，不凭词形把 NPST 默改成 IPFV。')
a('K05','Kakataibo','想要：同根 kwëën-','paën-xun kana ‘ë=n ‘atsa kwëën-i-n','get.drunk-S/A>A NAR.1SG 1SG=A manioc[ABS] want-IPFV-1/2','我喝醉时就想吃木薯。','Z2011','p. 381, (460)','E-A / 对象-ABS','严格语义可称欲望对象而非因果 Stimulus。')
a('K06','Kakataibo','高兴：同根 kwëën-','paën-ax kana ‘ë=x kwëën-i-n','get.drunk-S/A>S NAR.1SG 1SG=S be.happy-IPFV-1/2','我喝醉时很高兴。','Z2011','p. 381, (461)','E-S / St-无','原文第一行 paëanx、分析行 paën-ax 不一致，本库采用分析行；源 gloss 为 like 而译文为 am happy，依该节明确的三义分析标为 be.happy。')
a('K07','Kakataibo','喜欢／享受：同根 kwëën-','paën-ax kana ‘ë=x ‘atsa=n kwëën-i-n','get.drunk-S/A>S NAR.1SG 1SG=S manioc=INS like-IPFV-1/2','我喝醉时喜欢／享受木薯。','Z2011','p. 382, (462)','E-S / St-INS','这里的 =n 是 INS；作者以专用于工具格的代词 anun 支持这一分析（p.381注65）。与 A 标记同形不等于同功能。')
# Shipibo Konibo
a('S01','Shipibo-Konibo','生气','E-a-ra Yabi-ki sinat-ai','1-ABS-EV Yabi-DAT be.angry-INC','我生 Yabi 的气。','V2003','p. 340, ch.8 (50)','E-ABS / St-DAT','EV、INC 保留作者标签；原书用连字符记录 -ra，此处不擅改为 =。')
a('S02','Shipibo-Konibo','恐惧及额外受益／关涉者','E-a-ra ino-ki (mi-on) raké-ke','1-ABS-EV jaguar-DAT (2-INTRSS) be.scared.of-CMPL','我怕这只美洲豹（替你担心，因为它可能攻击你）。','V2003','p. 340, ch.8 (51)','E-ABS / St-DAT / 关涉者-INTRSS（可选）','保留原文括号：部分说话人允许额外的 interessive 补足语。mi-on 不是怕的直接 St。')
a('S03','Shipibo-Konibo','爱：同根 keen-','E-a-ra mi-on keen-ai','1-ABS-EV 2-INTRSS want-INC','我爱你。','V2003','p. 343, ch.8 (59)','E-ABS / St-INTRSS','源 gloss 为 want，正文明确此义为 love。原例还给出 *mi-a，排除本 love 义下的 ABS Stimulus；本库不把未录的非语法变体计成新例。')
a('S04','Shipibo-Konibo','想要：直接引语节录','Kankan-bicho-ressa no-a keen-ai papá','pineapple[ABS]-only-just.EV 1PL-ABS want-INC father.VOC','至少我们想要菠萝，父亲。','V2003','p. 343, ch.8 (57), 引语内部','E-ABS / 对象-ABS','原文来自 Bardales 1979:15，经 Valenzuela 分析。保留其引语内的完整分句；与 S03 显示语义制约，不能把所有 keen- 统一标成一个框架。')
# Newar
a('D01','Dolakha Newar','知道：E 作格，内容省略','siru=n sir-ai','Siru=ERG know-3SG.PRS','Siru 知道。','G1997','p. 40, (6)','E-ERG / 内容-省略','该例特意说明即使宾语省略，及物主语仍标 ERG。')
a('D02','Dolakha Newar','看见：St 与格','āpsin balaku keti twāŋsona=ta khon-ju','3PL.ERG beautiful girl Twāŋsona=DAT see-3SG.PST','他们看见了漂亮的女孩 Twāŋsona。','G1997','p. 51, (18)','E-ERG / St-DAT','动词原标 3sg:PST，虽主语3PL也不擅改；与格对象须结合有生性、可及性与篇章分析。')
# Fix one proper-name token directly to keep alignment
D[-1]['gloss']='3PL.ERG beautiful girl Twāŋsona=DAT see-3SG.PST'
a('D03','Dolakha Newar','看见：宾语关系化','jin khon-a keti','1SG.ERG see-NR2 girl','我看见的那个女孩。','G1997','p. 55, (24)','E-ERG / St-关系化空位','这是 NP 内的关系从句，不是独立双论元陈述句。证明心理谓词可进入修饰结构；NR2 是作者命名的第二关系化形式。')
a('D04','Dolakha Newar','记起：叙事链分句','āle āmu bisnu bāgabān=ta lyāsmisā=ta=ŋ samj-ai ju-en','then that Vishnu god=DAT young.woman=DAT=EXT remember-BVS be-PTCP','然后，（Śiva）想起了那位神 Viṣṇu／那位年轻女子……','G2017','p. 448, text clauses 33–34','E-依译文省略 / DAT-NP角色待核','保留原语序及链式未完结性质。英语译文把神及年轻女子作为所记起的对象；但作者p.439又以33–34行说明借入型DAT-subject。局部分析需与完整语法核对，不从本例直接判定E-DAT，也不排除该谓词的DAT-subject分析。samj- 来自 Nepali samjhanu；BVS=borrowed verb suffix。',status='原句已核；DAT角色分析待核')
a('D05','Dolakha Newar','尴尬：情绪名词＋感受','sibaji lās cār-a','Shiva embarrassment feel-3SG.PST','Śiva 感到尴尬。','G2017','p. 450, text clause 67','E-Ø / 外部St-未表达','lās 是情绪名词。E 无显性关系标记；与 D01 的作格认知谓词对照，尚不能仅据该例决定整个 lās cār- 的词汇句法分析。')
a('N01','Kathmandu Newar','恐惧状态','ji gyat-O','1SG.ABS be.afraid-PFV.SET2','我害怕起来了。','H1991','p. 63, (29)','E-ABS / St-未表达','SET2 是作者屈折范畴，不能直接改标第三人称。')
a('N02','Kathmandu Newar','喜欢','ji-tO musya yOː','1SG-DAT soybean[ABS] be.pleasant.IPFV.SET2','我喜欢（炒）黄豆。','H1991','p. 133, (30)','E-DAT / St-ABS','yOː 依作者不作人为后缀切分。')
a('N03','Kathmandu Newar','理解：非控制却仍作格','jiː wo-ya-gu khO thul-O','1SG.ERG 3-GEN-ATR matter[ABS] understand-PFV.SET2','我明白他的意思。','H1991','p. 138, (56)','E-ERG / 内容-ABS','该页同时给出 *SET1、*E-ABS、*E-DAT，支持固定 ERG + SET2；非意愿性不自动导致非作格。')
a('N04','Kathmandu Newar','愤怒：名词＋感受','ji tO cay-a','1SG.ABS anger feel-PST.SET1','我生气了。','H1991','p. 61, (22)','E-ABS / 外部St-未表达','tO 是情绪名词，不当作外部刺激。正文说此搭配强烈偏好 SET1；不把“生气”预设为必然非控制。')
a('N05','Kathmandu Newar','使害怕：使动对照','jiː wo-yatO khyan-a','1SG.ERG 3-DAT frighten-PST.SET1','我吓到了他／她。','H1991','p. 148, (10)','Causer-ERG / E-DAT','有生 causee 带 DAT。与 N01 的 E-ABS 构成词汇使动对照；此处 E 不是作格的我。')
for item in D:
 if item['source']=='H1991':
  item['status']='结构已核图；特殊元音字形待精校'
  item['note'] += ' 转写暂以 O 保存扫描本的特殊元音字形，O 不是零语素，也不作为标准 IPA 使用；精确字形须对原页，勿据此作音系构拟。'
(root/'research/第三轮/corpus.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
# Audit aligned words and overt morpheme boundaries; author-internal dots ignored.
errors=[]
for d in D:
 fs=d['form'].split();gs=d['gloss'].split()
 if len(fs)!=len(gs): errors.append((d['id'],'word_count',len(fs),len(gs)))
 for f,g in zip(fs,gs):
  if ''.join(re.findall(r'[-=]',f)) != ''.join(re.findall(r'[-=]',g)):
   errors.append((d['id'],'boundary',f,g))
print('Examples:',len(D),'by variety:',dict(collections.Counter(d['language'] for d in D)))
print('Alignment audit:',errors)
# Human-readable text
intro='''# 作通格／施事标记语言的心理谓词：五点位与亲缘材料例句库

整理日期：2026-11-05。第一版，共 **{count} 条**。这是可溯源的研究底稿，尚非穷尽的语言构式清单。

## 使用说明与证据边界

- 主点位为 Basque、Lezgian、Ronghong Qiang、Kakataibo、Dolakha Newar。对照分别为 Basque 方言、Agul（另加较远的 Bezhta）、Puxi Qiang、Shipibo-Konibo、Kathmandu Newar。Basque 没有已证实的外部亲属；不把其方言称为亲属语言。
- 每条均给出原文的语素分析行、依《莱比锡标注规则》规范的 gloss、中文意译、出处、论元框架和限制。分词与语素切分以原作者为基础；未另造例句。原句中未提供分解的融合形式不硬拆。排版标点、长音符号及上标作必要统一。
- `E`=Experiencer；`St`=Stimulus。认知内容、欲望对象、使动者、情绪名词会另说明，不强行混成一个语义角色。E/St 不等于主语／宾语。
- `Ø` 只表示例句中无显性关系标记；羌语中不自动改为 ABS。`未表达／省略` 不等于零格。`X[ABS]` 表示分析中存在而没有独立切分语素的 ABS；融合代词形式用 `1SG.ERG` 等。
- 原句的连接号 `-` 与附着词界 `=` 保留；句法成分范围在说明中注明，避免方括号范围被误当作词。两行逐词对齐；词汇释义中的点号连接一个词对应的多词译义。
- 莱比锡规范是一套**呈现约定**，不会自动证明原作者的格分析或论元分析。本库保留 CSM、SET1/2、INTRSS 等来源特定标签，并在末尾解释。
- **Mouton 合规状态：**五个主点位均有 Mouton 书目锚点，但当前例句全文证据并非全部取自出版社正式版：Basque 为 Mouton 期刊正文；Lezgian 多经二手文献引 MGL；羌语为公开稿；Kakataibo 为博士论文；Dolakha 为作者论文／章节。论文最终若要求所有例句直接引 Mouton 正式版，仍须逐条对版。不要把论文稿页码直接冒充 MGL 版页码。

## 来源索引

|代码|具体读到的来源与链接|出版性质与定位|
|---|---|---|
|B2020|Fernández, Zúñiga & Berro 2020, [Datives with psych nouns and adjectives in Basque](https://doi.org/10.1515/flin-2020-2050)；[全文](research/ergative/basque2020.pdf)|Folia Linguistica 54(3):647–696，De Gruyter；采用印刷页码|
|LSV2004|Lehmann, Shin & Verhoeven 2004, [Person prominence and relation prominence](research/参考全文/lehmann2004.pdf)，第2修订版，ASSidUE 12|二手转引 Haspelmath 1993；原书为 [MGL 9](https://doi.org/10.1515/9783110884210)|
|GMM2008|Ganenkov, Maisak & Merdanova, [Non-canonical Agent Marking in Agul](https://doi.org/10.1007/978-1-4020-6497-5_8)；[全文](research/ergative/agul_springer.pdf)|Differential Subject Marking, 173–198，Springer；PDF版权2008，Crossref记2009|
|CFK2013|Comrie, Forker & Khalilova 2013, [Alignment typology, reflexives, and reciprocals in Tsezic languages](https://doi.org/10.3765/bls.v37i2.810)；[全文](research/ergative/tsezic_pdf.pdf)|BLS 37 Special Session:32–51；非 Mouton|
|LH稿|LaPolla with Huang, [公开语法稿](https://publikationen.ub.uni-frankfurt.de/files/37958/LaPolla_and_Huang_1996_A_Grammar_of_Qiang.pdf)；[本地](research/ergative/qiang_grammar.pdf)|题页版权1996；关联正式书 LaPolla with Huang 2003, [MGL 31](https://doi.org/10.1515/9783110197273)；本库引公开稿印刷页／例号|
|H2004|Huang, Chenglong 2004, [A reference grammar of the Puxi variety of Qiang](https://pure.mpg.de/rest/items/item_406684_4/component/file_406683/content)；[本地](research/ergative/puxi2004.pdf)|香港城市大学博士论文；非 Mouton|
|Z2011|Zariquiey 2011, [A grammar of Kashibo-Kakataibo](https://opal.latrobe.edu.au/articles/thesis/A_grammar_of_Kashibo-Kakataibo/21844767)；[本地](research/ergative/kakataibo_thesis.pdf)|La Trobe博士论文；关联正式书2018 [A Grammar of Kakataibo, MGL 75](https://doi.org/10.1515/9783110765816)；引论文本身页码|
|V2003|Valenzuela, Pilar M. 2003, [Transitivity in Shipibo-Konibo Grammar](http://www.etnolinguistica.org/tese:valenzuela-2003)；[本地](research/ergative/shipibo2003.pdf)|University of Oregon博士论文；扫描本，例句已对图核查|
|G1997|Genetti 1997, [Object Relations and Dative Case in Dolakha Newari](https://carolgenetti.academicwebsite.com/publications/60174.pdf)；[本地](research/ergative/dolakha1997.pdf)|Studies in Language 21(1):37–68；非 Mouton，扫描本；注意不是33–62|
|G2017|Genetti 2017, Dolakha Newar，The Sino-Tibetan Languages 第2版:436–452；[作者全文](https://carolgenetti.academicwebsite.com/publications/59324.pdf)；[本地](research/ergative/dolakha2017.pdf)|Routledge；关联正式语法 Genetti 2007 [MGL 40](https://doi.org/10.1515/9783110198812)|
|H1991|Hargreaves, David J. 1991, [The concept of intentional action in the grammar of Kathmandu Newari](https://hdl.handle.net/1794/3088)；[全文](research/ergative/kathmandu1991.pdf)|University of Oregon博士论文；非 Mouton|

'''.format(count=len(D))
# Expand relative local links into absolute paths for desktop.
intro=re.sub(r'\]\((research/[^)]+)\)',lambda m:'](<'+str(root/m.group(1))+'>)',intro)
parts=[intro]
prev=None
for d in D:
 if d['language']!=prev:
  parts.append('\n## '+d['language']+'\n');prev=d['language']
 fs=d['form'].split();gs=d['gloss'].split();widths=[max(len(f),len(g))+2 for f,g in zip(fs,gs)]
 form=''.join(f.ljust(w) for f,w in zip(fs,widths)).rstrip()
 gloss=''.join(g.ljust(w) for g,w in zip(gs,widths)).rstrip()
 parts.append(f"\n### {d['id']}　{d['topic']}\n\n```text\n{form}\n{gloss}\n```\n\n“{d['translation']}”\n\n出处：{d['source']}，{d['location']}。证据：{d['status']}。\n\n编码：**{d['frame']}**。"+(f" {d['note']}" if d['note'] else '')+'\n')
 if d['source']=='H1991':
  pg={'N01':74,'N02':144,'N03':149,'N04':73,'N05':159}[d['id']]
  parts.append('\n[核对原页字形](<'+str(root/('research/第三轮/previews/kathmandu-'+str(pg)+'.png'))+'>)\n')
parts.append('''
## 缩写与标注规范

通用缩写：`1/2/3` 人称；`SG/PL` 单／复数；`A/S/O` 及物主体／不及物唯一论元／及物对象；`ABS/ERG/DAT/GEN/INS` 通格／作格／与格／属格／工具格；`OBL` 斜格词干／形式；`COM` 共格；`LAT` 向格；`LOC` 方位格；`DET/DEF` 限定词／定指；`CL` 量词／分类词；`COP/AUX` 系词／助动词；`NEG/PROH/Q/PRT` 否定／禁止／疑问／小品词；`IPFV/PFV/PRS/PST/NPST/AOR` 未完成体／完成体／现在／过去／非过去／不定过去；`INF/NMLZ/PTCP` 不定式／名词化／分词；`REFL` 反身；`INDF` 不定；`VOC` 呼格；`DIR` 方向成分。

来源特定缩写（不冒称全部是 Leipzig 标准库存）：

|标签|本库含义／保留理由|
|---|---|
|POEL / SBEL / SREL|Lezgian 的 postelative / subelative / superelative；应分别记录，不合并成同一个“离格”|
|CSM|羌语 change-of-state marker，状态变化标记；与人称融合时用点号|
|TP / NTP|Puxi 代词 topical / non-topical 形式，属于代词范式区分；不凭此直接命名为 NOM / ACC|
|IMPR.LOC|Kakataibo imprecise location，模糊位置格；保留其空间标签|
|NAR|Kakataibo 叙述／陈述范畴；后接人称特征，未硬拆融合形式|
|1/2|Kakataibo 第一或第二人称；斜线表示备选值，不表示“二分之一”或复数|
|S/A>A、S/A>S、A/S>S.SE、DS/A/O.PE|Kakataibo switch-reference 的来源特定标签；`>`后为后续主体类型，SE=simultaneous events，PE=previous event(s)。保留作者复合范畴；不能简化为普通时态|
|EV / INC / CMPL|Shipibo-Konibo 原书 evidential / incompletive / completive；此处保留而未把后两者与其他来源的 IPFV/PFV 完全等同|
|INTRSS|Shipibo-Konibo interessive case，关涉格；不要误读成 intransitive|
|II|Bezhta 名词类别第二类；不是第二人称|
|NR2|Dolakha 第二关系化后缀范畴；不是通用的 NMLZ 后加数字“二”|
|BVS / EXT|Genetti 2017 的 borrowed verb suffix / extensive 标记；保留作者术语。EXT 在本例呈附加／延展功能|
|ATR|Hargreaves 的 attributive 标记|
|SET1 / SET2|Kathmandu Newar 两套屈折形式；须与人称、言语角色、控制性及证据性一起分析，不能径改为有意／无意两种语素|

规范依据：[Leipzig Glossing Rules](https://www.eva.mpg.de/lingua/resources/glossing-rules.php)。统一了 IMPF→IPFV、PERF→PFV（Hargreaves 明确释为 perfective）、NOM（nominalizer）→NMLZ、NEG.IMP→PROH 及大写。形态切分和句法分析的调整均在各例说明中交代。

## 当前覆盖与未决问题

1. 此库是构式取样，不是各语言频率统计。一个框架有多个例子不代表更常用；文献没有例句的格子留未知。
2. Basque 覆盖最细；Lezgian 的普通爱／恐惧、身体部位构式已核二手转引，尚须正式版复核。反身格反转另见 Forker 2014:63(17)，未将其混入一般陈述句的格交替。
3. Agul 提供近亲的感知资料；Bezhta 明确另列为远亲。不能把 Agul 的 see 与 Lezgian 的 love 当作完全匹配词义的祖语构拟证据。
4. Ronghong 与 Puxi 支持多个无显性格标记的心理／感知构式及 E 人称索引。Puxi 作者明确将相关标记称 AGT，避免严格 ergative 分析；两者的共有 Ø 模式需要与普通动作谓词基线比较。
5. Kakataibo 与 Shipibo-Konibo 共同支持扩展不及物构式，但 K 的 fear-St 是 =mi，S 的 fear-St 是 -ki；两者的 love/want 系列也不应统一编码为一个义项。
6. Dolakha 目前仍缺可直接核实的完整 FEAR / LIKE 双论元句；Kathmandu 的资料只能作亲缘对照，不能填进 Dolakha 的空格。Dolakha G2017:439 的 DAT-subject 概述须另与完整例句对应，D04 按译文没有显性 E，且须核对正文 DAT-subject 概述与该例的分析。
7. 不在这一轮提出星号祖语句或原始格范式；共享模式、候选同源词根与历史构拟是三个证据强度不同的问题。
''')
(root/'90_历史方案/01_作通格阶段/心理谓词_五点位及亲缘语言_莱比锡例句库.md').write_text(''.join(parts))
with (root/'04_数据/历史数据/心理谓词_构式对照矩阵.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(D[0]));w.writeheader();w.writerows(D)
