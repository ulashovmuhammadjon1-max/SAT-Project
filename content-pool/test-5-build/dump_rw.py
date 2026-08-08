import json, re, sys, html
d=json.load(open('test5_rw.json'))
mod=sys.argv[1]; lo=int(sys.argv[2]); hi=int(sys.argv[3])
def txt(s):
    s=re.sub(r'<br\s*/?>','\n',s or '')
    s=re.sub(r'</(p|li|tr)>','\n',s)
    s=re.sub(r'<li>','  - ',s)
    s=re.sub(r'</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    return html.unescape(s).strip()
for q in d[mod]:
    if not (lo<=q['order']<=hi): continue
    print(f"### Q{q['order']}  [{q['skill']}]  recorded={q['correct']}")
    p=txt(q['passageHtml'])
    print("P:", p[:900])
    print("S:", txt(q['stem'])[:220])
    for c in q['choices']:
        print(f"   {c['label']}) {txt(c['content'])[:190]}")
    print()
