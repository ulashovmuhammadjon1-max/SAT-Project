"""Key audit for AP WORLD HISTORY: MODERN 1.1 (Unit 1, East Asia c. 1200 to c. 1450).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code, so a later reader can check the history rather than take it on
trust.

WHAT THE KEYS REST ON
---------------------
Every key here traces to one of six sentences and three thematic-focus
statements printed on this topic's CED pages:

  KC-3.2.I.A       states of the 13th century showed continuity, innovation and
                   diversity; the Song used traditional methods of Confucianism
                   and an imperial bureaucracy to maintain AND JUSTIFY its rule
  KC-3.1.III.D.i   Chinese cultural traditions continued and influenced
                   neighboring regions
  KC-3.1.III.D.ii  Buddhism and its core beliefs continued to shape societies in
                   Asia, in a variety of branches, schools and practices
  KC-3.3.III.A.i   the Song economy became increasingly commercialized WHILE
                   CONTINUING to depend on free peasant and artisanal labor
  KC-3.1.I.D       the Song economy flourished from increased productive
                   capacity, expanding trade networks, and innovations in
                   agriculture and manufacturing
  LO 1.A / 1.B / 1.C  the three learning objectives of this topic
  the GOV, CDI and ECN thematic-focus paragraphs

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Several distractors here are the SWAP of the key rather than an unrelated
claim: q17's distractors deny one half of KC-3.3.III.A.i while keeping the
other, and q20's alternatives differ only in the DIRECTION of cultural
influence. An anchor naming one clause would match the swap as well. Those
anchors therefore carry both clauses -- "still resting on the labor of free
peasants", "without any corresponding practice moving in the other direction"
-- which is the defect `verify_e2_1.py` shipped and `HISTORY_BRIEF.md` records.

DATA QUESTIONS
--------------
Items 11, 12 and 13 carry tables. Every number in them is HYPOTHETICAL and the
stem says so, because a real output series for Song China would be a fact the
CED does not print. Each keyed conclusion is recomputed below from the table
alone AND every distractor is shown false against the same numbers, so a
student can reach the key from the data without knowing anything in advance --
which is how the exam's stimulus sets work.

NEGATIVE CONTROL: `python3 verify_w1_1.py --selftest`.
"""
import sys

import cg_check as cg
import w1_1
import wh_check

IRON = "Iron output (index)"
HOUSE = "Registered urban households (thousands)"
CAND = "Candidates sitting the examination"
POSTS = "Official posts available"
BEFORE = "Rice harvests per year before the new variety"
AFTER = "Rice harvests per year after the new variety"


def q11(table, item):
    iron, house = cg.col(table, IRON), cg.col(table, HOUSE)
    assert all(b > a for a, b in zip(iron, iron[1:])), f"iron must rise at every step: {iron}"
    assert all(b > a for a, b in zip(house, house[1:])), f"households must rise: {house}"
    # and every distractor false on the same numbers
    assert not all(b < a for a, b in zip(iron, iron[1:])), "'iron fell' must be false"
    assert house[-1] <= 3 * house[0], "'more than tripled' must be false"
    assert iron[-1] != iron[-2], "'iron unchanged in the last step' must be false"
    assert len(set(iron)) > 1, "'iron stayed level throughout' must be false"
    return (f"iron {iron} and households {house} both rise at every step; the "
            f"final households are {house[-1]}, not above three times {house[0]}")


def q12(table, item):
    ratios = [c / p for c, p in zip(cg.col(table, CAND), cg.col(table, POSTS))]
    assert all(r > 10 for r in ratios), f"every ratio must exceed ten to one: {ratios}"
    assert not any(r < 1 for r in ratios), "'posts outnumber candidates somewhere' must be false"
    fewest = min(range(len(ratios)), key=lambda i: cg.col(table, CAND)[i])
    assert ratios[fewest] != max(ratios), \
        "'the prefecture with fewest candidates has the highest ratio' must be false"
    assert len(set(cg.col(table, POSTS))) == 1, "'posts differ from one another' must be false"
    cands = cg.col(table, CAND)
    assert not all(b < a for a, b in zip(cands, cands[1:])) or len(set(cg.col(table, POSTS))) == 1, \
        "candidates and posts cannot rise and fall together while posts are constant"
    return (f"candidates per post recompute to {ratios}, all above ten, while posts "
            f"are constant so the remaining alternatives fail")


def q13(table, item):
    before, after = cg.col(table, BEFORE), cg.col(table, AFTER)
    doubled = [i for i, (b, a) in enumerate(zip(before, after)) if a == 2 * b]
    assert len(doubled) == 2 and len(before) == 3, \
        f"key requires exactly two of three districts doubling; got {doubled}"
    unchanged = [i for i, (b, a) in enumerate(zip(before, after)) if a == b]
    assert len(unchanged) == 1, f"exactly one district must be unchanged; got {unchanged}"
    assert not all(a == 2 * b for b, a in zip(before, after)), "'every district doubled' is false"
    assert any(a > b for b, a in zip(before, after)), "'no district gathered more' is false"
    u = unchanged[0]
    assert not all(before[u] > before[j] for j in range(len(before)) if j != u), \
        "'the unchanged district gathered the most beforehand' must be false"
    assert not any(a < b for b, a in zip(before, after)), "'the count fell somewhere' is false"
    return (f"before {before} and after {after}: districts {doubled} double and district "
            f"{u} is unchanged, and no count falls")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

CLAIMS = [
 ("trained in Confucian learning",
  "KC-3.2.I.A states that the Song Dynasty utilized traditional methods of Confucianism and an imperial bureaucracy to maintain and justify its rule. An examination on the classics feeding appointments to provincial posts is that bureaucracy in operation; the CED gives monasteries, a hereditary nobility and the army no such role."),
 ("in different ways and for different purposes",
  "The Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes, and KC-3.2.I.A calls the states of the 13th century continuous, innovative AND diverse. Each rejected option asserts a uniformity the framework does not."),
 ("still resting on the labor of free peasants",
  "KC-3.3.III.A.i: the economy of Song China became increasingly commercialized while continuing to depend on free peasant and artisanal labor. Both clauses are in the anchor because each distractor keeps one half of the sentence and denies the other."),
 ("rise in productive capacity",
  "KC-3.1.I.D names increased productive capacity and innovations in agriculture among the causes of the Song economy flourishing; Champa rice is the topic page's own illustrative example of such an innovation. None of the other four outcomes is asserted anywhere in the CED."),
 ("widened the trade networks",
  "KC-3.1.I.D names expanding trade networks among the causes of the Song economy flourishing, and this topic's illustrative list names transportation innovations like the Grand Canal expansion. A waterway that carries goods between regions widens a network rather than sealing one."),
 ("variety of branches and schools",
  "KC-3.1.III.D.ii: Buddhism and its core beliefs continued to shape societies in Asia and included a variety of branches, schools, and practices. Theravada, Mahayana and Tibetan are the CED's own illustrative branches, so continuity and variety hold together."),
 ("without ceasing to be governed separately",
  "KC-3.1.III.D.i states that Chinese cultural traditions continued and influenced neighboring regions, and the illustrative list names Chinese literary and scholarly traditions and their spread to Heian Japan and Korea. Influence is asserted; political absorption is not."),
 ("tradition of filial obligation",
  "Learning Objective B asks for the effects of Chinese cultural traditions on East Asia over time, and the Cultural Developments thematic focus states that beliefs illustrate how groups view themselves and often carry social implications; the topic's illustrative list names filial piety and Confucian traditions of both respect for and expected deference from women."),
 ("cannot be separated by region",
  "KC-3.1.III.D.i and KC-3.1.III.D.ii both use the word continued, of Chinese traditions and of Buddhism, for the same societies in the same period, and the illustrative list pairs the influence of Neo-Confucianism and Buddhism in East Asia."),
 ("inherited body of teaching about right conduct",
  "KC-3.2.I.A says the Song used Confucian methods and a bureaucracy to maintain AND JUSTIFY its rule. Garrisons, taxes, weights and roads all bear on maintaining rule; only an appeal to a standard of right rule bears on justifying it."),
 ("both rose in every period shown",
  "Recomputed in q11 above from the table alone, including that each of the four alternatives is false on the same numbers. KC-3.1.I.D is the process such a pattern would illustrate: productive capacity rising alongside the economy."),
 ("by more than ten to one",
  "Recomputed in q12 above: the ratios are forty, thirty and twenty candidates per post. The competition described is a feature of the imperial bureaucracy KC-3.2.I.A names as a Song method of rule; no key here asks for a real figure."),
 ("Two of the three districts shown doubled",
  "Recomputed in q13 above from the before and after columns. KC-3.1.I.D names innovations in agriculture among the causes of the flourishing economy, and an effect that is real but uneven across districts is what such data shows."),
 ("rising productive capacity",
  "Suggested skill 4.A for this topic asks for the historical CONTEXT of a development rather than a restatement of it, and KC-3.1.I.D supplies that context by naming productive capacity, trade networks and innovation together. The other options describe or exemplify the development itself."),
 ("administrative practice that changed as dynasties succeeded one another",
  "KC-3.2.I.A describes states of the 13th century as demonstrating continuity, innovation, and diversity at once, and Learning Objective A asks how systems of government developed OVER TIME. Change resting on continuity is the framework's own combination."),
 ("expanding production for export",
  "KC-3.1.I.D names expanding trade networks and innovations in manufacturing, and this topic's illustrative list names textiles and porcelains for export. The date option also fails because the CED states its own dates are approximate and fixes no such threshold."),
 ("growth and continuity of the labor force are compatible",
  "KC-3.3.III.A.i settles the dispute in one sentence by joining increasing commercialization to continued dependence on free peasant and artisanal labor. Each rejected option denies one of the two halves the sentence holds together."),
 ("maintained order across a large territory",
  "The Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures, and KC-3.2.I.A names the imperial bureaucracy as a Song method. Recruitment, promotion and posting are that machinery."),
 ("rather than arriving in them",
  "KC-3.1.III.D.ii uses the word CONTINUED of Buddhism and its core beliefs in Asia during this period. Continuation is incompatible with a first arrival, and the same sentence's variety of branches defeats the single-school option."),
 ("without any corresponding practice moving in the other direction",
  "KC-3.1.III.D.i asserts influence running from Chinese traditions to neighboring regions and asserts nothing about a return flow. The anchor carries both the absence and its direction because the alternatives differ only in which way influence runs."),
 ("output of iron and steel",
  "KC-3.1.I.D distinguishes innovations in agriculture from innovations in manufacturing as separate causes, and this topic's illustrative list names steel and iron production and textiles and porcelains. Every rejected option is agricultural or climatic."),
 ("grounds on which obedience is claimed",
  "KC-3.2.I.A uses two verbs deliberately, maintain AND justify, and the Governance thematic focus separates how power is obtained, retained and exercised from the purposes for which it is used. The distinction is the framework's, not a matter of wording."),
 ("demonstrating continuity, innovation, and diversity at the same time",
  "KC-3.2.I.A states that empires and states in Afro-Eurasia and the Americas demonstrated continuity, innovation, and diversity in the 13th century. The two measures described are an instance of that combination; each rejected option attributes to the framework a claim it does not make."),
 ("reaching into rural households",
  "KC-3.3.III.A.i pairs increasing commercialization with continued dependence on free peasant and artisanal labor, and the Economics thematic focus states that societies affect and are affected by how they produce, exchange and consume. A peasant family buying cloth is both at once."),
 ("recruited by examination on classical texts",
  "KC-3.2.I.A asserts a matter of fact about how the Song governed, which evidence can settle. The other four questions ask what deserves obedience, what is just, which teaching is better and what ought to have been built, none of which observation decides."),
 ("removing any one of them leaves the growth unexplained",
  "KC-3.1.I.D lists three causes together for the flourishing of the Song economy: increased productive capacity, expanding trade networks, and innovations in agriculture and manufacturing. A multi-cause account is strengthened by evidence about the causes, not by a fact about one city."),
 ("language in which the dynasty defended its authority",
  "KC-3.2.I.A joins Confucianism and the imperial bureaucracy in a single sentence as the traditional methods used to maintain and justify rule. Each rejected option separates the institution from the learning that the framework binds together."),
 ("same teaching shaped conduct within ordinary households",
  "The Cultural Developments and Interactions thematic focus states that the interactions of societies and their beliefs often have political, social, and cultural implications, and KC-3.2.I.A supplies the political side by having the dynasty justify rule through Confucian methods."),
 ("may have begun before this period and continued after it",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period. KC-3.1.III.D.ii's word CONTINUED, used of Buddhism, is an instance of a process older than the period's opening."),
 ("while its economy was transformed by new techniques",
  "KC-3.2.I.A supplies the conservative half, traditional methods of Confucianism and an imperial bureaucracy, and KC-3.1.I.D the innovative half, innovations in agriculture and manufacturing. Holding both is what the framework's phrase continuity, innovation, and diversity describes."),
]

wh_check.run(w1_1, CLAIMS, TABLE_CHECKS, sys.argv)
