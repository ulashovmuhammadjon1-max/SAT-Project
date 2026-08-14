# -*- coding: utf-8 -*-
"""Rebuilt <table> figures for the College Board question-bank questions whose
data table did not survive PDF text extraction.

Every value here was read off a 120-dpi render of the source page (crop/<id>.png)
and cross-checked against the per-glyph word positions dumped by figwords.py.
Nothing is inferred or invented.
"""

TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'
TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">'


def build(title, header, rows, note=None):
    h = "".join(f"{TH}{c}</th>" for c in header)
    body = "".join("<tr>" + "".join(f"{TD}{c}</td>" for c in r) + "</tr>" for r in rows)
    out = f"<p><strong>{title}</strong></p>{TABLE}<thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>"
    if note:
        out += f"<p><em>{note}</em></p>"
    return out


TABLES = {
 "0147b080": dict(
   title="Pyramids in Egypt and the Americas",
   header=["Pyramid", "Country", "Height (meters)", "Age (years before present)"],
   rows=[["The Great Pyramid", "Mexico", "33", "2,050 to 2,400"],
         ["The Pyramid of Djoser", "Egypt", "60", "4,600 to 4,700"],
         ["The Pyramid of Sahure", "Egypt", "47", "4,400 to 4,500"],
         ["El Castillo", "Belize", "40", "1,100 to 1,400"]]),

 "6a6bbac3": dict(
   title="Number and Origin of Clamshell Tools Found at Different Levels Below the Surface in Neanderthal Cave",
   header=["Depth of tools found below surface in cave (meters)",
           "Clamshells that Neanderthals collected from the beach",
           "Clamshells that Neanderthals harvested from the seafloor"],
   rows=[["3&ndash;4", "99", "33"], ["6&ndash;7", "1", "0"], ["4&ndash;5", "2", "0"],
         ["2&ndash;3", "7", "0"], ["5&ndash;6", "18", "7"]]),

 "af125459": dict(
   title="Number and Origin of Clamshell Tools Found at Different Depths below the Surface in Neanderthal Cave",
   header=["Depth of tools found below surface in cave (meters)",
           "Clamshells that Neanderthals collected from the beach",
           "Clamshells that Neanderthals harvested from the seafloor"],
   rows=[["2&ndash;3", "7", "0"], ["3&ndash;4", "99", "33"], ["4&ndash;5", "2", "0"],
         ["5&ndash;6", "18", "7"], ["6&ndash;7", "1", "0"]]),

 "629fb8a9": dict(
   title="Percentages of New Year&rsquo;s Resolution Makers Who Make Certain Kinds of Resolutions",
   header=["Type of resolution", "Age 18-29", "Age 30-49", "Age 50-64", "Age 65+"],
   rows=[["Health and exercise", "79", "80", "79", "76"],
         ["Finances", "68", "63", "56", "47"],
         ["Personal relationships", "63", "53", "58", "52"],
         ["Hobbies", "65", "53", "51", "45"]]),

 "5cf5c0d3": dict(
   title="Credited Film Output of James Young Deer, Dark Cloud, Edwin Carewe, and Lillian St. Cyr",
   header=["Individual", "Years active", "Number of films known and commonly credited"],
   rows=[["James Young Deer", "1909&ndash;1924", "33 (actor), 35 (director), 10 (writer)"],
         ["Dark Cloud", "1910&ndash;1920", "35 (actor), 1 (writer)"],
         ["Edwin Carewe", "1912&ndash;1934", "47 (actor), 58 (director), 20 (producer), 4 (writer)"],
         ["Lillian St. Cyr (Red Wing)", "1908&ndash;1921", "66 (actor)"]]),

 "4411e15b": dict(
   title="Fiber Characteristics of Mouflon, Navajo-Churro, and Spanish Merino Sheep",
   header=["Type of sheep", "Diameter of outer coat fibers (in microns)", "Diameter of inner coat fibers (in microns)"],
   rows=[["Spanish Merino", "19&ndash;24", "17&ndash;21"],
         ["Navajo-Churro", "35 or higher", "10&ndash;35"],
         ["Mouflon", "150", "15"]]),

 "3fc06a91": dict(
   title="Employment by Sector in France and the United States, 1800&ndash;2012 (% of total employment)",
   header=["Year", "Agriculture in France", "Manufacturing in France", "Services in France",
           "Agriculture in US", "Manufacturing in US", "Services in US"],
   rows=[["1800", "64", "22", "14", "68", "18", "13"],
         ["1900", "43", "29", "28", "41", "28", "31"],
         ["1950", "32", "33", "35", "14", "33", "53"],
         ["2012", "3", "21", "76", "2", "18", "80"]],
   note="Rows in table may not add up to 100 due to rounding."),

 "9debe79a": dict(
   title="Average Temperatures in July in Four Locations in the Navajo Nation",
   header=["Location", "Average highest temperature (Fahrenheit)", "Average lowest temperature (Fahrenheit)"],
   rows=[["Teec Nos Pos", "94&deg;", "65&deg;"], ["Cameron", "99&deg;", "65&deg;"],
         ["Ramah", "83&deg;", "50&deg;"], ["Tuba City", "83&deg;", "50&deg;"]]),

 "cf7491c1": dict(
   title="Characteristics of Five Recently Discovered Gas Exoplanets",
   header=["Exoplanet designation", "Mass (Jupiters)", "Radius (Jupiters)", "Orbital period (days)",
           "Distance from the Sun (parsecs)"],
   rows=[["TOI-640 b", "0.88", "1.771", "5.003", "340"],
         ["TOI-1601 b", "0.99", "1.239", "5.331", "336"],
         ["TOI-628 b", "6.33", "1.060", "3.409", "178"],
         ["TOI-1478 b", "0.85", "1.060", "10.180", "153"],
         ["TOI-1333 b", "2.37", "1.396", "4.720", "200"]]),

 "e1546fd6": dict(
   title="Average Nitrate and Phosphate Concentrations in Seawater after Volcanic Eruption",
   header=["Nutrient",
           "Seawater in lava-affected area, 5&ndash;45 meters below surface",
           "Seawater in lava-affected area, 75&ndash;125 meters below surface",
           "Seawater outside of lava-affected area, 5&ndash;45 meters below surface",
           "Seawater outside of lava-affected area, 75&ndash;125 meters below surface"],
   rows=[["Nitrate (micromoles per liter)", "3.1", "0.4", "&le;0.03", "&le;0.01"],
         ["Phosphate (micromoles per liter)", "0.17", "0.09", "0.14", "0.06"]]),

 "b8199d5a": dict(
   title="Total Areas and 2022 Populations of Smallest Arabian Peninsula Countries",
   header=["Country", "Total area (square miles)", "Population"],
   rows=[["Kuwait", "6,880", "4,268,873"], ["Bahrain", "304", "1,472,233"], ["Qatar", "4,471", "2,695,122"]]),

 "ab94d40a": dict(
   title="Time Participants Spent Reading about Five London Museums",
   header=["Museum Name", "Ranking",
           "Percentage of total time spent reading about museum by participants provided with ranking",
           "Percentage of total time spent reading about museum by participants not provided with ranking"],
   rows=[["British Museum", "1", "36", "18"], ["National Gallery", "2", "21", "20"],
         ["Tate Modern", "4", "16", "17"], ["Victoria and Albert Museum", "5", "14", "23"],
         ["Natural History Museum", "3", "13", "22"]]),

 "e18d75ea": dict(
   title="Depths at Which Four Deep-Sea Fish Species Live",
   header=["Species", "Depth below the ocean surface"],
   rows=[["Footballfish", "200&ndash;1,000 meters"],
         ["Southern stoplight loosejaw", "500&ndash;2,000 meters"],
         ["Black seadevil", "250&ndash;2,000 meters"],
         ["Bollons&rsquo; rattail", "300&ndash;800 meters"]]),

 "df9c5a1d": dict(
   title="Juvenile Plants Found Growing on Bare Ground and in Patches of Vegetation for Five Species",
   header=["Species", "Bare ground", "Patches of vegetation", "Total", "Percent found in patches of vegetation"],
   rows=[["<em>T. moroderi</em>", "9", "13", "22", "59.1%"],
         ["<em>T. libanitis</em>", "83", "120", "203", "59.1%"],
         ["<em>H. syriacim</em>", "95", "106", "201", "52.7%"],
         ["<em>H. squamatum</em>", "218", "321", "539", "59.6%"],
         ["<em>H. stoechas</em>", "11", "12", "23", "52.2%"]]),

 "dd349efc": dict(
   title="Participants&rsquo; Evaluation of the Likelihood That Robots Can Work Effectively in Different Occupations",
   header=["Occupation", "Somewhat or very unlikely (%)", "Neutral (%)", "Somewhat or very likely (%)"],
   rows=[["television news anchor", "24", "9", "67"], ["teacher", "37", "16", "47"],
         ["firefighter", "62", "9", "30"], ["surgeon", "74", "9", "16"],
         ["tour guide", "10", "8", "82"]],
   note="Rows in table may not add up to 100 due to rounding."),

 "d102706f": dict(
   title="Estimates of Tyrannosaurid Bite Force",
   header=["Study", "Year", "Estimation method", "Approximate bite force (newtons)"],
   rows=[["Cost et al.", "2019", "muscular and skeletal modeling", "35,000&ndash;63,000"],
         ["Gignac and Erickson", "2017", "tooth-bone interaction analysis", "8,000&ndash;34,000"],
         ["Meers", "2002", "body-mass scaling", "183,000&ndash;235,000"],
         ["Bates and Falkingham", "2012", "muscular and skeletal modeling", "35,000&ndash;57,000"]]),

 "cbecb873": dict(
   title="Body Length, Filter Time, and Lunges per Dive for Four Whale Species",
   header=["Whale species", "Typical adult body length (meters)",
           "Average time to filter all engulfed water (seconds)",
           "Average number of lunges per dive deeper than 50 meters"],
   rows=[["fin", "18&ndash;22", "31.30", "3.95"], ["humpback", "11&ndash;17", "17.12", "6.28"],
         ["minke", "7&ndash;10", "8.88", "7.48"], ["blue", "24&ndash;34", "60.27", "4.02"]]),

 "38e79659": dict(
   title="Attendance and Cost of Hosting for Past Four US World&rsquo;s Fairs",
   header=["World&rsquo;s fairs held in the US", "Cost (in US dollars)", "Number of visitors"],
   rows=[["Century 21 Exposition (1962)", "$47 million", "9.60 million"],
         ["HemisFair &rsquo;68", "$156 million", "6.40 million"],
         ["1984 World&rsquo;s Fair", "$350 million", "7.35 million"],
         ["Expo &rsquo;74", "$78 million", "5.60 million"]]),

 "4042ff0b": dict(
   title="Comfort Ratings and Temperature-Adjustment Preferences from One Survey",
   header=["Participant", "Comfort rating", "Preferred temperature adjustment"],
   rows=[["20", "&minus;2", "Cooler"], ["1", "1", "Cooler"], ["21", "1", "Cooler"]]),

 "5ff1ba73": dict(
   title="Guilds in French Cities in the Late Eighteenth Century",
   header=["City", "Date", "Inhabitants", "Number of guilds", "Inhabitants per guild"],
   rows=[["Paris", "1766", "600,000", "133", "4,511"],
         ["Bordeaux", "1762", "80,000", "49", "1,633"],
         ["Rouen", "1775", "74,000", "112", "661"],
         ["Lyon", "1789", "143,000", "72", "1,986"]]),

 "145da981": dict(
   title="Effect of Paywall Introduction on Newspaper Companies&rsquo; Revenues",
   header=["Newspaper", "Total revenue change ($ in thousands)", "Percentage change (%)", "Newspaper size"],
   rows=[["Los Angeles Times", "93,966", "12.5", "large"],
         ["The New York Times", "235,788", "20", "large"],
         ["The Denver Post", "&minus;3,765", "&minus;1", "small"],
         ["Sun Sentinel", "&minus;24,899", "&minus;11.9", "small"],
         ["Chicago Tribune", "94,492", "19", "large"]]),

 "23b5cb59": dict(
   title="Total Electoral College Votes and Popular Votes in the 15th US Presidential Election",
   header=["Candidate", "Total electoral college votes", "Total popular votes"],
   rows=[["James K. Polk", "170", "1,339,494"], ["Henry Clay", "105", "1,300,004"],
         ["James Gillespie Birney", "0", "62,103"]]),

 "7a1877be": dict(
   title="Nucleobase Concentrations from Murchison Meteorite and Soil Samples in Parts per Billion",
   header=["Nucleobase", "Murchison meteorite sample 1", "Murchison meteorite sample 2", "Murchison soil sample"],
   rows=[["Isoguanine", "0.5", "0.04", "not detected"],
         ["Purine", "0.2", "0.02", "not detected"],
         ["Xanthine", "39", "3", "1"],
         ["Adenine", "15", "1", "40"],
         ["Hypoxanthine", "24", "1", "2"]]),

 "6317295c": dict(
   title="Properties of Select Rotating Radio Transients",
   header=["Name", "Right ascension (hours)", "Period (seconds)", "Frequency (hertz)"],
   rows=[["J0545-03", "5:45", "1.074", "0.931"],
         ["J1654-2335", "16:54:03", "0.545", "1.834"],
         ["J0103+54", "1:03:37", "0.354", "2.822"],
         ["J0121+53", "1:21", "2.725", "0.367"],
         ["J0614-03", "6:15", "0.136", "7.353"]]),

 "eb775f90": dict(
   title="Annual Car Production in the United States, 1910&ndash;1925",
   header=["Year", "Number of cars produced", "Number of companies producing cars"],
   rows=[["1910", "123,990", "320"], ["1915", "548,139", "224"],
         ["1920", "1,651,625", "197"], ["1925", "3,185,881", "80"]]),

 "43f4013a": dict(
   title="Global Strontium Seawater Curve",
   header=["<sup>87</sup>Sr/<sup>86</sup>Sr", "Age (Ma)"],
   rows=[["0.708980", "6.20"], ["0.709000", "5.86"], ["0.709020", "5.40"],
         ["0.709040", "4.75"], ["0.709060", "3.00"]]),
}


def html(qid):
    t = TABLES[qid]
    return build(t["title"], t["header"], t["rows"], t.get("note"))
