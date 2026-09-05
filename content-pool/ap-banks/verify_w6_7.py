"""Key audit for AP WORLD HISTORY: MODERN 6.7 Effects of Migration.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate is ``wh_check.run``, the shared World History gate: ``cg_check.check``
for structure and anchors, ``es_check.style`` for notation (World History is a
prose subject that ``export_units.py`` does not typeset), plus the two rules
history adds -- a CED citation in every ``why`` and every ``claim``, and no
figure language, since the bank cannot display an image.

WHAT THE KEYS REST ON
---------------------
This topic prints three historical developments:

    KC-5.4.III.A  Migrants tended to be male, leaving women to take on new roles
                  in the home society that had been formerly occupied by men.
    KC-5.4.III.B  Migrants often created ethnic enclaves in different parts of the
                  world that helped transplant their culture into new environments.
    KC-5.4.III.C  Receiving societies did not always embrace immigrants, as seen in
                  the various degrees of ethnic and racial prejudice and the ways
                  states attempted to regulate the increased flow of people across
                  their borders.

Items 1, 2, 14 rest on KC-5.4.III.A; items 3, 4, 15, 18 on KC-5.4.III.B; items
5, 6, 16, 17, 19 on KC-5.4.III.C. Items 7 to 11 rest on the CED's printed enclave
list and ask only for the REGIONS it prints, which is the only thing that list
settles. Items 12 and 13 rest on the CED naming the Chinese Exclusion Act and the
White Australia policy under its Regulation of immigrants heading. Item 27 rests
on Unit 6 Learning Objective H, item 28 on the Social Interactions and
Organization thematic focus, and items 29 and 30 are reasoning items about what
the three statements do and do not settle.

WHAT THE CED DOES NOT SAY, AND WHAT NO ITEM THEREFORE ASKS. The framework names
the Chinese Exclusion Act and the White Australia policy and states not one word
about what either provided, when it was made, by whom, or how long it lasted.
Both items that use them ask only which heading they are printed under. Item 29
makes that silence its subject, which is the honest way to use a name the source
does not explain.

TWO SWAPS THIS TOPIC INVITES.
  1. KC-5.4.III.A moves roles to WOMEN in the HOME society. Item 2 offers the
     reversal of the sexes and the relocation of the change to the receiving
     society, so its anchor carries both clauses.
  2. KC-5.4.III.C is QUALIFIED -- receiving societies did NOT ALWAYS embrace
     immigrants -- and "never embraced" overshoots it as badly as "always did".
     Items 5 and 6 turn on the qualification and their anchors carry it.

DATA ITEMS: 20 to 26 carry tables labelled hypothetical in the stem, and every
keyed conclusion is recomputed below from that table alone. Row labels are
matched EXACTLY rather than by substring, because ``es_check._corrupt`` appends
" CORRUPTED" to a cell and a substring test would still read the corrupted label
as its original -- the control would pass while proving nothing.

NEGATIVE CONTROL: ``python3 verify_w6_7.py --selftest`` runs wh_check's full
control set -- every key rotated, every anchor broken, every table cell
corrupted, every banned notation form injected against legal prose that must
pass, figure language injected against the two phrases this project has seen
falsely flagged, an uncited why and an uncited claim, a duplicate choice, a thin
why and a why naming an option by letter -- and each control asserts WHICH
message came back. It then runs legal-value controls on the guards the cell
corruption cannot reach, since a corrupted cell trips the label vocabulary or a
percentage bound before the guard under test ever runs.
"""
import sys

import cg_check as cg
import wh_check as wh
import w6_7

MEN = "Men among every hundred arrivals"
WOMEN = "Women among every hundred arrivals"
RECORDS = ["Record 1", "Record 2", "Record 3", "Record 4"]

BEFORE = "Households in which a woman performed it before the departures, out of one hundred"
AFTER = "Households in which a woman performed it after the departures, out of one hundred"
HOLDING = "Managing the family holding"
MARKET = "Selling produce at market"
HIRING = "Hiring seasonal labour"
WEAVING = "Weaving cloth for household use"
NEW_ROLES = (HOLDING, MARKET, HIRING)

COUNT = "Number recorded in the quarter"
WORSHIP = "Places of worship of the migrants' own tradition"
SCHOOLS = "Schools teaching the migrants' language"
SOCIETIES = "Mutual aid societies formed by the migrants"
PAPERS = "Newspapers printed in the migrants' language"

ADMITTED = "Admitted for every hundred who applied"
NEIGHBOUR = "Applicants from the neighbouring country"
CAPITAL = "Applicants holding capital above a stated sum"
RESTRICTED = "Applicants from a country whose nationals the state had restricted"
LABOURERS = "Labourers from that restricted country"


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _by_label(table, expected):
    """Rows keyed by an EXACT first-column label drawn from `expected`.

    Exact membership, never a substring test. The negative control corrupts a
    cell by appending " CORRUPTED"; a substring test would still read
    "Hiring seasonal labour CORRUPTED" as the hiring row, and the control would
    pass without exercising anything.
    """
    rows = _rows(table)
    label_col = table["headers"][0]
    got = [r[label_col] for r in rows]
    assert got == list(expected), f"row labels must be {list(expected)}, not {got}"
    return {r[label_col]: r for r in rows}


def _arrivals(table):
    by = _by_label(table, RECORDS)
    out = {}
    for name in RECORDS:
        m, w = cg.num(by[name][MEN]), cg.num(by[name][WOMEN])
        # The stem says "of every hundred arrivals", so the row must add to a
        # hundred. This is also what catches a corrupted count: the control
        # multiplies a cell by three and adds eleven, and no such value keeps the
        # row summing to 100.
        assert m + w == 100, f"{name} gives {m:g} men and {w:g} women, which is not a hundred"
        out[name] = (m, w)
    return out


def q20(table, item):
    a = _arrivals(table)
    assert all(m > w for m, w in a.values()), \
        f"men must lead in every record for the keyed pattern: {a}"
    assert not any(w > m for m, w in a.values()), "'women outnumbered men' must be false"
    assert not any(m == w for m, w in a.values()), "'equal numbers' must be false"
    assert len(a) == 4, "the stem says four arrival records"
    return ("men lead women in all four records, at 78 to 22, 71 to 29, 84 to 16 and "
            "66 to 34")


def q21(table, item):
    a = _arrivals(table)
    gaps = {k: abs(m - w) for k, (m, w) in a.items()}
    # UNIQUENESS BEFORE IDENTITY, and the order is load-bearing. min() returns the
    # first row holding the minimum, so a TIE for narrowest would be reported as
    # "the narrowest gap is Record 2" -- a control aimed at the tie guard would
    # fire on the identity assert and prove nothing about the guard it named. This
    # was caught by the control asserting on the message, not by reading the code.
    assert len(set(gaps.values())) == len(gaps), \
        f"two records share a gap, so the keyed record is not the unique answer: {gaps}"
    closest = min(gaps, key=gaps.get)
    assert closest == "Record 4", f"the narrowest gap is {closest}, not Record 4"
    return f"the gaps between the two columns are {gaps}, narrowest at Record 4"


def _tasks(table):
    by = _by_label(table, [HOLDING, MARKET, HIRING, WEAVING])
    out = {}
    for name in (HOLDING, MARKET, HIRING, WEAVING):
        b, a = cg.num(by[name][BEFORE]), cg.num(by[name][AFTER])
        # Both columns are counts out of one hundred households, so a value
        # outside 0 to 100 is not a reading at all. This is the bound that catches
        # a corrupted number.
        for v, which in ((b, "before"), (a, "after")):
            assert 0 <= v <= 100, f"{name} {which} is {v:g}, which is not a count out of a hundred"
        out[name] = (b, a)
    return out


def q22(table, item):
    t = _tasks(table)
    for name in NEW_ROLES:
        b, a = t[name]
        assert b < 25, f"{name} starts at {b:g}, which is not a task women had seldom performed"
        assert a > 40, f"{name} ends at {a:g}, which is not a task that passed largely to women"
        assert a - b > 30, f"{name} rises only {a - b:g}"
    b, a = t[WEAVING]
    assert b > 80, f"weaving starts at {b:g}, which is not a task women already performed"
    assert abs(a - b) <= 5, f"weaving changes by {a - b:g}, which is not little"
    rises = {k: v[1] - v[0] for k, v in t.items()}
    assert rises[WEAVING] == min(rises.values()), \
        "'the task women already performed showed the largest change' must be false"
    assert len(set(rises.values())) > 1, "'in equal measure' must be false"
    assert any(v > 0 for v in rises.values()), "'fewer of every task' and 'no change' must be false"
    return (f"the three formerly male tasks rise {[rises[k] for k in NEW_ROLES]} while "
            f"weaving, already at {b:g}, moves {rises[WEAVING]:g}")


def q23(table, item):
    t = _tasks(table)
    rises = {k: v[1] - v[0] for k, v in t.items()}
    # Uniqueness before identity, for the reason set out in q21 above.
    assert len(set(rises.values())) == len(rises), \
        f"two tasks share a rise, so the keyed task is not the unique answer: {rises}"
    top = max(rises, key=rises.get)
    assert top == HOLDING, f"the largest rise is {top}, not managing the family holding"
    assert rises[WEAVING] < 0, "'every task rose by the same amount' must be false"
    return f"the changes are {rises}, largest at managing the family holding"


def q24(table, item):
    by = _by_label(table, [WORSHIP, SCHOOLS, SOCIETIES, PAPERS])
    v = {k: cg.num(by[k][COUNT]) for k in (WORSHIP, SCHOOLS, SOCIETIES, PAPERS)}
    for k, n in v.items():
        assert n > 0, f"{k} is not recorded in the quarter, so the keyed plural is wrong"
    # The key claims a quarter sustaining worship, language and mutual assistance
    # together. No single kind may swamp the rest, or the plural claim is not what
    # the table shows -- and this is the guard that catches a corrupted count,
    # which a bare "is it still the largest" test would survive.
    biggest = max(v, key=v.get)
    assert v[biggest] < sum(n for k, n in v.items() if k != biggest), \
        f"{biggest} at {v[biggest]:g} outweighs every other kind combined"
    assert v[SOCIETIES] > v[PAPERS], "'more newspapers than mutual aid societies' must be false"
    assert v[SOCIETIES] > v[SCHOOLS], "'more schools than mutual aid societies' must be false"
    assert len(v) == 4, "'the only institutions were places of worship' must be false"
    return (f"all four kinds are present at {[v[k] for k in (WORSHIP, SCHOOLS, SOCIETIES, PAPERS)]}, "
            "and no one kind outweighs the others combined")


def _admission(table):
    by = _by_label(table, [NEIGHBOUR, CAPITAL, RESTRICTED, LABOURERS])
    v = {k: cg.num(by[k][ADMITTED]) for k in (NEIGHBOUR, CAPITAL, RESTRICTED, LABOURERS)}
    for k, n in v.items():
        assert 0 <= n <= 100, f"{k} is {n:g}, which is not a rate for every hundred applying"
    return v


def q25(table, item):
    v = _admission(table)
    high = (v[NEIGHBOUR], v[CAPITAL])
    low = (v[RESTRICTED], v[LABOURERS])
    assert min(high) > 80, f"the admitted categories stand at {high}, not high rates"
    assert max(low) < 20, f"the restricted categories stand at {low}, not low rates"
    assert min(high) > max(low), "the two groups of rates must not overlap"
    assert len(set(v.values())) > 1, "'about the same rate' must be false"
    assert v[RESTRICTED] < v[NEIGHBOUR], \
        "'the restricted country admitted more readily than their neighbours' must be false"
    assert min(v.values()) > 0, "'admitted no applicant in any category' must be false"
    return (f"origin and means separate the rates: {high} admitted against {low}, with no "
            "overlap between the two groups")


def q26(table, item):
    v = _admission(table)
    lowest = min(v, key=v.get)
    assert lowest == LABOURERS, f"the lowest rate belongs to {lowest}, not the restricted labourers"
    assert v[LABOURERS] == 4, \
        f"the keyed choice quotes four in every hundred; the record gives {v[LABOURERS]:g}"
    assert v[NEIGHBOUR] == 94, \
        f"a rejected option quotes ninety-four; the record gives {v[NEIGHBOUR]:g}"
    assert v[CAPITAL] < v[NEIGHBOUR], \
        "the rejected option about capital and neighbours must be TRUE of the record"
    assert len(v) == 4, "'the record distinguishes four categories' must be true"
    return ("the lowest rate in the record is 4 in every hundred, which is what refutes a "
            "claim that everyone who applied was admitted")


TABLE_CHECKS = {20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

CLAIMS = [
 ("Migrants tended to be male",
  "KC-5.4.III.A opens by stating that migrants tended to be male. The framework does make a statement about the sex of migrants, so the option denying that is false, and it describes a tendency rather than an even division in every stream."),
 ("Women in the home society took on new roles that had formerly been occupied by men",
  "KC-5.4.III.A states that migrants tending to be male left WOMEN to take on new roles in the HOME society that had been formerly occupied by MEN. Which sex takes up which roles, and in which society, are the whole content of that clause, so the anchor carries both because the reversal and the relocation to the receiving society are both offered."),
 ("helped transplant the migrants' culture into new environments",
  "KC-5.4.III.B states that migrants often created ethnic enclaves in different parts of the world that helped transplant their culture into new environments. Border regulation belongs to KC-5.4.III.C, and abandoning a culture is the opposite of transplanting it."),
 ("In different parts of the world",
  "KC-5.4.III.B places the enclaves in different parts of the world, and the CED's own list runs across Southeast Asia, the Caribbean, South America, North America and East and Southern Africa. That breadth is what makes each restricting option false."),
 ("Receiving societies did not always embrace immigrants",
  "KC-5.4.III.C verbatim, and the qualification is the framework's own: a claim that receiving societies always embraced immigrants and a claim that they never admitted any are both stronger than the sentence, and indifference is not what a statement about prejudice and regulation describes."),
 ("Various degrees of ethnic and racial prejudice, and the ways states attempted to regulate the flow of people across their borders",
  "KC-5.4.III.C names exactly those two things as where the treatment of immigrants could be seen. Wages, routes, enclave size and rates of return are not what that sentence points to, and encouraging further immigration is the reverse of regulating it."),
 ("Southeast Asia, the Caribbean, South America and North America",
  "The CED prints Chinese in Southeast Asia, the Caribbean, South America, and North America under Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. Each rejected option is a real list from that same heading belonging to the Indian, Irish or Italian entry."),
 ("East and Southern Africa, the Caribbean and Southeast Asia",
  "The CED prints Indians in East and Southern Africa, the Caribbean, and Southeast Asia under Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. The Chinese, Irish and Italian entries in the same list supply the other combinations offered."),
 ("Indians",
  "The CED's enclave list for topic 6.7 places Indians in East and Southern Africa and no other group in Africa: the Chinese entry runs through Southeast Asia and the Americas, the Irish entry is North America, the Italian entry North and South America. Japanese agricultural workers belong to topic 6.6's returning migrants. KC-5.4.III.B is the statement all of these illustrate."),
 ("Irish",
  "The CED prints Irish in North America under Migrant ethnic enclaves for topic 6.7 with no second region beside it, while Italians are listed in North and South America and the Chinese and Indian entries each run across several regions. Lebanese merchants belong to topic 6.6's returning migrants. KC-5.4.III.B is the statement illustrated."),
 ("North and South America",
  "The CED prints Italians in North and South America under Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. Naming one continent alone drops half the entry, and the remaining options belong to the Chinese and Indian entries in the same list."),
 ("The Chinese Exclusion Act and the White Australia policy",
  "The CED prints those two, and only those two, under its heading Regulation of immigrants for topic 6.7, illustrating KC-5.4.III.C. The Opium Wars and the Port of Buenos Aires illustrate economic imperialism in topic 6.5 and the remaining names belong to topic 6.3. The item asks which pair the framework names and asserts nothing about what either measure provided, because the CED says nothing about that."),
 ("states attempted to regulate the increased flow of people across their borders",
  "The CED prints the Chinese Exclusion Act under Regulation of immigrants for topic 6.7, beside KC-5.4.III.C, which is the statement the example illustrates. The four rejected options are KC-5.4.III.B, KC-5.4.III.A, KC-5.4.II.A and KC-5.4.I.B, each a real statement of this unit and none the one printed beside this example. Nothing about the measure's content is asserted, because the CED states none."),
 ("That women in the home society took on roles formerly occupied by men",
  "KC-5.4.III.A states that migrants tending to be male left women to take on new roles in the home society formerly occupied by men, and an unattributed village letter reporting that wives and mothers now sow and keep accounts is that clause in a source. Enclaves, prejudice, border regulation and return are separate statements of this unit."),
 ("an ethnic enclave that helped transplant a culture into a new environment",
  "KC-5.4.III.B states that ethnic enclaves helped transplant the migrants' culture into new environments, and worship, a newspaper and associations of the migrants' own are the institutions that do it. The source is unattributed and illustrative, and it describes no border regulation, no abandoning of culture and no change of roles."),
 ("prejudice being one form that took",
  "KC-5.4.III.C states that receiving societies did not always embrace immigrants, as seen in the various degrees of ethnic and racial prejudice, and an argument that a group cannot be made part of a people is prejudice of that kind. The anchor carries the qualifying half so it cannot match an option asserting that receiving societies always embraced immigrants."),
 ("a state attempting to regulate the increased flow of people across its border",
  "KC-5.4.III.C names the ways states attempted to regulate the increased flow of people across their borders, and a statute admitting some categories of one nationality while barring others is regulation of that kind. The statute in the item is unattributed and illustrative, and no provision of any real measure is asserted anywhere."),
 ("That ethnic enclaves helped transplant the migrants' culture into new environments",
  "KC-5.4.III.B states that migrants often created ethnic enclaves that helped transplant their culture into new environments, and a school in the migrants' language and the festivals of their calendar are that transplanting in practice. The framework says nothing about receiving states funding such institutions, and the last two options contradict KC-5.4.III.B and KC-5.4.III.A."),
 ("how the district's residents understood their own situation",
  "This key rests on the logic of evidence rather than on a framework assertion: a report written from the receiving state's side is good evidence of what that administration valued and poor evidence of the residents' own understanding, which it does not record. KC-5.4.III.C makes the attitude of receiving societies part of this topic, which is why an official source's point of view matters here."),
 ("In every record men outnumbered women among the arrivals",
  "Recomputed in q20 above: 78 to 22, 71 to 29, 84 to 16 and 66 to 34, so men lead in all four rows and every row is checked to sum to a hundred. KC-5.4.III.A states that migrants tended to be male, which is the tendency the record sets out."),
 ("Record 4",
  "Recomputed in q21 above: the gaps between the two columns are 56, 42, 68 and 32, narrowest at Record 4, and no two records tie, so the keyed record is the unique answer. KC-5.4.III.A describes a tendency, which is consistent with streams differing in how pronounced it is."),
 ("while the task they already performed changed little",
  "Recomputed in q22 above: managing the holding runs 12 to 57, selling produce 19 to 61 and hiring labour 7 to 44, while weaving, already at 88, ends at 86. KC-5.4.III.A speaks of NEW roles formerly occupied by men, and a task women already performed is not a new role, which is why it moves differently. The anchor carries the second clause because a distractor puts the largest change on that task."),
 ("Managing the family holding",
  "Recomputed in q23 above: the changes are a rise of 45 for managing the holding, 42 for selling produce, 37 for hiring labour and a fall of 2 for weaving, with no tie, so the keyed task is the unique answer. KC-5.4.III.A is the statement about new roles the record illustrates."),
 ("sustained institutions of the migrants' own worship, language and mutual assistance",
  "Recomputed in q24 above: six places of worship, four schools, nine mutual aid societies and three newspapers, all present and none outweighing the rest combined, with mutual aid societies above both the schools and the newspapers. KC-5.4.III.B states that ethnic enclaves helped transplant the migrants' culture into new environments, and these are the institutions through which that happens."),
 ("Admission turned on where an applicant came from and on the means they held",
  "Recomputed in q25 above: 94 and 89 admitted for every hundred applying against 11 and 4, with no overlap between the two groups of rates. KC-5.4.III.C describes the ways states attempted to regulate the increased flow of people across their borders, and a rate varying this widely by category is such an attempt."),
 ("Four in every hundred labourers from the restricted country were admitted",
  "Recomputed in q26 above: the lowest rate in the record is 4 in every hundred, which is what refutes a claim that everyone who applied was admitted. The rejected options are each checked to be TRUE of the record and to leave the claim standing, and KC-5.4.III.C is the statement about regulated borders the record illustrates."),
 ("Why did the departure of many men change what women did in the societies they left?",
  "Unit 6 Learning Objective H asks students to explain how and why new patterns of migration affected society from 1750 to 1900, and KC-5.4.III.A is such an effect with its cause attached. Dates, totals, rankings and lists of names are not what that objective asks for, and the framework prints none of them for this topic."),
 ("migration changed how societies grouped their members and how those groups treated one another",
  "The Social Interactions and Organization focus concerns the process by which societies group their members and the norms governing interactions between those groups. KC-5.4.III.A changes roles within a home society, KC-5.4.III.B creates new groups within receiving ones and KC-5.4.III.C concerns how those groups were treated."),
 ("What kinds of effect the framework identifies can be answered; what any named measure provided cannot",
  "KC-5.4.III.A, KC-5.4.III.B and KC-5.4.III.C name the kinds of effect and the CED prints the enclave regions, so those are answerable. The Chinese Exclusion Act and the White Australia policy are NAMED with no provision, date or number attached, so nothing about their content can be. The anchor carries both clauses because the exact reversal is offered."),
 ("created enclaves that carried their culture abroad, and met treatment in receiving societies that ranged from acceptance to prejudice and legal restriction",
  "KC-5.4.III.A gives the change in the home society, KC-5.4.III.B the enclaves that transplanted culture into new environments and KC-5.4.III.C the qualified reception, including prejudice and attempts at regulation. The key holds all three together and each rejected option deletes one side of the account."),
]


# --------------------------------------------------------- legal-value controls
#
# wh_check's cell control appends " CORRUPTED", which trips the exact label
# vocabulary in _by_label, and multiplies a number by three and adds eleven,
# which the "sums to a hundred" and "is a rate out of a hundred" bounds catch
# first. Both are real guards, but neither is the guard that makes a keyed row
# the ONLY defensible answer. So each of those gets a control that substitutes
# one LEGAL value for another: the table stays well formed and the only thing
# that changes is whether the key still stands alone. Each control asserts on the
# MESSAGE, because a control that fires for the wrong reason proves nothing about
# the guard it names.

def _fires(base, mutate, check, needle, label):
    import copy
    table = copy.deepcopy(base)
    mutate(table["rows"])
    try:
        check(table, None)
    except AssertionError as exc:
        assert needle in str(exc), \
            f"CONTROL FIRED FOR THE WRONG REASON ({label}): expected {needle!r}, got {exc}"
        return
    raise SystemExit(f"CONTROL FAILED: {label} -- {check.__name__} accepted the mutation")


def legal_value_control():
    ar, ts, qu, ad = (w6_7._T_ARRIVALS, w6_7._T_TASKS, w6_7._T_QUARTER, w6_7._T_ADMISSION)

    def flip_record_3(rows):
        rows[2][1], rows[2][2] = "16", "84"      # still sums to a hundred
    _fires(ar, flip_record_3, q20, "men must lead in every record",
           "item 20 with one record where women lead")

    def tie_the_gap(rows):
        rows[1][1], rows[1][2] = "66", "34"      # Record 2 now ties Record 4 at 32
    _fires(ar, tie_the_gap, q21, "two records share a gap",
           "item 21 with two records equally close to an even division")

    def move_the_narrowest(rows):
        # 80 and 20 keep the row summing to a hundred and give Record 4 a gap of 60,
        # which is distinct from 56, 42 and 68 -- so this control reaches the
        # identity assert instead of tripping the tie guard on the way past.
        rows[3][1], rows[3][2] = "80", "20"
    _fires(ar, move_the_narrowest, q21, "the narrowest gap is Record 2",
           "item 21 with the narrowest gap moved to another record")

    _fires(ts, lambda rows: rows[3].__setitem__(1, "30"), q22,
           "which is not a task women already performed",
           "item 22 with the already-female task made a formerly male one")
    _fires(ts, lambda rows: rows[2].__setitem__(2, "60"), q23,
           "the largest rise is Hiring seasonal labour",
           "item 23 with a new largest rise")
    # 14 is a legal count and still the largest, but it now outweighs the other
    # three combined, which is what the plural key asserts it does not.
    _fires(qu, lambda rows: rows[2].__setitem__(1, "14"), q24,
           "outweighs every other kind combined",
           "item 24 with one kind of institution swamping the rest")
    # 95 is a legal rate, and it removes the separation the key rests on.
    _fires(ad, lambda rows: rows[2].__setitem__(1, "95"), q25,
           "not low rates", "item 25 with the restricted category admitted freely")
    # 8 is a legal rate and still the lowest in the record, so this control reaches
    # the guard that pins the figure the keyed choice quotes rather than tripping
    # the identity assert on the way past. 30 makes another category the lowest,
    # which is the identity assert's own control.
    _fires(ad, lambda rows: rows[3].__setitem__(1, "8"), q26,
           "the record gives", "item 26 with the quoted figure moved off four")
    _fires(ad, lambda rows: rows[3].__setitem__(1, "30"), q26,
           "the lowest rate belongs to", "item 26 with the lowest rate moved to another category")

    # POSITIVE control: the same seven checks must ACCEPT the module's own tables,
    # so a check that rejected everything would be caught here rather than counted
    # as seven successes.
    for fn in (q20, q21):
        fn(ar, None)
    for fn in (q22, q23):
        fn(ts, None)
    q24(qu, None)
    for fn in (q25, q26):
        fn(ad, None)
    print("  control OK  every uniqueness and separation guard fires on a legal-value "
          "mutation, for the reason it names, and passes the real tables")


if "--selftest" in sys.argv:
    legal_value_control()

wh.run(w6_7, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
