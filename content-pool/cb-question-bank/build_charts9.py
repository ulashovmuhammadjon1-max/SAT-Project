# -*- coding: utf-8 -*-
"""Rebuild the 9 flattened R&W graph passages as real figures.

Every value below was measured from the College Board source page rendered at
300 dpi and read visually + by pixel analysis of bar tops / marker centres --
never inferred from the flattened prose string. Three of the nine are
independently corroborated by the CB rationale's own stated readings
(0992bd73: 96/46/55/53/97 ; 303bcc41: 1.3/0.6/1.9/2.7 ; 627d93e3: 0.16/0.18/0.06).

Seven become real <table> markup (CLAUDE.md style block, byte-for-byte).
Two -- 224428ac and 30c3aa98 -- keep a chart, because both hang on the SHAPE of
the drawn trend: "increased overall" / "steadily decreased" / "the difference
remained relatively steady" for the condors, and "the rise ... slowed from 1902
to 1909" for the copper, whose x-axis is drawn as three evenly spaced
categories even though the year gaps are 13 and 7 -- a table would invert that
reading.
"""
import json, os, re
from html import escape

BANK = '/home/user/SAT-Project/content-pool/cb-question-bank'
TSTYLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'

def table(headers, rows):
    out = [TSTYLE, '<thead><tr>']
    out += [TH + h + '</th>' for h in headers]
    out.append('</tr></thead><tbody>')
    for r in rows:
        out.append('<tr>' + ''.join(TD + c + '</td>' for c in r) + '</tr>')
    out.append('</tbody></table>')
    return ''.join(out)

# cb_id -> (title, headers, rows, prose_start, alt_for_chart)
TABLES = {
 '37a49687': (
   'Number of Young Fish Collected at Mangrove Sites in the Egyptian Red Sea '
   'During Three Seasons of 2010',
   ['Season', 'Common silver-biddy', 'Red Sea goatfish', 'Milkfish'],
   [['Winter', '35', '2', '12'],
    ['Spring', '17', '6', '7'],
    ['Fall', '10', '0', '0']],
   'Mangroves are trees or bushes'),

 '0992bd73': (
   'Percent of UK Survey Respondents Who Trust People At Least Somewhat',
   ['Year of study', 'People they meet for the first time (%)',
    'People they know personally (%)'],
   [['2005', '46', '96'],
    ['2018', '55', '97'],
    ['2022', '53', '97']],
   'Social scientists distinguish'),

 'a9ac31e4': (
   'Area of Three Glaciers in the 2016 Swiss Glacier Inventory',
   ['Glacier', 'Area (square km)'],
   [['Gorner', '41.2'],
    ['Fiescher', '30.0'],
    ['Unteraar', '22.7']],
   'To monitor changes to glaciers'),

 '303bcc41': (
   'Top Four Species of Wild Land Mammals by Global Biomass',
   ['Species', 'Global biomass (millions of metric tons)'],
   [['African bush elephant', '1.3'],
    ['eastern gray kangaroo', '0.6'],
    ['wild boar', '1.9'],
    ['white-tailed deer', '2.7']],
   'Global biomass is the total mass'),

 '239d3535': (
   'Census Data for Four Canadian Cities, 1871–1901',
   ['City (population in thousands)', '1871', '1881', '1891', '1901'],
   [['Halifax', '30', '36', '39', '41'],
    ['Montréal', '107', '141', '217', '268'],
    ['Québec City', '60', '62', '63', '69'],
    ['Toronto', '56', '86', '181', '208']],
   'The first national census in Canada'),

 'e99a38ec': (
   'Humility Scores for Participants’ Scenario Responses',
   ['Group', 'Average humility score (higher values = more humility)'],
   [['mistake with learning', '3.12'],
    ['mistake without learning', '2.66'],
    ['control', '2.85']],
   'Jia Hu and colleagues hypothesized'),

 '627d93e3': (
   'Modeled Radial Growth of Sugar Maple Trees',
   ['Climate scenario', 'Radial growth with nitrogen (centimeters per year)',
    'Radial growth without nitrogen (centimeters per year)'],
   [['current', '0.21', '0.16'],
    ['moderate change', '0.185', '0.15'],
    ['extreme change', '0.06', '0.04']],
   'Inés Ibáñez and colleagues studied'),
}

CHARTS = {
 '224428ac': ('California Condor Populations 2014–2020',
   'The California Condor Recovery Program',
   'Line graph titled "California Condor Populations 2014-2020." The horizontal '
   'axis is labeled "Year" and is marked 2014 through 2020; the vertical axis is '
   'labeled "Number of condors" and is marked from 0 to 400. One line is labeled '
   '"wild" and one is labeled "captive."'),
 '30c3aa98': ('Copper Production for Three States, 1889-1909',
   'Copper had been mined in the US',
   'Line graph titled "Copper Production for Three States, 1889-1909." The '
   'horizontal axis is labeled "Year" and is marked 1889, 1902, and 1909; the '
   'vertical axis is labeled "Yearly copper production (in millions of pounds)" '
   'and is marked from 0 to 400. The three lines are labeled "Montana," '
   '"Arizona," and "Michigan."'),
}

# ------------------------------------------------------------------ load
src = {}
for f in ('rw_tests_6_10.json', 'rw_tests_11_15.json'):
    for t in json.load(open(os.path.join(BANK, f))):
        for m in t['modules']:
            for q in m['questions']:
                if q.get('cb_id'):
                    src[q['cb_id']] = q

imgs = json.load(open(os.path.join(BANK, 'charts9_img.json')))

def prose_of(cb_id, start):
    p = src[cb_id]['passage']
    i = p.find(start)
    assert i > 0, (cb_id, 'prose start not found')
    return p[i:].strip()

out = []
for cb_id, (title, headers, rows, start) in TABLES.items():
    prose = prose_of(cb_id, start)
    passage = ('<p><strong>' + title + '</strong></p>'
               + table(headers, rows)
               + '<p>' + prose + '</p>')
    out.append({'cb_id': cb_id, 'passage': passage, 'kind': 'table'})

for cb_id, (title, start, alt) in CHARTS.items():
    prose = prose_of(cb_id, start)
    uri = imgs[cb_id]
    passage = ('<p><strong>' + title + '</strong></p>'
               + '<p><img src="' + uri + '" alt="' + escape(alt, quote=True)
               + '" style="max-width:100%;height:auto;" /></p>'
               + '<p>' + prose + '</p>')
    out.append({'cb_id': cb_id, 'passage': passage, 'kind': 'chart',
                'image': uri})

order = ['37a49687', '0992bd73', 'a9ac31e4', '303bcc41', '239d3535',
         'e99a38ec', '224428ac', '30c3aa98', '627d93e3']
out.sort(key=lambda d: order.index(d['cb_id']))
json.dump(out, open(os.path.join(BANK, 'charts9.json'), 'w'),
          ensure_ascii=False, indent=1)
print('wrote charts9.json with', len(out), 'entries')
for d in out:
    print(' ', d['cb_id'], d['kind'], 'passage', len(d['passage']), 'chars')
