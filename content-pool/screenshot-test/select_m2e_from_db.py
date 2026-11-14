import json, re, collections, random
C=json.load(open('candidates.json'))
T='/home/user/SAT-Project/content-pool/screenshot-test/'
own=[q for f in ['rw_m1.json','rw_m2_hard.json','math_m1.json','math_m2_hard.json'] for q in json.load(open(T+f))['questions']]
def txt(h): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h or '')).lower()
def grams(t,n=6):
    w=re.findall(r"[a-z0-9’'.]+",txt(t)); return {' '.join(w[i:i+n]) for i in range(len(w)-n+1)}
BOILER=re.compile(r'(while researching a topic, )?a student has taken the following notes:|bulleted notes:',re.I)
def body(q): return BOILER.sub(' ', q.get('passage') or q['stem'])   # passages for R&W; the stem is boilerplate there
OWN=[grams(body(q)) for q in own]
def math_sig(t):  # numbers + operators: template fingerprint
    return set(re.findall(r'\d+(?:\.\d+)?', txt(t)))
OWNM=[math_sig(q['stem']) for q in own if 'choices' in q or 'answerFR' in q]
def audit_ok(h):
    h=re.sub(r'<img[^>]*>','',h or '')
    outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',h,flags=re.S)
    return not re.search(r'\^|sqrt\(|(?<![A-Za-z])pi(?![A-Za-z])|!=|<=|>=|\\(frac|sqrt|pi|le|ge)\b|\btheta\b',outside)
def ok(q):
    if q['type']=='MULTIPLE_CHOICE':
        ch=q['choices'] or []
        if len(ch)!=4 or sum(c['isCorrect'] for c in ch)!=1: return False
        if not all(audit_ok(c['content']) for c in ch): return False
    else:
        try: v=json.loads(q['fr'] or 'null'); assert isinstance(v,list) and v
        except Exception: return False
    blob=(q['stem'] or '')+(q['passage'] or '')
    if re.search(r'\b(graph|figure|shown|histogram|scatterplot)\b',txt(blob)) and not (q['has_img'] or q['p_img'] or '<table' in blob): return False
    if 'TABLE_' in blob or 'cut off' in blob: return False
    allt=blob+''.join(c['content'] for c in (q['choices'] or []))
    if q['subject']=='READING_WRITING' and '*' in re.sub(r'<[^>]+>','',allt): return False   # markdown asterisk renders literally
    if not audit_ok(q['stem']) or not audit_ok(q['passage']): return False
    if q['expl']==0: return False          # only items whose key passed the independent-solve gate
    if q['test'] in ('Test 3','Test 4'): return False   # transcribed keys under review (CLAUDE.md)
    g=grams(body(q))
    if any(len(g&o)>=3 for o in OWN): return False
    return True
exp=lambda q:q['qa']+q['resp']
random.seed(7)
fr_count=[0]
def pick(pool,n,used,chosen_grams,key=exp):
    out=[]
    for q in sorted(pool,key=lambda q:(q['moduleId'] is not None, key(q), q['id'])):
        if len(out)==n: break
        if q['id'] in used: continue
        g=grams(body(q))
        if any(len(g&c)>=3 for c in chosen_grams): continue
        if q['subject']=='MATH' and q['type']!='MULTIPLE_CHOICE' and fr_count[0]>=3: continue
        if q['subject']=='MATH':
            s=math_sig(q['stem'])
            if len(s)>=2 and any(len(s&o)>=max(2,len(s)-0) for o in OWNM+[math_sig(x['stem']) for x in out]): continue
            if any(x['skill']==q['skill'] and len(math_sig(x['stem'])&s)>=2 for x in out): continue
        out.append(q); used.add(q['id']); chosen_grams.append(g)
        if q['subject']=='MATH' and q['type']!='MULTIPLE_CHOICE': fr_count[0]+=1
    assert len(out)==n,(n,len(out))
    return out
import os
EXCLUDE=set(json.load(open('math_excluded.json'))) if os.path.exists('math_excluded.json') else set()
V=[q for q in C if ok(q) and q['id'] not in EXCLUDE]
used=set(); cg=[]
# ---------- Math M2 Easy: 10E / 9M / 3H, FR <= 3
M=[q for q in V if q['subject']=='MATH']
plan=[('EASY','ALG',4),('EASY','ADV',3),('EASY','PSDA',2),('EASY','GT',1),
      ('MEDIUM','ALG',2),('MEDIUM','ADV',3),('MEDIUM','PSDA',2),('MEDIUM','GT',2),('HARD','GT',3)]
math=[]
for dif,dom,n in plan:
    pool=[q for q in M if q['difficulty']==dif and q['dom']==dom]
    got=pick(pool,n,used,cg)
    math+=got
rank={'EASY':0,'MEDIUM':1,'HARD':2}
math.sort(key=lambda q:rank[q['difficulty']])
print("MATH M2E", collections.Counter(q['difficulty'] for q in math), "FR", sum(q['type']!='MULTIPLE_CHOICE' for q in math))
# ---------- R&W M2 Easy: 21E / 6M, block order
R=[q for q in V if q['subject']=='READING_WRITING']
def sub(q):
    s=txt(q['stem'])
    if q['skill']=='CAS-WV': return 1 if 'most nearly mean' in s else 0
    if q['skill']=='INI-CE': return 0 if 'quotation' in s else (2 if re.search(r'support|weaken|undermine',s) else 1)
    return 0
plan=[('CAS-WV','EASY',5),('CAS-TS','EASY',2),('CAS-CT','MEDIUM',1),('INI-CI','EASY',2),
      ('INI-CE','EASY',1),('INI-CE','MEDIUM',2),('INI-IE','EASY',1),('INI-IE','MEDIUM',1),
      ('SEC-BS','EASY',3),('SEC-FS','EASY',2),('SEC-FS','MEDIUM',1),('EOI-TR','EASY',3),('EOI-RS','EASY',2),('EOI-RS','MEDIUM',1)]
rw=[]
for sk,dif,n in plan: rw+=pick([q for q in R if q['skill']==sk and q['difficulty']==dif],n,used,cg)
order={'CAS-WV':1,'CAS-TS':2,'CAS-CT':3,'INI-CI':4,'INI-CE':5,'INI-IE':6,'SEC-BS':7,'SEC-FS':7,'EOI-TR':8,'EOI-RS':9}
rw.sort(key=lambda q:(order[q['skill']],sub(q)))
print("RW M2E", collections.Counter(q['difficulty'] for q in rw), "bank-only", sum(q['moduleId'] is None for q in rw))
print("sources", collections.Counter(q['test'] or 'Question Bank' for q in rw+math))
print("max exposure rw", max(exp(q) for q in rw), "math", max(exp(q) for q in math))
json.dump({"RW_M2E":rw,"MATH_M2E":math},open('m2e_selected.json','w'),ensure_ascii=False)
