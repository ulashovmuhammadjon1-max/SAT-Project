import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words, shapes
from calib import context
from collections import defaultdict

def analyze(qid):
    c=context(qid); m,b,off,ybot=c['m'],c['b'],c['off'],c['ybot']
    pv=lambda y:m*y+b-off
    shs=shapes(qid); ws=words(qid)
    print(f"### {qid} ticks {c['ticks'][0]:g}..{c['ticks'][-1]:g} off={off:.3f}")
    # segments
    byser=defaultdict(list)
    for s in shs:
        pts=s['pts']
        if len(pts)!=2 or not s['stroke'] or s['sw']<0.9: continue
        ys=[p[1] for p in pts]
        if max(ys)<136 or min(ys)>ybot: continue
        if abs(pts[0][0]-pts[1][0])<1: continue
        byser[(s['stroke'],round(s['sw'],2))].append(sorted(pts))
    for k,v in byser.items():
        v.sort()
        seq=[]
        for p in v:
            for x,y in p:
                if not seq or abs(seq[-1][0]-x)>0.5 or abs(seq[-1][1]-y)>0.5: seq.append((x,y))
        print(f" LINE c{k[0]} w{k[1]}: "+" ".join(f"({x:.0f},{pv(y):.2f})" for x,y in seq))
    # markers
    seen=set(); mk=defaultdict(list)
    for s in shs:
        pts=s['pts']; xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        w=max(xs)-min(xs); h=max(ys)-min(ys)
        if len(pts)<3 or w>16 or h>16 or w<2 or h<2: continue
        if max(ys)<136 or min(ys)>ybot: continue
        key=(round(min(xs),1),round(min(ys),1))
        if key in seen: continue
        seen.add(key)
        u=len(dict.fromkeys(pts))
        mk[(u,s['fill'],round(w,1))].append(((min(xs)+max(xs))/2, pv((min(ys)+max(ys))/2)))
    for k,v in sorted(mk.items()):
        v.sort()
        print(f" MARK verts={k[0]} fill={k[1]} sz={k[2]}: "+" ".join(f"({x:.0f},{val:.2f})" for x,val in v))
    # x labels
    fw=[w for w in ws if 136<w['y']<ybot]
    fw.sort(key=lambda w:(round(w['y']/4),w['x']))
    line=[];cy=None
    print(" TEXT:")
    for w in fw:
        if cy is None or abs(w['y']-cy)>4:
            if line: print("   y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))
            line=[];cy=w['y']
        line.append((w['x'],w['t']))
    if line: print("   y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))

if __name__=='__main__':
    for q in sys.argv[1:]: analyze(q)
