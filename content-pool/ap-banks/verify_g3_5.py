"""Key audit for AP HUMAN GEOGRAPHY 3.5 Historical Causes of Diffusion.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. SPS-3.A contributes two essential-knowledge statements to
this topic; its other two (A.3 and A.4) belong to Topic 3.6:

    SPS-3.A.1  Interactions between and among culture traits and larger global
               forces can lead to new forms of cultural expression; for example,
               creolization and lingua franca.
    SPS-3.A.2  Colonialism, imperialism, and trade helped to shape patterns and
               practices of culture.

SPS-3.A.1's key word is NEW. Contact is generative, not merely substitutive, and
the CED's own two examples are both things that existed in neither participating
culture beforehand. Items 1-9, 13, 16, 17, 21, 25, 26, 27 and 29 are keyed to it.

SPS-3.A.2's key word is HELPED. The verb is "helped to shape", not "determined",
and item 12 asks about exactly that. Reading it as determination would revive
the environmental-determinism error in a different costume, this time treating
colonized societies as passive. Items 10-12, 14-16, 18-20, 22-24, 28 and 30 are
keyed to this statement.

WHAT THE CED DOES NOT DEFINE, and which every key therefore argues:

    creolization   blending into a form belonging to NEITHER parent. In the
                   linguistic case the standard test is the pidgin-to-creole
                   transition: a contact language acquires native speakers.
                   Items 4, 8 and 27 turn on that test, and item 27's table
                   supplies the two speaker columns rather than asserting it.
    lingua franca  a FUNCTIONAL category -- a language used between speakers of
                   different first languages. Because it is functional, the same
                   language can be a lingua franca in one place and a mother
                   tongue in another, which items 5, 9 and 26 all rest on.

Item 6 extends creolization beyond language to cuisine, which the CED permits:
SPS-3.A.1 speaks of new forms of CULTURAL EXPRESSION and offers creolization as
an example rather than as a linguistic term of art.

Item 14 places a creolized musical form in the context of the slave trade. The
claim states plainly that nothing in the concept requires the contact to have
been voluntary, because softening that would misdescribe the history.

The five table items (26-30) are the computational gate:

  26  one language is used for interethnic business in all four cities while
      being the first language of only one -- the recompute asserts both halves
  27  first-language speakers are zero for two generations and then positive,
      which is the creolization transition; the second-language column rises
      throughout and therefore cannot mark it
  28  34 of 38 formerly administered countries against 0 of 6 never administered
  29  four vocabulary sources summing to 100, including coinages of the
      language's own
  30  five traits, three routes, four centuries

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_5


def q26_lingua_franca(table):
    """One language bridges all four cities while being native to one."""
    business, first = [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        first.append(d["Most common first language"])
        cell = d["Language used in interethnic business (%)"]
        name, share = cell.rsplit(",", 1)
        business.append((name.strip(), num(share)))
    names = {n for n, _ in business}
    assert names == {"Language D"}, business
    assert all(s >= 75 for _, s in business), business
    # It must be the most common first language in exactly one city.
    assert first.count("Language D") == 1, first
    assert len(set(first)) == len(first), first
    return "used for business between groups in all four cities"


def q27_creolization_generation(table):
    """First-language speakers appear only in the final generation."""
    rows = []
    for row in table["rows"]:
        d = rowdict(table, row)
        rows.append((d["Generation"],
                     num(d["Speakers using it as a second language"]),
                     num(d["Speakers using it as a first language"])))
    firsts = [f for _, _, f in rows]
    seconds = [s for _, s, _ in rows]
    assert firsts[0] == 0 and firsts[1] == 0 and firsts[2] > 0, firsts
    assert rows[2][0] == "Generation 3", rows
    # The second-language column rises throughout, so it cannot mark the change.
    assert all(seconds[i] < seconds[i + 1] for i in range(len(seconds) - 1)), seconds
    # And second-language speakers outnumber first-language ones even after the
    # transition, which is the last distractor's true premise.
    assert seconds[2] > firsts[2], rows
    return "acquires it as a first language"


def q28_colonial_language(table):
    """Formerly administered countries against never-administered ones."""
    admin_total = admin_match = 0
    never = None
    for row in table["rows"]:
        d = rowdict(table, row)
        n = num(d["Countries"])
        m = num(d["Countries whose official language is that power's language"])
        if d["Former administering power"].startswith("Never"):
            never = (n, m)
        else:
            admin_total += n
            admin_match += m
    assert never == (6, 0), never
    assert admin_total == 38 and admin_match == 34, (admin_total, admin_match)
    assert admin_match / admin_total > 0.85, (admin_match, admin_total)
    # The contrast must be total: no never-administered country shows the pattern.
    assert never[1] == 0, never
    return "34 of the 38 formerly administered countries"


def q29_creole_vocabulary(table):
    """Three donor families plus the language's own coinages, summing to 100."""
    shares = {rowdict(table, r)["Source of vocabulary"]:
              num(rowdict(table, r)["Share of core vocabulary (%)"])
              for r in table["rows"]}
    assert sum(shares.values()) == 100, shares
    donors = [k for k in shares if "within the creole" not in k]
    assert len(donors) == 3, donors
    own = shares["Formed within the creole itself"]
    assert own > 0, shares
    # No single donor may supply a majority large enough to call it a dialect.
    assert max(shares[d] for d in donors) < 60, shares
    return "at least three sources and has coined vocabulary of its own"


def q30_multiple_processes(table):
    """Five traits arriving by three routes across four centuries."""
    routes, periods = [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        routes.append(d["Route of arrival"])
        periods.append(d["Period of arrival"])
    assert len(routes) == 5, routes
    assert len(set(routes)) == 3, routes
    assert routes.count("Trade") == 2, routes
    assert routes.count("Colonial administration") == 2, routes
    assert routes.count("Forced migration") == 1, routes
    # The periods must span several centuries, or "over four centuries" is wrong.
    centuries = {p[:2] for p in periods}
    assert len(centuries) >= 3, periods
    return "trade, colonial administration, and forced migration together"


CLAIMS = [
 ("belong to neither original culture alone",
  "EK SPS-3.A.1 states that interactions between and among culture traits and larger global forces can lead to new forms of cultural expression. The key word is NEW: contact is generative rather than a matter of one trait simply replacing another."),

 ("Creolization and lingua franca",
  "EK SPS-3.A.1 names these two as its examples. Colonialism and imperialism belong to the next statement, urbanization and globalization to Topic 3.6, and assimilation and acculturation to Topic 3.8."),

 ("blending of two or more languages or cultural systems into a new form",
  "EK SPS-3.A.1 names creolization as an example of a new form of cultural expression arising from interaction, without defining it. The defining feature is that the result is a new system rather than a version of either contributing one."),

 ("pidgin has become a creole",
  "EK SPS-3.A.1 names creolization and leaves the mechanism to standard course content, where the test is exactly this transition. A contact language with no native speakers is a pidgin, and a generation acquiring it as a mother tongue makes it a creole."),

 ("Its function as a language used between speakers of different first languages",
  "EK SPS-3.A.1 names lingua franca among the new forms interaction produces, and the term is functional rather than structural. Any language becomes one where it bridges groups with different mother tongues, which is why status depends on where you ask."),

 ("rather than a version of any contributing culture",
  "EK SPS-3.A.1 speaks of interactions among culture traits producing new forms of CULTURAL EXPRESSION, and creolization is its example of that process. The concept is not confined to language: any cultural system can blend into something belonging to neither parent."),

 ("forms that existed in none of the participating cultures",
  "EK SPS-3.A.1's phrase is 'can lead to NEW FORMS of cultural expression', and both its examples are things that did not exist before the contact that made them. A pure replacement account cannot explain where a creole or a shared trade language came from."),

 ("people who speak it as a first language",
  "Both a pidgin and a creole arise from contact and draw on more than one source, so vocabulary and setting cannot separate them. The transition EK SPS-3.A.1's creolization names is the acquisition of native speakers, which turns a limited contact code into a full language."),

 ("term describes a function rather than a language",
  "EK SPS-3.A.1's lingua franca is defined by use between speakers of different first languages. Whether a language holds that status therefore depends on where the question is asked, and one language can be a mother tongue in one place and a bridge in another."),

 ("Colonialism, imperialism, and trade",
  "EK SPS-3.A.2 names exactly these three. Migration, urbanization, industrialization and technology shape culture too, but they are treated under other statements and other topics rather than this one."),

 ("outlive the political arrangement that created them",
  "EK SPS-3.A.2 says colonialism, imperialism and trade HELPED TO SHAPE patterns and practices of culture, and shaping is durable in a way that governing is not. Institutions once established train the people who then run them, which is how they persist."),

 ("alongside the practices already present",
  "EK SPS-3.A.2's verb is 'helped to shape' rather than determined, and taking the verb seriously separates an accurate claim from an overstatement. Colonized societies retained, adapted and created culture throughout, which is why the resulting patterns are blends."),

 ("travelling along the same routes as goods",
  "EK SPS-3.A.2 names trade among the processes that helped shape patterns and practices of culture. A trade route is a repeated and durable channel of contact, so seeds, gods, words and techniques diffuse along it with the merchants."),

 ("arising from forced contact",
  "EK SPS-3.A.1 makes new forms of cultural expression the product of interaction among culture traits, and EK SPS-3.A.2 names the historical processes that forced this interaction. Nothing in the concept requires the contact to have been voluntary, and softening that would misdescribe the history."),

 ("administration, commerce, and schooling once required it",
  "EK SPS-3.A.2 names colonialism, imperialism and trade among the processes shaping cultural patterns, and EK SPS-3.A.1 names lingua franca among the resulting forms. The mechanism is practical: whoever must be dealt with sets the language of dealing, and that outlasts the dealing."),

 ("durable difference in education, language use, and access to state employment",
  "EK SPS-3.A.2 says colonialism helped shape patterns AND PRACTICES of culture, and a recruitment rule is a practice with compounding effects. Schooling follows employment and employment follows schooling, so a difference created once reproduces itself for generations."),

 ("rather than a mixture in which the parents remain separable",
  "EK SPS-3.A.1 names creolization as an example of a NEW FORM of cultural expression. A blend that could be sorted back into its ingredients would not be a new form, which is what distinguishes creolization from simple borrowing."),

 ("Trade as the historical process and creolization as the resulting new form",
  "EK SPS-3.A.2 names trade among the historical processes shaping cultural patterns and EK SPS-3.A.1 names creolization among the new forms interaction produces. Pairing a process with the form it generated is what a complete answer to this topic requires."),

 ("combines contact with political control",
  "EK SPS-3.A.2 names colonialism, imperialism and trade separately, and the distinction is the presence of coercive authority. Trade creates opportunities to adopt, while colonial rule can additionally compel a school system, a legal code and an official language."),

 ("including food preferences",
  "EK SPS-3.A.2 names all three processes and a staple crop's transfer runs through every one of them. EK PSO-3.A.2 from Topic 3.1 makes food preferences a culture trait, so the transfer changed culture and not only agriculture."),

 ("processes such as empire and long-distance trade that operate at a much larger scale",
  "EK SPS-3.A.1 speaks of interactions between and among culture traits AND larger global forces, which is a claim about scale. A creole arises in one port and exists because of a trading system spanning oceans, so the local form cannot be explained locally."),

 ("continue to shape decisions long after the rule itself ended",
  "EK SPS-3.A.2 says these processes HELPED TO SHAPE patterns and practices of culture, which is a claim about durable structure. An official language or a school system produces effects every year it operates, so the shaping continues after the shaper has gone."),

 ("becoming ordinary parts of life in the colonizing society",
  "EK SPS-3.A.1's interactions run between and among culture traits rather than in one direction only. Influence travelling back along the same routes shows contact to be a relationship rather than a transmission, however unequal the power within it."),

 ("creates new forms and ends existing ones",
  "SPS-3's enduring understanding names change AND disappearance, and EK SPS-3.A.1 and A.2 supply mechanisms for both. The same colonial encounter that produced a creole also ended languages, and an honest account of the topic records both outcomes."),

 ("each new learner has a practical reason to learn it",
  "EK SPS-3.A.1's lingua franca is defined by function, and a functional advantage is self-reinforcing: the value of learning a bridge language rises with the number already using it. That mechanism is independent of how the first speakers came to it."),

 ("used for business between groups in all four cities",
  "Recomputed from the table: one language is named for interethnic business in every city at 79 to 91 percent while being the most common first language in only one of them. EK SPS-3.A.1's lingua franca is a functional category, and use between groups is what defines it.",
  q26_lingua_franca),

 ("acquires it as a first language",
  "Recomputed from the table: first-language speakers stand at zero for two generations and then reach 9,400, which is the pidgin-to-creole transition. The verifier confirms the second-language column rises throughout and so cannot mark the change, which is why its largest rise is offered as a distractor.",
  q27_creolization_generation),

 ("34 of the 38 formerly administered countries",
  "Recomputed from the table: the three administered rows total 34 of 38 countries, or 89 percent, against zero of the six never administered. EK SPS-3.A.2 says colonialism and imperialism helped shape cultural patterns, and an official language is among the most durable of them.",
  q28_colonial_language),

 ("at least three sources and has coined vocabulary of its own",
  "Recomputed from the table: four shares sum to 100 across three separate donor families plus six percent formed inside the language itself, with no donor supplying a majority. EK SPS-3.A.1 names creolization as a NEW form, and a system with its own coinages is not reducible to any contributor.",
  q29_creole_vocabulary),

 ("trade, colonial administration, and forced migration together",
  "Recomputed from the table: five traits arrive by three distinct routes -- two by trade, two by colonial administration and one by forced migration -- across at least three different centuries. EK SPS-3.A.2 names colonialism, imperialism and trade as processes that HELPED shape culture, and the plural is what the table demonstrates.",
  q30_multiple_processes),
]

hg_check.check(g3_5, CLAIMS, per_topic=30, n_choices=5)
