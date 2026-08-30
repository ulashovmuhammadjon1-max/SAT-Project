"""Key audit for AP HUMAN GEOGRAPHY 2.8 Women and Demographic Change.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. SPS-2.B prints two essential-knowledge statements:

    SPS-2.B.1  Changing social values and access to education, employment,
               health care, and contraception have reduced fertility rates in
               most parts of the world.
    SPS-2.B.2  Changing social, economic, and political roles for females have
               influenced patterns of fertility, mortality, and migration, as
               illustrated by Ravenstein's laws of migration.

SPS-2.B.1 is unusually generous to a question writer, because it is a closed
list of mechanisms rather than a bare name: social values, education,
employment, health care, contraception. Items 1, 2, 3, 4, 5, 6, 13, 14, 20, 21,
25, 26, 27 and 30 are keyed to that list and cite it.

Two features of the sentence the module takes seriously:

  * "in MOST parts of the world" -- not everywhere. Item 6 asks about the
    qualification directly, because reading it as a universal law is the kind of
    overstatement that turns a correct claim into a wrong key.
  * The statement covers FERTILITY only. It is SPS-2.B.2 that extends the
    consequence to MORTALITY and MIGRATION, and items 7, 8, 16, 19 and 29 are
    keyed to that extension, which is the half of the topic students skip.

RAVENSTEIN. SPS-2.B.2 names the laws and does not print them, so the ten laws
are set out in the module header and every Ravenstein key is traced to one of
them there. Items 9, 10, 11, 12, 17, 18, 22, 23 and 28 use them.

The honesty problem this topic contains, and how the module handles it: the
sixth law -- women more migratory within a country, men over long international
distances -- described Britain in the 1880s, and women are now close to half of
international migrants worldwide. Presenting a Victorian generalization as a
present-day fact would be a wrong key dressed as a citation. Items 15 and 24
therefore test the laws AS A MODEL to be checked against data, and item 28's
table supplies its own numbers rather than asking a student to trust the law.

The five table items (26-30) are the computational gate:

  26  fertility falls monotonically as female enrolment rises, with no reversal
  27  one country is deliberately OFF the line -- the second-highest prevalence
      paired with the second-highest fertility -- because the framework names
      contraception as one channel among several, not the only one
  28  the sex split reverses between internal and intercontinental flows, and
      the recompute asserts the reversal rather than trusting the eye
  29  a fall of 510 per 100,000 is a fall of 82 percent, not 510 percent
  30  the relationship holds WITHIN one country, and the largest education group
      is not the highest-fertility group

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_8


def q26_enrolment_and_fertility(table):
    """Fertility falls at every step as enrolment rises."""
    rows = sorted((num(rowdict(table, r)["Female secondary enrolment (%)"]),
                   num(rowdict(table, r)["Total fertility rate"]))
                  for r in table["rows"])
    tfr = [t for _, t in rows]
    enrol = [e for e, _ in rows]
    assert all(tfr[i] > tfr[i + 1] for i in range(len(tfr) - 1)), tfr
    assert tfr[0] == 5.8 and tfr[-1] == 1.7, tfr
    assert enrol[0] == 24 and enrol[-1] == 94, enrol
    # The highest-enrolment country must have the LOWEST fertility, or a
    # distractor becomes true.
    assert tfr[-1] == min(tfr), tfr
    return "from 5.8 at 24 percent enrolment to 1.7"


def q27_off_the_line(table):
    """Three countries line up on prevalence; the fourth deliberately does not."""
    data = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        data[d["Country"]] = (num(d["Contraceptive prevalence (%)"]),
                              num(d["Total fertility rate"]))
    ordered = sorted(data, key=lambda c: data[c][0])
    tfrs = [data[c][1] for c in ordered]
    # Exactly one adjacent pair must break the descending order.
    breaks = [i for i in range(len(tfrs) - 1) if tfrs[i] < tfrs[i + 1]]
    assert len(breaks) == 1, (ordered, tfrs)
    outlier = ordered[breaks[0] + 1]
    assert outlier == "Country M", (ordered, tfrs)
    # Its prevalence is near the top and its fertility above the second country's.
    assert data["Country M"][0] > data["Country K"][0], data
    assert data["Country M"][1] > data["Country K"][1], data
    assert abs(data["Country M"][0] - data["Country L"][0]) <= 5, data
    return "Country M"


def q28_ravenstein_sixth(table):
    """Women lead every internal flow; men lead the intercontinental one."""
    internal, international = [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        f = num(d["Female migrants"])
        m = num(d["Male migrants"])
        (international if "continent" in d["Type of move"] else internal).append((f, m))
    assert len(internal) == 2 and len(international) == 1, (internal, international)
    assert all(f > m for f, m in internal), internal
    f, m = international[0]
    assert m > f, international
    assert m / f >= 3, international
    return "women outnumber men in both internal flows"


def q29_maternal_mortality(table):
    """A fall of 510 per 100,000 is a fall of 82 percent, not 510 percent."""
    rows = [(num(rowdict(table, r)["Female literacy (%)"]),
             num(rowdict(table, r)["Maternal deaths per 100,000 births"]))
            for r in table["rows"]]
    rows.sort()
    lit = [l for l, _ in rows]
    mmr = [m for _, m in rows]
    assert all(lit[i] < lit[i + 1] for i in range(len(lit) - 1)), lit
    assert all(mmr[i] > mmr[i + 1] for i in range(len(mmr) - 1)), mmr
    fall = 100 * (mmr[0] - mmr[-1]) / mmr[0]
    assert 80 < fall < 85, fall
    assert mmr[0] - mmr[-1] == 510, mmr
    # The percent-versus-points distractor must be genuinely wrong.
    assert abs(fall - (mmr[0] - mmr[-1])) > 400, (fall, mmr)
    return "more than 80 percent"


def q30_within_country(table):
    """Fertility falls at every education level, and the biggest group is not the top."""
    rows = [(rowdict(table, r)["Mother's education"],
             num(rowdict(table, r)["Total fertility rate"]),
             num(rowdict(table, r)["Share of women in this group (%)"]))
            for r in table["rows"]]
    tfr = [t for _, t, _ in rows]
    share = [s for _, _, s in rows]
    assert all(tfr[i] > tfr[i + 1] for i in range(len(tfr) - 1)), tfr
    assert sum(share) == 100, share
    # Every group must be substantial, or the pattern rests on a handful of women.
    assert min(share) >= 10, share
    # The largest group must NOT be the highest-fertility group.
    biggest = max(range(len(share)), key=lambda k: share[k])
    assert tfr[biggest] != max(tfr), (rows, biggest)
    assert tfr[-1] == min(tfr), tfr
    return "falls with each additional level of schooling"


CLAIMS = [
 ("access to education, employment, health care, and contraception",
  "EK SPS-2.B.1 lists exactly these channels alongside changing social values, and the list is closed. Each acts on the same household decision from a different direction, which is why fertility has fallen across societies with very different politics and religions."),

 ("delays marriage and first birth and raises the earnings a woman gives up",
  "EK SPS-2.B.1 names access to education among the channels reducing fertility. The mechanism runs through timing and opportunity cost: years in school are years not spent childbearing, and qualifications make the forgone earnings of a large family much larger."),

 ("Wanting a smaller family and being able to achieve one are different things",
  "EK SPS-2.B.1 lists changing social values and access to contraception as separate items, and the separation is substantive rather than stylistic. Where the means are unavailable, unintended births hold measured fertility above stated preferences, which is a supply failure rather than a preference."),

 ("no longer need to bear extra children",
  "EK SPS-2.B.1 names access to health care among the channels reducing fertility, and the mechanism runs through child survival. Where many children died young, high fertility was the insurance, and removing the risk removes the reason for the insurance."),

 ("each additional child has a real price",
  "EK SPS-2.B.1 lists employment among the channels through which fertility has fallen. The cost of a child is not only what it consumes but what its mother forgoes, and that second cost rises with her earning opportunities."),

 ("about a widespread pattern rather than a universal law",
  "EK SPS-2.B.1's own wording is 'in most parts of the world', and taking that phrase seriously is the difference between a geographic generalization and an overstatement. Where schooling, work and contraception remain out of reach, the fall has not occurred."),

 ("affect mortality and migration as well as fertility",
  "EK SPS-2.B.1 covers fertility alone while EK SPS-2.B.2 extends the consequence to fertility, mortality AND migration. The second and third of those are the half of this topic students most often leave out."),

 ("maternal and infant mortality fall",
  "EK SPS-2.B.2 names mortality among the patterns influenced by changing social, economic and political roles for females. Literacy, income and autonomy each raise the chance that a health problem is recognized, treated and paid for in time."),

 ("within a country women are more migratory than men",
  "EK SPS-2.B.2 names Ravenstein's laws as the illustration of gendered migration, and only one of the ten laws concerns sex. The distractors each invert a real law about distance, counterstreams, age or rural mobility, which is why they are wrong rather than merely off point."),

 ("Travel only a short distance",
  "The first of Ravenstein's laws is that most migration is short-distance, which is distance decay stated for people. The other options each contradict one of the remaining laws about stages, age and economic motive."),

 ("up the settlement hierarchy in stages",
  "Step migration is a sequence of shorter moves reaching the destination a single long move would, and it is the law connecting the short-distance rule to the growth of large cities. Each individual step is short even though the total displacement is large."),

 ("smaller flow of returnees and retirees back",
  "A counterstream is a smaller flow in the opposite direction created by the same connection that produced the main stream: information, family ties, and return after work or retirement. Equal exchange would leave no net migration at all, which is a different situation entirely."),

 ("all more accessible in cities",
  "EK SPS-2.B.1 makes access to education, employment, health care and contraception the mechanisms, and access is exactly what varies between a capital and a remote district. The uneven geography of the fertility fall follows from the uneven geography of the channels."),

 ("Withdrawing girls from secondary school",
  "EK SPS-2.B.1's channels work by raising the cost of a large family and widening the alternatives open to women, so closing them removes both at once. The other options improve access generally and would if anything strengthen the fall the framework describes."),

 ("must be checked against current evidence",
  "EK SPS-2.B.2 offers Ravenstein as an ILLUSTRATION of gendered migration patterns rather than as a law of nature. Most of the laws still describe migration well, and the one about sex is the clearest case where the world has moved since the 1880s."),

 ("influence fertility, mortality, and migration",
  "EK SPS-2.B.2 names fertility and mortality together among the patterns influenced by women's changing roles, which is exactly the pair of outcomes the programme produced. A single intervention moving both is the framework's claim in its clearest form."),

 ("large towns grow more by migration than by natural increase",
  "One of Ravenstein's laws states this directly: a large town's growth is fed by arrivals rather than by births to the people already living there. The other options are true laws about who moves and why, but only this one is about a city's own growth accounting."),

 ("removes both current labour and future births",
  "A selective loss changes composition as well as size, because migrants take their future children with them. Both the labour force and the birth count at the origin fall, which is why sustained out-migration ages a region."),

 ("legislation on maternal health, childcare, and family planning",
  "EK SPS-2.B.2 names political roles alongside social and economic ones. Political voice changes which problems reach the statute book, and the policies that follow act on precisely the fertility and mortality channels EK SPS-2.B.1 lists."),

 ("a consequence of gains rather than of a failure",
  "EK SPS-2.B.1 identifies the channels, and every one of them is something a country pursues for its own sake. Recognising that low fertility is a by-product of widely desired gains is what makes the resulting policy question hard rather than obvious."),

 ("while fertility stayed at 6.0 for thirty years",
  "A causal claim is tested by the case in which its stated causes are present and its predicted effect is absent. The other four options are all instances of the pattern EK SPS-2.B.1 describes rather than challenges to it."),

 ("numbers fall as distance rises",
  "Distance decay is the decline of interaction with separation, and Ravenstein's short-distance law is that statement applied to migration. The remaining options describe who migrates, why, and what the destination gains, none of which is a distance relationship."),

 ("distinguishes internal migration, where women predominate",
  "EK SPS-2.B.2 cites Ravenstein as the illustration of gendered migration, and the sixth law is the one that separates internal from long-distance international movement. The scenario shows both halves of that law operating in one country at one time."),

 ("tendencies to be tested against current data",
  "EK SPS-2.B.2 calls the laws an illustration, which is a claim about usefulness rather than universality. The productive use of a generalization is to notice its exceptions, since a departure from the expected pattern is where a particular case's geography shows up."),

 ("themselves durable, and few societies reverse them deliberately",
  "EK SPS-2.B.1's channels are social and economic conditions rather than events, and they persist once established. That durability is what makes pronatalist policy so much harder than the antinatalist policy of the previous topic."),

 ("from 5.8 at 24 percent enrolment to 1.7",
  "Recomputed from the table: enrolment rises 24, 51, 78, 94 while fertility falls 5.8, 3.9, 2.3, 1.7, with no reversal at any step. Four points cannot establish causation, but they show the association EK SPS-2.B.1's account predicts.",
  q26_enrolment_and_fertility),

 ("Country M",
  "Recomputed from the table: three countries line up in order -- 14 with 6.1, 38 with 4.2 and 62 with 2.6 -- while exactly one breaks the sequence by pairing near-top prevalence with the second-highest fertility. The verifier asserts there is exactly one such break, since contraception is one of EK SPS-2.B.1's channels rather than the only one.",
  q27_off_the_line),

 ("women outnumber men in both internal flows",
  "Recomputed from the table: women lead 62,000 to 41,000 and 48,000 to 44,000 inside the country while men lead 57,000 to 19,000 on the intercontinental move. The verifier asserts the reversal and the three-to-one ratio, which is the exact content of Ravenstein's sixth law.",
  q28_ravenstein_sixth),

 ("more than 80 percent",
  "Recomputed from the table: maternal deaths fall from 620 to 110 per 100,000, a reduction of 510 points and 82 percent, while literacy rises from 31 to 84 percent. The verifier confirms the points figure and the percent figure differ by hundreds, which disposes of the distractor conflating them.",
  q29_maternal_mortality),

 ("falls with each additional level of schooling",
  "Recomputed from the table: fertility runs 6.4, 5.1, 3.2 and 2.0 across the four education levels while the shares sum to 100 with every group above ten percent. The verifier also confirms the largest group is not the highest-fertility group, so the pattern is not an artefact of one small category.",
  q30_within_country),
]

hg_check.check(g2_8, CLAIMS, per_topic=30, n_choices=5)
