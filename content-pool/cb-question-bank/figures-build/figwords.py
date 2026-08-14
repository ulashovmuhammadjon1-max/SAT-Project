import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words
from prose import lines_of, prose

def figregion(qid):
    ws=words(qid)
    ps,keep,_f=prose(qid)
    ytop=136
    ybot=keep[0][0]['y']-4 if keep else 700
    L=[l for l in lines_of(ws) if ytop<l[0]['y']<ybot]
    out=[]
    for l in L:
        out.append(("  y%.1f | "%l[0]['y'])+" | ".join(f"{w['t']}@{w['x0']:.0f}-{w['x1']:.0f}" for w in l))
    return out

if __name__=='__main__':
    cat=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cat.json')))
    ids=sys.argv[1:] or list(cat)
    for qid in ids:
        print('='*10, qid, cat.get(qid))
        for l in figregion(qid): print(l)
