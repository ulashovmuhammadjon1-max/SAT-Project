import json,subprocess,os,sys
sys.path.insert(0,'.')
from probe import words
from PIL import Image
U='/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45/'
pages=json.load(open('pages.json'))
os.makedirs('crop',exist_ok=True)
DPI=120
for qid,(pdf,pg) in pages.items():
    if os.path.exists(f'crop/{qid}.png'): continue
    ws=words(qid)
    ay=[w['y'] for w in ws if w['t']=='Answer' and w['x0']<20]
    top=136; bot=(ay[0]-6) if ay else 700
    tmp=f'/tmp/_c{qid}'
    subprocess.run(['pdftoppm','-f',str(pg),'-l',str(pg),'-r',str(DPI),'-png','-singlefile',U+pdf,tmp],check=True)
    im=Image.open(tmp+'.png')
    s=DPI/72.0
    im=im.crop((0,int(top*s),im.width,min(im.height,int(bot*s))))
    im.save(f'crop/{qid}.png')
    os.remove(tmp+'.png')
print('ok')
