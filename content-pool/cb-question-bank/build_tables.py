# -*- coding: utf-8 -*-
"""Rebuild flattened R&W data tables as real <table> HTML.

Every table below was transcribed from the College Board source PDF page rendered
to PNG and read visually (see MANIFEST in the agent report) - never inferred from
the flattened prose string alone.
"""
import json, re, os, sys

BANK = '/home/user/SAT-Project/content-pool/cb-question-bank'
OUT = os.path.join(BANK, 'tables.json')

TSTYLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'

MINUS = '−'
RSQUO = '’'
NDASH = '–'
DEG = '&deg;'

# cb_id -> (title, headers, rows, prose_start_substring)
SPEC = {
 'f8244f7c': (
   'North American Thrasher Mean Bill Size and Habitat Temperature Range',
   ['Species', 'Mean bill surface area (cm<sup>2</sup>)',
    'Mean maximum temperature of warmest month (' + DEG + 'C)',
    'Mean minimum temperature of coldest month (' + DEG + 'C)'],
   [['Brown thrasher', '1.86', '30.40', MINUS + '4.29'],
    ['Bendire' + RSQUO + 's thrasher', '1.98', '36.57', '0.24'],
    ['Long-billed thrasher', '2.24', '35.27', '8.82'],
    ['Cozumel thrasher', '2.28', '33.27', '18.21'],
    ['Ocellated thrasher', '3.26', '27.56', '5.45']],
   'It has been hypothesized'),

 '0b96fa93': (
   'Maximum Height of Maple Trees When Fully Grown',
   ['Tree type', 'Maximum height (feet)', 'Native to North America'],
   [['Sugar maple', '75', 'yes'],
    ['Silver maple', '70', 'yes'],
    ['Red maple', '60', 'yes'],
    ['Japanese maple', '25', 'no'],
    ['Norway maple', '50', 'no']],
   'For a school project'),

 '95388117': (
   'Land Area Covered by Native Flowering Plants at a Site in Antarctica',
   ['Species', 'Area covered in 2009 (in square meters)',
    'Area covered in 2018 (in square meters)',
    'Percent increase in area covered from 2009 to 2018'],
   [['<em>Deschampsia antarctica</em>', '1,230', '1,576', '28%'],
    ['<em>Colobanthus quitensis</em>', '6.9', '10.7', '55%']],
   'The only flowering plant species native to Antarctica'),

 '014b3394': (
   'Average Number and Duration of Torpor Bouts and Arousal Episodes for '
   'Alaska Marmots and Arctic Ground Squirrels, 2008' + NDASH + '2011',
   ['Feature', 'Alaska marmots', 'Arctic ground squirrels'],
   [['torpor bouts', '12', '10.5'],
    ['duration per bout', '13.81 days', '16.77 days'],
    ['arousal episodes', '11', '9.5'],
    ['duration per episode', '21.2 hours', '14.2 hours']],
   'When hibernating'),

 'ede3f942': (
   'Total Areas of Five Tribal Nations in California',
   ['Tribal nation', 'Location', 'Area (square miles)'],
   [['Hoopa Valley Tribe', 'Northern California', '141.68'],
    ['La Jolla Band of Luiseño Indians', 'Southern California', '13.50'],
    ['Pauma Band of Luiseño Mission Indians', 'Southern California', '9.36'],
    ['Agua Caliente Band of Cahuilla Indians', 'Northern California', '53.68'],
    ['Los Coyotes Band of Cahuilla and Cupeño Indians', 'Southern California', '39.21']],
   'In what is now the state of California'),

 '55df0275': (
   'Ablation Rates for Three Elements in Cosmic Dust, by Dust Source',
   ['Element', 'SPC', 'AST', 'HTC', 'OCC'],
   [['iron', '20%', '28%', '90%', '98%'],
    ['potassium', '44%', '74%', '97%', '100%'],
    ['sodium', '45%', '75%', '99%', '100%']],
   'Earth' + RSQUO + 's atmosphere is bombarded'),

 '84136d69': (
   'Five of the Responses to Survey about Actions to Conserve Energy',
   ['Action', 'Action category', 'Percentage of respondents selecting action (%)'],
   [['Use efficient cars/hybrids', 'efficiency', '2.8'],
    ['Change thermostat setting', 'curtailment', '6.3'],
    ['Use bike or public transportation instead of car', 'curtailment', '12.9'],
    ['Use efficient light bulbs', 'efficiency', '3.6'],
    ['Turn off lights', 'curtailment', '19.6']],
   'In a survey of public perceptions'),

 '81498c6a': (
   'Average Prices Received by US Growers for Citrus Fruits, 2020' + NDASH +
   '2021 (dollars per box)',
   ['Fruit', 'June 2020', 'June 2021', 'July 2020', 'July 2021'],
   [['Grapefruits', '$13.80', '$23.72', '$16.13', '$22.98'],
    ['Oranges', '$16.15', '$11.09', '$15.53', '$13.79'],
    ['Lemons', '$19.50', '$28.94', '$21.01', '$31.78']],
   'An employee of a citrus grower'),

 'a95075c5': (
   'Mean Ratings for Patients after 21 Days',
   ['Measure', 'Mean rating for participants aware of taking a placebo',
    'Mean rating for participants in the control group'],
   [['Global improvement', '5.0', '3.9'],
    ['Symptom severity reduction', '92.00', '46.00'],
    ['Quality of life improvement', '11.4', '5.4']],
   'To test whether a medication is effective'),

 '7c21b4b5': (
   'Survey Results for Two Online Account Sign-in Methods',
   ['Sign-in method', 'Percent of participants in the UK who chose method',
    'Percent of participants in Japan who chose method',
    'Percent of participants in India who chose method'],
   [['Biometrics (for example, a face scan)', '33', '29', '22'],
    ['Onetime passcodes', '16', '8', '25']],
   'A survey listed methods'),

 'faaf484f': (
   'Percent of Residents of City Areas in Favor of Adding More Bike Paths',
   ['City Area', 'Percent of area' + RSQUO + 's residents in favor of adding more bike paths'],
   [['North East', '12%'],
    ['North Central', '26%'],
    ['North West', '46%'],
    ['South West', '88%'],
    ['South Central', '33%']],
   'A city' + RSQUO + 's Parks and Recreation department'),

 'c4bee178': (
   'Moons of Dwarf Planets',
   ['Dwarf planet name', 'Number of moons', 'Name of moons'],
   [['Haumea', '2', 'Hi‘iaka, Namaka'],
    ['Ceres', '0', 'N/A'],
    ['Makemake', '1', 'MK 2'],
    ['Eris', '1', 'Dysnomia'],
    ['Pluto', '5', 'Charon, Nix, Kerberos, Styx, Hydra']],
   'Like Earth, some dwarf planets'),

 'd6e97054': (
   'Four Studies of Food Choices in Various Contexts',
   ['Location', 'Food choices related to...', 'Study population', 'Number of participants'],
   [['Canada', 'sports', 'adults', '17'],
    ['United States', 'school', 'children', '44'],
    ['India', 'community', 'adolescents and adults', '94'],
    ['Ghana and Kenya', 'food shops', 'adolescents', '142']],
   'The table shows information from four studies'),

 '0ec15b5a': (
   'Incorporated and Unincorporated Self-Employment Rates in Four Occupational Fields, 2015',
   ['Occupational field', 'Incorporated self-employment rate',
    'Unincorporated self-employment rate'],
   [['Construction and resource extraction', '4.4%', '14.8%'],
    ['Installation, maintenance, and repair', '2.7%', '6.2%'],
    ['Management, business, and financial services', '8.9%', '9.7%'],
    ['Sales and related', '5.8%', '7.8%']],
   'Self-employed workers'),

 'a0203977': (
   'Annual Spending by International Tourists in Four Countries (in billions of US dollars)',
   ['Country', '2016', '2017', '2018'],
   [['South Korea', '$21.0', '$17.2', '$23.1'],
    ['Japan', '$33.5', '$37.0', '$45.3'],
    ['Thailand', '$48.5', '$57.1', '$61.4'],
    ['Malaysia', '$19.7', '$20.3', '$21.8']],
   'One measure of international tourism'),

 '75e07a4d': (
   'Sample of Food Items from Gemini Mission Menus',
   ['Food item', 'Day', 'Meal'],
   [['Sugar cookie cubes', '1', 'B'],
    ['Chicken and vegetables', '2', 'B'],
    ['Shrimp cocktail', '4', 'C'],
    ['Hot cocoa', '3', 'A']],
   'To make sure they got the nutrition'),

 '0cf13ece': (
   'Recordings of Female Bottlenose Dolphins with Their Calves',
   ['Dolphin ID', 'Recording year'],
   [['FB07', '2012'],
    ['FB25', '1989'],
    ['FB43', '1992'],
    ['FB79', '2018']],
   'In a study of bottlenose dolphins'),

 'a7c52fa4': (
   'Mean Time (in Seconds) Spent per Flower for Four Pollinator Genera',
   ['Pollinator genus', 'Seconds per intact pin flower', 'Seconds per damaged pin flower',
    'Seconds per intact thrum flower', 'Seconds per damaged thrum flower'],
   [['<em>Habropoda</em>', '2.7', '5.4', '4.1', '9.5'],
    ['<em>Osmia</em>', '5.2', '8.2', '7.1', '8.3'],
    ['<em>Pierid</em>', '2.6', '4.0', '2.4', '1.9'],
    ['<em>Xylocopa</em>', '2.3', '2.8', '2.5', '2.2']],
   'To study how floral damage'),

 'ccf414c9': (
   'E-book Sales as a Percentage of Total Unit Sales in All Book Formats for a '
   'Large US Trade Publisher, by Genre, 2006, 2011, 2016',
   ['Genre', '2006', '2011', '2016'],
   [['science fiction and fantasy', '0.6', '27.7', '36.7'],
    ['cookbooks', '0', '2.9', '10.5'],
    ['travel guides', '0', '5.5', '24.6'],
    ['romance', '0.3', '40.6', '56.2']],
   'E-books became an increasingly popular'),

 '46e45728': (
   'Daily Distance Traveled by Adult Mountain Lions in Three Seasons',
   ['Season', 'Kilometers per day traveled by adult females',
    'Kilometers per day traveled by adult males'],
   [['cold-dry', '9.28', '15.81'],
    ['monsoon', '12.64', '18.93'],
    ['hot-dry', '12.48', '18.87']],
   'Wildlife researcher Dana L. Karelus'),

 '25b70215': (
   'Effect of Neighboring Species on Pollinator Visits to Target Species',
   ['Neighboring species', 'Target species', 'Effect value'],
   [['Virginia spring beauty', 'star chickweed', '0.4853'],
    ['Himalayan balsam', 'marsh woundwort', '0.7905'],
    ['common dandelion', 'cat' + RSQUO + 's ear', MINUS + '0.6254']],
   'Researchers Carolina Laura Morales'),
}

# Confirmed bar/line charts - handled by a separate effort, not forced into tables.
CHARTS = [
 {'cb_id': '37a49687', 'visual': 'line chart',
  'title': 'Number of Young Fish Collected at Mangrove Sites in the Egyptian Red Sea During Three Seasons of 2010'},
 {'cb_id': '0992bd73', 'visual': 'grouped bar chart',
  'title': 'Percent of UK Survey Respondents Who Trust People At Least Somewhat'},
 {'cb_id': 'a9ac31e4', 'visual': 'bar chart',
  'title': 'Area of Three Glaciers in the 2016 Swiss Glacier Inventory'},
 {'cb_id': '303bcc41', 'visual': 'bar chart',
  'title': 'Top Four Species of Wild Land Mammals by Global Biomass'},
 {'cb_id': '239d3535', 'visual': 'line chart',
  'title': 'Census Data for Four Canadian Cities, 1871–1901'},
 {'cb_id': 'e99a38ec', 'visual': 'bar chart',
  'title': 'Humility Scores for Participants’ Scenario Responses'},
 {'cb_id': '224428ac', 'visual': 'line chart',
  'title': 'California Condor Populations 2014–2020'},
 {'cb_id': '30c3aa98', 'visual': 'line chart',
  'title': 'Copper Production for Three States, 1889-1909'},
 {'cb_id': '627d93e3', 'visual': 'grouped bar chart',
  'title': 'Modeled Radial Growth of Sugar Maple Trees'},
]
CHART_IDS = [c['cb_id'] for c in CHARTS]


def load_targets():
    out = {}
    for f in ['rw_tests_6_10.json', 'rw_tests_11_15.json']:
        for t in json.load(open(os.path.join(BANK, f))):
            for m in t['modules']:
                for q in m['questions']:
                    st = q.get('stem') or ''
                    ps = q.get('passage') or ''
                    if re.search(r'\b(table|graph|chart|figure)\b', st, re.I) and '<table' not in ps:
                        out[q['cb_id']] = q
    return out


def build_table(title, headers, rows):
    parts = ['<p><strong>%s</strong></p>' % title, TSTYLE, '<tr>']
    for h in headers:
        parts.append(TH + h + '</th>')
    parts.append('</tr>')
    for r in rows:
        parts.append('<tr>')
        for c in r:
            parts.append(TD + c + '</td>')
        parts.append('</tr>')
    parts.append('</table>')
    return ''.join(parts)


NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')


def numeric_tokens(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return sorted(NUM.findall(s))


def main():
    targets = load_targets()
    missing = set(targets) - set(SPEC) - set(CHART_IDS)
    extra = set(SPEC) - set(targets)
    if missing:
        print('UNHANDLED TARGETS:', missing)
    if extra:
        print('SPEC IDS NOT IN TARGETS:', extra)

    result = []
    problems = []
    for cb_id, (title, headers, rows, prose_start) in SPEC.items():
        q = targets[cb_id]
        orig = q['passage']
        i = orig.find(prose_start)
        if i < 0:
            problems.append('%s: prose start %r not found' % (cb_id, prose_start))
            continue
        prose = orig[i:].strip()
        passage = build_table(title, headers, rows) + '<p>' + prose + '</p>'

        # --- verification -------------------------------------------------
        if passage.count('<table') != 1 or passage.count('</table>') != 1:
            problems.append('%s: unbalanced <table>' % cb_id)
        ncol = len(headers)
        for tr in re.findall(r'<tr>(.*?)</tr>', passage, re.S)[1:]:
            if tr.count('<td') != ncol:
                problems.append('%s: row has %d cells, expected %d' % (cb_id, tr.count('<td'), ncol))
        if passage.count('<tr>') != passage.count('</tr>'):
            problems.append('%s: unbalanced <tr>' % cb_id)
        if passage.count('<td') != passage.count('</td>') or passage.count('<th') != passage.count('</th>'):
            problems.append('%s: unbalanced cell tags' % cb_id)
        before, after = numeric_tokens(orig), numeric_tokens(passage)
        lost = [t for t in before if before.count(t) > after.count(t)]
        if lost:
            problems.append('%s: numeric tokens lost/reduced: %s' % (cb_id, sorted(set(lost))))
        # sign check: every U+2212 in the original must survive
        if orig.count(MINUS) != passage.count(MINUS):
            problems.append('%s: minus-sign count changed %d -> %d'
                            % (cb_id, orig.count(MINUS), passage.count(MINUS)))
        result.append({'cb_id': cb_id, 'passage': passage})

    result.sort(key=lambda r: r['cb_id'])
    if problems:
        print('PROBLEMS:')
        for p in problems:
            print('  ' + p)
        sys.exit(1)

    with open(OUT, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    with open(os.path.join(BANK, 'tables_charts.json'), 'w') as f:
        json.dump({'charts': CHARTS}, f, indent=2, ensure_ascii=False)
    print('wrote %d tables to %s' % (len(result), OUT))
    print('skipped %d charts: %s' % (len(CHARTS), ', '.join(CHART_IDS)))


if __name__ == '__main__':
    main()
