import json,sys,re,os,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from prose import prose

BANK=json.load(open('/home/user/SAT-Project/content-pool/cb-question-bank/bank_parsed.json'))
BY={q['id']:q for q in BANK}

def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=s.replace('—','-').replace('–','-').replace('−','-')
    return re.sub(r'\s+','',s)

# qid -> literal prefix of the real passage prose; everything before it in the
# extracted question string is shredded figure text.
OVERRIDE={
 '6a6bbac3':'Studying tools unearthed at a cave site',
 'af125459':'Two kinds of clamshell tools used by Neanderthals',
}

def cleaned(qid):
    orig=BY[qid]['question']
    if qid in OVERRIDE:
        n=norm(orig); p=n.find(norm(OVERRIDE[qid]))
        if p<0: return None,norm(OVERRIDE[qid]),n
        idx=[i for i,ch in enumerate(orig) if norm(ch)]
        return orig[idx[p]:].strip(), None, None
    ps,_,_fig=prose(qid)
    target=norm(" ".join(ps))
    # index map
    idx=[]; n=[]
    for i,ch in enumerate(orig):
        c=norm(ch)
        if c:
            n.append(c); idx.append(i)
    N="".join(n)
    p=N.find(target)
    if p<0: return None, target, N
    start=idx[p]; end=idx[p+len(target)-1]+1
    return orig[start:end].strip(), target, N

if __name__=='__main__':
    pages=json.load(open('pages.json'))
    bad=[]
    for qid in pages:
        try:
            c,t,N=cleaned(qid)
        except Exception as e:
            bad.append((qid,'EXC '+str(e))); continue
        if c is None: bad.append((qid,'NOMATCH')); continue
        # residual shred check: 8+ consecutive bare numbers
        if re.search(r'(?:(?:[\d,\.]+)\s+){7}[\d,\.]+', c): bad.append((qid,'SHRED?'))
    print('problems:',bad)
