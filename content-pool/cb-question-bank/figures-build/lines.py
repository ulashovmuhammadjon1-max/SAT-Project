import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words, shapes
from dump import fit_axis
from prose import prose

def analyze(qid):
    ws=words(qid); shs=shapes(qid)
    ps,keep,_=prose(qid)
    ybot=keep[0][0]['y']-4 if keep else 700
    ax=fit_axis(ws,(136,ybot))
    if not ax: print(qid,"NO AXIS"); return
    n,m,b,x1,items,resid=ax
    pv=lambda y:m*y+b
    print(f"### {qid}  YAXIS "+",".join(f"{v:g}@{y:.1f}" for y,v in items))
    segs=[];marks=[]
    for s in shs:
        pts=s['pts']
        ys=[p[1] for p in pts]; xs=[p[0] for p in pts]
        if max(ys)<136 or min(ys)>ybot: continue
        if len(pts)==2 and s['stroke'] and abs(pts[0][0]-pts[1][0])>1:
            segs.append((pts,s['stroke'],s['sw']))
        elif len(pts)>=3 and (max(xs)-min(xs))<16 and (max(ys)-min(ys))<16:
            marks.append((pts,s['fill'],s['stroke']))
    print("SEGMENTS (polyline vertices, exact data values):")
    for pts,c,sw in sorted(segs,key=lambda s:s[0][0][0]):
        print(f"  c{c} w{sw:.2f} ({pts[0][0]:.1f},{pv(pts[0][1]):.2f}) -> ({pts[1][0]:.1f},{pv(pts[1][1]):.2f})")
    print("MARKERS (bbox center / centroid):")
    for pts,f,st in sorted(marks,key=lambda s:min(p[0] for p in s[0])):
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        u=list(dict.fromkeys(pts))
        cx=sum(p[0] for p in u)/len(u); cy=sum(p[1] for p in u)/len(u)
        print(f"  fill={f} stroke={st} n={len(u)} x={(min(xs)+max(xs))/2:.1f} bboxc={pv((min(ys)+max(ys))/2):.2f} centroid={pv(cy):.2f}")
    print("X LABELS:")
    fw=[w for w in ws if 136<w['y']<ybot]
    fw.sort(key=lambda w:(round(w['y']/4),w['x']))
    line=[];cy=None
    for w in fw:
        if cy is None or abs(w['y']-cy)>4:
            if line: print("  y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))
            line=[];cy=w['y']
        line.append((w['x'],w['t']))
    if line: print("  y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))

if __name__=='__main__':
    for q in sys.argv[1:]: analyze(q)
