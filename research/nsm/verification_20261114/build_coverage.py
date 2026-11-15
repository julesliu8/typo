"""Evidence inventory; no semantic node assignments are generated."""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parent
sources={
 'H2000': {'author_year':'Hasada 2000','title':'An exploratory study of expression of emotions in Japanese: Towards a semantic interpretation','doi':'10.25911/5d7638ab55e24','local_pdf':'/Users/jessicac/Downloads/Hasada_2000_Japanese_emotions_PhD.pdf','read_status':'selected chapters and definition scans; not whole thesis','ocr_warning':'research/nsm/hasada2000_fulltext.txt is partial OCR despite filename'},
 'S2026': {'author_year':'Sakaba 2026','title':'Conceptualization of emotion in Japanese: Adjectives vs. verbs','doi':'10.22363/2687-0088-42740','local_pdf':'research/nsm/sakaba2026.pdf','read_status':'target sections; pp222–223 template and negative pair explications'},
 'T2005': {'author_year':'Tuovila 2005','title':'Kun on tunteet: Suomen kielen tunnesanojen semantiikkaa','url':'https://oulurepo.oulu.fi/handle/10024/34538','local_pdf':'research/nsm/tuovila2005.pdf','read_status':'full file obtained; selected sections pp85–90,111–112,146–147; core pages visually checked','scope_warning':'capitalized headings denote conceptual family cores; derivational meanings acknowledged but not individually differentiated'},
 'V2014': {'author_year':'Vanhatalo, Tissari & Idström 2014','title':'Revisiting the universality of Natural Semantic Metalanguage: A view through Finnish','url':'https://journal.fi/finjol/article/view/152992/98516','local_pdf':'research/nsm/vanhatalo_etal2014.pdf','read_status':'pp83–84 and93 WANT exponent discussion and diagnostics'},
 'V2019': {'author_year':'Vanhatalo et al. 2019','title':'“Something bad can now happen to me here”: Meaning components of emotion words','url':'https://journal.fi/finjol/article/view/153054','local_pdf':'research/nsm/vanhatalo_etal2019.pdf','read_status':'provenance, method/results and Appendix A; ilo/rakkaus pp172–173'},
 'Y2003': {'author_year':'Yoon 2003','title':'Constructing a Korean natural semantic metalanguage','doi':'10.25911/5d5158f90d84d','local_text':'research/korean_pilot/yoon2003_repository_fulltext.txt','read_status':'official repository extracted text, selected sections; original PDF not visually checked','ocr_warning':'do not restore damaged Korean text as verified transcription'}
}
rows=[]
def add(language,lexeme,status,source=None,pages=None,scope='',summary='',related=None):
 rows.append(dict(language=language,lexeme=lexeme,evidence_status=status,source=source,pages=pages,definition_scope=scope,semantic_paraphrase_zh=summary,related_expression=related,final_semantic_node=None))
for lex,pg,sc,sm in [
 ('suki da','173–174','person/thing vs activity, double prototype','相处／做此事时常感到好，因此想与其相处／做此事；思考—感受及一般态度框架'),
 ('aisuru','195','interpersonal caring love; not all object/activity uses','知道对方好坏，仍想到许多好处；希望相处并为对方做好事；持久意愿'),
 ('horeru','200','person or personal quality','正面思考某人或其特质，想一直相处并有所行动，难以想别的事'),
 ('akogareru','204–205','person/thing idealization and distance','觉得对象好；像对方／接近对象会好；尚未如此且想如此'),
 ('ureshii','236–237','subjective use; prose/final formulation differs','与自己有关的好事发生，愿其如此，此刻不想别的；非常好的感受'),
 ('tanoshii','237','subjective and descriptive variants separate','这里正在发生好事，希望继续；思考一段时间及好感受；描述型为他人也能如此感受'),
 ('shiawase da','241','subjective contented state','好事正发生且已持续一些时间；现在一切好，不能再想更多；非常好的感受'),
 ('koi(suru)','177','additional relational love comparator; frame discrepancy retained','强烈希望与对方相处，距离／难以停止思念；不预设持久')]:
 add('Japanese',lex,'D', 'H2000',pg,sc,sm)
for lex in ['yorokobu','tanoshimu']:
 add('Japanese',lex,'T','S2026','214–215,222–223','target-specific discussion and generic template; model thought left blank','动词与有意保持思考相关；模板不等于该词完整释义')
for lex in ['hoshii','hoshigaru','-tai','manzoku da','daisuki da','ki ni iru']:
 add('Japanese',lex,'U',scope='no independently verified full explication in checked sources')
for lex in ['haluta','tahtoa']:
 add('Finnish',lex,'P','V2014','83–84,93','tentative WANT exponent comparison; TAHTOA proposed','TAHTOA被提出为较中性的基元表达；未给出haluta的完成版分解')
for lex,rel,pg,sm in [
 ('rakastaa','RAKKAUS/rakkaus','111–112','人际关怀；想到对方感到很好，希望对方好；持续较久'),
 ('rakastua','RAKKAUS/rakkaus','111–112','作者将rakastuminen/rakastunut并入核心，同时承认另分的合理性；不提供起始义的独立释义'),
 ('olla iloinen','ILO/ilo','86–87','很好的事已发生／正在发生，想要这样；一段时间感觉很好'),
 ('iloita','ILO/ilo','86–87','同词族核心可参考；没有独立动词释义'),
 ('olla onnellinen','ONNELLISUUS/onnellisuus','87–88','很好的事已发生／正在发生，不想别的，长时间感觉很好'),
 ('olla tyytyväinen','TYYTYVÄISYYS/tyytyväisyys','88','好事已发生，现在不想别的，一段时间感觉好'),
 ('toivoa','TOIVO/toivo','90','希望好事发生，不知道将发生什么，认为有可能，因此感觉好；不能覆盖请求等所有用法')]:
 add('Finnish',lex,'F','T2005',pg,'related conceptual-family core; no independent target-predicate explication',sm,rel)
for lex in ['pitää','tykätä','nauttia']:
 add('Finnish',lex,'U',scope='no independently verified preference/enjoyment explication in checked sources')
for lex,pg,sm in [('ILO/ilo','86–87','很好之事已发生／正在发生，想要这样；一段时间感觉很好'),('ONNELLISUUS/onnellisuus','87–88','很好的事已发生／正在发生，不想别的；长时间感觉很好'),('TYYTYVÄISYYS/tyytyväisyys','88','好事已发生，现在不想别的；一段时间感觉好'),('TOIVO/toivo','90','想要好事发生；不知道结果，认为有可能；感觉好'),('RAKKAUS/rakkaus','111–112','想到另一个人感到很好；希望对方好；长时间的好感受')]:
 add('Finnish',lex,'F_SOURCE','T2005',pg,'formal NSM-inspired conceptual-core scenario, not a separately differentiated predicate',sm)
add('Finnish','ilo (2019 survey candidate)','F_SOURCE','V2019','151–154,172','English joy analysis adapted/translated for Finnish survey; distinct from Tuovila version','正在发生非常好的事，希望如此；思考带来很好的感受')
for lex in ['원하다','-고 싶다']:
 add('Korean',lex,'P','Y2003','125–129,138','WANT combinatorial allolexes in tested canonical sentences','名词性内容与动词组合分工；不是复杂心理词的分解定义')
for lex in ['좋다','좋아하다']:
 add('Korean',lex,'T','Y2003','111–114','GOOD/polysemous psychological LIKE and verbalization discussion','正向评价与心理吸引需分义；非完整偏好词释义')
for lex in ['사랑하다','아끼다','바라다','기쁘다','기뻐하다','즐겁다','즐기다','행복하다','만족하다','반갑다','흐뭇하다','마음에 들다']:
 add('Korean',lex,'U',scope='no independently verified full target explication in checked sources; dictionary entries are separate evidence')
import sys
sys.path.insert(0,str(OUT.parents[1]/'korean_pilot'))
from romanization import romanize
for row in rows:
 if row['language']=='Korean':row['romanization_yale']=romanize(row['lexeme'])
(OUT/'coverage.json').write_text(json.dumps({'date':'2026-11-14','status_legend':{'D':'independent formal explication verified, scope-limited','P':'prime-exponent evidence; not a reductive definition','T':'partial semantic discussion or template','F':'related conceptual-family scenario only; target not independently explicated','F_SOURCE':'source conceptual-core scenario or survey candidate','U':'no verified independent full explication in checked material; not proof of absence'},'sources':sources,'records':rows},ensure_ascii=False,indent=2))
print('coverage records',len(rows))
