import json,sys,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words

def lines_of(ws, ytol=4.0):
    ws=sorted(ws,key=lambda w:(w['y'],w['x']))
    out=[];cur=[]
    for w in ws:
        if cur and abs(w['y']-cur[0]['y'])>ytol:
            out.append(sorted(cur,key=lambda a:a['x'])); cur=[]
        cur.append(w)
    if cur: out.append(sorted(cur,key=lambda a:a['x']))
    return out

def is_prose(l):
    if len(l)<5: return False
    if min(w['x0'] for w in l)>30: return False
    gaps=[l[i+1]['x0']-l[i]['x1'] for i in range(len(l)-1)]
    return max(gaps)<20

def prose(qid, ws=None):
    ws=ws or words(qid)
    ans=[w for w in ws if w['t']=='Answer' and w['x0']<25]
    ay=ans[0]['y']
    L=[l for l in lines_of(ws) if 136 < l[0]['y'] < ay-3]
    i0=None
    for i,l in enumerate(L):
        if is_prose(l): i0=i; break
    if i0 is None: return [], [], L
    keep=L[i0:]
    paras=[]; cur=[]; prev=None
    for l in keep:
        if prev is not None and l[0]['y']-prev>18:
            paras.append(" ".join(cur)); cur=[]
        cur.append(" ".join(w['t'] for w in l))
        prev=l[0]['y']
    if cur: paras.append(" ".join(cur))
    return paras, keep, L[:i0]

if __name__=='__main__':
    for qid in sys.argv[1:]:
        ps,_,fig=prose(qid)
        print('==',qid)
        for p in ps: print('  P:',p)
