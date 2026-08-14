import json,subprocess,os,sys
sys.path.insert(0,'.')
from probe import words
from prose import prose
from PIL import Image
U='/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45/'
pages=json.load(open('pages.json'))
cat=json.load(open('cat.json'))
os.makedirs('fig',exist_ok=True)
DPI=120
for qid,(pdf,pg) in pages.items():
    if cat[qid]=='TABLE': continue
    if os.path.exists(f'fig/{qid}.png'): continue
    ws=words(qid)
    ps,keep,_=prose(qid)
    bot=(keep[0][0]['y']-4) if keep else 700
    tmp=f'/tmp/_f{qid}'
    subprocess.run(['pdftoppm','-f',str(pg),'-l',str(pg),'-r',str(DPI),'-png','-singlefile',U+pdf,tmp],check=True)
    im=Image.open(tmp+'.png'); s=DPI/72.0
    im=im.crop((0,int(138*s),im.width,min(im.height,int(bot*s))))
    im.save(f'fig/{qid}.png'); os.remove(tmp+'.png')
print('ok')
