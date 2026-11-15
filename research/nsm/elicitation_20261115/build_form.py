"""Standalone, offline elicitation form. No external resources or uploads."""
from pathlib import Path
import json, html, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'research/korean_pilot'))
from romanization import romanize

scenarios=json.loads((HERE/'scenarios.json').read_text())
entries=json.loads((HERE/'inventory.json').read_text())
components=json.loads((HERE/'component_probes.json').read_text())
def enrich(words):
    return [dict(word=w,label=w+' ('+romanize(w)+')') for w in words]
for q in scenarios:q['candidate_labels']=enrich(q['candidates'])
for c in components:c['candidate_labels']=enrich(c['candidates'])
models=[dict(id=e['id'],label=' / '.join(enrich(e['forms'])[i]['label'] for i in range(len(e['forms']))),
             text=e['english'],status=e['status']) for e in entries if e['language']=='Korean']
payload=json.dumps(dict(scenarios=scenarios,components=components,models=models),ensure_ascii=False).replace('</','<\/')

TEMPLATE=r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Korean words for attitudes and feelings</title>
<style>
:root{--ink:#172d35;--muted:#4c6068;--line:#c4cdd1;--accent:#145b67;--paper:#fff;--bg:#f3f6f6}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Apple SD Gothic Neo",sans-serif}
main{max-width:1080px;margin:0 auto;padding:40px 28px 80px}h1{font-size:32px;line-height:1.2;margin:10px 0 20px;color:#000}h2,h3{color:#000;line-height:1.35}h2{font-size:23px;margin-top:38px}h3{font-size:18px;margin:0 0 12px}.intro{max-width:78ch}.meta{color:var(--muted);font-size:13px;letter-spacing:.04em}.tools{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:20px 0}button,.button{font:inherit;cursor:pointer;background:var(--accent);color:white;border:1px solid var(--accent);border-radius:5px;padding:9px 14px;display:inline-block}button.secondary,.button.secondary{background:white;color:var(--accent)}button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid #d3ab55;outline-offset:2px}label{display:block;font-size:14px;color:var(--muted)}input,select,textarea{font:inherit;color:var(--ink);background:#fff;border:1px solid #9faeb5;border-radius:4px;padding:8px;max-width:100%}textarea{width:100%;min-height:75px;resize:vertical;line-height:1.45}input{width:100%}select{width:100%}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 20px}.wide{grid-column:1/-1}.question{margin:28px 0;padding:22px 0;border-top:1px solid var(--line);break-inside:avoid-page}.question p{margin:8px 0 16px;max-width:88ch}.qid{font-size:14px;color:var(--accent);font-weight:700;margin-right:10px}.hint{font-size:14px;color:var(--muted)}.response{margin:12px 0}.tablewrap{overflow:auto;margin-top:18px}table{width:100%;border-collapse:collapse;font-size:14px;table-layout:fixed}th,td{border:1px solid var(--line);padding:10px;vertical-align:middle;text-align:left}th{background:#e4edef;font-weight:600}td textarea{font-size:14px;min-height:72px}td select{font-size:14px}td.word{overflow-wrap:anywhere}table.rating th:nth-child(1){width:17%}table.rating th:nth-child(2){width:33%}table.rating th:nth-child(3){width:14%}table.rating th:nth-child(4){width:15%}table.rating th:nth-child(5){width:21%}pre{white-space:pre-wrap;font:15px/1.65 ui-monospace,monospace;padding:15px 0;max-width:90ch}nav{display:flex;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line);padding-bottom:16px;margin:30px 0 20px}nav button{background:transparent;color:var(--accent)}nav button.active{background:var(--accent);color:#fff}[hidden]{display:none!important}.status{min-height:24px;font-size:14px;color:var(--accent)}.pending{font-style:italic}.phaseIntro{max-width:84ch}.newreview{margin-top:28px;border-top:1px solid var(--line);padding-top:20px}.linecheck{min-height:100px}.nowrap{white-space:nowrap}
@media(max-width:700px){main{padding:24px 16px}.grid{grid-template-columns:1fr}.wide{grid-column:auto}.rating{min-width:740px}h1{font-size:27px}}
@media print{@page{size:A4;margin:17mm}body{background:#fff;font-size:10.5pt;line-height:1.45}main{max-width:none;padding:0}.tools,nav,.noprint{display:none!important}h1{font-size:22pt}.question{margin:18px 0;padding:14px 0}.tablewrap{overflow:visible}table{font-size:9pt}td,th{padding:5px}td textarea,td select{font-size:9pt}textarea{min-height:65px;border-color:#aaa}input,select{padding:4px;font-size:10pt}h2{break-after:avoid}pre{font-size:10pt}.printlabel{display:block}#status{display:none}}
</style></head><body><main>
<div class="meta">PILOT · 15 NOVEMBER 2026 · NO RESPONSES HAVE BEEN PRE-FILLED</div>
<h1>Korean words for attitudes and feelings</h1>
<div class="intro"><p>Please describe the situations naturally in Korean. <strong>More than one expression may fit a situation.</strong> We are interested in overlapping meanings as well as differences. There is no single correct word.</p>
<p>First give your own expressions in Part A. Complete that part for your session before opening Part B. You can leave anything blank or say that a situation is unclear. The English prompts and draft paraphrases are research materials to be checked, not definitions you have to accept.</p></div>
<div class="grid" id="participant">
<label>Participant code<input data-key="participant_code" autocomplete="off"></label>
<label>Date<input type="date" data-key="date"></label>
<label>Main region / dialect while growing up<input data-key="dialect"></label>
<label>Languages used regularly<input data-key="languages"></label>
<label>English prompt comprehension<select data-key="english_comprehension"><option value="">Choose</option><option>Clear without help</option><option>Some help needed</option><option>Korean translation needed</option></select></label>
<label>Session scope<select id="scope" data-key="scope"><option value="core">Core 16 situations</option><option value="extension">Additional 16 situations</option><option value="both">All 32 situations</option></select></label>
<label class="wide">Prompt language actually used, translator / facilitator, clarification or other session notes<textarea data-key="session_notes"></textarea></label>
</div>
<div class="tools"><button type="button" id="export">Download responses</button><label class="button secondary">Load saved responses<input id="import" type="file" accept="application/json" hidden></label><button class="secondary" type="button" id="print">Print current part</button></div>
<p class="hint">This file works offline and sends no data anywhere. Answers stay in the open page until you download them. Download before closing; you can load the saved JSON file to continue. A downloaded file contains all parts, including hidden parts.</p>
<div class="status" id="status" role="status" aria-live="polite"></div>
<nav aria-label="Questionnaire parts"><button data-phase="A" class="active" type="button">A · Own expressions</button><button data-phase="B" type="button">B · Independent word ratings</button><button data-phase="C" type="button">C · Meaning checks</button><button data-phase="D" type="button">D · Sentence forms</button></nav>
<section id="phaseA"><h2>Part A · Your own expressions</h2><p class="phaseIntro">For each situation, first say whether it is clear. Then give one or more complete Korean sentences. A short or longer expression is fine. Do not look for a particular word. If you change a situation to make it understandable, record the change.</p><div id="itemsA"></div></section>
<section id="phaseB" hidden><h2>Part B · Rate each expression independently</h2><div id="gate"><p>Only open the word lists after completing Part A for this session.</p><button id="openB" type="button">I have finished Part A for this session</button></div><div id="bbody" hidden><p class="phaseIntro">Make a complete Korean sentence with each word if possible. Rate that sentence in the stated situation. Multiple words can all receive high ratings. You may change endings, tense and politeness level. If a word needs a different meaning or a change to the situation, explain.</p><p class="hint">Naturalness: 1 very unnatural · 2 rather unnatural · 3 possible with conditions · 4 natural · 5 very natural · ? unsure or unfamiliar. Meaning fit is a separate judgment. A polite formula may be usable without stating an actual feeling.</p><div id="itemsB"></div></div></section>
<section id="phaseC" hidden><h2>Part C · Check proposed meanings</h2><p class="phaseIntro">Work with a sentence you have already given. The proposed English paraphrases below are preliminary research hypotheses. You can reject, shorten, expand or rewrite them. It is fine if two different words overlap.</p><h3>Whole paraphrase review</h3><p class="hint">Choose an expression, fix a particular sentence and situation, and check the whole paraphrase. Then mark each line as necessary, usual only, optional, incorrect, or unsure. Give a new example or counterexample. WANT items are diagnostic frames, not decompositions of WANT.</p><div id="reviews"></div><button type="button" id="addreview" class="secondary noprint">Add another paraphrase review</button><h2>Component checks</h2><p>For each word independently, can the stated component be absent while your sentence is still true? Please give a Korean sentence, not just a dictionary form.</p><p class="hint">N = necessary in this use · T = usual association but not necessary · O = may be present or absent · W = incorrect or wrong meaning · ? = unsure. These options do not force words into separate categories.</p><div id="itemsC"></div></section>
<section id="phaseD" hidden><h2>Part D · Sentence forms and related words</h2><p class="phaseIntro">The facilitator can complete these after the meaning checks. First give the most natural sentence; then try an alternative without changing the intended meaning. An alternative may be equally good. Do not invent a sentence if none feels natural.</p><div id="itemsD"></div></section>
<p class="hint">Pilot materials, not a validated measurement scale. The source scenario labels, proposed categories and expected answers are intentionally not presented as solutions.</p>
<script id="materials" type="application/json">__PAYLOAD__</script>
<script>
'use strict';
const DATA=JSON.parse(document.getElementById('materials').textContent);
const VERSION='2026-11-15-v1-overlap';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const order=['S01','S13','S04','S22','S09','S17','S02','S14','S07','S05','S10','S18','S03','S15','S08','S06','S25','S11','S19','S27','S16','S29','S23','S12','S26','S20','S31','S24','S28','S21','S32','S30'];
const byId=Object.fromEntries(DATA.scenarios.map(q=>[q.id,q]));
const sorted=order.map(id=>byId[id]);
const textarea=(key,label,cls='')=>`<label class="response ${cls}">${esc(label)}<textarea data-key="${esc(key)}"></textarea></label>`;
const select=(key,opts,label='Choose')=>`<select aria-label="${esc(key)}" data-key="${esc(key)}"><option value="">${esc(label)}</option>${opts.map(([v,t])=>`<option value="${esc(v)}">${esc(t)}</option>`).join('')}</select>`;
const nat=[['1','1 · very unnatural'],['2','2 · rather unnatural'],['3','3 · with conditions'],['4','4 · natural'],['5','5 · very natural'],['?','? · unsure / unfamiliar']];
const fit=[['yes','same intended meaning'],['part','partly fits'],['change','needs changed situation'],['formula','polite formula only'],['no','does not fit'],['?','unsure']];
for(const q of sorted){
 const a=document.createElement('article');a.className='question scenario';a.dataset.block=q.block;
 a.innerHTML=`<h3><span class="qid">${q.id}</span>Situation</h3><p>${esc(q.prompt_en)}</p><label>Is this situation clear?${select(q.id+'.clear',[['yes','Yes'],['clarified','Yes, after clarification'],['no','No'],['odd','Understandable but unusual']])}</label>${textarea(q.id+'.clarification','Clarification, changed details, or translated prompt actually used')}${textarea(q.id+'.free','Your own Korean expression or expressions')}${textarea(q.id+'.free_notes','Other possible expressions, differences, or uncertainty')}`;
 document.getElementById('itemsA').append(a);
 const b=document.createElement('article');b.className='question scenario';b.dataset.block=q.block;
 b.innerHTML=`<h3><span class="qid">${q.id}</span>Independent ratings</h3><p>${esc(q.prompt_en)}</p><div class="tablewrap"><table class="rating"><thead><tr><th>Expression</th><th>Your complete Korean sentence</th><th>Naturalness</th><th>Meaning fit</th><th>Difference or change needed</th></tr></thead><tbody>${q.candidate_labels.map((w,i)=>`<tr><td class="word">${esc(w.label)}</td><td><textarea aria-label="${q.id} ${esc(w.label)} sentence" data-key="${q.id}.candidate.${i}.sentence"></textarea></td><td>${select(q.id+'.candidate.'+i+'.naturalness',nat)}</td><td>${select(q.id+'.candidate.'+i+'.meaning',fit)}</td><td><textarea aria-label="${q.id} ${esc(w.label)} notes" data-key="${q.id}.candidate.${i}.notes"></textarea></td></tr>`).join('')}</tbody></table></div>${textarea(q.id+'.alternatives','Other natural expressions (always allowed)')}${textarea(q.id+'.overlap','If more than one fits, what does each expression add? Can both descriptions be true?')}`;
 document.getElementById('itemsB').append(b);
}
const componentOptions=[['N','N · necessary'],['T','T · usual only'],['O','O · optional'],['W','W · incorrect'],['?','? · unsure']];
for(const c of DATA.components){
 const el=document.createElement('article');el.className='question';
 el.innerHTML=`<h3><span class="qid">${c.id}</span>${esc(c.title)}</h3><p>Proposed component: <strong>${esc(c.component)}</strong></p><p>Now try this: ${esc(c.contrast)}</p><div class="tablewrap"><table><thead><tr><th>Expression</th><th>Component status</th><th>Your sentence, explanation or counterexample</th></tr></thead><tbody>${c.candidate_labels.map((w,i)=>`<tr><td>${esc(w.label)}</td><td>${select(c.id+'.'+i+'.status',componentOptions)}</td><td><textarea aria-label="${c.id} ${esc(w.label)} explanation" data-key="${c.id}.${i}.notes"></textarea></td></tr>`).join('')}</tbody></table></div>${textarea(c.id+'.context','Which use, sentence, or changed context did you judge?')}`;
 document.getElementById('itemsC').append(el);
}
let reviewCount=0;
function addReview(){
 const i=reviewCount++;const el=document.createElement('article');el.className='newreview';
 el.innerHTML=`<h3>Paraphrase review ${i+1}</h3><label>Proposed paraphrase${select('review.'+i+'.model',DATA.models.map(m=>[m.id,m.id+' · '+m.label]))}</label><pre id="modeltext${i}">Choose a model above. Every complex Korean-word model here is a project draft.</pre>${textarea('review.'+i+'.sentence','Your complete Korean sentence and situation')}${textarea('review.'+i+'.reading','The particular meaning you are judging (not all uses of the word)')}<label>How well does the whole paraphrase preserve your meaning?${select('review.'+i+'.fit',[['0','0 · does not match'],['1','1 · only partly'],['2','2 · mostly, needs changes'],['3','3 · matches'],['?','? · cannot judge']])}</label>${textarea('review.'+i+'.lines','For each paraphrase line: necessary / usual only / optional / wrong / unsure, with changes','linecheck')}${textarea('review.'+i+'.counterexample','A new example or counterexample, and a better paraphrase if possible')}`;
 document.getElementById('reviews').append(el);
 el.querySelector('select').addEventListener('change',e=>showModel(i,e.target.value));
}
function showModel(i,id){const m=DATA.models.find(x=>x.id===id);document.getElementById('modeltext'+i).textContent=m?m.text:'Choose a model above.';}
addReview();document.getElementById('addreview').onclick=addReview;
const modules=[
 ['D01','Entity and event noun phrases','For any word that fits the meaning, give a sentence about a particular cup or gift, and a sentence about swimming. Please keep the cup or gift explicitly as the object being discussed; do not replace it with “receiving a gift”. An event noun or event nominalization is allowed.'],
 ['D02','Natural and alternative markings','Start with your most natural sentence. Then try another marking on the target noun phrase while keeping the intended meaning. Record each full sentence and whether meaning, emphasis or naturalness changes. A topic expression need not be treated as the same thing as a case expression.'],
 ['D03','State words and related forms','Compare 좋다 (cohta) / 좋아하다 (cohahata), 기쁘다 (kipputa) / 기뻐하다 (kippehata), and 즐겁다 (culkepta) / 즐거워하다 (culkewehata). Use your own present experience, your past experience, another person’s reported experience, and an observer’s inference. Do any forms require an outward display? Can two forms describe the same experience?'],
 ['D04','Three related expressions','Compare 즐겁다 (culkepta), 즐기다 (culkita), and 즐거워하다 (culkewehata) in contexts where they fit. Do they all work? What, if anything, changes? Give actual sentences.'],
 ['D05','Uncertain noun-phrase possibilities','Can 기쁘다 (kipputa) be used with an explicit ordinary cup or gift noun phrase? Can 아끼다 (akkita), in the sense of valuing or cherishing rather than saving, be used with an explicit event noun phrase? There may be more than one answer or no natural sentence.'],
 ['D06','Nouns and related predicates','If you use 사랑 (salang), 행복 (hayngpok), or 만족 (mancok), compare your noun expression with a sentence using 사랑하다 (salanghata), 행복하다 (hayngpokhata), or 만족하다 (mancokhata). Can the two descriptions be true together? Do they have exactly the same meaning in your example?']
];
for(const [id,title,prompt] of modules){let el=document.createElement('article');el.className='question';el.innerHTML=`<h3><span class="qid">${id}</span>${esc(title)}</h3><p>${esc(prompt)}</p>${textarea(id+'.sentences','Full Korean sentences and contexts')}${textarea(id+'.judgments','Judgments, alternatives, meaning changes and limits')}`;document.getElementById('itemsD').append(el);}
function filterScope(){const value=document.getElementById('scope').value;document.querySelectorAll('.scenario').forEach(el=>el.hidden=value!=='both'&&el.dataset.block!==value);}
document.getElementById('scope').addEventListener('change',filterScope);filterScope();
let currentPhase='A',bUnlocked=false,dirty=false;
document.querySelectorAll('[data-phase]').forEach(button=>button.onclick=()=>{
 currentPhase=button.dataset.phase;['A','B','C','D'].forEach(p=>document.getElementById('phase'+p).hidden=p!==currentPhase);
 document.querySelectorAll('[data-phase]').forEach(b=>b.classList.toggle('active',b===button));
});
document.getElementById('openB').onclick=()=>{bUnlocked=true;document.getElementById('gate').hidden=true;document.getElementById('bbody').hidden=false;};
document.getElementById('print').onclick=()=>window.print();
document.addEventListener('input',e=>{if(e.target.hasAttribute('data-key')){dirty=true;document.getElementById('status').textContent='Changes in this page have not been downloaded yet.';}});
function serialize(){let answers={};document.querySelectorAll('[data-key]').forEach(el=>answers[el.dataset.key]=el.value);return {version:VERSION,exported_at:new Date().toISOString(),current_phase:currentPhase,b_unlocked:bUnlocked,review_count:reviewCount,scope:document.getElementById('scope').value,presentation_order:order.filter(id=>document.getElementById('scope').value==='both'||byId[id].block===document.getElementById('scope').value),answers,stimuli:DATA.scenarios.map(q=>({id:q.id,prompt_en:q.prompt_en,candidates:q.candidates})),component_probes:DATA.components,paraphrase_models:DATA.models};}
document.getElementById('export').onclick=()=>{const data=serialize();const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'});const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;let p=(data.answers.participant_code||'anonymous').replace(/[^a-zA-Z0-9_-]/g,'_');a.download='korean_psych_'+p+'_'+new Date().toISOString().slice(0,10)+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1500);dirty=false;document.getElementById('status').textContent='Response download requested. Keep the downloaded JSON file to continue later.';};
document.getElementById('import').onchange=async e=>{const f=e.target.files[0];if(!f)return;try{const data=JSON.parse(await f.text());if(data.version!==VERSION||!data.answers||typeof data.answers!=='object')throw Error('This is not a compatible response file.');const count=Number(data.review_count||1);if(!Number.isInteger(count)||count<1||count>100)throw Error('Invalid review count.');while(reviewCount<count)addReview();document.querySelectorAll('[data-key]').forEach(el=>el.value=typeof data.answers[el.dataset.key]==='string'?data.answers[el.dataset.key]:'');for(let i=0;i<reviewCount;i++)showModel(i,data.answers['review.'+i+'.model']);filterScope();bUnlocked=Boolean(data.b_unlocked);document.getElementById('gate').hidden=bUnlocked;document.getElementById('bbody').hidden=!bUnlocked;dirty=false;document.getElementById('status').textContent='Responses loaded. Please check the participant code and session scope.';}catch(err){document.getElementById('status').textContent=err.message;}e.target.value='';};
window.addEventListener('beforeunload',e=>{if(dirty){e.preventDefault();e.returnValue='';}});
</script></main></body></html>'''
out=ROOT/'02_语言材料/韩语/母语者测试/韩语心理词_离线测试表.html'
out.write_text(TEMPLATE.replace('__PAYLOAD__',payload))
print(out)
