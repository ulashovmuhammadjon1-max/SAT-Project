import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from figwords import figregion
cl=json.load(open('cleaned.json'))
for qid in sys.argv[1:]:
    print('='*20, qid)
    for l in figregion(qid): print(l)
    print('  CLEANED:', cl[qid])
