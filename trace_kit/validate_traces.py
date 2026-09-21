"""validate_traces.py: automatic safety nets over cut traces. Writes a verdict per trace."""
import json, re, sys
from collections import defaultdict
STOP=set("with from that this than then their there these those which while where about into onto over under after before between across along vol excess zrsi2 zrb2 sic composite composites content sample samples without through".split())
def words(s): return {w for w in re.findall(r'[a-z]{5,}', s.lower()) if w not in STOP}
def bigrams(s):
    w=[x for x in re.findall(r'[a-z]{4,}', s.lower()) if x not in STOP]; return {(a,b) for a,b in zip(w,w[1:])}
def nums(s): return set(re.findall(r'\d+(?:\.\d+)?', s))
def stem(ws): return {re.sub(r'(ing|ed|es|s)$','',w) for w in ws}
FIGREF=r'\bF\d+[a-z]?(?:-F?\d*[a-z]?)?\b'   # figure/panel references (F7, F8a, F8a-e, F6a-F6e) are citations, not quantities
def run(graph_path, traces_path):
    g=json.load(open(graph_path)); T=json.load(open(traces_path)); N={n['id']:n for n in g['nodes']}
    inn=defaultdict(list); out=defaultdict(list)
    for e in g['edges']: inn[e['dst']].append(e); out[e['src']].append(e)
    sweep_nums=set().union(*[nums(n['label']) for n in g['nodes'] if n['type'].startswith('DES/variable_sweep')]) if any(n['type'].startswith('DES/variable_sweep') for n in g['nodes']) else set()
    report=[]
    for t in T['traces']:
        v={'id':t['id'],'status_in':t['status'],'nets':{}, 'notes':[]}
        if not t.get('walk') or t['status']=='closed': v['verdict']='closed'; report.append(v); continue
        hid=set(t.get('hidden',[])); given=[s['node'] for s in t['walk'] if s['node'] not in hid]
        # target = what is graded: infer -> observation+claim; explain competing -> mechanisms; mechanism -> claim; rejection -> evidence; intervene -> decision
        redacted={r['node'] for r in t.get('redactions',[])}
        target=[t['evidence'][0], t['seed_claim']] if t['root']=='infer' else ([h for h in t.get('hidden',[]) if h not in redacted] if t['subtype']=='competing causes' else [t['seed_claim']] if t['subtype']=='mechanism' or t['root']=='intervene' else t['evidence'][:1])
        target=[x for x in target if x in N]
        # N1 leak: hidden targets vs given text (+question), bigrams and non-sweep numbers
        gtxt=' '.join(N[i]['label'] for i in given)+' '+t.get('question','')
        htxt=' '.join(N[i]['label'] for i in target)
        bg=bigrams(htxt)&bigrams(gtxt); nn=(nums(htxt)&nums(gtxt))-sweep_nums
        # for explain/rejection and mechanism the seed claim is given by design, so drop its own words
        if t['root']=='explain' and t['subtype'] in ('rejection',): bg=set()
        # content-word test (added after ceramic run 1, which missed a question naming the answer's classes):
        # words of the graded targets that no given node uses, and that the question uses anyway
        cw_given=stem(words(' '.join(N[i]['label'] for i in given)))
        cw_hidden=stem(words(htxt))-cw_given
        leak_words=sorted(cw_hidden & stem(words(t.get('question',''))))
        v['nets']['leak']={'bigrams':sorted(' '.join(b) for b in bg),'numbers':sorted(nn),'content_words':leak_words,'pass':len(bg)==0 and len(nn)==0 and not leak_words}
        # N2 disjoint + grader channel withheld
        v['nets']['disjoint']={'pass':not (hid & set(given))}
        gr=t.get('grader',''); held=re.findall(r'channel (\w+)', gr)
        v['nets']['grader_withheld']={'pass':all(h not in given for h in held),'held':held}
        # N3 derivability of the graded target
        if t['root']=='infer':
            ok=bool(N[t['evidence'][0]].get('panel_ids')) and any(e['src']==t['evidence'][0] for e in inn[t['seed_claim']])
            why='observation has panels and evidences the claim'
        elif t['subtype']=='competing causes':
            causes=[e['src'] for e in inn[t['seed_claim']] if e['rel']=='causes']
            ok=all(any(e['dst'] in causes+[t['seed_claim']] or e['src'] in causes for e in (out[m]+inn[m])) for m in target); why='each hidden mechanism connects to a cause or the claim'
        elif t['subtype']=='mechanism':
            ok=any(e['src'] in t['evidence'] for e in inn[t['seed_claim']]); why='evidence edge into the mechanism'
        elif t['root']=='intervene':
            ok=True; why='prediction task: graded by held-out outcome, derivability n/a'
        else:
            ok=bool(N[t['evidence'][0]].get('panel_ids') or N[t['evidence'][0]].get('figs')); why='audit node has a figure'
        v['nets']['derivable']={'pass':ok,'why':why}
        # N4 necessity condition + panels exist (well-formed ids)
        pids=[p for i in t['evidence'] for p in (N[i].get('panel_ids') or [])]
        v['nets']['panels']={'pass':all(re.match(r'.+#F\d+[a-z]?\d?$',p) for p in pids) and (bool(pids) or t['root']!='infer'),'n':len(pids)}
        # N5 linear structure
        lin=t.get('linear',[]); steps={s['step'] for s in lin}
        ok=all(all(d in steps and d<s['step'] for d in s['depends_on']) for s in lin) and all(any(n in s['nodes'] for s in lin) for n in target)
        v['nets']['linear']={'pass':ok}
        # N6 answer-key consistency for rank items graded by an independent channel
        if t['root']=='infer' and t['subtype']=='rank' and held:
            ch=held[0]; series=nums(N[ch]['label']); conds=[c.get('condition') for c in ((N[t['evidence'][0]].get('attrs') or {}).get('panel_conditions') or [])]
            npan=len(N[t['evidence'][0]].get('panel_ids') or [])
            ok=len([x for x in series if '.' in x])>=npan and npan>=3 and len(conds)>0
            v['nets']['key_consistency']={'pass':ok,'why':f'{npan} panels, {len([x for x in series if "." in x])} values in the channel, conditions {"named" if conds else "missing"}'}
        # N7 provenance of the written answer key: every number in it appears in some cited/hidden node label;
        # most content words do too (writer may paraphrase, so a ratio, not equality)
        grader_nodes={x for x in re.findall(r'\b([a-z]\d+)\b', t.get('grader','')+' '+t.get('grading','')) if x in N}
        src_ids=set(t.get('hidden',[]))|set(t.get('evidence',[]))|{t['seed_claim']}|set(t.get('answer_key_nodes',[]))|{n for s_ in t.get('linear',[]) for n in s_['nodes']}|grader_nodes
        src_txt=' '.join(N[i]['label'] for i in src_ids if i in N)
        key=re.sub(r'\b([a-z]\d+)\b',lambda m:'' if m.group(1) in N else m.group(1),t.get('answer_key',''))   # node ids of this graph are citations, not numbers
        key=re.sub(FIGREF,'',key)   # so are figure references: 'On F7' is not an unsourced 7
        kn=nums(key)-sweep_nums; missing_nums=sorted(x for x in kn if x not in nums(src_txt))
        kw=stem(words(key)); cov=(len(kw&stem(words(src_txt)))/len(kw)) if kw else 1.0
        v['nets']['provenance']={'pass':not missing_nums and (cov>=0.5 or len(kn)>=3),'missing_numbers':missing_nums,'word_coverage':round(cov,2),'numbers_checked':len(kn),'rule':'no missing numbers, and word coverage >= 0.5 or at least three sourced numbers','sources':sorted(src_ids)}
        fails=[k for k,r in v['nets'].items() if not r['pass']]
        v['verdict']='survives' if not fails else 'flagged'; v['fails']=fails
        if t['status']=='control': v['verdict']+=' (control)'
        report.append(v)
    return report
if __name__=='__main__':
    rep=run(sys.argv[1], sys.argv[2]); json.dump(rep, open(sys.argv[3],'w'), indent=1)
    for v in rep:
        f=v.get('fails',[]); lk=v.get('nets',{}).get('leak',{})
        extra=(' leak='+', '.join(lk.get('bigrams',[])[:3]+lk.get('numbers',[])[:3])) if lk and not lk['pass'] else ''
        print(f"{v['id']:4s} {v['status_in']:8s} -> {v['verdict']:18s} {('FAIL: '+', '.join(f)) if f else ''}{extra}")
