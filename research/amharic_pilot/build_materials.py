"""Amharic first round. Curated source excerpts; does not rewrite earlier languages."""
from pathlib import Path
import json
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = ROOT/'02_语言材料/阿姆哈拉语/阿姆哈拉语心理谓词_实体事件构式_例句与标注.md'
NOTE = ROOT/'03_文献笔记/NSM/阿姆哈拉语心理谓词_NSM与Mouton正文核读.md'

def dump(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

sources = [
 dict(id='FSI1964',citation='Obolensky, Serge, Debebow Zelelie & Mulugeta Andualem. 1964. Amharic Basic Course, Volume 1, Units 1–50. Washington, DC: Foreign Service Institute.',
      url='https://archive.org/download/Fsi-AmharicBasicCourse-StudentText/Fsi-AmharicBasicCourse-Volume1-StudentText.pdf',local='fsiv1.pdf',mouton=False,
      status='full_file_selected_pages_read',printed_to_pdf='Arabic printed page + 19 = PDF page',
      used_pages=[43,45,188,189,243,252,335,337,340,341,380,382,403,437,467,468],
      role='教学编写对话、结构练习和语法说明；不是全部自然发生语料',retrieval_record='fsiv1_source.json'),
 dict(id='BakerKramer2014',citation='Baker, Mark & Ruth Kramer. 2014. Rethinking Amharic prepositions as case markers inserted at PF. Lingua 145:141–172.',
      doi='10.1016/j.lingua.2014.03.005',url='https://sites.rutgers.edu/mark-baker/wp-content/uploads/sites/199/2019/07/amharic-preps-as-case-offprint.pdf',local='bakerkramer2014.pdf',mouton=False,
      status='full_file_selected_pages_read',used_pages=[141,142,152],role='事件名物化ACC例43、前缀的分析；其例43转引Leslau1995:395，本轮未直接核该版',retrieval_record='bakerkramer2014_source.json'),
 dict(id='Kacprzak2026',citation='Kacprzak, Aleksander. 2026. Conceptualising love in Amharic: Lexis, metaphors, and cultural contexts. Studies in African Languages and Cultures 60:9–35.',
      doi='10.32690/SALC60.1',url='https://salc.uw.edu.pl/index.php/SALC/article/download/734/407',local='love2026.pdf',mouton=False,
      status='full_file_selected_pages_read',used_pages=[13,14,15,16,19,23,24],role='爱／喜欢词族的语义与文学引例；并非正式NSM explication',retrieval_record='love2026_source.json'),
 dict(id='Kozicki2018',citation='Kozicki, Michał. 2018. Planning of the Amharic language against a background of planning processes in ethnic and of artificial languages. Doctoral dissertation, Adam Mickiewicz University, Poznań.',
      url='https://repozytorium.amu.edu.pl/bitstreams/2e984fa8-0af8-4e31-bf5f-6f07bd504feb/download',local='amharic_planning.pdf',mouton=False,
      status='full_file_selected_pages_read',used_pages=[200,211,213],role='语法综述中的例句；章节以Leslau1995为依据，本轮引用实际读到的论文页',retrieval_record='amharic_planning_source.json'),
 dict(id='Amberber2001',citation='Amberber, Mengistu. 2001. Testing emotional universals in Amharic. In Jean Harkins & Anna Wierzbicka (eds.), Emotions in Crosslinguistic Perspective, 35–68. Berlin/New York: Mouton de Gruyter.',
      doi='10.1515/9783110880168.35',url='https://api.pageplace.de/preview/DT0400.9783110880168_A19976887/preview-9783110880168_A19976887.pdf',local='emotion2001_preview.pdf',mouton=True,
      status='partial_body_read',available_chapter_pages=[35,36,37],used_pages=[35,36,37],missing_chapter_pages='38–68',
      role='实际使用NSM方法说明、语法概述及FEEL＋happiness例4a；没有外部刺激Y，不能补足八节点',retrieval_record='emotion2001_preview_source.json'),
 dict(id='Amberber2008',citation='Amberber, Mengistu. 2008. Semantic primes in Amharic. In Cliff Goddard (ed.), Cross-Linguistic Semantics, 83–119. John Benjamins.',
      doi='10.1075/slcs.102.09amb',url='https://benjamins.com/catalog/slcs.102.09amb',local=None,mouton=False,status='bibliography_only',role='待取得正文，未据标题填目标词'),
 dict(id='MeneteEtAl2026',citation='Menete, Sérgio N., Guiying Jiang & Betelhem Tirusew Bayu. 2026. The heart and positive emotions: a view from Amharic. Journal of African Languages and Linguistics 47(1):135–169.',
      doi='10.1515/jall-2024-0026',url='https://doi.org/10.1515/jall-2024-0026',local=None,mouton=True,status='metadata_abstract_only',
      role='Crossref/OpenAlex核到书目及OA许可，出版端返回202空响应；正文未读，不作为构式或完整释义证据'),
 dict(id='Leslau1969',citation='Leslau, Wolf. 1969. An Amharic Reference Grammar. ERIC ED036793.',
      url='https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Afro-Asiatic/Semitic/Amharic%20Reference%20Grammar%20%28Leslau%29.pdf',local='leslau1969.pdf',mouton=False,status='full_scan_title_verified',
      role='题名页核为1969；不能冒充被Baker/Kozicki引用的1995正式语法；本轮未从此件提取独立例句'),
]

rows=[]
def add(n, lexeme, labels, content, source, page, pdfpage, section, text, seg, gloss, zh, en, y, flag, note,
        *,eligible=True,reason=None,e=None,index=None,syntax=None,translation='source',excerpt=True):
    assert len(seg.split())==len(gloss.split()),(n,seg,gloss)
    prefix={'FSI1964':'fsi','BakerKramer2014':'bk','Kacprzak2026':'love','Kozicki2018':'kozicki','Amberber2001':'amberber'}[source]
    img=f'verified_pages/{prefix}_{pdfpage}.png'
    assert (OUT/img).exists(),img
    rows.append(dict(id=f'A{n:02}',language='Amharic',lexeme=lexeme,provisional_labels=labels,content_type=content,
      source_id=source,printed_page=page,pdf_page=pdfpage,source_locator=section,source_text=text,
      text_policy='保留来源转写体系；FSI省去重音、下划线与语调箭头，换行合并；不回译生成埃塞字母',
      is_excerpt=excerpt,segmented=seg,gloss=gloss,gloss_status='project_analysis_except_explicitly_noted',
      translation_zh=zh,translation_en=en,english_translation_status=translation,Y_span=y,Y_np_flagging=flag,
      E_np=e or dict(realization='omitted',surface_flagging=None,syntactic_role='experiencer subject' if lexeme in ['fällägä','wäddädä'] else 'not established from overt E NP'),
      verbal_indexing=index,Y_syntactic_status=syntax or 'object',internal_arguments_separate=True,
      comparison_eligible=eligible,exclusion_reason=reason,notes=note,verification_image=img,
      visually_verified=True,final_semantic_node=None,native_speaker_verified=False))

add(1,'fällägä',['WANT'],'EVENT','FSI1964',43,62,'Unit 5, Basic Sentences, final utterance',
 'kiflun mayət ifəlligalləhu.','kifl-u-n ma-yət ifəlligalləhu','room-DEF-ACC NMLZ-see want.IPFV.1SG',
 '我想看看这个房间。',"I’d like to see the room.",'kiflun mayət','ZERO',
 '整个事件名物化无外层格标记；kifl-u-n的ACC只标“看”的内部宾语。英语would like在酒店询房语境表示当下意愿，不能仅因like译词另立偏好义。',index='体验者1SG主语范式；无显性E NP')
add(2,'fällägä',['WANT'],'ENTITY','FSI1964',45,64,'Unit 5, Structure Sentences, Perfective',
 'gənzəb fəlləgš.','gənzəb fəlləg-š','money want.PFV-2FSG',
 '你（女）想要钱。','You (f) wanted money.','gənzəb','ZERO',
 '本页单列money和wanted，目标句明确译wanted money；钱按普通实体，不改写为获得钱事件。',index='E=2FSG主语')
add(3,'fällägä',['WANT'],'EVENT','FSI1964',45,64,'Unit 5, Structure Sentences, Perfective',
 'səwiyyew abbatun məTrat fəlləgə.','səwiyye-w abbat-u-n mə-Trat fəlləgə','man-DEF father-POSS.3MSG-ACC NMLZ-call want.PFV.3MSG',
 '那个人想叫他的父亲。','The man wanted to call his father.','abbatun məTrat','ZERO',
 'E的-w为定指后缀，不是NOM；Y为“叫父亲”的事件名物化。父亲上的-n为内部宾格。',
 e=dict(realization='overt_NP',span='səwiyyew',surface_flagging='ZERO',syntactic_role='subject'),index='E=3MSG主语')
add(4,'fällägä',['WANT'],'ENTITY','FSI1964',188,207,'Unit 15, Basic Sentences, John food order',
 'lərase yədoro wəT, kənəCC injəra gar ifəlligalləhu.',
 'lə-ras-e yə-doro wəT kə-nəCC injəra gar ifəlligalləhu','for-self-POSS.1SG GEN-chicken stew with-white bread with want.IPFV.1SG',
 '我自己想要辣鸡肉炖菜，配白色面饼。',"For myself I’d like spiced chicken stew with some white bread.",
 'yədoro wəT','ZERO','在点餐语境为想要某种食物。配菜的kə…gar属于伴随短语，不能给整个Y编码COM；食物不重释为吃的事件。',index='E=1SG主语')
add(5,'wäddädä',['LIKE'],'ENTITY','FSI1964',189,208,'Unit 15, Basic Sentences, fish utterance',
 'asa siləmmitwəd, asa wəTun amTallat.','asa siləmmitwəd','fish because.like.IPFV.3FSG',
 '因为她喜欢鱼，给她端些炖鱼来。','Since she likes fish, bring her some stewed fish.','asa','ZERO',
 '分词注释只覆盖目标载句前半“因为她喜欢鱼”；后半的使役／带来动词不属于目标心理谓词。记录鱼的偏好，不推定同一形式必用于当下欲望。',index='E=3FSG主语')
add(6,'wäddädä',['LIKE'],'ENTITY','FSI1964',243,262,'Unit 19, comparative examples, first Lemma sentence',
 'kəkəbbədə ləmman iwəddalləhu.','kə-kəbbədə ləmma-n iwəddalləhu','than-Kebbede Lemma-ACC like.IPFV.1SG',
 '比起Kebbede，我更喜欢Lemma。','I like Lemma better than Kebbede.','ləmman','ACC',
 'Lemma是目标Y，-n为外层ACC；kə-Kebbede标比较基准，不是Y的格。页面上更强程度的重复句不另增记录。',index='E=1SG主语')
add(7,'fällägä',['WANT','LIKE?'],'ENTITY','FSI1964',243,262,'Unit 19, comparative examples, first coffee sentence',
 'kəwətət bunna ifəlligalləhu.','kə-wətət bunna ifəlligalləhu','than-milk coffee want.IPFV.1SG',
 '比起牛奶，我更想要咖啡。',"I’d rather have coffee than milk.",'bunna','ZERO',
 '当前选择／相对意愿与一般偏好可能重叠。来源同组后续句使用like coffee better的译法；不据英译强行判为排他LIKE义。咖啡仍为实体。',index='E=1SG主语')
add(8,'wäddädä',['LIKE','WANT?'],'EVENT','FSI1964',380,399,'Note 35.2, last example',
 'inkwan gənzəb agñito, bayagəññim indəhabtam mənor yiwəddal.',
 'ində-habtam mə-nor yiwəddal','like-rich.person NMLZ-live like.IPFV.3MSG',
 '不论有没有钱，他都喜欢像富人那样生活。',"He likes to live like a rich man, whether he’s got money or not.",
 'indəhabtam mənor','ZERO','注释覆盖心理谓词及其名物化Y；前半让步载句不改变Y的名词性。是生活方式偏好，但欲望读法的可用范围仍需语境测试。',index='E=3MSG主语')
add(9,'wäddädä',['LOVE','LIKE?'],'ENTITY','FSI1964',382,401,'Unit 35, Questions and Answers, enemy question',
 'Təlatihn tiwəddalləh?','Təlat-ih-n tiwəddalləh','enemy-POSS.2MSG-ACC love.IPFV.2MSG',
 '你爱自己的敌人吗？',None,'Təlatihn','ACC',
 '原页为未附逐句英译的问答练习；中文为项目译。LOVE为语境候选，LIKE的边界未由该问题单独排除。原转写ihn对应后缀序列，不补写未印出的元音。',translation='project_Chinese_only',index='E=2MSG主语')
add(10,'wäddädä',['LIKE'],'EVENT','FSI1964',403,422,'Unit 38, Questions and Answers, second question',
 'yəamerika hizb frafre məblat yiwəddal?','yə-amerika hizb frafre mə-blat yiwəddal',
 'GEN-America people fruit NMLZ-eat like.IPFV.3MSG',
 '美国人喜欢吃水果吗？',None,'frafre məblat','ZERO',
 '原页未给逐句英译；中文为项目译。E为yəamerika hizb，yə-是其内部属格修饰语，不是E外层格。frafre为名物化内部对象。',translation='project_Chinese_only',
 e=dict(realization='overt_NP',span='yəamerika hizb',surface_flagging='ZERO',syntactic_role='subject'),index='E为集合名词，动词3MSG')
add(11,'wäddädä',['LIKE'],'ENTITY','FSI1964',468,487,'Unit 46, Basic Sentences, Yohannis area utterance',
 'issun səfər bəTam iwəddəwalləhu.','issu-n səfər bəTam iwəddəwalləhu','that-ACC area very like.IPFV.1SG.3MSG.O',
 '我很喜欢那个地段。','I like that area very much.','issun səfər','ACC',
 'ACC附在指示成分issu上，不能只看səfər无后缀而编码整个NP为无标记；动词上的对象索引另外记录。',index='E=1SG主语；Y另有3MSG对象索引')
add(12,'wäddädä',['LIKE'],'ENTITY','FSI1964',468,487,'Unit 46, Basic Sentences, Yohannis rental question',
 'betun wəddijjewalləhunna, siləkirayu yingəruñ.','bet-u-n wəddijjewalləhu-nna',
 'house-DEF-ACC like.PRF.1SG.3MSG.O-and',
 '既然我喜欢这个房子，跟我说说租金吧。',"(Since) I like the place. How about (‘tell me’) the rental?",'betun','ACC',
 '注释只覆盖目标前半。来源英语把房子译place，阿姆哈拉语为bet“房子”。复合完成形式保留整体gloss，不强拆其融合音段。',index='E=1SG主语；Y=3MSG对象索引')
add(13,'wäddädä',['WANT'],'EVENT','BakerKramer2014',152,13,'example (43), citing Leslau 1995:395',
 'agär-ɨh mä-k’rät-u-n bɨ-ttɨ-wädd…','agär-ɨh mä-k’rät-u-n bɨ-ttɨ-wädd',
 'country-your NMLZ-stay-DEF-ACC if-2S-want',
 '如果你想留在自己的国家……',"If you want to stay in your country…",'agär-ɨh mä-k’rät-u-n','ACC',
 '保留来源分词和gloss（仅把NOML统一为NMLZ）。-u按此出处写DEF，不擅改为POSS；-n显式标在名物化上。心理谓词处于if载句不等于Y是条件分句。尚不能由此与LIKE事件无标记例推断同义自由交替。',index='来源2S为体验者主语',excerpt=True)
add(14,'wäddädä',['LIKE'],'EVENT','Kacprzak2026','23–24',15,'example (10), target sentence; Bealu 1983:356',
 'setoččən makbärənna mänkäbakkäb yäwäddalu.',
 'set-očč-ən ma-kbär-ənna mänkäbakkäb yäwäddalu',
 'woman-PL-ACC NMLZ-respect-and take.care.of.NMLZ like.IPFV.3PL',
 '他们喜欢尊重并善待女性。','They like to respect and treat women well.',
 'setoččən makbärənna mänkäbakkäb','ZERO',
 '来自文学引文，按实际读到的Kacprzak例10引用，未冒充直接核读Bealu原书。女性上的ACC在名物化内部；外层两个并列名物化没有-n。来源转写用ä，不能和FSI的ə机械混同。',index='E=3PL；上下文先行名词为来自中部的男性')
add(15,'däss alä',['HAPPY'],'EVENT','FSI1964',335,354,'Note 30.1, first example',
 'antən bəmayəte dess aləñ.','antə-n bə-ma-yət-e dess alə-ñ',
 'you-ACC BA-NMLZ-see-POSS.1SG pleasant say.PFV.3MSG-1SG.O',
 '见到你我很高兴。',"I’m pleased to see you (‘because of my seeing you’).",'antən bəmayəte','BA',
 '外层Y是bə-事件名物化；antən是“看见”的内部ACC。-e是名物化属主1SG，不是矩阵E NP的格。bə短语有原因／情绪根据功能，是否为选定论元尚待句法分析。SAY译法为构词性gloss，不分析为CAUS。',
 index='矩阵动词-ñ索引体验者1SG',syntax='causal oblique; selected argument vs adjunct unresolved')
add(16,'däss alä',['HAPPY'],'EVENT','FSI1964',340,359,'Unit 30, Questions and Answers, New York question',
 'wədə niwyork bəməhedih dess aləh?','wədə niwyork bə-mə-hed-ih dess alə-h',
 'to New.York BA-NMLZ-go-POSS.2MSG pleasant say.PFV.3MSG-2MSG.O',
 '你为去纽约感到高兴吗？',None,'wədə niwyork bəməhedih','BA',
 '来源为未附逐句英译的问答练习；中文为项目译。wədə是“去”的方向成分，外层情绪相关标记为bə-。名物化内属主-ih与矩阵体验者索引-h分别记录。',translation='project_Chinese_only',
 index='矩阵-h索引体验者2MSG',syntax='causal oblique; argumenthood unresolved')
add(17,'däss alä',['HAPPY'],'EVENT','FSI1964',341,360,'Unit 30, Questions and Answers, new house question',
 'addis bet bəməsratu dess aləw?','addis bet bə-mə-srat-u dess alə-w',
 'new house BA-NMLZ-build-POSS.3MSG pleasant say.PFV.3MSG-3MSG.O',
 '他为建了新房子感到高兴吗？',None,'addis bet bəməsratu','BA',
 '中文为项目译。房子是“建造”内部的对象；整个Y内容是建房事件。-u按该语境为名物化主语的属主3MSG；不把它当外层E的格。',translation='project_Chinese_only',
 index='矩阵-w索引体验者3MSG',syntax='causal oblique; argumenthood unresolved')
add(18,'däss alä',['HAPPY'],'EVENT','FSI1964',437,456,'Unit 42, Questions and Answers, reply to cinema invitation',
 'awo, kanta gar məhedinna sinima mayət bəTam dess yiləññal.',
 'awo kə-anta gar mə-hed-inna sinima ma-yət bəTam dess yiləññal',
 'yes with-you with NMLZ-go-and movie NMLZ-see very pleasant say.IPFV.3MSG.1SG.O',
 '好啊，和你一起去看电影会让我很高兴。',None,'kanta gar məhedinna sinima mayət','ZERO',
 '中文为项目译。两个并列事件名物化未带外层bə-；kə-anta gar“和你一起”属于去的内部伴随成分。此例的时间／模态与A15–17不完全相同，不能直接称为自由交替。来源yiləññal有融合，gloss整词。',translation='project_Chinese_only',
 index='矩阵动词索引体验者1SG',syntax='unmarked nominal stimulus; exact subject/argument analysis unresolved')
add(19,'däss alä',['HAPPY'],'EVENT','Kozicki2018',211,211,'§8.4.1, causal verbal-noun example',
 'ənnatun bä-mayät-u bäṭam däss aläw.','ənnat-u-n bä-ma-yät-u bäṭam däss alä-w',
 'mother-POSS.3MSG-ACC BA-NMLZ-see-POSS.3MSG very pleasant say.PFV.3MSG-3MSG.O',
 '他因为见到了母亲而非常高兴。','he was very pleased because he saw his mother',
 'ənnatun bä-mayät-u','BA',
 '该页作者明确把-u解释为suffix pronoun，并说明bä+verbal noun。母亲上的-n是内部ACC。引用实际读到的Kozicki，不把其Leslau1995参考依据当作本轮直接核读。',
 index='矩阵-w索引体验者3MSG',syntax='explicitly described causal adjunct/oblique')

# Background and excluded records remain separate from nominal-frame comparison.
add(20,'afäqqärä',['LOVE'],'ENTITY','Kacprzak2026',15,7,'§3, I love you forms',
 'afäqrəšallähu / afäqrəhallähu','afäqrəšallähu / afäqrəhallähu',
 'love.IPFV.1SG.2FSG.O / love.IPFV.1SG.2MSG.O',
 '我爱你（对女／男说）。','I love you',None,None,
 '两个人称变体合为一条，不虚增词项数。只有动词上的对象人称形式，没有独立Y NP，因此无法观察NP的ACC／无标记。作者论述强调强烈亲密的爱情表达；不是完整NSM释义。',
 eligible=False,reason='只有代词性动词索引，缺独立Y NP',index='E=1SG；Y=2FSG/2MSG对象形式')
add(21,'wäddädä',['LOVE'],'ENTITY','Kacprzak2026',19,11,'example (4), Yisimake 2023:128',
 'qiṭe əskiqqaṭṭäl wäddädkut.','qiṭ-e əskiqqaṭṭäl wäddäd-ku-t',
 'butt-POSS.1SG until.burn love.PFV-1SG-3MSG.O',
 '我爱他爱到屁股都烧起来了。','I loved him until my ass burned.',None,None,
 '文学中的夸张隐喻；没有独立Y NP，-t对象索引不等于名词ACC。沿用来源引文，不用此例证明一般实体NP格框架。',eligible=False,reason='只有代词性Y索引',index='E=1SG；Y=3MSG.O')
add(22,'afqari',['LOVE','LIKE'],'UNRESOLVED','Kacprzak2026',16,8,'§3, derived nominal expressions',
 'säwən afqari; həzbun afqari; yäsport / yämuziqa afqari',
 'säw-ən afqari','person-ACC one.who.loves',
 '爱人／爱民者；体育迷／音乐迷。','one who loves people; sport / music fan',None,None,
 '这是一个派生名词的用法清单记录，分词仅展示第一式。säwən和həzbun含ACC，体育／音乐表达含yä-，但不是同一完整矩阵构式。体育／音乐迷不自动算LOVE_EVENT。非使役afqari应与该页后文同形或近形的使役派生词区别。',eligible=False,reason='派生名词短语，缺完整E/Y谓词构式',index=None)
add(23,'(tä-)sämmä',['HAPPY'],'FEELING_CONTENT','Amberber2001',37,43,'§3.1, example (4a)',
 'dəssita yi-ssəmma-ññ-al','dəssita yi-ssəmma-ññ-al',
 'happiness 3M.IMP-feel-1-IMP',
 '我感到高兴。','I feel happy.',None,None,
 'gloss保留作者原缩写与切分（作者1表示第一人称）。happiness是所感受的状态内容，不是外部刺激实体／事件。用此例支持FEEL与体验者索引讨论，不补HAPPY_ENTITY或HAPPY_EVENT。动词形态／历史与当前FEEL词汇化分开，不据此建立被动目标框架。',eligible=False,reason='感受内容，不含研究所需外部刺激Y',index='作者把-ññ标第一人称')
add(24,'däss alä',['HAPPY'],'NO_OVERT_Y','FSI1964',337,356,'Note 30.1, Present paradigm, first form',
 'dess aləñ.','dess alə-ñ','pleasant say.PFV.3MSG-1SG.O',
 '我很高兴。',"I’m pleased/happy (‘it pleases me’).",None,None,
 '原页明确把dess malət列为impersonal verb。时态标签“Present”为来源的范式功能标签，SAY基体形态按PFV作构词gloss，二者不混同。无Y，不能决定外部刺激的格。',eligible=False,reason='没有显性Y',index='矩阵-ñ索引体验者1SG')
add(25,'fällägä',['WANT'],'EVENT','Kozicki2018',200,200,'§8.3 discussion, lə + simple imperfect example',
 'sərawən tolo lič’ärräs yəfälləgal.','səra-w-ən tolo li-č’ärräs yəfälləgal',
 'work-POSS.3MSG-ACC quickly PURP-finish.JUSS.3MSG want.IPFV.3MSG',
 '他想很快完成自己的工作。','He wants to finish his work quickly',
 'sərawən tolo lič’ärräs',None,
 '来源转写保留；内部work的-n不能投射到外层。lə＋有限／祈愿形式不同于本轮纳入的mə-名物化。',eligible=False,reason='外层Y为非名物化分句，退出当前比较',index='E=3MSG主语',syntax='non-nominal lə/jussive complement')
add(26,'wäddädä',['WANT','LIKE?'],'EVENT','Kozicki2018',213,213,'§8.4.2, conditional used with liking',
 'bə-säraw əwäddalläwh nägär gən gize yälläññəmm.',
 'bə-sära-w əwäddalläwh nägär gən gize yälläññəmm',
 'COND-work.IPFV-1SG like.IPFV.1SG thing but time not.exist.1SG',
 '我想工作，可是没有时间。','I would like to work, however I have no time.',
 'bə-säraw',None,
 '作者明确说此处结构上没有infinitive，bə＋imperfect提供条件式解读。即便英语译to work，也不能编码为bə-名物化。与A13区别在Y自身的形式，不在整个句子是否条件载句。',eligible=False,reason='条件分句Y，非NP名物化',index='E=1SG主语',syntax='conditional non-nominal complement')
add(27,'asfällägä',['NEED'],'EVENT','FSI1964',252,271,'Note 20.2, hospital example',
 'bəmətamməmə mikniyatə wədə hospital məhed yasfəlligəññal.',
 'wədə hospital mə-hed yasfəlligəññal','to hospital NMLZ-go need.IPFV.3MSG.1SG.O',
 '因为我病了，我得去医院。',"Since I am ill, I’ll have to go to the hospital.",
 'wədə hospital məhed','ZERO',
 '分词覆盖“去医院是我所需”。来源同页区分asfällägä的cause to want和无人称necessary/need义；NEED不能自动并入WANT。当前排除CAUS，另须分析词汇化need与使役形态的关系。',eligible=False,reason='NEED义不在四标签内；使役来源形式亦待界定',index='E=1SG对象形式',syntax='impersonal need construction')

current=[r for r in rows if r['comparison_eligible']]
background=[r for r in rows if not r['comparison_eligible']]
groups=defaultdict(list)
for r in current:groups[(r['lexeme'],r['content_type'],r['Y_np_flagging'])].append(r['id'])
frame_groups=[dict(id=f'AF{i:02}',lexeme=k[0],content_type=k[1],Y_np_flagging=k[2],example_ids=v,
    scope='observed Y surface form only; not proof of identical sense or complete E/Y construction',
    E_np_evidence=[r['id'] for r in current if r['id'] in v and r['E_np']['realization']=='overt_NP']) for i,(k,v) in enumerate(groups.items(),1)]
dump('sources.json',sources);dump('examples.json',rows);dump('current_comparison_examples.json',current)
dump('background_and_excluded_examples.json',background);dump('frame_groups.json',frame_groups)
dump('coverage.json',dict(total_records=len(rows),current_formal_scope=len(current),background_or_excluded=len(background),
  current_content_counts=dict(Counter(r['content_type'] for r in current)),
  current_lexeme_counts=dict(Counter(r['lexeme'] for r in current)),
  final_nodes_assigned=0,semantic_categories_nonexclusive=True,
  gaps=['HAPPY_ENTITY的外部普通实体刺激NP','afäqqärä的完整实体/事件NP句','LOVE_EVENT的独立高强度用法','显性体验者NP在däss alä中的标记','同词同义的名物化ACC/无标记交替条件','Amberber2001 pp38–68及其他Mouton目标分析正文'] ))

intro='''# 阿姆哈拉语心理谓词：实体／事件构式第一轮

更新：2026-11-15。依[当前方案](../../01_研究方案/当前方案.md)继续采集。共 **27条证据记录（A01–A27），19条进入当前名词形式比较，8条为背景或范围外材料**。19条中8条ENTITY、11条EVENT；不是27个词项，也不是八节点全部补齐。教学例句、文学引文、论文分析例分别保留来源性质。

这一轮能观察到：fällägä“想要／寻找”接无标记实体与事件名物化；wäddädä覆盖喜欢、爱及想要等用法，实体有无标记和ACC，事件名物化有无标记和ACC；däss alä“高兴”相关事件表达有bə-/bä-及无标记形式。**这些是已见形式的归纳，不代表同义自由交替或完整E/Y框架已经一致。** 多数例句省去体验者NP，只能观察动词人称形式；本轮只有A03、A10同时有显性矩阵体验者NP。

## 阅读与编码约定

- 原文沿用各来源的罗马转写，FSI去掉重音、下划线和问句语调箭头，保留i、ə及T／C／K等原书记号；不把OCR结果直接充作转写，也不自行回译埃塞字母。不同作者的ä／ə等记号不能机械逐字对应。词项标题用通行学术写法，不据拼写差异另立词。
- 下列分词和Leipzig式gloss主要为**项目分析**，不是作者原有逐词注释。非线性、融合的人称时体形式可用一个词对应点号连接的gloss，不猜拆全部音段。A13、A23保留来源已有分析并说明缩写差异。英文仅在来源确有译文时列出；未附英译的练习题只给项目中文译。
- ENTITY是普通实体；EVENT是内容，NP／名物化是形式。内层宾语的-n、内层属格yə-和方向／伴随短语都不充作外层Y标记。ACC附在NP内指示语上也算该NP的显性标记（A11）。
- `ZERO`表示本例显性Y未见外层格／介词；不等于不存在其他形式。E NP没有出现时，E的NP flagging记未观察，不从动词对象后缀推出ACC或DAT。
- `BA`保留bə-/bä-的表面形式及原因／情绪根据功能，不武断统一为DAT。特别是däss alä的BA事件短语，论元还是附加语尚未解决；无标记事件的句法地位也待进一步核查。
- LIKE／LOVE／WANT／HAPPY只是暂时组织标签，可以重叠。问号是待检验；所有记录的最终语义节点为空，尚无母语者验证。

缩写：ACC宾格；BA表面bə-/bä-前缀；COND条件；DEF定指；GEN属格；IPFV未完成；JUSS祈愿；NMLZ名物化；O对象索引；PFV完成；PL复数；POSS属主；PRF复合完成；PURP目的；SG单数。3MSG等为人称／性／数。SAY的构词gloss不表示本轮把däss alä当作使役句；as-/a-使役材料另行排除。

## 词项与证据概况

|词项|本轮可比较的形式|意义与限制|
|---|---|---|
|fällägä|ENTITY无标记；EVENT名物化无标记|点餐、想看房、想叫父亲等WANT语境；咖啡比较例可能兼有偏好，保留重叠|
|wäddädä|ENTITY无标记／ACC；EVENT名物化无标记／ACC|LIKE、LOVE、WANT有实际用例；不能把不同语境的表面形式差异直接叫作自由交替|
|afäqqärä|暂只有对象人称形式|通常与强烈爱情、承诺相关；偶尔也用于祖国、自由或子女，不是与wäddädä互斥的“仅爱情词”|
|afqari|派生名词短语|“爱人者／体育迷／音乐迷”；独立记录，不移植动词义项或配价|
|däss alä|EVENT名物化BA／无标记|体验者见于动词对象形式；尚无足够显性E NP证据；HAPPY_ENTITY未知|
|(tä-)sämmä＋dəssita|FEEL＋happiness|有Mouton原页例证，但happiness是感受内容，不能算外部实体刺激|

Kacprzak（2026:14–16、24及脚注17）明确支持wäddädä与afäqqärä覆盖重叠：前者范围更广，后者有典型倾向而非绝对排他限制。该研究为词汇、隐喻与文化语境分析，不能改称完整NSM释义。

## 当前形式分组

|词项|Y内容|外层Y表面标记|例号|
|---|---|---|---|
'''
for g in frame_groups:
    intro+=f"|{g['lexeme']}|{g['content_type']}|{g['Y_np_flagging']}|{'、'.join(g['example_ids'])}|\n"
intro+='''
上述分组仅按Y的可见形式排列。A03和A10的E为无外层格标记的主语NP，其余当前例句无显性E NP；不能把“省略E＋主语索引”与“省略E＋对象索引”一并写成同一完整E/Y框架。

## 当前比较例句

'''

srcmap={s['id']:s for s in sources}
def card(r):
    s=srcmap[r['source_id']]
    doc=f"../../research/amharic_pilot/{s['local']}"
    pic=f"../../research/amharic_pilot/{r['verification_image']}"
    lines=[f"### {r['id']}　{r['lexeme']} · {'／'.join(r['provisional_labels'])} · {r['content_type']}", '',
      f"> {r['source_text']}", '',f"```text\n{r['segmented']}\n{r['gloss']}\n```",'',f"中文（项目译）：{r['translation_zh']}"]
    if r['translation_en']:lines.append(f"原出处英译：{r['translation_en']}")
    if r['comparison_eligible']:
      ep=r['E_np']; et=(ep.get('span','')+'；外层'+str(ep['surface_flagging'])) if ep['realization']=='overt_NP' else '本例未出现独立E NP，NP格未观察'
      lines += ['',f"- Y：`{r['Y_span']}`；外层 **{r['Y_np_flagging']}**；句法：{r['Y_syntactic_status']}。",
       f"- E：{et}。动词形式：{r['verbal_indexing']}。"]
    else:lines+=['',f"**暂不进入当前比较：{r['exclusion_reason']}。**"]
    lines += ['',r['notes'],'',f"出处：[{r['source_id']}]({doc})，书内／印刷页 {r['printed_page']}；PDF第{r['pdf_page']}页；{r['source_locator']}。[核页图片]({pic})。",'']
    return '\n'.join(lines)+'\n'

body=intro+''.join(card(r) for r in current)+'## 背景与范围外记录\n\n'+''.join(card(r) for r in background)
body+='''## 尚未补齐的部分

|问题|本轮状态|下一步需要的证据|
|---|---|---|
|HAPPY_ENTITY|未知；未用感受内容或条件分句代填|普通实体刺激NP的原句及完整上下文，特别是显性E NP|
|afäqqärä的实体／事件NP|只有人称形式与语义讨论|完整独立NP句；非浪漫对象及事件用法的实际实例|
|LOVE_EVENT|未单独确立|高强度活动热爱等情境的词项选择；不能把LIKE事件或“音乐迷”直接升级|
|名物化ACC／无标记条件|已见两种形式，机制未知|同词、同义、可比定指性／语境的最小对照|
|däss alä的BA／无标记|均已见；句法与时体不同|论元／附加语分析，外部E NP的标记与动词索引配合|
|NSM正式释义|只读到Amberber2001章前三页，未取得完整目标词释义|pp38–68与2008专章；用共同scenario逐词测试，允许重叠|
|Mouton要求|实际使用2001章pp35–37的方法、概述和FEEL例；目标外部Y构式仍待补|完整相关分析正文；2026心脏情绪论文正文尚未取得|

尚不据这些缺口编码“不存在”，也不输出定稿八节点地图。语义测试可沿用既有共同情境：平常喜欢而现在不想、平常不喜欢而现在想、对人的关怀与接近欲望、具体事件后的好感受等；这是后续测试设计，不是新造的阿姆哈拉语自然用例。

## 来源与数据入口

'''
for s in sources:
    body+=f"- {s['citation']} "
    body+=f"[来源]({s['url']})。{s['role']}。\n"
body+='''
机器数据：[全部27条](../../research/amharic_pilot/examples.json)、[当前19条](../../research/amharic_pilot/current_comparison_examples.json)、[背景／范围外8条](../../research/amharic_pilot/background_and_excluded_examples.json)、[形式分组](../../research/amharic_pilot/frame_groups.json)、[来源表](../../research/amharic_pilot/sources.json)。另见[NSM与Mouton核读记录](../../03_文献笔记/NSM/阿姆哈拉语心理谓词_NSM与Mouton正文核读.md)。
'''
REPORT.parent.mkdir(parents=True,exist_ok=True);REPORT.write_text(body)

NOTE.write_text('''# 阿姆哈拉语心理谓词：NSM与Mouton正文核读

更新：2026-11-15。配套[第一轮例句稿](../../02_语言材料/阿姆哈拉语/阿姆哈拉语心理谓词_实体事件构式_例句与标注.md)。本轮已经实际使用Mouton章节的一部分正文，但不声称通读全章、目标词已有完整NSM定义或八节点已齐。

## Amberber 2001：已读章内35–37页，38–68页未取得

Mengistu Amberber. “Testing emotional universals in Amharic.” In Jean Harkins & Anna Wierzbicka (eds.), *Emotions in Crosslinguistic Perspective*, 35–68. Mouton de Gruyter。[DOI](https://doi.org/10.1515/9783110880168.35)。[本地预览](../../research/amharic_pilot/emotion2001_preview.pdf)共43页；PDF41–43对应该章印刷35–37页。版权页明确Mouton品牌，预览的其余页属于书前和前章，不能把43页当作本章全文。

|原页|本轮直接核到的内容|如何使用／不越界|
|---|---|---|
|35|作者以NSM为理论框架，认为FEEL是研究跨语言情绪概念的途径；列出Wierzbicka1999假说|已能确认方法立场，不再写“只知标题、立场未知”；尚不能据开头宣称四目标词均有正式explication|
|36|研究目标为检验上述假说；介绍词根模板、主语一致、基本SOV等|用于理解名物化与非线性词形，不能把一般语法介绍当作目标构式证据|
|37|定指宾语-n、主语NP无标记；§3.1以(tä-)sämmä为FEEL表达；例4a `dəssita yi-ssəmma-ññ-al` “I feel happy”|A23单独保存；happiness是所感受内容，并非外部ENTITY刺激。第一人称在动词上表示，不等于显性E NP被标ACC|

原页图片：[35](../../research/amharic_pilot/verified_pages/amberber_41.png)、[36](../../research/amharic_pilot/verified_pages/amberber_42.png)、[37](../../research/amharic_pilot/verified_pages/amberber_43.png)。本轮语法背景和FEEL证据确实来自Mouton正文；当前19条外部Y名词形式例句主要来自FSI、Lingua论文、SALC论文及学位论文，不能更换出版标签。

例4a中的语义内容与本项目Y的定义尤其要分开：“感到幸福”不等于“为一份礼物／某事感到幸福”。这里只确认FEEL表达和相关词形，未抄造任何英语NSM释义。

## Amberber 2008：仍为书目级

“Semantic primes in Amharic”, in *Cross-Linguistic Semantics*, 83–119，John Benjamins，[DOI](https://doi.org/10.1075/slcs.102.09amb)。正文未取得；不按标题或基元WANT的存在填入LIKE／LOVE／HAPPY的独立释义。John Benjamins不计Mouton来源。

## Kacprzak 2026：有词义讨论与派生词，非正式NSM释义

[全文](../../research/amharic_pilot/love2026.pdf)，*Studies in African Languages and Cultures*60:9–35，[DOI](https://doi.org/10.32690/SALC60.1)。本轮核读pp13–16、19、23–24等目标段。

- pp14–15：wäddädä涵盖爱、喜欢、想要，afäqqärä典型指浪漫爱情，常有更强烈感情及承诺；但后者偶尔可用于祖国、自由等。作者转述的语料频数不是本项目新采例数。
- p24及脚注17：afäqqärä通常不作家庭之爱的默认表达，但偶尔可以强调对子女极强烈的爱；“通常不自然”不能写为绝对不合语法或语义互斥。
- p16：afqari的“爱人者／爱民者／体育音乐迷”等派生名词表达分别保留。不能把动词的典型语义直接移给派生名词，也不能把名词短语的标记当矩阵心理动词的E/Y格。
- pp23–24例10提供“喜欢尊重和照顾女性”的真实文学引例（转引Bealu1983:356），本轮A14用作EVENT名物化证据；女性上的ACC为内部宾语。

这些分析可形成**待检验成分**：强度、长期承诺、典型对象、一般偏好和当前意愿。其适用范围可以重叠；本文不是用受限NSM词汇逐行给出的完整explication，不能把上述概述改装为文献原有英语定义。

## Menete、Jiang与Bayu 2026：Mouton书目与摘要已核，正文未读

*The heart and positive emotions: a view from Amharic*, *Journal of African Languages and Linguistics*47(1):135–169，[DOI](https://doi.org/10.1515/jall-2024-0026)。[Crossref记录](../../research/amharic_pilot/heart_crossref.json)、[OpenAlex记录](../../research/amharic_pilot/heart_openalex.json)已保存。该刊为Mouton，记录显示OA及CC-BY；本次出版端PDF／HTML访问返回202空响应，未获得正文。摘要的认知语言学主旨不能代替其具体例句、页码或NSM释义。

## 版本与引用防误

1. 实际读到的Baker & Kramer2014例43转引Leslau1995:395，Kozicki2018语法综述也以1995为依据。本地另下载的[Leslau扫描件](../../research/amharic_pilot/leslau1969.pdf)经题名页核为**1969 ERIC版本**，不是1995出版语法，不能用它假装完成1995页码的直接核查。
2. FSI材料是1964第一卷，罗马转写及老式符号沿用原页；印刷阿拉伯数字页码＋19＝本文件PDF页码。OCR只用于定位，目标例句均另查页面图。
3. Baker & Kramer的*Lingua*论文属Elsevier；FSI、SALC、Kozicki论文也不计Mouton。不能因题目有Amharic或引了Mouton文献就计入出版社门槛。
4. 本轮仍需取得Amberber2001后续正文及其他目标分析。**已经有部分Mouton正文实用，尚未完成外部Y框架与完整语义覆盖的验收。**

逐例数据与读取状态见[来源表](../../research/amharic_pilot/sources.json)及[采集说明](../../research/amharic_pilot/README.md)。所有最终节点为空，后续通过共同scenario、正反情境和必要成分测试再判定，不要求词义互斥。
''')

(OUT/'README.md').write_text('''# 阿姆哈拉语第一轮采集

2026-11-15。阅读入口：[例句与标注](../../02_语言材料/阿姆哈拉语/阿姆哈拉语心理谓词_实体事件构式_例句与标注.md)；[NSM／Mouton核读](../../03_文献笔记/NSM/阿姆哈拉语心理谓词_NSM与Mouton正文核读.md)。

- `examples.json`：A01–A27，共27条证据记录；派生词清单／人称变体合并记，不视为27个独立自然句或词项。
- `current_comparison_examples.json`：19条当前NP形式范围记录，8实体、11事件。`background_and_excluded_examples.json`：8条背景／范围外记录及原因。
- `frame_groups.json`：仅Y表面形式分组；`coverage.json`记录缺口。所有`final_semantic_node=null`、`native_speaker_verified=false`。语义标签允许重叠，形式合格不等于已确立语义节点。
- `sources.json`：书目、实际核读范围、出版者及本轮作用。单次下载响应、访问时间和SHA256保存在对应`*_source.json`。`heart_crossref.json`／`heart_openalex.json`只用于书目及开放状态，不当正文。
- `verified_pages/`：目标原页图，`*_small.png`为阅读缩图。FSI印刷页＋19＝PDF页；love2026印刷页＝PDF页＋8；Baker2014例43印刷152＝PDF13；Amberber章35–37＝预览PDF41–43；Kozicki页码两者相同。
- `fsiv1_clean.txt`是Internet Archive OCR，定位用，不能直接复制当作核准文本。`*_pages.json`是抽取文本。原图为最终校对依据。
- `leslau1969.pdf`题名页为1969 ERIC版本；曾按网络文件标签误命名为1995，核查后已改正；不与引用的Leslau1995混用。
- `search.py`、`fetch.py`、`ocr.swift`是检索辅助；有些200／202响应实际为空或错误页。文件存在不代表正文已读。`build_materials.py`只生成本轮报告与数据，后续人工编辑前先比较差异，勿运行旧脚本覆盖人工补例。

当前主要缺口：HAPPY实体外部刺激、afäqqärä独立NP句、LOVE事件的独立语义证据、däss alä显性E NP、名物化格交替条件、Mouton后续正文。没有找到不编码为不存在。
''')
print(json.dumps(dict(total=len(rows),current=len(current),background=len(background),groups=len(frame_groups),contents=dict(Counter(r['content_type'] for r in current))),ensure_ascii=False))
