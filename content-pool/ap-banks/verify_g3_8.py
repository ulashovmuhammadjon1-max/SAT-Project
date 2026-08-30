"""Key audit for AP HUMAN GEOGRAPHY 3.8 Effects of Diffusion.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic has one essential-knowledge statement and it is a
closed list of four names:

    SPS-3.B.1  Acculturation, assimilation, syncretism, and multiculturalism are
               effects of the diffusion of culture.

Membership in that list is citable and items 1 and 23 test it directly, item 23
as a NOT question keyed to nationalism, which belongs to Unit 4. Nothing else
here can be cited, because the CED defines none of the four. Every classification
key therefore rests on the definitions set out in the module header:

    acculturation     adoption WITH substantial retention
    assimilation      distinctive traits largely LOST
    syncretism        two traditions FUSED into a third form
    multiculturalism  several cultures COEXISTING, distinctiveness maintained

THE STRUCTURE THAT ORGANIZES THEM, and the reason most items are comparative:
acculturation and assimilation are two points on ONE scale (how much survives),
syncretism is not a point on that scale at all (it is a fusion), and
multiculturalism describes the SOCIETY rather than a group inside it. Items 5,
7, 9, 13, 15 and 21 each turn on keeping those three kinds of claim apart, and
item 7 asks directly which of the four is a property of a society.

TWO PLACES THIS MODULE REFUSES A TIDY ANSWER, both deliberate:

  * Item 19 keys against the claim that acculturation is "the first stage of
    assimilation". Communities have remained acculturated and distinct for
    centuries, so treating retention as temporary builds a prediction into a
    definition. The tidy answer here would be the wrong one.
  * Item 25 keys to "it depends on the size and concentration of the group, its
    institutions, and how the receiving society responds" rather than to any
    outcome. The CED lists four effects side by side without ranking them, which
    is itself the claim that circumstances select among them.

ON POLITICAL WEIGHT. These four terms are contested and assimilation in
particular has been demanded of minorities by force. Every item asks what a
process IS or what conditions produce it; none asks whether it is desirable,
because that question has no answer a key could defend. Items 10 and 24 name
coercion where it is present rather than describing state pressure as though it
were ordinary contact.

The five table items (26-30) are the computational gate, and 26 and 27 are a
deliberate PAIR -- the same two columns for two communities, giving acculturation
in one case and assimilation in the other. The recomputes assert the contrast
rather than each case in isolation:

  26  home-language use falls only to 58 percent while fluency reaches 99
  27  home-language use collapses to 4 percent while fluency reaches 100
  28  two elements from each tradition plus one combined -- fusion, not transfer
  29  all four communities receive all three forms of public support
  30  retention ranges 80 points across four domains of one community

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Items 26 and 27 both carry two INDEPENDENT
percentage columns that do not sum to 100, and the recomputes assert that, since
reading them as a composition is the error the tables invite.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_8


def _language_series(table):
    """The two independent percentage columns, in generation order."""
    rows = []
    order = {"First": 0, "Second": 1, "Third": 2}
    for row in table["rows"]:
        d = rowdict(table, row)
        rows.append((order[d["Generation"]],
                     num(d["Speak the community language at home (%)"]),
                     num(d["Speak the national language fluently (%)"])))
    rows.sort()
    return [h for _, h, _ in rows], [n for _, _, n in rows]


def q26_acculturation(table):
    """Fluency reaches nearly all; home use stays a majority."""
    home, national = _language_series(table)
    # The two columns are independent shares, not a composition.
    assert any(h + n != 100 for h, n in zip(home, national)), (home, national)
    assert national[-1] >= 99, national
    assert home[-1] > 50, home
    assert home[0] > 90 and national[0] < 40, (home, national)
    # Home use falls, but far less than fluency rises.
    assert (home[0] - home[-1]) < (national[-1] - national[0]), (home, national)
    return "a majority still uses the community language at home"


def q27_assimilation(table):
    """Home use collapses while fluency reaches everyone."""
    home, national = _language_series(table)
    assert any(h + n != 100 for h, n in zip(home, national)), (home, national)
    assert national[-1] == 100, national
    assert home[-1] <= 5, home
    assert home[0] > 90, home
    # The contrast with item 26 is the point: that community kept a majority.
    other_home, _ = _language_series(g3_8.QUESTIONS[25]["table"])
    assert other_home[-1] > 50 > home[-1], (other_home, home)
    return "fallen to 4 percent"


def q28_syncretism_elements(table):
    """Elements from both traditions, plus one combined -- a fused form."""
    sources = [rowdict(table, r)["Source"] for r in table["rows"]]
    local = sum(1 for s in sources if s == "Pre-existing local tradition")
    arriving = sum(1 for s in sources if s == "Arriving tradition")
    combined = sum(1 for s in sources if s.startswith("Both"))
    assert local == 2 and arriving == 2 and combined == 1, sources
    # Neither tradition may dominate, or the case would be transfer rather than
    # fusion.
    assert local == arriving, sources
    assert combined >= 1, sources
    return "elements of both traditions are fused"


def q29_multiculturalism(table):
    """All four communities receive all three forms of public support."""
    n = 0
    for row in table["rows"]:
        d = rowdict(table, row)
        assert num(d["Publicly funded schools in the community language"]) > 0, d
        assert num(d["Community associations receiving public funds"]) > 0, d
        assert d["Public signage in the community language"] == "Yes", d
        n += 1
    assert n == 4, n
    return "public institutions support four communities"


def q30_uneven_retention(table):
    """Retention spans a very wide range across the four domains."""
    vals = {rowdict(table, r)["Domain"]:
            num(rowdict(table, r)["Households still practising (%)"])
            for r in table["rows"]}
    assert len(vals) == 4, vals
    lo, hi = min(vals.values()), max(vals.values())
    assert hi - lo >= 75, vals
    assert min(vals, key=vals.get) == "Community language at home", vals
    assert max(vals, key=vals.get) == "Cuisine at family occasions", vals
    # Three of the four must remain substantial, or this would be assimilation.
    assert sum(1 for v in vals.values() if v > 60) == 3, vals
    return "language nearly lost while cuisine, festivals, and observance persist"


CLAIMS = [
 ("Acculturation, assimilation, syncretism, and multiculturalism",
  "EK SPS-3.B.1 names exactly these four as effects of the diffusion of culture. Creolization belongs to Topic 3.5's statement, relocation and expansion are types of diffusion from Topic 3.4, and migration and urbanization are processes rather than effects."),

 ("traits of the host culture have been adopted while substantial elements",
  "EK SPS-3.B.1 names acculturation among the effects of diffusion without defining it, and the standard definition is partial adoption with substantial retention. Both cultures remain identifiable in the community's practice, which is what separates it from assimilation."),

 ("distinctive traits have largely been lost",
  "EK SPS-3.B.1 names assimilation among the effects of diffusion. It differs from acculturation in degree rather than in kind: distinctive traits are not merely supplemented but largely gone, which is usually the work of several generations."),

 ("two traditions have blended into a combined form",
  "EK SPS-3.B.1 names syncretism among the effects of diffusion, and its defining feature is fusion rather than coexistence or replacement. Neither tradition is intact and neither has vanished; what exists is a third form built out of both."),

 ("How much of the original culture survives",
  "EK SPS-3.B.1 lists both effects without defining either, and the standard distinction between them is one of degree along a single dimension. Both can be voluntary or coerced and both operate on groups, so neither of those axes separates them."),

 ("organized to let several cultures coexist while remaining distinct",
  "EK SPS-3.B.1 names multiculturalism among the effects of diffusion. Unlike the other three it describes the SOCIETY rather than a group inside it, and it is frequently a deliberate arrangement rather than an outcome nobody chose."),

 ("Multiculturalism",
  "Acculturation and assimilation describe what happens to a group's traits and syncretism describes what happens to two traditions, while multiculturalism describes how a society is arranged. That is why it is the one term of the four that can be a stated policy."),

 ("keeping enough of its own that it remains culturally distinguishable",
  "EK SPS-3.B.1 lists both terms, and using them together this way places a community at a particular point on the retention scale. The claim is precise: substantial adoption has occurred and substantial distinctiveness has survived it."),

 ("produces a fused third form",
  "EK SPS-3.B.1 lists syncretism and acculturation separately, and the difference is what the result looks like. An acculturated community does some things one way and some the other; a syncretic form cannot be separated back into its sources."),

 ("pursued by state coercion rather than arising through ordinary contact",
  "EK SPS-3.B.1 names assimilation among the effects of diffusion without saying how it comes about, and it can arise gradually or be demanded by a state. Naming the mechanism is what makes the description accurate, since the outcome sought is the same in either case."),

 ("without the original being displaced",
  "EK SPS-3.B.1's acculturation is adoption with retention, and holding both repertoires intact is exactly that. Syncretism would require the two to have fused into something new rather than remaining separately available."),

 ("no longer transmitted to children",
  "EK SPS-3.B.1 lists both effects and the difference between them is retention, which is measured by what passes to the next generation. Adopting a working language or a holiday is compatible with keeping everything else, whereas the end of transmission is not."),

 ("schools in several community languages, matched to multiculturalism",
  "EK SPS-3.B.1 names all four terms, and only this pairing attaches a case to the term whose defining feature it actually has. Losing a language entirely is assimilation, fusion is syncretism, and adding a language while keeping the first is acculturation."),

 ("blend that belongs to neither parent",
  "EK SPS-3.A.1 names creolization among the new forms interaction produces and EK SPS-3.B.1 names syncretism among the effects of diffusion. The underlying idea is the same fusion into a third form, and the difference is which process the CED attaches each to."),

 ("describes how a society is arranged and can therefore be legislated for",
  "EK SPS-3.B.1's multiculturalism describes an arrangement of a society rather than a change inside a group, and arrangements are what policy makes. Assimilation has also been pursued by policy, but it is an outcome rather than a way of organizing coexistence."),

 ("Group size, spatial concentration, institutional support",
  "EK SPS-3.B.1 lists acculturation and assimilation as effects rather than inevitabilities, so the rate at which either occurs must depend on conditions. A large, concentrated community with its own institutions can transmit practices a small dispersed one cannot."),

 ("fused into a locally distinctive form",
  "EK SPS-3.B.1 names syncretism among the effects of diffusion. The diagnostic is that the result exists in neither source region, since a form that could be found intact elsewhere would be diffusion without fusion."),

 ("different groups, different generations, and different domains",
  "EK SPS-3.B.1 lists four effects without ordering them or making them exclusive. One community may be assimilating while another acculturates, a religious practice fuses, and the city's institutions operate multiculturally, all in the same year."),

 ("can persist indefinitely without leading to assimilation",
  "EK SPS-3.B.1 lists the two as separate effects rather than as points on a required sequence. Communities have remained acculturated and distinct for centuries, so treating retention as temporary would build a prediction into a definition."),

 ("several cultures coexist while remaining distinct",
  "EK SPS-3.B.1 names multiculturalism as an effect of diffusion and it describes coexistence with maintained distinctiveness. That each community also adapts somewhat is a separate observation about each group rather than about the district."),

 ("calendars, figures, and rituals that can be recombined",
  "EK SPS-3.B.1 names syncretism without restricting it to religion, so the explanation must be about why the case is common rather than exclusive. Faiths carry many separable elements, and arriving traditions have often gained adherents faster by absorbing local practice than by forbidding it."),

 ("uneven across domains",
  "EK SPS-3.B.1's acculturation is partial adoption with retention, and nothing requires the partition to fall the same way in every domain. Language shifts fastest because school and work require it, while food and music carry no comparable pressure."),

 ("Nationalism",
  "This is a NOT question, and EK SPS-3.B.1's list contains acculturation, assimilation, syncretism and multiculturalism and only those four. Nationalism is a political force treated in Unit 4 rather than an effect of cultural diffusion named here."),

 ("From a policy pursuing assimilation to one supporting multiculturalism",
  "EK SPS-3.B.1 names both assimilation and multiculturalism among the effects of diffusion, and a state can pursue either. Requiring abandonment aims at the loss of distinctiveness while funding institutions aims at its maintenance, which are opposite goals."),

 ("depends on the size and concentration of the arriving group",
  "EK SPS-3.B.1 lists four effects side by side without ranking them or making any inevitable. The listing itself implies that circumstances select among them, which is why an honest general statement names the circumstances rather than an outcome."),

 ("a majority still uses the community language at home",
  "Recomputed from the table: national language fluency rises from 34 to 99 percent while home use of the community language falls only from 97 to 58, so a majority still transmits it. The verifier also confirms the two columns are independent shares rather than a composition summing to 100.",
  q26_acculturation),

 ("fallen to 4 percent",
  "Recomputed from the table: home use collapses from 94 to 4 percent across three generations while national fluency reaches 100. The verifier compares this directly against the previous item's community, which kept a majority, since the pair of tables is what shows the two outcomes differ in degree.",
  q27_assimilation),

 ("elements of both traditions are fused",
  "Recomputed from the table: two elements come from each tradition and one is a combination of both, so neither tradition is intact and neither has been replaced. EK SPS-3.B.1's syncretism is exactly a fused form, and one existing in neither source region cannot be simple transfer.",
  q28_syncretism_elements),

 ("public institutions support four communities",
  "Recomputed from the table: all four communities receive funded schools, funded associations and public signage in their own languages. EK SPS-3.B.1's multiculturalism is the only one of the four terms describing an arrangement of a society rather than a change within a group.",
  q29_multiculturalism),

 ("language nearly lost while cuisine, festivals, and observance persist",
  "Recomputed from the table: retention runs from 11 percent for language to 91 percent for cuisine, a range of 80 points, with three of the four domains still above 60. Partial adoption with retention is acculturation, and nothing requires the partition to fall the same way in every part of cultural life.",
  q30_uneven_retention),
]

hg_check.check(g3_8, CLAIMS, per_topic=30, n_choices=5)
