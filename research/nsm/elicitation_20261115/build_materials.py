"""Build the NSM working inventory and the Korean pilot from explicit records.

No elicitation responses or final semantic nodes are supplied by this builder.
The existing example databases are not modified. Run from any directory.
"""
from pathlib import Path
import sys, json, hashlib, shutil, html, re

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/korean_pilot'))
from romanization import romanize, annotate_markdown
HERE = Path(__file__).resolve().parent
NOTE = ROOT / '03_文献笔记/NSM/三语言心理词_英语explications与待测草案_20261115.md'
TEST = ROOT / '02_语言材料/韩语/母语者测试'
LECTURE = Path('/Users/jessicac/.codex/attachments/f4aef163-d55c-4879-ac08-43980a8781bb/98345b860cbbb0643d382c014832f1b6.pdf')

entries = []
def add(id, language, forms, status, scope, source, text, caution='', probes=()):
    entries.append(dict(id=id, language=language, forms=forms, status=status,
        scope=scope, source=source, english=text.strip(), caution=caution,
        scenario_ids=list(probes), final_semantic_node=None,
        native_speaker_verified=False))

def feel_model(thoughts, degree='good', time='at this time'):
    return (f'someone X thinks like this {time}:\n' +
        '\n'.join('    '+x for x in thoughts) +
        f'\nbecause of this, X feels something {degree} {time}\n' +
        'like people often feel when they think like this')

# Q = checked English source wording, layout/punctuation only normalized.
# T = project English translation of a checked non-English source.
# H = project hypothesis; no claim of published or native-validated explication.
# P = prime expression/diagnostic, intentionally not a reductive definition.

add('E01','English',['pleased'],'Q','He was pleased at that time',
    'Goddard 2018, Lecture 3, p.77, fig.12; PDF15', '''
this someone (= he) thought like this (at that time):
    "something good happened before
    I wanted this"
because of this, he felt something good
    like people often feel when they think like this''', probes=['S13','S14','S15'])
add('E02','English',['contented'],'Q','He was contented at that time',
    'Goddard 2018, p.77, fig.12; PDF15', '''
this someone (= he) thought like this (at that time):
    "something good is happening to me now
    I want this
    I don’t want anything else now"
because of this, he felt something good
    like people often feel when they think like this''', probes=['S17','S18'])
add('E03','English',['delighted'],'Q','He was delighted at that time; greeting formulas excluded',
    'Goddard 2018, p.77, fig.12; PDF15', '''
this someone (= he) thought like this (at that time):
    "something very good happened a moment before
    I didn’t know before that it would happen"
because of this, he felt something good
    like people often feel when they think like this''', probes=['S14','S15'])
add('E04','English',['happy'],'Q','bare predicative modern emotional happy, not happy with',
    'Goddard 2018, p.85, fig.22; PDF23', '''
this someone (= he) thought like this (at that time):
    "many good things are happening to me now as I want
    I can do many things now as I want
    this is good"
because of this, he felt something good
    like people often feel when they think like this''',
    'p.86/fig.23 discusses happy with but does not give a complete explication; do not invent one and cite it as Goddard’s.', ['S19','S20'])

add('J01','Japanese',['suki da ENTITY'],'Q','person/animate/inanimate object, excluding activities',
    'Hasada 2000, p.173; PDF97', '''
X felt something because X thought something about another person/thing Y
sometimes a person thinks about someone else/something:
    "when I am with this person/thing, I often feel something good
    because of this, I want to be with this person/thing"
when this person thinks this, this person feels something good
this person feels good towards this someone else/something
X felt something like this
because X thought something like this about Y''', probes=['S01','S02'])
add('J02','Japanese',['suki da EVENT'],'Q','activity prototype, independent from J01',
    'Hasada 2000, pp.173–174; PDF97–98', '''
X felt something because X thought something about something Y
sometimes a person thinks about something:
    "when I do this thing, I often feel something good
    because of this, I want to do this thing"
when this person thinks this, this person feels something good
this person feels good towards this something
X felt something like this
because X thought something like this about Y''', probes=['S03','S04'])
add('J03','Japanese',['ai(suru)','aisuru'],'Q','enduring interpersonal caring love',
    'Hasada 2000, p.195; PDF108', '''
X felt something because X thought something about another person Y (in place Y)
sometimes a person thinks about someone else for a long time:
    "I know good/bad things of this person
    I can think many good things about this person
    I want to be with this person
    I want to do good things for this person
    if I could do something good for this person, I would do it.
    I will always want this"
when this person thinks this, this person feels something good
this person feels something very good towards this someone else
X felt something like this
because X thought something like this about Y''',
    'Retains the source’s awkward “(in place Y)”. The human-only generalization conflicts with its dog example and later activity evidence. This is not a definition of all modern aisuru uses.', ['S09','S10','S11'])
add('J04','Japanese',['horeru'],'Q','attraction to a person or a quality of a person',
    'Hasada 2000, p.200; PDF111', '''
X felt something because X thought something about another person Y
sometimes a person thinks about someone else/something about someone else Y:
    "I think good things about this person/thing about this person
    because of this I want to be with this person all the time
    I want to do something because of this
    I cannot think of anything else"
when this person thinks this, this person feels something good
this person feels something very good towards Y
X felt something like this
because X thought something like this about Y''',
    'The source component lettering skips (g); no missing component has been supplied.', ['S11'])
add('J05','Japanese',['akogare(ru)','akogareru'],'Q','idealization and desired similarity/proximity',
    'Hasada 2000, pp.204–205; PDF113', '''
X felt something because X thought something about another person/thing Y
sometimes a person thinks about someone/something else [Y]:
    "I think this person/thing is good
    if I were like this person/if I were near this thing,
    I would feel something good
    I am not like this person/I am not near this thing
    I want to be like this person/I want to be near this thing"
when this person thinks this, this person feels something good
this person feels something good towards Y
X felt something like this
because X thought something like this''',
    'The formal block has “good” in the towards-Y line; following prose has “very good”. Preserve the formal block and the discrepancy.', ['S12'])
add('J06','Japanese',['ureshii'],'Q','subjective use',
    'Hasada 2000, pp.236–237; PDF129', '''
I feel something because I thought something about something Y
sometimes a person thinks:
    "something good happened to me
    I want these things like this to be happening
    I don’t want anything else now"
when this person thinks this, this person feels something very good
I feel something like this
because I thought something like this about Y''',
    'The commentary says “I wanted something like this to happen”; the final block instead has present “I want…”. Do not silently standardize.', ['S13','S16'])
add('J07','Japanese',['tanoshii SUBJECTIVE'],'Q','subjective feeling; source optional brackets retained',
    'Hasada 2000, p.237; PDF129', '''
I feel something [because I thought something about something Y]
sometimes a person thinks for some time:
    "some good things are happening here
    I want these things to be happening"
when this person thinks this, this person feels something good
I feel something like this
[because I thought something like this about Y]''', probes=['S05','S06'])
add('J08','Japanese',['tanoshii ATTRIBUTIVE'],'Q','source’s descriptive/general-evaluation use, not just syntactic attributive position',
    'Hasada 2000, p.237; PDF129', '''
I want to say something about something Y
sometimes a person thinks for some time:
    "some good things are happening here
    I want these things to be happening"
when this person thinks this, this person feels something good
I say: other people can feel like this when they think about Y''',
    'Do not equate this source label with ENTITY content or with a Y case frame.', ['S05','S30'])
add('J09','Japanese',['shiawase da'],'Q','subjective good circumstances and contentment',
    'Hasada 2000, p.241; PDF131', '''
X felt something because X thought something
sometimes a person thinks for some time:
    "some good things are happening to me now
    these things have been happening for some time
    everything is good now
    I can’t want anything more now"
when this person thinks this, this person feels something very good
X felt something like this
because X thought something like this''',
    'The prose allows very different actual durations, including an eating episode; not a categorical lifelong state.', ['S17','S19','S20'])
add('J10','Japanese',['koi(suru)','koisuru'],'Q','additional reference, not automatically a new target node',
    'Hasada 2000, p.177; PDF99', '''
X felt something because X thought something about another person Y
sometimes a person thinks about someone else for some time,
    not for a long time:
    "there are two kinds of people
    sometimes I think something very good about a person of the other kind
    when I think about this person, I want to be with this other kind of person
    I know: I am not with this other kind of person now
    I would do anything if I could be with this other kind of person
    I cannot not think about this person"
when this person thinks this, this person feels something
this person feels something good towards this someone else
X felt something like this
because X thought something like this about Y''',
    'The author’s “two kinds/other kind” component is reported, not adopted as a universal requirement. Source Y-o/Y-ni discrepancy remains.', ['S11'])

def finn(thought, feeling='very good', duration='for some time'):
    return ('X feels something because X thinks something\nsometimes a person thinks:\n'+
        '\n'.join('    '+s for s in thought)+
        f'\nwhen this person thinks this, this person feels something {feeling}'+
        (' '+duration if duration else '')+
        '\nX feels something like this because X thinks something like this')

add('F01','Finnish',['ILO','ilo','related iloinen / iloita'],'T','concept-family core, not separate derived-word definitions',
    'Tuovila 2005, p.87; PDF89; project English translation',
    finn(['"something very good has happened / is happening now','I want this"']),
    'Slash alternatives are in the source. Distinct from the English joy version used in Vanhatalo et al. 2019.', ['S13','S14','S15'])
add('F02','Finnish',['ONNELLISUUS','onnellisuus','related onnellinen'],'T','concept-family core',
    'Tuovila 2005, pp.87–88; PDF89–90; project English translation',
    finn(['"something very good has happened / is happening now','I don’t want anything else"'],duration='for a long time'), probes=['S17','S19','S20'])
add('F03','Finnish',['TYYTYVÄISYYS','tyytyväisyys','related tyytyväinen'],'T','concept-family core',
    'Tuovila 2005, p.88; PDF90; project English translation',
    finn(['"something good has happened','I don’t want anything else now"'],feeling='good'), probes=['S17','S18','S21'])
add('F04','Finnish',['TOIVO','toivo','related toivoa'],'T','hope-type core, not all verbal request/desire uses',
    'Tuovila 2005, p.90; PDF92; project English translation',
    finn(['"I want something good to happen','I don’t know what will happen','I think: this can happen"'],feeling='good',duration=''),
    'This explication says nothing about PART/GEN alternation.', ['S07','S08'])
add('F05','Finnish',['RAKKAUS','rakkaus','related rakastaa / rakastua'],'T','interpersonal concept-family core',
    'Tuovila 2005, p.112; PDF114; project English translation, compared with Vanhatalo et al. 2019:173',
    finn(['"I think: there is another person','when I think about this person, I feel something very good','I want good things for this person"'],duration='for a long time'),
    'Not a separate definition of the inchoative rakastua or of activity-loving. The 2019 authors’ gloss says “good” on the long-duration line although Tuovila has hyvin hyvää; this translation follows Tuovila.', ['S09','S10'])

add('P01','Korean',['원하다'],'P','neutral WANT reading in the tested diagnostic frames',
    'Yoon 2003, pp.125–129,138', '''
X wants this thing.
X wants to do this.
X wants something to happen.''',
    'WANT is not reduced further. These are English diagnostic frames, not fabricated Korean corpus examples or a proof that every wenhata use has identical meaning.', ['S02','S04','S07'])
add('P02','Korean',['-고 싶다'],'P','V-ko siphta WANT construction',
    'Yoon 2003, pp.125–129,138', 'X wants to do this.',
    'Combinatorial allolexy concerns tested frames. The object of the embedded V is not a direct entity argument of siphta.', ['S04','S07'])
add('P03','Finnish',['haluta','tahtoa'],'P','WANT-exponent candidates',
    'Vanhatalo et al. 2014, pp.83–84,93, fn.18', '''
X wants this thing.
X wants to do this.
X wants something to happen.''',
    'Tentative exponent choice, not a demonstrated absolute desire/will opposition. These frames do not define all uses of either verb.')

# Shared test models; assigning a word to a model is a hypothesis, never a finding.
ENTITY_LIKE=feel_model(['"when I am with this someone/something, I often feel something good',
    'because of this, I want to be with this someone/something"'])
ACTIVITY_LIKE=feel_model(['"when I do this, I often feel something good',
    'because of this, I want to do this at many times"'])
CARE=feel_model(['"I often think about this someone', 'when I think about this someone, I feel something very good',
    'I want good things to happen to this someone','I want to do good things for this someone"'])
ENTHUSIASM=feel_model(['"when I do this, I feel something very good',
    'I want to do this at many times','I want to do this for a long time"'],degree='very good')
JOY=feel_model(['"something good happened','I wanted something like this to happen"'])
PLEASANT=feel_model(['"some good things are happening here now','I want it to be like this for some time"'])
CONTENT=feel_model(['"it is like this now','this is good','I don’t want anything else now"'])
WELLBEING=feel_model(['"many good things are happening to me now','it has been like this for some time',
    'I want it to be like this for a long time"'])
HOPE=feel_model(['"I want something to happen after now','I don’t know if it will happen','I think: it can happen"'])

def hyp(id,language,forms,scope,text,source,caution,probes):
    add(id,language,forms,'H',scope,source,text,caution,probes)

hyp('K01','Korean',['좋다'],'psychological attraction to an entity; GOOD reading kept separate',ENTITY_LIKE,
    'Project hypothesis; Yoon 2003:111–114 motivates GOOD/LIKE distinction; J01 as comparison',
    'Cohta can also evaluate an entity as GOOD without attraction. Do not require every cohta example to imply wanting to be with Y.', ['S01','S02','S29','S30'])
hyp('K02','Korean',['좋다'],'activity preference, not necessarily current enjoyment',ACTIVITY_LIKE,
    'Project hypothesis compared with J02; K41 grammatical evidence only',
    'A preference reading and an evaluation of an event may overlap; test, do not stipulate a polysemy split.', ['S03','S04','S05'])
hyp('K03','Korean',['좋아하다'],'entity preference',ENTITY_LIKE,
    'Project hypothesis; Yoon 2003:111–114 and dictionary LIKE uses; J01 as comparison',
    'Independently test the same model for cohta and cohahata. No obligatory overt display of emotion is included.', ['S01','S02','S09'])
hyp('K04','Korean',['좋아하다'],'activity preference',ACTIVITY_LIKE,
    'Project hypothesis; dictionary activity uses and J02',
    'The event nominalization variants are pooled at this stage; they remain visible in the elicited sentence.', ['S03','S04','S05','S26'])
hyp('K05','Korean',['사랑하다'],'interpersonal caring reading',CARE,
    'Project hypothesis compared with J03 and F05; Korean dictionary senses',
    'Neither caring alone nor feeling very good alone is assumed sufficient. Romantic and family uses may overlap without identical conditions.', ['S09','S10','S11'])
hyp('K06','Korean',['사랑하다'],'activity-directed strong positive attachment',ENTHUSIASM,
    'Project hypothesis; attested Korean activity use K42; J03 does not supply this definition',
    'Do not force good-for-another-person components onto an activity. Test possible expressive or genre effects.', ['S03','S26'])
hyp('K07','Korean',['아끼다'],'cherish a person',feel_model(['"this someone is very good to me',
    'I don’t want bad things to happen to this someone','I want to do good things for this someone"']),
    'Project hypothesis from Korean dictionary cherish sense, not saving sense',
    'Check whether “very good to me” overstates the personal relation. No pleasure component is forced inside the model thought.', ['S09','S10','S27'])
hyp('K08','Korean',['아끼다'],'cherish an object',feel_model(['"this something is very good to me',
    'I don’t want something bad to happen to it','because of this, I want to do some things"']),
    'Project hypothesis from Korean dictionary cherish sense',
    'The feeling clause itself is a testable conjecture. Saving water or withholding praise cannot confirm this meaning.', ['S27','S28'])
hyp('K09','Korean',['바라다'],'hope-type reading',HOPE,
    'Project hypothesis compared with F04; Korean dictionary wish/hope uses',
    'Test uncertainty and good feeling independently; palata may express a wish/request without these components. Other outer clausal forms stay outside the flagging sample.', ['S07','S08'])
hyp('K10','Korean',['기쁘다'],'good-event reaction',JOY,
    'Project hypothesis compared with E01, J06 and F01; Korean dictionary examples',
    'Good versus very good, personal beneficiary, prior desire and surprise are separately tested; not imposed together.', ['S13','S14','S15','S16','S25'])
hyp('K11','Korean',['기뻐하다'],'reaction directed towards Y',JOY,
    'Project hypothesis independently tested against kipputa; dictionary and K24/K47/K61/K62',
    'The provisional core matches K10. This is not a verified complete account of -e hata. Check viewpoint/inference without assuming visible expression or controllability.', ['S13','S16','S25','S31','S32'])
hyp('K12','Korean',['즐겁다'],'ongoing pleasant experience',PLEASANT,
    'Project hypothesis compared with J07; Korean dictionary and K48/K70',
    'Do not impose a long duration or conscious deliberate thought. An evaluative/descriptive reading remains possible.', ['S05','S06','S30'])
hyp('K13','Korean',['즐기다'],'current participation with good feeling', '''
X is doing something at this time
when X does this, X feels something good
X wants to do this for some time''',
    'Project hypothesis from Korean enjoy uses; compare, do not copy, J07',
    'Participation, pleasure and wanting continuation all need testing; this is not a proved volitional or causative analysis.', ['S05','S06','S26'])
hyp('K14','Korean',['즐기다'],'habitual activity', '''
X does this at many times
when X does this, X often feels something good
X wants to do this at many times''',
    'Project hypothesis from dictionary habitual participation use',
    'Whether “often does” is entailed or merely a tendency must be tested; compare current and habitual contexts.', ['S03','S04','S26'])
hyp('K15','Korean',['행복하다'],'overall positive circumstances',WELLBEING,
    'Project hypothesis compared with J09, F02 and E04; no claim of their equivalence',
    'Test short episodes, personal freedom, interpersonal care, intensity, and wanting nothing else independently.', ['S17','S18','S19','S20'])
hyp('K16','Korean',['만족하다'],'contentment about something',CONTENT,
    'Project hypothesis compared with F03 and E02; Korean dictionary',
    'A result can meet a standard while the person still wants more; S21 tests this counterexample. Verb/adjective labels do not settle sense identity.', ['S17','S18','S21'])
hyp('K17','Korean',['반갑다'],'encountering a person',feel_model(['"I wanted to see this someone',
    'I see this someone now','this is good"']),
    'Project hypothesis from Korean dictionary encounter use',
    'Prior wanting and prior separation may not be necessary. Greeting formulas are tested separately from experienced emotion.', ['S22','S23'])
hyp('K18','Korean',['반갑다'],'a welcome occurrence or piece of information',feel_model([
    '"I wanted something like this to happen','I know now: something like this is happening / happened','this is good"']),
    'Project hypothesis; resumption-of-publication example K60 and dictionary news examples',
    'Not restricted to seeing a person; slash marks alternatives to be separated if judgments differ.', ['S13','S24'])
hyp('K19','Korean',['흐뭇하다'],'positive assessment with a settled good feeling',feel_model([
    '"I think about this someone/something now','some good things happened / are happening',
    'I wanted it to be like this','it is like this now"']),
    'Project hypothesis from Korean dictionary and K64/K65/K71; compared with F03',
    'Do not require personal achievement, own child, silence, pride, or a maum subject without evidence.', ['S16','S17','S18','S21'])
hyp('K20','Korean',['마음에 들다'],'positive evaluation of a particular Y',feel_model([
    '"I think about this someone/something now','this is good','I want something like this"']),
    'Project hypothesis from Korean idiom entry and K38/K57/K58',
    'Wanting-to-choose and becoming acquainted are hypotheses, not established entailments. Internal maum-ey is not Y-LOC.', ['S01','S02','S29','S30'])
hyp('K21','Korean',['즐거워하다'],'derived comparison item, not yet in main corpus',PLEASANT,
    'Project hypothesis; official dictionary derivational link culkepta → culkewehata',
    'Same provisional core as K12 solely to test overlap and viewpoint differences. No attested frame is added to the corpus.', ['S05','S06','S31','S32'])

# Remaining Japanese/Finnish targets receive explicitly separate working drafts.
for id,lang,forms,scope,text,src,caution in [
 ('JH01','Japanese',['hoshii'],'entity desire','X wants this something.','grammar evidence only','WANT-content diagnostic; not yet a full account of hoshii evaluation or construction'),
 ('JH02','Japanese',['hoshigaru'],'third-person/entity desire','X wants this something.','derivational relation to hoshii; grammar evidence only','Content-only draft. Does not yet explicate -garu or assert obligatory behavioral evidence'),
 ('JH03','Japanese',['V-tai'],'desire to do','X wants to do this.','grammar evidence only','Prime-based content diagnostic, not a complete construction explication'),
 ('JH04','Japanese',['yorokobu'],'good-event reaction',JOY,'Hasada grammatical discussion; Sakaba 2026 template only','Independent draft; not an attested complete positive-verb NSM definition'),
 ('JH05','Japanese',['tanoshimu'],'current enjoyment','X is doing something at this time.\nwhen X does this, X feels something good.\nX wants to do this for some time.','Sakaba 2026:214–215,222–223 discussion/template','Participation/continuation draft, not copied from tanoshii as an established derived definition'),
 ('JH06','Japanese',['manzoku da'],'contentment',CONTENT,'no independent definition verified','Compared with F03/E02, not defined by translating satisfied'),
 ('JH07','Japanese',['daisuki da ENTITY'],'strong entity preference',ENTITY_LIKE.replace('something good','something very good'),'no independent definition verified','Strengthening is a testable hypothesis; not the only possible difference from suki'),
 ('JH08','Japanese',['daisuki da EVENT'],'strong activity preference',ACTIVITY_LIKE.replace('something good','something very good'),'no independent definition verified','Test expressive emphasis and context rather than fixing an intensity scale'),
 ('JH09','Japanese',['ki ni iru'],'positive evaluation of a particular Y',feel_model(['"I think about this someone/something now','this is good','I want something like this"']),'no independent definition verified','Acquisition of preference versus continuing state remains unresolved'),
 ('FH01','Finnish',['pitää LIKE'],'entity preference',ENTITY_LIKE,'no independent definition verified','Other pitää meanings excluded; activity extension must be tested separately'),
 ('FH02','Finnish',['tykätä'],'entity preference',ENTITY_LIKE,'no independent definition verified','Similarity to pitää is a hypothesis; register and word choice can differ'),
 ('FH03','Finnish',['pitää LIKE EVENT','tykätä EVENT'],'activity preference',ACTIVITY_LIKE,'no independent definition verified','Shared draft only; not evidence that these words have one invariant meaning'),
 ('FH04','Finnish',['nauttia'],'current enjoyment','X is doing something at this time.\nwhen X does this, X feels something good.\nX wants to do this for some time.','no independent definition verified','Entity enjoyment may require another specification; do not pragmatically recode an entity as an event'),
 ('FH05','Finnish',['rakastua'],'entering an interpersonal state','before this time, X did not feel something like this about Y\nnow X feels something very good when X thinks about Y\nX wants to be with Y\nX wants good things to happen to Y','F05 core plus inchoative hypothesis','Not Tuovila’s independent definition of rakastua; test relation to caring and attraction'),
]:
    hyp(id,lang,forms,scope,text,'Project draft; '+src,caution,[])

# Explicit application table: every current lexeme is represented without pretending
# that family-level or source-language definitions transfer automatically.
applications = [
 ('Japanese','suki da','J01, J02','two source prototypes'),
 ('Japanese','aisuru','J03','interpersonal source; activity meaning still outside this definition'),
 ('Japanese','hoshii','JH01','content diagnostic draft'),('Japanese','hoshigaru','JH02','content-only derived-form draft'),
 ('Japanese','V-tai','JH03','content diagnostic draft'),('Japanese','yorokobu','JH04','project draft'),
 ('Japanese','tanoshimu','JH05','project draft, not J07 substitution'),('Japanese','ureshii','J06','source subjective use'),
 ('Japanese','tanoshii','J07, J08','related comparison adjective; not identical to tanoshimu'),
 ('Japanese','shiawase da','J09','related comparison term'),('Japanese','horeru','J04','source scoped definition'),
 ('Japanese','akogareru','J05','source scoped definition'),('Japanese','manzoku da','JH06','project draft'),
 ('Japanese','daisuki da','JH07, JH08','project drafts'),('Japanese','ki ni iru','JH09','project draft'),
 ('Japanese','koi(suru)','J10','additional source comparison'),
 ('Finnish','pitää LIKE','FH01, FH03','project drafts'),('Finnish','tykätä','FH02, FH03','project drafts'),
 ('Finnish','rakastaa','F05','family core only; activity use not defined'),
 ('Finnish','rakastua','F05, FH05','family reference plus inchoative draft'),
 ('Finnish','haluta','P03','prime candidate; not all senses'),('Finnish','tahtoa','P03','prime candidate; not all senses'),
 ('Finnish','toivoa','F04','hope-family reference; verbal request senses not defined'),
 ('Finnish','nauttia','FH04','project draft'),('Finnish','olla iloinen','F01','family core only'),
 ('Finnish','iloita','F01','family core only; no independent verb definition'),
 ('Finnish','olla onnellinen','F02','family core only'),('Finnish','olla tyytyväinen','F03','family core only'),
 ('Korean','좋다','K01, K02','two working readings; GOOD kept separate'),
 ('Korean','좋아하다','K03, K04','independent drafts'),('Korean','사랑하다','K05, K06','person/activity drafts'),
 ('Korean','아끼다','K07, K08','cherish drafts; saving sense excluded'),('Korean','원하다','P01','WANT diagnostic evidence'),
 ('Korean','바라다','K09','hope-type draft; other readings remain open'),('Korean','-고 싶다','P02','WANT construction diagnostic'),
 ('Korean','기쁘다','K10','project draft'),('Korean','기뻐하다','K11','separate project draft'),
 ('Korean','즐겁다','K12','project draft'),('Korean','즐기다','K13, K14','current/habitual drafts'),
 ('Korean','행복하다','K15','project draft'),('Korean','만족하다','K16','project draft'),
 ('Korean','반갑다','K17, K18','encounter/occurrence drafts'),('Korean','흐뭇하다','K19','project draft'),
 ('Korean','마음에 들다','K20','project draft'),('Korean','즐거워하다','K21','additional derived comparison; no corpus frame claimed'),
]

scenarios=[]
def scenario(id, block, text, zh, y, candidates, models, contrast, basis):
    scenarios.append(dict(id=id,block=block,prompt_en=text,prompt_zh=zh,
        target_content=y,candidates=candidates,explication_ids=models,
        contrast=contrast,basis=basis,source_type='project-authored elicitation stimulus',
        native_response=None,semantic_node=None))

scenario('S01','core','Think about a particular cup. You often feel good when you see it or use it. This has been so for a long time. You do not want to buy it or use it right now. Say something in Korean about the cup and how you feel about it.',
 '一只特定的杯子，你长期看见或使用它时常感觉好，但现在不想购买或使用。请描述对杯子的感受。','ENTITY',['좋다','좋아하다','마음에 들다','아끼다'],['J01','K01','K03','K08','K20'],'S02: enduring attraction versus present desire','J01; project contrast')
scenario('S02','core','Think about the same cup. You do not usually feel good about this kind of cup. Today you need one for a task and want to have this cup now. Say something in Korean about what you want.',
 '同一只杯子，你平常对这类杯子没有好感；今天有用途，当前想要它。','ENTITY',['원하다','좋다','좋아하다','마음에 들다'],['P01','K01','K03','K20'],'S01; present desire can coexist with low preference','Project contrast; WANT diagnostic')
scenario('S03','core','You often feel good when you swim. You have felt this way for years. Today you are tired and do not want to swim. Describe in Korean how you generally feel about swimming.',
 '长期游泳时常感觉好；今天累，不想游。描述平常对游泳的态度。','EVENT',['좋아하다','좋다','즐기다','사랑하다'],['J02','K02','K04','K06','K14'],'S04: general attitude versus current wish','J02; project contrast')
scenario('S04','core','Swimming is usually unpleasant for you. Today you have a particular reason to swim once, and you want to do it now. Describe this in Korean.',
 '平常游泳不愉快；今天有特定理由，当前想游一次。','EVENT',['-고 싶다','원하다','좋아하다','즐기다'],['P01','P02','K04','K14'],'S03; wanting does not presuppose pleasure','Project contrast; WANT diagnostic')
scenario('S05','core','You are swimming now. While doing it, you feel good and want to continue for a while. You have never tried it before today. Describe the experience in Korean.',
 '首次尝试游泳，正在做，感觉好，希望继续一会儿。','EVENT',['즐겁다','즐기다','좋다','좋아하다','행복하다','즐거워하다'],['J07','K02','K04','K12','K13','K15','K21'],'S06; first-time present experience','J07; project extension')
scenario('S06','core','You are swimming now to finish required training. You usually enjoy swimming, but today you feel bad while doing it and want it to end. Describe both your general attitude and today’s experience in Korean.',
 '为了完成训练正在游泳，平常感觉好，但今天难受，希望结束。分别描述通常态度和这次体验。','EVENT',['즐기다','즐겁다','좋아하다','좋다','즐거워하다'],['K04','K12','K13','K14','K21'],'S05; habitual participation and present feeling may diverge','Project counterexample to participation/enjoyment inference')
scenario('S07','core','Your friend will take an examination tomorrow. You want the friend to pass. You do not know whether this will happen, but think it can happen. You feel good when thinking about this possibility. Describe your attitude in Korean.',
 '朋友明天考试，希望通过，不确定，但认为有可能；想到这个可能性感觉好。','EVENT',['바라다','원하다','-고 싶다'],['F04','P01','P02','K09'],'S08; uncertainty and positive feeling','F04; subject-control test is separate')
scenario('S08','core','Your friend will take an examination tomorrow. You want the friend to pass, but think passing is impossible. Thinking about it feels bad. Describe your attitude in Korean.',
 '同样希望朋友通过，但认为不可能，想来难受。','EVENT',['바라다','원하다'],['F04','P01','K09'],'S07 changes possibility and feeling together; follow-up must vary them separately','Project stress test of F04/K09; not a clean one-factor pair')
scenario('S09','core','Think about a person close to you. For a long time you have wanted good things to happen to this person and wanted to do good things for them. You do not always feel good when you are with them. Describe your feelings in Korean.',
 '长期希望亲近的人过得好，也愿意为对方做好事，但相处并非总感觉好。','ENTITY_PERSON',['사랑하다','아끼다','좋아하다','좋다'],['J03','F05','K05','K07','K03'],'S10; caring and pleasant company can overlap without entailing each other','J03/F05; project counterexample')
scenario('S10','core','You feel very good when you are with a person and often want to be with them. At the same time, you do not care whether good or bad things happen to that person. Can you describe your attitude in Korean? If the situation seems strange, say why.',
 '相处感觉很好，也常想一起，但不关心对方好坏。先判断情境能否理解，再描述。','ENTITY_PERSON',['좋아하다','사랑하다','아끼다','좋다'],['J01','J03','F05','K03','K05','K07'],'S09; possible unusual conjunction, not assumed contradiction','Project boundary probe; do not count situation rejection as lexical rejection')
scenario('S11','extension','You met someone recently. You think very good things about them, want to be with them, and keep thinking about them when apart. You do not yet know them well. Describe this in Korean.',
 '新近认识某人，评价很好，想一起，分开仍不断想到，尚不熟悉。','ENTITY_PERSON',['사랑하다','좋아하다','좋다'],['J03','J04','J10','K03','K05'],'S09; attraction and caring can be simultaneously applicable','J04/J10; no two-kinds assumption in stimulus')
scenario('S12','extension','You think a person’s way of doing things is very good. You want to be like this person, but do not want a close personal relationship with them. Describe this in Korean, using any expression you find natural.',
 '认为某人的做事方式很好，想成为那样的人，但不想发展亲密关系。','ENTITY_PERSON',['좋아하다','좋다','원하다'],['J05','K01','K03','P01'],'comparison meaning may require a word outside current inventory','J05; open vocabulary deliberately retained')
scenario('S13','core','Your friend passed an examination. You had wanted this to happen. You feel good about it now. You gain nothing from it yourself. Describe your feeling in Korean.',
 '朋友通过考试，之前希望如此，现在感觉好，自己没有获益。','EVENT',['기쁘다','기뻐하다','흐뭇하다','반갑다','행복하다'],['E01','J06','F01','K10','K11','K15','K18','K19'],'S16 personal benefit; not every good reaction must be self-directed','E01 vs J06; project contrast')
scenario('S14','core','You have just learned that you received an award. You had not expected it and had not thought about wanting it before. You now feel very good. Describe your feeling in Korean.',
 '刚得知获奖，事先没有预料，也没有想过要这个奖；当前感觉很好。','EVENT',['기쁘다','기뻐하다','행복하다','흐뭇하다'],['E03','K10','K11','K15','K19'],'S15; unexpectedness and prior wanting are separate follow-up variables','E03; project contrast')
scenario('S15','core','You have just learned that you received an award. You had expected it for a long time and wanted it. You now feel very good. Describe your feeling in Korean.',
 '刚得知获奖，长期预料且希望获奖，当前感觉很好。','EVENT',['기쁘다','기뻐하다','행복하다','흐뭇하다'],['E01','E03','K10','K11','K15','K19'],'S14; do not infer a surprise entailment from preference alone','Project contrast to E03')
scenario('S16','extension','You passed an examination. You had wanted this to happen and now feel good. Describe your feeling in Korean.',
 '自己通过考试，之前希望如此，现在感觉好。','EVENT',['기쁘다','기뻐하다','흐뭇하다','행복하다'],['J06','K10','K11','K15','K19'],'S13; other beneficiary versus self','J06; project contrast')
scenario('S17','core','You are sitting quietly after a good meal. Nothing very good has just happened. At present you feel good and do not want anything else. Describe your present state in Korean.',
 '用餐后安静坐着，没有刚发生的特别好事；当前感觉好，也不想别的。','STATE_CONTEXT',['만족하다','행복하다','흐뭇하다','즐겁다','기쁘다'],['E02','F02','F03','J09','K12','K15','K16','K19'],'S18; absence of further wants','E02; project instantiation')
scenario('S18','core','You are sitting quietly after a good meal. Nothing very good has just happened. At present you feel good, but you also strongly want other things to happen in your life. Describe your present state in Korean.',
 '同样安静坐着、当前感觉好，但仍强烈希望生活中发生其他事。','STATE_CONTEXT',['만족하다','행복하다','흐뭇하다','즐겁다','기쁘다'],['E02','F02','F03','J09','K12','K15','K16','K19'],'S17; global wanting more may differ from wanting another meal','Project contrast; specify domain of “anything else” in follow-up')
scenario('S19','extension','For a long time, many things in your life have been going as you want. You have good relationships and can do many things you want to do. You feel good about your life. Describe this in Korean.',
 '较长时间生活顺意，关系良好，也能做许多想做的事；对生活感觉好。','STATE_CONTEXT',['행복하다','만족하다','즐겁다','흐뭇하다'],['E04','J09','F02','K15','K16','K19'],'S20; duration may affect word choice without being a hard condition','E04/J09/F02; mixed positive setting')
scenario('S20','extension','Your life has been difficult recently. Right now, for just a few minutes, you are with someone close to you, feel very good, and think that you want this moment to continue. Describe this moment in Korean.',
 '最近生活困难，但与亲近的人共处的这几分钟感觉很好，希望继续。','STATE_CONTEXT',['행복하다','즐겁다','기쁘다','만족하다'],['J09','F02','K12','K15','K16'],'S19; several contextual dimensions differ, so use follow-up before assigning a duration feature','J09 short eating episodes; project contrast')
scenario('S21','extension','The result of your work is good enough for what you needed. You think you do not need to change it. You feel no particular pleasure, and you still want many other things in life. Describe your assessment of this result in Korean.',
 '工作结果达到所需，无需修改；没有特别愉悦，生活中仍想要很多。描述对结果的评价。','ENTITY_RESULT',['만족하다','마음에 들다','좋다','흐뭇하다'],['F03','K01','K16','K19','K20'],'S17; evaluation meeting a standard versus an emotional state','Project counterexample to obligatory good feeling/global no-more-wanting')
scenario('S22','core','You unexpectedly meet a friend whom you have wanted to see for a long time. Seeing the friend now feels good. Describe your feeling in Korean.',
 '意外遇到长期想见的朋友，见到对方感觉好。','ENTITY_PERSON',['반갑다','기쁘다','좋다','행복하다'],['K17','K10','K01','K15'],'S23; past wish and greeting formula','Korean dictionary encounter use')
scenario('S23','extension','You meet someone for the first time at a formal event. You had not wanted to see this particular person beforehand and do not feel any particular pleasure. What would you say to them? Separately, how would you describe your actual feeling?',
 '正式场合初次见面，之前未想见此人，也无特别愉悦。分别给见面用语和实际感受描述。','ENTITY_PERSON',['반갑다','기쁘다','좋다'],['K17','K10','K01'],'S22; formula truth and felt emotion rated separately','Goddard 2018:76 greeting-formula warning; project Korean test')
scenario('S24','extension','A magazine you wanted to read stopped publication. You now learn that publication has resumed, and you feel good about this. Describe your feeling about the resumption in Korean.',
 '想读的杂志停刊后复刊，得知后感觉好。','EVENT',['반갑다','기쁘다','기뻐하다','좋다'],['K18','K10','K11','K02'],'S22; occurrence without person encounter','K60 lexical event example, expanded context authored for test')
scenario('S25','extension','A friend asks you about a particular gift, a cup. You feel good about this cup. Say a short Korean sentence that explicitly mentions the cup and your feeling about it.',
 '朋友问一只作为礼物的杯子；你对这只杯子感觉好。说一句显式提及杯子和感受的短句。','ENTITY',['기쁘다','기뻐하다','좋다','마음에 들다','행복하다'],['K10','K11','K01','K20','K15'],'S13; preserve concrete NP, do not silently substitute receiving event','K61/K62 ordinary gifts; project syntax probe')
scenario('S26','extension','You have spent years swimming whenever possible, and you often feel very good while doing it. It matters a great deal to you. Describe your attitude to swimming in Korean. More than one description can fit.',
 '多年尽可能游泳，常感觉很好，对自己很重要。可给多个合适描述。','EVENT',['사랑하다','좋아하다','즐기다','좋다','아끼다'],['K04','K06','K14','K02','K08'],'S03; stronger involvement does not make weaker descriptions false','K42 activity love; project overlap probe')
scenario('S27','extension','An old cup from someone close to you matters a great deal to you. You do not enjoy using it, but do not want it to break and handle it carefully. Describe your attitude to the cup in Korean.',
 '亲近的人留下的旧杯子很重要；使用不愉快，但不愿损坏并小心对待。','ENTITY',['아끼다','사랑하다','좋아하다','마음에 들다'],['K08','K03','K20'],'S01; cherish need not be identical to pleasure','Korean dictionary cherish sense; project contrast')
scenario('S28','extension','You use less water because water costs money. You have no special feeling about the water itself. Describe what you do in Korean.',
 '因为水费而少用水，对水本身没有特别感情。','ENTITY',['아끼다','좋아하다'],['K08','K03'],'S27; distinct saving use must not count as cherish coverage','Korean dictionary saving sense; negative control')
scenario('S29','extension','You see a cup for the first time, think that it is just the kind you want, and choose it. You have not used it and do not know whether using it will feel good. Describe your assessment in Korean.',
 '初见杯子，觉得正是想要的类型并选择；未用过，不知道使用会否愉快。','ENTITY',['마음에 들다','좋다','좋아하다','원하다'],['K20','K01','K03','P01'],'S01; immediate evaluation versus prior experience','Project boundary probe')
scenario('S30','extension','A cup is very good for a particular task. You recognize this, but feel no attraction to it and do not want it. Describe both its quality and your attitude in Korean.',
 '杯子适合某项任务，但自己没有好感也不想要。分别描述质量和个人态度。','ENTITY',['좋다','좋아하다','마음에 들다'],['K01','K03','K20'],'S01/S29; GOOD and attraction are not presumed equivalent','Yoon 2003:111–114; project contrast')
scenario('S31','extension','I tell you: “When I learned the good news, I felt very good inside, but I did not smile, speak, or do anything to show it.” Report this in Korean. Then say it as your own first-person past experience.',
 '本人说好消息后内心感觉很好，但没有表露；先转述，再以第一人称过去经历说。','EVENT',['기쁘다','기뻐하다','즐겁다','즐거워하다'],['K10','K11','K12','K21'],'S32; known inner state without display; joy/enjoyment must also be controlled','Project derivation/viewpoint probe, not a claim that every target suits the news')
scenario('S32','extension','You see someone smiling and saying good things after hearing news, but you do not know how they feel inside. First describe only what you know. Then suppose they tell you that they felt no good feeling at all. Can your first description still be true?',
 '看到对方听消息后微笑说好话，不知道内心；再告知其没有好感受，问先前描述是否仍真。','EVENT',['기뻐하다','기쁘다','즐거워하다','즐겁다'],['K11','K10','K21','K12'],'S31; evidential basis, pragmatic inference and truth must be separated','Project derivation/viewpoint probe')

components = [
 ('C01','Pleasure without present desire','When I am with Y / do Y, I often feel something good.','I do not want to be with Y / do Y now.',['좋다','좋아하다','즐기다','마음에 들다'],['S01','S03','S06'],'K01–K04,K14,K20'),
 ('C02','Desire without positive feeling','X wants this / wants to do this.','X feels nothing good when thinking about it.',['원하다','바라다','-고 싶다'],['S02','S04','S08'],'P01,P02,K09'),
 ('C03','Possibility in hope','I think: this can happen.','I know that this cannot happen.',['바라다','원하다'],['S07','S08'],'K09,F04'),
 ('C04','Good for another person','I want good things to happen to this someone.','I do not care if bad things happen to this someone.',['사랑하다','아끼다','좋아하다'],['S09','S10'],'K05,K07,K03'),
 ('C05','Prior wanting','I wanted something like this to happen.','I had never wanted or thought about this before.',['기쁘다','기뻐하다','반갑다','흐뭇하다'],['S13','S14','S15','S24'],'K10,K11,K18,K19'),
 ('C06','Unexpectedness','I did not know before that this would happen.','I had known for a long time that this would happen.',['기쁘다','기뻐하다'],['S14','S15'],'K10,K11,E03'),
 ('C07','Personal beneficiary','Something good happened to me.','Something good happened only to someone else.',['기쁘다','기뻐하다','흐뭇하다'],['S13','S16'],'K10,K11,K19,J06'),
 ('C08','Wanting nothing else','I do not want anything else now.','I also want other things now.',['만족하다','행복하다','흐뭇하다'],['S17','S18','S21'],'K15,K16,K19'),
 ('C09','Duration','It has been like this for some time.','It has been like this for only a few moments.',['행복하다','즐겁다','기쁘다'],['S19','S20'],'K15,K12,K10'),
 ('C10','Pleasure in satisfaction','X feels something good about this.','X thinks this is good enough, but feels no good feeling.',['만족하다','마음에 들다','흐뭇하다'],['S21'],'K16,K20,K19'),
 ('C11','Prior wish to meet','I wanted to see this someone before now.','I had never thought about seeing this someone.',['반갑다'],['S22','S23'],'K17'),
 ('C12','Protection in cherishing','I do not want something bad to happen to Y.','I do not care if something bad happens to Y.',['아끼다','사랑하다'],['S09','S27','S28'],'K07,K08,K05'),
 ('C13','Current participation','X is doing this now and feels something good.','X often does this, but now feels bad while doing it.',['즐기다','좋아하다','즐겁다'],['S03','S05','S06'],'K13,K14,K04,K12'),
 ('C14','Expressed versus private feeling','X feels something good inside.','X does nothing that other people can see or hear because of it.',['기뻐하다','기쁘다','즐거워하다','즐겁다'],['S31','S32'],'K10,K11,K12,K21'),
 ('C15','Good quality versus attraction','I think this is good for doing something.','I do not want this and feel nothing good towards it.',['좋다','좋아하다','마음에 들다'],['S30'],'K01,K03,K20'),
 ('C16','Prior experience','When I do this / am with this, I often feel something good.','I have never done this / been with this before.',['좋아하다','좋다','마음에 들다'],['S05','S29'],'K01–K04,K20'),
]

def display(word):
    return word+' ('+romanize(word)+')' if re.search('[가-힣]',word) else word

def build_note():
    head='''# 三语言心理词的英语 explications 与待测草案

日期：2026-11-15。用途：先整理可核的完整英语释义与相关词族核心，再以明确标记的项目草案补缺，供韩语母语者测试及后续跨语言比较。**同一情境可以适用多个词；同一词可以覆盖多个情境。所有模型都允许覆盖范围重叠，不作互斥分类。**

本稿是研究者用材料。不要在自由回答阶段把词项、释义或预期成分交给受试者。测试用稿见[韩语测试说明](../../02_语言材料/韩语/母语者测试/研究者说明与测试表.md)；可填写版见[离线问卷](../../02_语言材料/韩语/母语者测试/韩语心理词_离线测试表.html)。

## 读法与证据等级

|标记|内容|引用规则|
|---|---|---|
|Q|原文英语完整释义，已核页图；只统一排版、引号及去掉成分字母|可以注明原作者和页码引用；不是无争议事实|
|T|已核非英语原文的项目英语翻译|必须写“本项目译”；不冒充已发表的英语措辞|
|P|WANT 基元表达及英语诊断框架|不是用更简单词分解 WANT，也不是所有义项的完整定义|
|H|本项目 NSM 式初步释义或内容草案|未由母语者验证；不声称为文献定义，也不声称已严格通过全部 NSM 词汇及句法审查|

T 的芬兰语条目是概念词族核心，不能直接提升成每个派生动词的独立定义。H 的来源栏只解释草案灵感和已知用法，不把来源作者列成草案作者。没有释义的词可以有初步工作草案；允许测试后删除或重写。

## 讲座中的格式与本项目的使用

Goddard（2018）Lecture 3 “Explicating Emotion Concepts across Languages and Cultures”，pp.63–93，DOI 10.1163/9789004357723_004。用户提供31页章节，页序1对应印刷p.63。

- pp.66–67：释义是解释性转述；需要合式，也要放回实际用例中检验、反复修改。受试者能理解和修正它很重要。
- pp.68–69：不同义项可能需要不同释义；需要检验单一释义是否足以覆盖，不能预先按翻译词分箱。
- pp.71–72，figs.8–9：`X was A` 常用 model thought → feeling → typicality；`X felt A` 可先写感受再写典型思考。词类／句式会影响分析的起点。
- pp.74–77：pleased / contented / delighted 提供可对照的完整模板；pp.75–76说明 prototypical 不等于每次逐字经历，礼貌套语要另测。
- p.76：可先参照已有同类词模板，再按目标语言适配。**这支持借用模板作为起点，不证明完整释义可以自动移植。**
- pp.85–86：bare happy 和 happy with 不同；后者只有讨论，没有在本章给出完整释义。

情绪模板示意如下，只是结构示意，不是一个已经完成的词义定义：

```text
someone X thought like this at this time:
    [specified model thought]
because of this, X felt something good/bad at this time
like people often feel when they think like this
```

WANT 是 NSM 原语，不强制加入 FEEL GOOD。偏好、享受、状态起始和派生词也不能一律硬套同一情绪模板。英语释义里的 LIKE 是“像”，不是心理偏好“喜欢”。

## 全部词项与释义的对照

下表涵盖当前三语言清单及少量直接相关参照词。共用某个工作模型表示“拟检验这组内容”，不表示已经确认同义。实体／活动用法分列时，也不是预先证明它们必定是两个词义。

|语言|词项|条目|当前解释层级|
|---|---|---|---|
'''
    for lang,form,ids,comment in applications:
        head+=f'|{lang}|{form}|'+', '.join(f'[{x}](#{x.lower()})' for x in ids.split(', '))+f'|{comment}|\n'
    head+='\n## 完整英语材料\n\n'
    for e in entries:
        head+=f'<a id="{e["id"].lower()}"></a>\n\n### {e["id"]}　'+ ' / '.join(e['forms'])+f'　{e["status"]}\n\n'
        head+=f'语言：{e["language"]}。范围：{e["scope"]}。\n\n来源与状态：{e["source"]}。\n\n```text\n{e["english"]}\n```\n\n'
        if e['caution']:head+='保留问题：'+e['caution']+'\n\n'
        if e['scenario_ids']:head+='对应测试：'+', '.join(e['scenario_ids'])+'。\n\n'
    head+='''## 从释义到测试和地图

先记录情境可理解性、自由表达、各词独立可用程度；再对某个已经得到的完整句子做释义替换及成分取消测试。适用性、常见性、必要性分别记录。母语者选了某词不证明整套释义都属于其词义；没有自由产出某词也不证明不能用。

同一词根的状态词与派生词分别判断。同一个候选模型可同时适用于两个词，随后研究视角、时体、论元和信息来源的差别。不预设派生一定意味着外显行为、可控性、起始性或 NOM→ACC。

句中Y的实体／事件内容与认知场景内部的“发生某事”分开。普通杯子／礼物仍为ENTITY；事件名物化为EVENT内容＋NP实现。语义测试可以用较长情境；最终flagging只纳入用户确定的形式范围。韩语除-ko siphta外的外层分句、被动、使役不纳入；自由回答若用了它们，照录后另作形式范围标记，不判受试者答错。

暂不根据本稿赋最终八节点，也不据若干情境的共同可用词直接宣称测得语义距离。先考察各语言内部的Y标记、完整E/Y框架和完整构式三个层次；一般及物性、构词家族不作为多条独立语义证据。

## 来源与核查范围

- Hasada, Rie. 2000. *An exploratory study of expression of emotions in Japanese: Towards a semantic interpretation*. ANU PhD. DOI 10.25911/5d7638ab55e24。相关释义页本轮再次核对扫描图；不是全论文通读声明。
- Tuovila, Seija. 2005. *Kun on tunteet: Suomen kielen tunnesanojen semantiikkaa*. Oulu。pp.87–90,112；大写标题表示概念词族核心。T条目为本项目英文翻译。
- Vanhatalo et al. 2014. *Revisiting the universality of Natural Semantic Metalanguage: A view through Finnish*. SKY27:67–94。WANT候选。
- Vanhatalo et al. 2019. *“Something bad can now happen to me here”: Meaning components of emotion words*. SKY32:145–179。附录的rakkaus英语翻译与原文对照；允许多选的调查思路与本测试兼容，不把匹配率当互斥分类准确率。
- Yoon, Kyung-Joo. 2003. *Constructing a Korean natural semantic metalanguage*. ANU PhD. DOI 10.25911/5d5158f90d84d。原扫描PDF现已由用户提供；pp.42–44,251,282,308已核图。当前WANT/GOOD段主要仍依据机构库抽取文本，不宣称全部核图。
- Sakaba 2026, DOI 10.22363/2687-0088-42740。正向动词的讨论与模板，不是已展开的完整独立正向释义。
- Goddard, Cliff. 2018. Lecture3，见本稿格式说明。原PDF与完整抽取文本另存于`research/nsm/elicitation_20261115/`，来源记录含页码对应及校验值。
- 韩语官方词典与已采实例见[第三轮复核](../../02_语言材料/韩语/韩语心理谓词_名词框架与缺例复核_第三轮.md)及[同根词讨论](../../02_语言材料/韩语/韩语心理谓词_同根词与共时构词.md)。词典释义是草案用法基础，不冒充正式NSM释义。

生成数据见`research/nsm/elicitation_20261115/inventory.json`。记录中`native_speaker_verified=false`指本项目尚未收到本轮母语者核验；Q/T仍明确是已有作者的分析。`final_semantic_node`始终为空。
'''
    NOTE.write_text(annotate_markdown(head))

def build_interviewer():
    s='''# 韩语心理词母语者测试说明与记录表

版本：2026-11-15。研究者用。**允许多词、多义、部分重叠，不要求把词语分成互斥类别。** 每个词独立判断；多个词都自然是有价值的结果。不要问“哪个才是真正的LIKE／LOVE／HAPPY”。

## 材料和顺序

- [英语释义与草案](../../../03_文献笔记/NSM/三语言心理词_英语explications与待测草案_20261115.md)：研究者先读，首阶段不展示。
- [离线填写版](韩语心理词_离线测试表.html)：英文受试者提示，可在本机浏览器打开、打印或导出JSON。不上传答案；阶段B需明确点击后才显示。
- 本稿中英对照情境用于访问者说明；英文是测试语言，不假定受试者英语熟练。先询问理解程度；若需译成韩语，逐条记录实际译文及译者，先请受试者复述情境，不能把英译理解问题编码为韩语词义拒绝。当前没有伪装成母语审定的韩语情境译文。
- 全部情境与韩语释义草案均为项目自拟、尚待测试。词典原例和项目例号是设计依据，不是本问卷自然语料的来源。

建议分次做：先完成16道core题的全部自由回答，再做相同16题的候选词判断；随后按需要做extension题与释义复核。不要同一题自由回答后马上给候选词，以免影响后续题。离线版A/B采用固定交错顺序，把近似情境分开；多位受试者可交替倒序，记录顺序。不是标准化量表，不预报效度或完成时长。

## 受试者与版本记录

|字段|填写|
|---|---|
|匿名编号| |
|日期及版本| |
|主要成长地区和方言| |
|当前常用语言| |
|英语情境理解程度| |
|呈现语言、是否协助翻译及译者| |
|本次范围 core / extension / both| |
|实际题序与中断位置| |

## 阶段 A 自由表达

先不展示词表、NSM模型和目标格。每题先确认受试者能理解这个情境，再请其自然表达。可以提供多个句子，不要求一个词、一个句式或显式格。明确区分“情境不太现实”和“语言不能这样说”。

English instruction: “Please describe the situation naturally in Korean. You may give more than one expression. There is no single correct word. If the situation is unclear or unusual, please tell me. Please distinguish what you would say politely from what describes the person’s actual feeling.”

## 阶段 B 逐词判断

自由回答完成后才给每题候选词；候选词只是待测范围，不是答案。请母语者为每个词先构造一个适合情境的完整韩语句，再对该句分别判断。**若字典形本身看起来不合适，允许调整屈折、敬语和时体；不把词类或人称限制误记为词义不适用。**

自然度：1完全不自然；2较不自然；3有条件可用；4自然；5非常自然；?不确定／不认识。每个候选都可以同时评4或5。另记录意义是否忠实、是否要改变情境，以及是否为礼貌套语。不要把“最常用”当“唯一能用”。

同一情境中两个词都适用，不自动证明同义；它们可能突出不同侧面。追问“这两句各多表达什么？换词后，关于感受或态度的断言改变了吗？”

## 情境表

下列每题均预留同一套字段：情境理解；自由原句；其他自由原句；阶段B每个候选的完整句／独立自然度／意义保留；改动；其他自然词。建议用离线填写版保存答案。

'''
    for q in scenarios:
        s+=f'### {q["id"]}　{q["block"]}\n\n{q["prompt_en"]}\n\n访问者中文：{q["prompt_zh"]}\n\n'
        s+=f'候选词（阶段B才看）：'+ '；'.join(q['candidates'])+'。其他词始终允许。\n\n'
        s+=f'研究者备注：{q["contrast"]}。依据：{q["basis"]}。语义内容：{q["target_content"]}；不是预填实际Y形式。\n\n'
        s+='|理解／自由表达|记录|\n|---|---|\n|情境是否清楚，有何修改| |\n|自然韩语完整句，可多句| |\n|候选词各自的句子、评分和意义变化| |\n|其他自然词、犹豫或语域| |\n\n'
    s+='''## 阶段 C 释义替换与成分复核

从阶段B已产生的真实完整句中选择目标。先固定义项和语境，再给相应K/P条目的完整英语候选释义；可请受试者用自己的韩语重述，但保持原句以便回查。不要只展示成分卡就声称完成了完整explication验证。

完整释义对应程度单独记：0不对应；1只部分对应；2基本对应但需改；3对应；?无法判断。请逐行标明过强、过弱或缺失，并至少找一个新的可用场合和一个可能的反例。对同一词的多个义项分别填写，不从一个例句推广全部。

成分地位：N这句用此词时必需；T通常联想但可没有；O可以有也可以没有；W这个成分不合适／意思不对；?不知道。**T/O不是排斥，N也需要取消测试和反例复核。**

下面是检查卡，不是预期答案。每卡对所有列出的词分别判断，保留同一词在不同语境中的不同回答。每次只修改一个成分；例如S07/S08同时改了可能性和情绪，不能直接把差异归给某一个义素。

|卡号|候选成分或释义行|取消／对照|候选词（逐词独立）|情境|
|---|---|---|---|---|
'''
    for id,title,line,cancel,words,qs,models in components:
        s+=f'|{id} {title}|{line}|{cancel}|'+ ' / '.join(words)+'|'+','.join(qs)+'|\n'
    s+='''
每个完整释义复核使用以下记录：

|字段|填写|
|---|---|
|词项与实际完整句| |
|对应情境、释义ID与具体义项| |
|释义整体对应度0–3/?| |
|每行N/T/O/W/?与理由| |
|移除该行后是否仍表达原意| |
|否定该成分后句子是否还能为真| |
|新的正例／反例，实际韩语句| |
|受试者修改后的释义和另一可用词| |

## 阶段 D 构式和同根词复核

先完成意义判断，再做本部分。以受试者自己的句子为起点，区分意义不合、词类／人称限制、构式不合和语体效果。这里请求的句子均是诱导材料，不伪装成已证例句，也不预置星号。

|模块|操作|必须记录|
|---|---|---|
|D01 实体与事件NP|对S01/S25的杯子或礼物，与S03/S05的游泳，分别请受试者使用每个已判断适用的词。事件允许词汇事件名词、-기及-는 것名物化；此轮不比较两种名物化的细节。|实际Y、实体/事件、外层格、是否省格；不要把礼物改成收到礼物后假装补到ENTITY。|
|D02 默认和替代形式|请先给最自然完整句，再只改外层Y标记；按实际得到的形式测试NOM/ACC/에或TOP，不机械遍历所有组合。|替代后自然度、意义是否改变、是否强调或对比；TOP另记，不反推被替代的格。|
|D03 A与A-어하다|分别测좋다/좋아하다、기쁘다/기뻐하다、즐겁다/즐거워하다。在第一人称当下、第一人称过去、第三人称亲口报告、第三人称只凭观察四种情境中请母语者分别造句。|人称、时体、信息来源、内心感受是否被断言、是否必须外显。多词都成立时照录；不能预设“动词形=装出来/展示”。|
|D04 历史同根比较|独立比较즐겁다、즐기다、즐거워하다，询问意义重叠及替换后的差别。|分别写实际完整句；不把즐기다分析成名物化-기，也不凭表面相似设定现代派生规则。|
|D05 未补齐的普通实体|对기쁘다显式请求杯子或普通礼物NP；对아끼다的珍爱读法请求一个事件NP。|不强制给出句子；无自然表达、只可换词、必须改分句、改为节省义分别记。|
|D06 词基和派生形式|如受试者自发给사랑、행복、만족等名词，另问名词句与相应谓词句在同一情境可否同真。|不因同根便移植explication，也不把同一构词规则多次计算成独立证据。|

愿望例外仅-ko siphta保留；其内部V的宾语不是siphta直接ENTITY补足。被动、CAUS和其他外层非名物化分句可以作为原回答存档，`comparison_eligible=false`，但不得删除受试者的有效语义回答。没有显式Y的STATE_CONTEXT题只提供语义证据，不能凭空填E/Y框架。

## 如何使用结果

一个受试者给出的是个体判断和试测线索。保存实际回答、语境和修订过程；不报总体比例或跨语言共性。独立保存自然度、释义对应度、成分地位与构式可用性，不能合成一个“正确/错误”分数。多词重叠的记录用于覆盖关系；不强制每个词只分配一个节点。问卷未被填写的格子都是未知，不能当0或反例。

原始JSON结构、释义和情境数据在`research/nsm/elicitation_20261115/`。本表尚无受试者答案；不向现有K01–K72语料库补入任何自拟的韩语句子。
'''
    (TEST/'研究者说明与测试表.md').write_text(annotate_markdown(s))

if __name__ == '__main__':
    TEST.mkdir(parents=True,exist_ok=True)
    build_note(); build_interviewer()
    for e in entries:
        if e['language']=='Korean':
            e['forms_romanized']=[romanize(w) for w in e['forms']]
            e['romanization_system']='Yale-style spelling transliteration'
    for q in scenarios:
        q['candidates_romanized']=[romanize(w) for w in q['candidates']]
    (HERE/'inventory.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
    (HERE/'scenarios.json').write_text(json.dumps(scenarios,ensure_ascii=False,indent=2)+'\n')
    (HERE/'component_probes.json').write_text(json.dumps([
        dict(id=x[0],title=x[1],component=x[2],contrast=x[3],candidates=x[4],
             candidates_romanized=[romanize(w) for w in x[4]],scenarios=x[5],models=x[6])
        for x in components],ensure_ascii=False,indent=2)+'\n')
    print(f'{len(entries)} entries; {len(applications)} lexical application rows; {len(scenarios)} scenarios; {len(components)} component cards')
