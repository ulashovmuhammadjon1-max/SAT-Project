import sys,re,json,os
from probe import words, shapes

def num(t):
    t=t.replace(',','').replace('%','').replace('$','')
    try: return float(t)
    except: return None

def analyze(qid, verbose=True):
    ws=words(qid); shs=shapes(qid)
    bars=[]
    for s in shs:
        if s['fill'] and s['stroke'] and len(s['pts'])>=5:
            xs=[p[0] for p in s['pts']]; ys=[p[1] for p in s['pts']]
            w=max(xs)-min(xs); h=max(ys)-min(ys)
            if w>2 and h>1 and len(set([round(p[0],1) for p in s['pts']]))<=2:
                bars.append({'x0':min(xs),'x1':max(xs),'y0':min(ys),'y1':max(ys),'c':s['fill']})
    # numeric words -> potential axis ticks
    nums=[(w,num(w['t'])) for w in ws if num(w['t']) is not None]
    print(f"--- {qid} :: bars={len(bars)}")
    # y axis candidates: numbers sharing same x1 (right-aligned)
    from collections import defaultdict
    byx=defaultdict(list)
    for w,v in nums: byx[round(w['x1'],0)].append((w['y'],v,w['t']))
    axis=None
    for x1,items in sorted(byx.items(), key=lambda kv:-len(kv[1])):
        if len(items)>=3:
            axis=(x1,sorted(items))
            break
    if axis:
        x1,items=axis
        print(f"Y-AXIS ticks at x1={x1}: "+", ".join(f"{v}@{y:.1f}" for y,v,t in items))
        ys=[i[0] for i in items]; vs=[i[1] for i in items]
        n=len(ys); sx=sum(ys); sy=sum(vs); sxx=sum(y*y for y in ys); sxy=sum(y*v for y,v in zip(ys,vs))
        m=(n*sxy-sx*sy)/(n*sxx-sx*sx); b=(sy-m*sx)/n
        pred=lambda y: m*y+b
        resid=max(abs(pred(y)-v) for y,v in zip(ys,vs))
        print(f"fit: value = {m:.4f}*y + {b:.3f}   max residual {resid:.4f}")
        for bar in sorted(bars,key=lambda r:r['x0']):
            print(f"  bar x{bar['x0']:7.2f}-{bar['x1']:7.2f} c{bar['c']}  top={pred(bar['y0']):9.2f} bot={pred(bar['y1']):9.2f}  VAL={pred(bar['y0'])-pred(bar['y1']):9.2f}")
    else:
        print("no numeric y-axis found")
        for bar in sorted(bars,key=lambda r:r['x0']):
            print(f"  bar x{bar['x0']:7.2f}-{bar['x1']:7.2f} y{bar['y0']:7.2f}-{bar['y1']:7.2f} c{bar['c']}")
    return ws,shs,bars

if __name__=='__main__':
    analyze(sys.argv[1])
