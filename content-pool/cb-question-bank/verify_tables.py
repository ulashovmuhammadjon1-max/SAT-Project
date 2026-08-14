# -*- coding: utf-8 -*-
"""Independent verification of tables.json against the flattened originals."""
import json, re, os, sys

BANK = '/home/user/SAT-Project/content-pool/cb-question-bank'
tables = json.load(open(os.path.join(BANK, 'tables.json')))
charts = json.load(open(os.path.join(BANK, 'tables_charts.json')))['charts']

orig = {}
for f in ['rw_tests_6_10.json', 'rw_tests_11_15.json']:
    for t in json.load(open(os.path.join(BANK, f))):
        for m in t['modules']:
            for q in m['questions']:
                orig[q['cb_id']] = q

NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
WORD = re.compile(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'’]*")
fail = []

STYLE_T = '<table style="border-collapse:collapse;margin:0.75rem 0;">'
STYLE_TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">'
STYLE_TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'


def strip_tags(s):
    return re.sub(r'<[^>]+>', ' ', s)


ids = [e['cb_id'] for e in tables]
assert len(ids) == len(set(ids)), 'duplicate cb_id in tables.json'

for e in tables:
    cid, new = e['cb_id'], e['passage']
    old = orig[cid]['passage']

    # 1. structure
    if new.count('<table') != 1 or new.count('</table>') != 1:
        fail.append(cid + ': table tags unbalanced')
    if STYLE_T not in new:
        fail.append(cid + ': wrong <table> style block')
    if new.count('<th ') and STYLE_TH not in new:
        fail.append(cid + ': wrong <th> style block')
    if STYLE_TD not in new:
        fail.append(cid + ': wrong <td> style block')
    if new.count('<tr>') != new.count('</tr>'):
        fail.append(cid + ': <tr> unbalanced')
    if new.count('<td') != new.count('</td>') or new.count('<th') != new.count('</th>'):
        fail.append(cid + ': cell tags unbalanced')

    rows = re.findall(r'<tr>(.*?)</tr>', new, re.S)
    ncol = rows[0].count('<th')
    if ncol < 2:
        fail.append(cid + ': header row has %d cells' % ncol)
    for r in rows[1:]:
        if r.count('<td') != ncol:
            fail.append(cid + ': body row has %d cells, header has %d' % (r.count('<td'), ncol))
    if len(rows) < 2:
        fail.append(cid + ': no body rows')

    # 2. caption paragraph above the table
    if not re.match(r'^<p><strong>.+?</strong></p>' + re.escape(STYLE_T), new):
        fail.append(cid + ': missing/misplaced <p><strong>title</strong></p> above table')

    # 3. numeric tokens preserved with multiplicity
    ob, nb = NUM.findall(strip_tags(old)), NUM.findall(strip_tags(new))
    for tok in set(ob):
        if nb.count(tok) < ob.count(tok):
            fail.append('%s: numeric token %r %dx -> %dx' % (cid, tok, ob.count(tok), nb.count(tok)))

    # 4. word tokens preserved (catches a dropped row label or prose sentence)
    # the flattened originals contain PDF-extraction artefacts "Bendire’ s" /
    # "area’ s"; the rebuilt table restores the apostrophe-s as printed in the
    # source PDF, so normalise that before comparing words.
    ow = WORD.findall(re.sub(r'’\s+s\b', '’s', strip_tags(old)))
    nw = WORD.findall(strip_tags(new))
    ow_l = [w.lower() for w in ow]
    nw_l = [w.lower() for w in nw]
    for w in set(ow_l):
        if nw_l.count(w) < ow_l.count(w):
            fail.append('%s: word %r %dx -> %dx' % (cid, w, ow_l.count(w), nw_l.count(w)))

    # 5. minus signs preserved
    if old.count('−') != new.count('−'):
        fail.append(cid + ': U+2212 count changed')

    # 6. trailing prose present and wrapped
    if not new.rstrip().endswith('</p>'):
        fail.append(cid + ': does not end with </p>')
    tail = new.split('</table>', 1)[1]
    if not tail.startswith('<p>') or len(strip_tags(tail).split()) < 10:
        fail.append(cid + ': prose after table missing or too short')

# charts must not be in tables.json, and must be real targets
for c in charts:
    if c['cb_id'] in ids:
        fail.append(c['cb_id'] + ': listed as both chart and table')
    if c['cb_id'] not in orig:
        fail.append(c['cb_id'] + ': chart id not in bank')

print('tables: %d   charts: %d   total: %d' % (len(tables), len(charts), len(tables) + len(charts)))
if fail:
    print('FAILURES (%d):' % len(fail))
    for f in fail:
        print('  ' + f)
    sys.exit(1)
print('ALL CHECKS PASSED')
