import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe import words, shapes
from dump import fit_axis
from prose import prose

def context(qid):
    ws=words(qid); shs=shapes(qid)
    ps,keep,_=prose(qid)
    ybot=keep[0][0]['y']-4 if keep else 700
    ax=fit_axis(ws,(136,ybot))
    n,m,b,x1,items,resid=ax
    ticks=[v for y,v in items]
    step=abs(ticks[0]-ticks[1])
    # gridlines: thin horizontal 2-pt lines spanning wide
    grid=[]
    for s in shs:
        pts=s['pts']
        if len(pts)==2 and s['stroke'] and abs(pts[0][1]-pts[1][1])<0.4 and abs(pts[0][0]-pts[1][0])>60:
            y=pts[0][1]
            if 136<y<ybot: grid.append(y)
    offs=[]
    for y in grid:
        v=m*y+b
        near=min(ticks,key=lambda t:abs(t-v))
        if abs(v-near)<step*0.3: offs.append(v-near)
    off=sum(offs)/len(offs) if offs else 0.0
    return dict(m=m,b=b,off=off,ticks=ticks,ybot=ybot,ngrid=len(offs))

if __name__=='__main__':
    for q in sys.argv[1:]:
        c=context(q); print(q,'offset=%.4f'%c['off'],'ngrid=',c['ngrid'],'ticks',c['ticks'][:3])
