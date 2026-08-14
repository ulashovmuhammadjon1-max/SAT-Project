import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words, shapes
from dump import fit_axis
from prose import prose

def analyze(qid, maxsize=16):
    ws=words(qid); shs=shapes(qid)
    ps,keep,_=prose(qid)
    ybot=keep[0][0]['y']-4 if keep else 700
    ax=fit_axis(ws,(136,ybot))
    n,m,b,x1,items,resid=ax
    pv=lambda y:m*y+b
    print(f"### {qid} ticks "+",".join(f"{v:g}" for y,v in items))
    seen=set(); out=[]
    for s in shs:
        pts=s['pts']; xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        w=max(xs)-min(xs); h=max(ys)-min(ys)
        if len(pts)<3 or w>maxsize or h>maxsize or w<2 or h<2: continue
        if max(ys)<136 or min(ys)>ybot: continue
        key=(round(min(xs),1),round(min(ys),1),round(w,1),round(h,1))
        if key in seen: continue
        seen.add(key)
        u=list(dict.fromkeys(pts))
        out.append(((min(xs)+max(xs))/2, pv((min(ys)+max(ys))/2), len(u), s['fill'], s['stroke'], round(w,1), round(h,1)))
    for x,v,nn,f,st,w,h in sorted(out):
        print(f"  x={x:7.1f} val={v:9.2f} verts={nn} fill={f} stroke={st} size={w}x{h}")

if __name__=='__main__':
    for q in sys.argv[1:]: analyze(q)
