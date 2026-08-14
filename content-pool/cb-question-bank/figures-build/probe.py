import subprocess, json, re, sys, os
U='/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45/'
D=os.path.dirname(os.path.abspath(__file__))
pages=json.load(open(os.path.join(D,'pages.json')))

def words(qid):
    pdf,pg=pages[qid]
    h=subprocess.run(['pdftotext','-bbox','-f',str(pg),'-l',str(pg),U+pdf,'-'],capture_output=True,text=True).stdout
    out=[]
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',h):
        x0,y0,x1,y1=map(float,m.groups()[:4])
        t=m.group(5).replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&#39;',"'").replace('&quot;','"')
        out.append({'x':(x0+x1)/2,'y':(y0+y1)/2,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'t':t})
    return out

def shapes(qid):
    pdf,pg=pages[qid]
    tmp=f'/tmp/_p{qid}.svg'
    subprocess.run(['pdftocairo','-svg','-f',str(pg),'-l',str(pg),U+pdf,tmp],check=True)
    s=open(tmp).read(); os.remove(tmp)
    body=s.split('</defs>')[-1]
    out=[]
    for m in re.finditer(r'<path ([^>]*?)d="([^"]+)"([^>]*)/>',body):
        attrs=m.group(1)+m.group(3); d=m.group(2)
        fm=re.search(r'fill="rgb\(([\d.]+)%, ([\d.]+)%, ([\d.]+)%\)"',attrs)
        fill=tuple(round(float(fm.group(i))*2.55) for i in (1,2,3)) if fm else None
        sm=re.search(r'stroke="rgb\(([\d.]+)%, ([\d.]+)%, ([\d.]+)%\)"',attrs)
        stroke=tuple(round(float(sm.group(i))*2.55) for i in (1,2,3)) if sm else None
        swm=re.search(r'stroke-width="([\d.]+)"',attrs)
        sw=float(swm.group(1)) if swm else 0.0
        tf=re.search(r'transform="matrix\(([-\d.]+), ([-\d.]+), ([-\d.]+), ([-\d.]+), ([-\d.]+), ([-\d.]+)\)"',attrs)
        pts=[(float(a),float(b)) for a,b in re.findall(r'([-\d.]+) ([-\d.]+)',d)]
        if tf:
            a,b,c,dd,e,f=[float(x) for x in tf.groups()]
            pts=[(a*x+c*y+e, b*x+dd*y+f) for x,y in pts]
            sw=sw*abs(a)
        closed = d.strip().endswith('Z') or 'Z' in d
        out.append({'fill':fill,'stroke':stroke,'sw':sw,'pts':pts,'closed':closed})
    return out

def fmt(shs, xr=None, yr=None):
    lines=[]
    for s in shs:
        xs=[p[0] for p in s['pts']]; ys=[p[1] for p in s['pts']]
        if xr and (max(xs)<xr[0] or min(xs)>xr[1]): continue
        if yr and (max(ys)<yr[0] or min(ys)>yr[1]): continue
        bbox=f"x{min(xs):7.2f}-{max(xs):7.2f} y{min(ys):7.2f}-{max(ys):7.2f}"
        kind='RECT' if len(set(s['pts']))<=4 and s['fill'] else ('POLY' if len(s['pts'])>2 else 'LINE')
        lines.append(f"{kind} {bbox} fill={s['fill']} stroke={s['stroke']} n={len(s['pts'])} " + ("" if kind=='RECT' else " ".join(f"({x:.1f},{y:.1f})" for x,y in s['pts'][:60])))
    return lines

if __name__=='__main__':
    qid=sys.argv[1]
    mode=sys.argv[2] if len(sys.argv)>2 else 'all'
    if mode in ('all','w'):
        print('=== WORDS ===')
        ws=words(qid)
        ws.sort(key=lambda w:(round(w['y']/3,0),w['x']))
        for w in ws: print(f"{w['x']:7.1f} {w['y']:7.1f}  {w['t']}")
    if mode in ('all','r'):
        print('=== SHAPES ===')
        for l in fmt(shapes(qid)): print(l)
