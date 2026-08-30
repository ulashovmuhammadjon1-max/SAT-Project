"""Key audit for AP COMPARATIVE GOVERNMENT 1.3 Democracy vs. Authoritarianism.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
The topic's own learning objective is PAU-1.B, whose three statements supply
most of the keys:

  PAU-1.B.1  the degree of democracy or authoritarianism is indicated by state
             adherence to rule of law, itemized as .a governed by law and not by
             arbitrary decisions of individual officials, .b the degree of state
             influence on or control of the media, .c the degree AND PRACTICE of
             free and fair elections, .d the degree of transparency of
             governmental decision making, .e the nature of citizen participation
  PAU-1.B.2  branches of national government are more likely to be independent of
             one another in democratic than in authoritarian regimes, and that
             independence can prevent any one branch from controlling all
             governmental power
  PAU-1.B.3  authoritarian regimes include illiberal democracies or hybrid
             regimes, one-party states, theocracies, totalitarian governments,
             and military regimes

Where a country appears, the claim names the statement that puts it there:
PAU-1.D.1.b (Iran's post-1979 theocracy), PAU-4.A.2 (China's one governing party
alongside eight permitted ones), PAU-2.A.1 (China, Iran and the United Kingdom as
unitary), DEM-1.C.2 to DEM-1.C.6 (media, transparency, Russia as a competitive
authoritarian regime, and civil-liberties data as a way of placing a regime on
the scale), DEM-1.B.3 (BOTH regime types regulate formal participation) and
DEM-2.B.4.a (a vetting body restricting ballot access).

TWO TRAPS THIS MODULE IS BUILT TO AVOID
---------------------------------------
1. No item asks a student to classify China or Iran as parliamentary,
   presidential or semi-presidential. PAU-3.A assigns those labels only to the
   United Kingdom, Mexico, Nigeria and Russia, so an item asking it would have no
   defensible key. See AP_COMP_GOV_CED.md note 2.
2. No item treats a media constraint or a participation restriction as
   exclusively authoritarian. DEM-1.C.2 and DEM-1.B.3 both say the two regime
   types differ in DEGREE, and the CED's own sample set is built on that trap.
   Item 8 and item 26 key the framework's position rather than the intuition.

DATA ITEMS
----------
Items 16-18 share one table and items 19-20 another. Every figure is
HYPOTHETICAL and the stems say so, because the framework prints no index value
for any country; a student reaches these keys from the table plus one framework
sentence, without needing a fact about a real country. Each key is recomputed
below and the arithmetic distractors are checked false on the same numbers.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_3

ROL = "Adherence to rule of law (0-10)"
MEDIA = "State control of media (0 = none, 10 = total)"
ELEC = "Elections judged free and fair (0-10)"
TRANS = "Transparency of decision making (0-10)"
OWN10 = "Share of broadcast outlets under state ownership, 2010"
OWN20 = "Share of broadcast outlets under state ownership, 2020"

_DEMOCRATIC_COLS = (ROL, ELEC, TRANS)


def _by(table, header):
    return dict(zip(cg.labels(table), cg.col(table, header)))


def q16(table, item):
    media = _by(table, MEDIA)
    worst_media = max(media, key=media.get)
    assert worst_media == "Country S", f"the highest media-control score belongs to {worst_media}"
    for h in _DEMOCRATIC_COLS:
        v = _by(table, h)
        assert min(v, key=v.get) == worst_media, f"{worst_media} is not last on {h}"
    # each distractor false on the same numbers
    rol, trans = _by(table, ROL), _by(table, TRANS)
    assert any(trans[c] <= rol[c] for c in rol), "'transparency above rule of law everywhere' must be false"
    low_media = sorted(media, key=media.get)[:2]
    low_elec = sorted(_by(table, ELEC), key=_by(table, ELEC).get)[:2]
    assert set(low_media) != set(low_elec), "'least media control holds the lowest election scores' must be false"
    order_rol = cg.ranked(table, ROL)
    order_media = cg.ranked(table, MEDIA)
    assert order_rol == list(reversed(order_media)), \
        "rule of law and media control must move inversely, so 'they rise together' is false"
    counts = [sum(1 for h in _DEMOCRATIC_COLS if _by(table, h)[c] > 5) + (1 if media[c] > 5 else 0)
              for c in cg.labels(table)]
    assert any(n < 3 for n in counts), "'all four score above 5 on at least three measures' must be false"
    return "Country S holds the highest media-control score and the lowest score on each of the other three indicators; all four distractors are false on these numbers"


def q17(table, item):
    order = cg.ranked(table, ROL)
    for h in (ELEC, TRANS):
        assert cg.ranked(table, h) == order, f"{h} orders the countries differently from rule of law"
    assert cg.ranked(table, MEDIA, reverse=False) == order, \
        "media control must order the countries the same way once inverted"
    assert order == ["Country P", "Country Q", "Country R", "Country S"], f"the order is {order}"
    return f"all four indicators, with media control inverted, place the countries in the order {order}"


def q18(table, item):
    rol, media = _by(table, ROL), _by(table, MEDIA)
    # the student's premise is a real feature of the table -- the objection is to
    # the causal reading, not to the reading of the numbers
    assert cg.ranked(table, ROL) == list(reversed(cg.ranked(table, MEDIA))), \
        "the two columns must move inversely, or the item's premise is not in the data"
    assert len(cg.labels(table)) == 4, "the item's objection turns on there being only four observations"
    assert len(set(media.values())) == 4 and len(set(rol.values())) == 4, \
        "no ties, so the association is unambiguous and only its direction is at issue"
    return "the two columns do move inversely across all four rows, so what the key rejects is the causal reading and not the reading of the numbers"


def q19(table, item):
    d = {lab: cg.cell(table, lab, OWN20) - cg.cell(table, lab, OWN10) for lab in cg.labels(table)}
    assert d["Country U"] == 25, f"the keyed rise of 25 points recomputes to {d['Country U']}"
    assert d["Country T"] == 4, f"the four-point rise recomputes to {d['Country T']}"
    assert d["Country V"] == -1, f"the one-point fall recomputes to {d['Country V']}"
    assert d["Country U"] == max(d.values()) and d["Country U"] > 5 * abs(d["Country T"]), \
        "the keyed rise must dominate, not merely lead"
    assert any(cg.cell(table, lab, OWN10) > 50 for lab in cg.labels(table)) is False, \
        "no 2010 share is above half, which is why the 'none, nothing above half at the start' distractor is tempting"
    return "state ownership rises 25 points in one country against a 4-point rise and a 1-point fall in the others"


def q20(table, item):
    v20 = _by(table, OWN20)
    majority = [lab for lab, s in v20.items() if s > 50]
    assert majority == ["Country U"], f"exactly one country may hold a majority in 2020; got {majority}"
    assert v20["Country U"] == 71, f"the keyed 71 percent reads as {v20['Country U']}"
    assert cg.cell(table, "Country U", OWN10) == 46, \
        "the 46 percent distractor must be that country's 2010 value, so the trap is the wrong year"
    return "only one 2020 share exceeds half, at 71 percent, and the 46 percent distractor is that country's 2010 figure"


CLAIMS = [
 ("arbitrary decisions of individual officials",
  "EK PAU-1.B.1.a names as a rule-of-law indicator the principle that a state should be governed by law and not by arbitrary decisions made by individual government officials. An unreviewable personal licensing power is that indicator failing, and it touches none of the other four."),
 ("degree and practice",
  "EK PAU-1.B.1.c makes the indicator the degree AND PRACTICE of free and fair elections, so the occurrence of an election does not settle it. EK DEM-1.C.5 describes contested elections held with limited degrees of competitiveness, which is the same distinction applied to Russia."),
 ("controlling all governmental power",
  "EK PAU-1.B.2 states that independence among branches can serve to prevent any one branch from controlling all governmental power. Speed of policy making, direct election of every branch, constitutional form and federal structure are questions the framework treats elsewhere."),
 ("theocracies",
  "EK PAU-1.B.3 lists illiberal democracies or hybrid regimes, one-party states, theocracies, totalitarian governments and military regimes as the authoritarian types. Executive-legislative type, territorial structure and stage of democratization are separate classifications that cut across this one."),
 ("Islamic Sharia",
  "EK PAU-1.D.1.b states the transition of power from dictatorial rule in Iran to a theocracy based on Islamic Sharia law after the 1979 Revolution, and EK PAU-1.B.3 places theocracy among the authoritarian types. The rejected descriptions are the framework's own words about Nigeria, Mexico and Russia."),
 ("broaden discussion and consultation",
  "EK PAU-4.A.2 states that China's rules allow only the Communist Party of China to control governing power while allowing eight other parties to exist to broaden discussion and consultation. The permitted parties exist without competing for control, which is what makes it a one-party state under EK PAU-1.B.3."),
 ("limited degrees of competitiveness",
  "EK DEM-1.C.5 states that Russia is characterized as a competitive authoritarian regime or illiberal democracy, holding contested elections but with limited degrees of competitiveness and providing minimal civil liberty protections and governmental transparency."),
 ("both democratic and authoritarian regimes",
  "EK DEM-1.C.2 states that both democratic and authoritarian regimes impose constraints on the media to protect citizens and maintain order, while democratic regimes generally tolerate a high degree of media freedom. The framework's difference is one of degree, and the exclusive reading is the trap its own sample set is built on."),
 ("citizen control of the political agenda",
  "EK DEM-1.C.2 gives this as the reason democratic regimes tolerate a high degree of media freedom: to encourage citizen control of the political agenda and to check political power and corruption. The purpose is a check on government rather than an allocation of airtime."),
 ("maintain political control",
  "EK DEM-1.C.3 introduces both examples with the statement that stronger authoritarian regimes monitor and restrict citizens' media access to a greater degree to maintain political control, then names the Great Firewall and the nationalization of most Russian broadcast media as instances."),
 ("revoking media licences",
  "EK DEM-1.C.3.b describes Iranian courts suspending or revoking media licences when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. The firewall example is China's and the broadcast nationalization is Russia's."),
 ("circulate openly",
  "EK DEM-1.C.4 defines a transparent government as one that allows information about government and policy making to circulate openly. Contested elections, constitutional ratification, branch independence and judicial review are indicators the framework lists separately."),
 ("maximize order",
  "EK DEM-1.C.4 states that authoritarian regimes tend to prefer secret or closed proceedings to maximize order, which is the framework's own account of the motive rather than an inference from it."),
 ("more likely to be independent of one another",
  "EK PAU-1.B.2 is the claim at issue, and a court whose members serve at the executive's pleasure and has never ruled against it is the dependent case the statement contrasts with. The other options state framework claims that bear on different indicators."),
 ("territorially concentrated",
  "EK PAU-2.A.1 lists China, Iran and the United Kingdom together as unitary states, while EK PAU-1.B.1 supplies a wholly separate set of indicators for the democratic-authoritarian scale. Two states can therefore share a territorial structure and sit at opposite ends of the scale, so neither classification can be read off the other."),
 ("holds the lowest scores",
  "Recomputed in q16 above: the row with the highest media-control score is last on rule of law, on elections and on transparency, and each of the four distractors is false on the same numbers."),
 ("Country P, then Country Q",
  "Recomputed in q17 above: three columns rise with democracy and one falls with it, and once the media column is inverted all four indicators agree on the same ordering."),
 ("nothing that isolates",
  "EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls an observed co-movement an association. Recomputed in q18 above: the columns really do move together, so what fails is the causal step and not the reading."),
 ("rose by 25 percentage points",
  "EK DEM-1.C.3.c presents nationalization of broadcast media as the mechanism by which a regime tightens control. Recomputed in q19 above: one country's state-owned share rises 25 points against a 4-point rise and a 1-point fall."),
 ("at 71 percent",
  "Recomputed in q20 above: exactly one 2020 share exceeds half. The lower figure offered for the same country is its 2010 value, so the distractor is a wrong-year reading rather than a wrong-country one."),
 ("authoritarian-democratic scale",
  "EK DEM-1.C.6 states that comparing data showing how far governments protect or restrict civil liberties over time can determine regime placement on an authoritarian/democratic scale. The framework treats regime type as a matter of degree, which is what makes such a placement meaningful."),
 ("hybrids that combine",
  "EK DEM-1.C.5 states that competitive authoritarian regimes act as a hybrid of democratic and authoritarian regimes. The rejected options describe a consolidated democracy, a closed authoritarian regime, a theocracy and a military regime, each a distinct type under EK PAU-1.B.3."),
 ("military regime",
  "EK PAU-1.B.3 names military regimes among the authoritarian types, and rule by a council of commanders after the suspension of the constitution is the clearest instance. A theocracy rests on religious authority and an illiberal democracy still holds contested elections."),
 ("law drawn from scripture",
  "EK PAU-1.B.3 lists theocracies and one-party states as separate authoritarian types, and the framework's own illustrations keep them apart: EK PAU-1.D.1.b grounds Iran's theocracy in Islamic Sharia law while EK PAU-4.A.2 grounds China's arrangement in the exclusive governing role of one legal party."),
 ("disqualified most opposition candidates",
  "EK PAU-1.B.1.c makes the degree and practice of free and fair elections the indicator, and EK DEM-2.B.4.a treats exclusion of candidates by a vetting body as the clearest reduction of electoral competition. Turnout, a seat bonus produced by the counting rule, a shifted date and voluntary abstention are each consistent with a free contest."),
 ("kinds of participation it permits",
  "EK PAU-1.B.1.e names the nature of citizen participation in government as the indicator, which is a question about the forms participation may take. EK DEM-1.B.3 adds that both regime types regulate formal participation and that authoritarian regimes do so to a much greater extent, so presence against absence is the wrong axis."),
 ("transparency of governmental decision making",
  "EK PAU-1.B.1.d names the degree of transparency of governmental decision making as an indicator and EK DEM-1.C.4 defines transparency as letting information about government and policy making circulate openly. Both states in the item hold multiparty elections, so the electoral indicator cannot separate them."),
 ("formally separate but not independent",
  "EK PAU-1.B.2 concerns whether branches are in fact independent and whether that independence stops one branch from controlling all governmental power. A constitutional grant that no institution enforces leaves the executive exercising the legislature's power, which is the concentration the statement is about."),
 ("closing cabinet proceedings",
  "EK PAU-1.B.1 makes state control of the media and the transparency of decision making two of its five indicators, so a change worsening both moves a regime on two of the scale's own measures at once. An election date, a chamber's size, national symbols and the level at which roads are maintained touch none of the five."),
 ("illiberal democracy",
  "EK PAU-1.B.3 lists illiberal democracies or hybrid regimes among the authoritarian types and EK DEM-1.C.5 describes this exact combination, contested elections alongside minimal civil liberty protections and minimal transparency. Real elections rule out the closed categories, and territorial structure is a different classification altogether."),
]

cg.check(k1_3, CLAIMS, table_checks={16: q16, 17: q17, 18: q18, 19: q19, 20: q20})
