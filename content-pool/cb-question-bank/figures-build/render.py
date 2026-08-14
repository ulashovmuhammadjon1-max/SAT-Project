import json,subprocess,os
U='/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45/'
idx=json.load(open('figbuild/idx.json'))
d=json.load(open('/home/user/SAT-Project/content-pool/cb-question-bank/bank_parsed.json'))
nf=[q for q in d if q.get('needs_figure')]
os.makedirs('figbuild/png',exist_ok=True)
m={}
for q in nf:
    pdf,pg=idx[q['id']][0]
    m[q['id']]=[pdf,pg]
    out=f"figbuild/png/{q['id']}"
    if not os.path.exists(out+'.png'):
        subprocess.run(['pdftoppm','-f',str(pg),'-l',str(pg),'-r','110','-png','-singlefile',U+pdf,out],check=True)
json.dump(m,open('figbuild/pages.json','w'),indent=1)
print('done',len(m))
