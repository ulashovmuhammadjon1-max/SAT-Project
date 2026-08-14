import json,os,sys
sys.path.insert(0,'.')
from probe import words, shapes
from collections import defaultdict

def num(t):
    t=t.replace(',','').replace('%','').replace('$','')
    if t.endswith('.'): t=t[:-1]
    try: return float(t)
    except: return None

def fit_axis(ws, region):
    """find right-aligned column of >=3 numbers => y axis"""
    nums=[(w,num(w['t'])) for w in ws if num(w['t']) is not None and region[0]<=w['y']<=region[1]]
    byx=defaultdict(list)
    for w,v in nums: byx[round(w['x1'],0)].append((w['y'],v))
    best=None
    for x1,items in byx.items():
        if len(items)>=3:
            items=sorted(items)
            ys=[i[0] for i in items]; vs=[i[1] for i in items]
            n=len(ys); sx=sum(ys); sy=sum(vs); sxx=sum(y*y for y in ys); sxy=sum(y*v for y,v in zip(ys,vs))
            den=(n*sxx-sx*sx)
            if den==0: continue
            m=(n*sxy-sx*sy)/den; b=(sy-m*sx)/n
            resid=max(abs(m*y+b-v) for y,v in zip(ys,vs))
            span=max(vs)-min(vs)
            if span==0: continue
            if resid/span<0.02 and (best is None or len(items)>best[0]):
                best=(len(items),m,b,x1,items,resid)
    return best

def analyze(qid):
    ws=words(qid); shs=shapes(qid)
    region=(136, max([w['y'] for w in ws], default=700))
    bars=[]; polys=[]; rules=[]; dots=[]
    for s in shs:
        xs=[p[0] for p in s['pts']]; ys=[p[1] for p in s['pts']]
        w=max(xs)-min(xs); h=max(ys)-min(ys)
        if max(ys)<130: continue
        if s['fill'] and s['stroke'] and len(s['pts'])>=5 and w>2 and h>1 and len(set(round(p[0],1) for p in s['pts']))<=2:
            bars.append({'x0':min(xs),'x1':max(xs),'y0':min(ys),'y1':max(ys),'c':s['fill']})
        elif s['fill'] and not s['stroke'] and (w<2 or h<2):
            rules.append((min(xs),max(xs),min(ys),max(ys)))
        elif len(s['pts'])>2 and (w>5 and h>2):
            polys.append(s)
        elif s['fill'] and w<=12 and h<=12 and len(s['pts'])>4:
            dots.append({'x':(min(xs)+max(xs))/2,'y':(min(ys)+max(ys))/2,'c':s['fill'],'n':len(s['pts'])})
    ax=fit_axis(ws,region)
    L=[]
    L.append(f"### {qid}  bars={len(bars)} polys={len(polys)} dots={len(dots)} rules={len(rules)}")
    if ax:
        n,m,b,x1,items,resid = ax
        L.append(f"YAXIS x1={x1} ticks="+",".join(f"{v:g}@{y:.1f}" for y,v in items)+f"  fit v={m:.5f}*y+{b:.4f} resid={resid:.4f}")
        pv=lambda y: m*y+b
        base=None
        if bars:
            from collections import Counter
            base=Counter(round(bb['y1'],1) for bb in bars).most_common(1)[0][0]
            L.append(f"BARS (baseline y={base}, value0={pv(base):.2f}):")
            for bb in sorted(bars,key=lambda r:r['x0']):
                L.append(f"  x{bb['x0']:7.2f}-{bb['x1']:7.2f} c{bb['c']} top={pv(bb['y0']):10.3f} bot={pv(bb['y1']):10.3f} H={pv(bb['y0'])-pv(bb['y1']):10.3f}")
        for i,s in enumerate(polys):
            pts=s['pts']
            L.append(f"POLY{i} fill={s['fill']} stroke={s['stroke']} n={len(pts)}: "+" ".join(f"({x:.1f},{pv(y):.2f})" for x,y in pts[:80]))
        if dots:
            L.append("DOTS: "+" ".join(f"({d['x']:.1f},{pv(d['y']):.2f}){d['c']}" for d in sorted(dots,key=lambda d:d['x'])))
    else:
        L.append("NO Y AXIS FIT")
        for bb in sorted(bars,key=lambda r:r['x0'])[:40]:
            L.append(f"  bar x{bb['x0']:7.2f}-{bb['x1']:7.2f} y{bb['y0']:7.2f}-{bb['y1']:7.2f} c{bb['c']}")
        for i,s in enumerate(polys[:20]):
            L.append(f"POLY{i} fill={s['fill']} stroke={s['stroke']}: "+" ".join(f"({x:.1f},{y:.1f})" for x,y in s['pts'][:60]))
        if dots: L.append("DOTS: "+" ".join(f"({d['x']:.1f},{d['y']:.1f})" for d in sorted(dots,key=lambda d:d['x'])[:60]))
    # words in figure region, grouped by line
    L.append("WORDS:")
    fw=[w for w in ws if w['y']>136]
    fw.sort(key=lambda w:(round(w['y']/4),w['x']))
    line=[];cy=None
    for w in fw:
        if cy is None or abs(w['y']-cy)>4:
            if line: L.append("  y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))
            line=[];cy=w['y']
        line.append((w['x'],w['t']))
    if line: L.append("  y%.1f | "%cy+" | ".join(f"{t}@{x:.0f}" for x,t in line))
    return "\n".join(L)

if __name__=='__main__':
    pages=json.load(open('pages.json'))
    os.makedirs('geo',exist_ok=True)
    for qid in (sys.argv[1:] or pages):
        try:
            open(f'geo/{qid}.txt','w').write(analyze(qid))
        except Exception as e:
            open(f'geo/{qid}.txt','w').write(f"ERROR {e}")
            print(qid,'ERR',e)
    print('done')
