"""Key audit for AP WORLD HISTORY: MODERN 7.8 Mass Atrocities After 1900.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

WHAT THE KEYS REST ON
---------------------
KC-6.2.III.C is the whole of this topic's required content: "The rise of
extremist groups in power led to the attempted destruction of specific
populations, notably the Nazi killing of the Jews in the Holocaust during World
War II, and to other atrocities, acts of genocide, or ethnic violence."

  the stated cause, extremist groups
    in power                            items 1, 14, 15, 19, 29, 30
  the attempted destruction of
    SPECIFIC populations                items 2, 13, 16, 28, 29, 30
  "notably" the Holocaust, placed
    DURING World War II                 items 3, 5, 9, 29, 30
  other atrocities, acts of genocide,
    or ethnic violence                  items 4, 28, 29, 30
  the CED's four illustrative examples  items 6, 7, 24, 25, 27
  Learning Objective H, 1900 to
    the present                         items 10, 18, 23, 26
  suggested skill 5.B                   items 8, 12, 17, 21, 25
  the SIO thematic focus                items 11, 13, 26

Items 9 and 14 are the SWAP items: the framework places the Holocaust DURING
World War II while naming the rise of extremist groups in power as what LED TO
it, so both anchors carry both clauses and neither can match a reversal.

HOW THIS MODULE IS BOUNDED, and why the bounding is part of the audit
---------------------------------------------------------------------
Nothing here asserts anything about any specific atrocity beyond the words the
CED itself prints. No key rests on a number of victims, a method, a date beyond
the period the CED assigns, an organisation, a perpetrator's name beyond the
CED's own "Nazi", a place beyond the CED's own, or any account of what was done.
No stimulus depicts an atrocity: every source in the module is a source ABOUT
the study of these events -- an archive finding aid, a commission's terms of
reference, a relief register, a government's own denial, a historian's methods
argument -- each explicitly unattributed and illustrative, with no testimony
invented and nothing attributed to a real person or organisation.

The single table is a REFERENCE table holding the CED's four illustrative
examples with the place and period the CED assigns each: Armenians in the
Ottoman Empire during and after World War I; Ukraine in the Soviet Union in the
1920s and 1930s; Cambodia during the late 1970s; Tutsi in Rwanda in the 1990s.
It carries no casualty data, because inventing casualty figures for these events
would be exactly the invented detail this module refuses. ``q7`` below checks
the table against the CED's four examples cell by cell, so a corrupted cell is
caught rather than silently read as data.

Items 8 and 25 relate this topic's statement to two others, which is what
suggested skill 5.B asks for: KC-6.2.IV.B.ii names the rise to power of fascist
and totalitarian regimes among the causes of World War II, and KC-6.3.I.A.i
states that in the Soviet Union the government controlled the national economy
through the Five Year Plans, often implementing repressive policies, with
negative repercussions for the population. Neither item asserts that either
statement caused what the other describes; each asks only what the framework
places alongside what.

WHAT IS NOT KEYED, deliberately: nothing about outcomes, aftermaths, trials,
recognition, restitution or law, none of which the framework states here; and no
item ranks or compares atrocities against one another.

NEGATIVE CONTROLS: ``python3 verify_w7_8.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of the table, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_8

EXAMPLE = "Illustrative example printed in the CED"
WHERE = "Where the CED places it"
WHEN = "When the CED places it"

# The four illustrative examples the CED prints beside KC-6.2.III.C, with the
# place and period it assigns each. Nothing beyond these words is asserted.
CED_EXAMPLES = {
    ("Armenians in the Ottoman Empire", "The Ottoman Empire",
     "During and after World War I"),
    ("Ukraine in the Soviet Union", "The Soviet Union", "The 1920s and 1930s"),
    ("Cambodia", "Cambodia", "The late 1970s"),
    ("Tutsi in Rwanda", "Rwanda", "The 1990s"),
}


def _text_col(table, header):
    """Every value in the named column, as strings, in row order."""
    try:
        j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    except ValueError:
        raise AssertionError(
            f"no column {header!r}; headers are {table['headers']}"
        ) from None
    return [str(r[j]) for r in table["rows"]]


def q7(table, item):
    rows = set(zip(_text_col(table, EXAMPLE), _text_col(table, WHERE),
                   _text_col(table, WHEN)))
    # The table reproduces the CED's own illustrative examples, so every cell of
    # it is checkable against the CED rather than against an author's memory.
    assert rows == CED_EXAMPLES, (
        "the table must reproduce the CED's four illustrative examples exactly; "
        f"it differs by {sorted(rows ^ CED_EXAMPLES)}"
    )
    places = _text_col(table, WHERE)
    periods = _text_col(table, WHEN)
    assert len(set(places)) > 1, "'all drawn from a single region' must be false"
    assert len(set(periods)) > 1, "'all drawn from a single decade' must be false"
    early = [p for p in periods if "World War I" in p or "1920s" in p]
    late = [p for p in periods if "1970s" in p or "1990s" in p]
    assert early and late, (
        f"the examples must span more than one part of the century; got {periods}"
    )
    assert late, "'all placed before the Second World War' must be false"
    assert [p for p in periods if "1990s" not in p], \
        "'all placed after the end of the Cold War' must be false"
    return (f"the four rows are the CED's own illustrative examples, they name "
            f"{len(set(places))} different places, and their periods run from "
            f"{sorted(early)} to {sorted(late)}")


TABLE_CHECKS = {7: q7}

CLAIMS = [
 ("The rise of extremist groups in power",
  "KC-6.2.III.C states that the rise of extremist groups in power led to the attempted destruction of specific populations and to other atrocities, acts of genocide, or ethnic violence, so that is the development this sentence names as the cause."),
 ("attempted destruction of specific populations",
  "KC-6.2.III.C says the rise of extremist groups in power led to the attempted destruction of specific populations, which is the framework's own wording for what this topic covers."),
 ("Nazi killing of the Jews in the Holocaust during World War II",
  "KC-6.2.III.C singles this instance out with the word 'notably' inside the required statement itself, whereas the CED's other examples for this topic are printed beside the statement as illustrative examples."),
 ("Other atrocities, acts of genocide, or ethnic violence",
  "KC-6.2.III.C ends by saying the rise of extremist groups in power led also to other atrocities, acts of genocide, or ethnic violence, so the sentence names two things it led to."),
 ("During World War II",
  "KC-6.2.III.C places the Nazi killing of the Jews in the Holocaust during World War II. That is the period the framework itself assigns, and nothing further about the period is asserted here."),
 ("During and after World War I",
  "The CED prints the Armenians in the Ottoman Empire during and after World War I among the illustrative examples beside KC-6.2.III.C, and nothing is asserted beyond the words the CED uses."),
 ("more than one region and from more than one part of the twentieth century",
  "Unit 7 Learning Objective H covers the period from 1900 to the present, and the CED's four illustrative examples for KC-6.2.III.C name four different places across periods running from the First World War to the 1990s. Checked in q7 above cell by cell against the CED's own examples."),
 ("rise to power of fascist and totalitarian regimes was among the causes of the Second World War",
  "KC-6.2.III.C names the rise of extremist groups in power and KC-6.2.IV.B.ii names the rise to power of fascist and totalitarian regimes, and suggested skill 5.B asks how one development relates to another; the two statements describe the same kind of government coming to power."),
 ("places the killing during the war, without presenting either one as the cause",
  "KC-6.2.III.C assigns the Nazi killing of the Jews in the Holocaust to the period of World War II and names the rise of extremist groups in power as what led to it, so the anchor carries both halves because a reversal in either direction is the plausible error."),
 ("What caused mass atrocities in the period from 1900 to the present",
  "Unit 7 Learning Objective H asks students to explain the various causes and consequences of mass atrocities in the period from 1900 to the present."),
 ("how societies group their members and the norms governing relations between those groups",
  "The CED's Social Interactions and Organization thematic focus is stated as the process by which societies group their members and the norms that govern interactions between these groups and between individuals, and KC-6.2.III.C concerns actions directed at specific populations."),
 ("Explain how one historical development or process relates to another",
  "Suggested skill 5.B for this topic is to explain how a historical development or process relates to another, and KC-6.2.III.C supplies the developments to be related; the other options are skills the CED attaches to other topics."),
 ("directed at particular populations rather than at a population in general",
  "KC-6.2.III.C says the attempted destruction was of SPECIFIC populations, and the CED's Social Interactions and Organization focus concerns how a society groups its members, so the adjective marks the target as a particular group."),
 ("came first, and the framework describes it as leading to what followed",
  "KC-6.2.III.C says the rise of extremist groups in power LED TO the attempted destruction of specific populations and to other atrocities, so the anchor carries the ordering because the reversed reading is the plausible error."),
 ("attributes them to the rise of extremist groups in power",
  "KC-6.2.III.C names the rise of extremist groups in power as what led to these developments, while the peace settlement appears in KC-6.2.IV.B.ii as a cause of the Second World War, which is a different statement about a different subject."),
 ("how a government in power directed official action towards a specific population",
  "KC-6.2.III.C attributes the attempted destruction of specific populations to the rise of extremist groups in power, so the administrative records of the office through which such a government acted bear directly on that claim."),
 ("Explaining how one historical development or process relates to another",
  "Suggested skill 5.B is to explain how a historical development or process relates to another, and KC-6.2.III.C itself groups the attempted destruction of specific populations with other atrocities, acts of genocide, or ethnic violence under one stated cause."),
 ("Both the causes and the consequences that the objective names",
  "Unit 7 Learning Objective H asks students to explain the various causes AND consequences of mass atrocities in the period from 1900 to the present, so a body charged with establishing what led to events and reporting their effects addresses both halves."),
 ("cause common to them, the rise of extremist groups in power",
  "KC-6.2.III.C attributes the attempted destruction of specific populations and other atrocities, acts of genocide, or ethnic violence to a single named development, so the framework asserts a common cause rather than a series of unconnected accidents."),
 ("reason to deny that anything occurred",
  "KC-6.2.III.C locates these developments in the actions of extremist groups in power, so the government of the territory concerned is the interested party in any account it gives; that is a limit on the source rather than a reason to set it aside."),
 ("starting point for investigation rather than an explanation",
  "KC-6.2.III.C names the rise of extremist groups in power as what led to these developments, and a register of arrivals reaches no cause on its own; suggested skill 5.B requires evidence relating one development to another."),
 ("instructions and internal records the government itself produced",
  "KC-6.2.III.C attributes the attempted destruction of specific populations to the rise of extremist groups in power, so what such a government instructed and recorded is the material bearing on its intentions."),
 ("From 1900 to the present",
  "Unit 7 Learning Objective H covers the period from 1900 to the present, the CED's own illustrative examples run from the First World War to the 1990s, and the framework states that developments are not constrained by the dates given for a period."),
 ("Cambodia during the late 1970s and the Tutsi in Rwanda in the 1990s",
  "The CED assigns each of its four illustrative examples for KC-6.2.III.C a period, and only these two fall in the decades after the Second World War."),
 ("Ukraine in the Soviet Union in the 1920s and 1930s",
  "KC-6.3.I.A.i states that in the Soviet Union the government controlled the national economy through the Five Year Plans, often implementing repressive policies with negative repercussions for the population, and the CED places this illustrative example in that state in those decades; suggested skill 5.B asks students to relate developments without asserting that either produced the other."),
 ("Political, economic, and cultural institutions and organization",
  "The CED's Social Interactions and Organization focus states that how societies group their members, and the norms governing relations between those groups, influence political, economic, and cultural institutions and organization, which is the framework's own statement of what such developments bear on under Unit 7 Learning Objective H."),
 ("four different states in widely separated parts of the world",
  "The CED prints the Armenians in the Ottoman Empire, Ukraine in the Soviet Union, Cambodia, and the Tutsi in Rwanda as its illustrative examples beside KC-6.2.III.C, which places the subject in four widely separated states rather than in one region."),
 ("Two: the attempted destruction of specific populations",
  "KC-6.2.III.C says the rise of extremist groups in power led to the attempted destruction of specific populations and to other atrocities, acts of genocide, or ethnic violence, so the sentence carries two consequences joined by 'and to'."),
 ("identifies no development that led to the events it describes",
  "KC-6.2.III.C states a cause, two consequences, and a period for the instance it singles out, so a claim that the framework identifies no such development contradicts the sentence while the other options restate parts of it."),
 ("the instance the framework singles out",
  "KC-6.2.III.C names the rise of extremist groups in power as the cause, the attempted destruction of specific populations as what it led to, the Nazi killing of the Jews in the Holocaust during World War II as the instance marked 'notably', and other atrocities, acts of genocide, or ethnic violence as the rest, so a summary must carry the cause, both consequences and the direction between them."),
]

wh_check.run(w7_8, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
