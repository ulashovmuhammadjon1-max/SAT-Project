import subprocess, os, json, re
U='/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45/'
names="""2ed369bf-READING_QUESTION_BANK__Part_1_p1657.pdf
8c8ffed5-101199.pdf
52d3c471-199270.pdf
6d987b2d-270350.pdf
32be1440-350430.pdf
e910bf54-430490.pdf
f2fe21e4-490560.pdf
312b4c6e-560657.pdf
975e5973-657730.pdf
8db208c3-730820.pdf
e9e3a960-820910.pdf
4b1cc719-9101000.pdf
576c8826-10001090.pdf
e5100e35-10901180.pdf
22a8b3c1-11801270.pdf
81335798-12701360.pdf
bcf5f898-13601450.pdf
3a338872-14501540.pdf
357ecf08-15401630.pdf
a5cdff23-16301720.pdf
da9e8563-17201810.pdf
0a346a68-18101900.pdf
f51b6e8d-19001971.pdf""".split()
idx={}
for n in names:
    p=U+n
    if not os.path.exists(p):
        print("MISSING",n); continue
    txt=subprocess.run(['pdftotext','-raw',p,'-'],capture_output=True,text=True).stdout
    pages=txt.split('\f')
    for i,pg in enumerate(pages,1):
        for m in re.finditer(r'Question ID[:\s]+([0-9a-f]{8})', pg):
            idx.setdefault(m.group(1),[]).append([n,i])
    print(n,len(pages))
json.dump(idx,open('figbuild/idx.json','w'))
print("ids",len(idx))
