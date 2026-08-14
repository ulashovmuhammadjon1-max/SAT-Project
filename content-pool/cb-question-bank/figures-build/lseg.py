import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words, shapes
from dump import fit_axis
from prose import prose
from collections import defaultdict

def analyze(qid):
    ws=words(qid); shs=shapes(qid)
    ps,keep,_=prose(qid)
    ybot=keep[0][0]['y']-4 if keep else 700
    ax=fit_axis(ws,(136,ybot))
    if not ax: print(qid,"NO AXIS"); return
    n,m,b,x1,items,resid=ax
    pv=lambda y:m*y+b
    print(f"### {qid} ticks "+",".join(f"{v:g}" for y,v in items)+f"  (y {items[0][0]:.1f}..{items[-1][0]:.1f})")
    byser=defaultdict(list)
    for s in shs:
        pts=s['pts']
        if len(pts)!=2 or not s['stroke']: continue
        if s['sw']<0.9: continue
        ys=[p[1] for p in pts]
        if max(ys)<136 or min(ys)>ybot: continue
        if abs(pts[0][0]-pts[1][0])<1: continue
        byser[(s['stroke'],round(s['sw'],2))].append(pts)
    for k,v in byser.items():
        v.sort(key=lambda p:min(p[0][0],p[1][0]))
        vals=[]
        for pts in v:
            p=sorted(pts)
            vals.append(p[0]); vals.append(p[1])
        # dedupe consecutive
        seq=[]
        for x,y in vals:
            if not seq or abs(seq[-1][0]-x)>0.5 or abs(seq[-1][1]-y)>0.5:
                seq.append((x,y))
        print(f" SERIES color={k[0]} width={k[1]}: "+" ".join(f"({x:.1f},{pv(y):.2f})" for x,y in seq))

if __name__=='__main__':
    for q in sys.argv[1:]: analyze(q)
