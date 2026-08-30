"""Key audit for AP HUMAN GEOGRAPHY 3.6 Contemporary Causes of Diffusion.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. SPS-3.A contributes two essential-knowledge statements to
this topic; A.1 and A.2 belong to Topic 3.5:

    SPS-3.A.3  Cultural ideas and practices are socially constructed and change
               through both small-scale and large-scale processes such as
               urbanization and globalization. These processes come to bear on
               culture through media, technological change, politics, economics,
               and social relationships.
    SPS-3.A.4  Communication technologies, such as the internet and the
               time-space convergence, are reshaping and accelerating
               interactions among people; changing cultural practices, as in the
               increasing use of English and the loss of indigenous languages;
               and creating cultural convergence and divergence.

SPS-3.A.3 carries three separable claims, and this module tests all three:

  * SOCIALLY CONSTRUCTED -- items 1, 4 and 11. The phrase is about how a
    practice comes to be and to persist, not about whether it is valuable, and
    items 4 and 11 both key to answers that say so explicitly. Reading it as
    "therefore worthless" is the standing misuse of the term.
  * BOTH SMALL-SCALE AND LARGE-SCALE -- items 2, 5, 6 and 9. The CED's "both"
    is doing work: a module that only ever asks about globalization teaches half
    the sentence.
  * THE FIVE CHANNELS, a closed list -- media, technological change, politics,
    economics, social relationships. Items 3, 8, 12, 17, 21, 24 and 26 use it,
    and item 26's table maps five survey categories one to one onto the five so
    that every option names a real channel and only the counts decide.

SPS-3.A.4 names THREE consequences and the third is a PAIR. Items 10, 13, 15,
18, 19, 23, 25, 29 and 30 rest on convergence and divergence occurring together.
This is the point of the topic most easily got wrong: item 19 keys against the
claim that globalization is "erasing local culture everywhere", and item 29's
table supplies a dispersed community sustaining practice through the same
technologies usually cited for convergence. A module teaching only convergence
would contradict the CED's own sentence.

TIME-SPACE CONVERGENCE is named in SPS-3.A.4 and undefined there. Item 7 keys to
the standard definition and its claim states the relationship to Topic 1.4's
time-space compression rather than pretending the two terms are unconnected --
they describe one phenomenon from the side of the places and of the traveller
respectively.

The five table items (26-30) are the computational gate:

  26  five categories mapping one to one onto the five channels, summing to
      4,500, with media ahead of the next by a wide margin
  27  contact rises with access at every step, multiplying more than nineteenfold
  28  the national language gains while all three indigenous languages lose more
      than three quarters of their speakers
  29  classes, participants and participating countries all rise -- divergence
  30  international media consumption AND local associations both rise, which is
      convergence and divergence in one table

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_6

# EK SPS-3.A.3's five channels, mapped to the survey wording of item 26.
CHANNEL_OF_RESPONSE = {
    "Online video and social platforms": "media",
    "A friend or family member": "social relationships",
    "At work or through an employer": "economics",
    "A government campaign or school": "politics",
    "A new device or application itself": "technological change",
}


def q26_five_channels(table):
    """Each response category is one of the five channels; media leads."""
    counts, total = {}, 0.0
    for row in table["rows"]:
        d = rowdict(table, row)
        label = d["Channel of first encounter"]
        assert label in CHANNEL_OF_RESPONSE, f"unmapped channel: {label!r}"
        n = num(d["Respondents"])
        counts[CHANNEL_OF_RESPONSE[label]] = n
        total += n
    assert set(counts) == set(CHANNEL_OF_RESPONSE.values()), counts
    assert total == 4500, total
    top = max(counts, key=counts.get)
    assert top == "media" and counts["media"] == 1940, counts
    runner_up = sorted(counts.values(), reverse=True)[1]
    assert counts["media"] > runner_up * 1.5, counts
    return "1,940 of 4,500 respondents"


def q27_access_and_contact(table):
    """Contact rises with access at every step and multiplies far more."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Households with internet access (%)"]),
                   num(rowdict(table, r)["Reporting daily contact abroad (%)"]))
                  for r in table["rows"])
    access = [a for _, a, _ in rows]
    contact = [c for _, _, c in rows]
    assert all(access[i] < access[i + 1] for i in range(len(access) - 1)), access
    assert all(contact[i] < contact[i + 1] for i in range(len(contact) - 1)), contact
    assert access[0] == 14 and access[-1] == 86, access
    assert contact[0] == 3 and contact[-1] == 58, contact
    assert contact[-1] / contact[0] > 19, contact
    # The "access rose faster in every period" distractor must be false.
    faster = [(access[i + 1] - access[i]) > (contact[i + 1] - contact[i])
              for i in range(len(access) - 1)]
    assert not all(faster), (access, contact)
    # And contact must never reach 100 percent, disposing of another distractor.
    assert contact[-1] < 100, contact
    return "from 3 to 58 percent"


def q28_language_loss(table):
    """The national language gains; every indigenous language loses heavily."""
    national, indigenous = None, []
    for row in table["rows"]:
        d = rowdict(table, row)
        before = num(d["Speakers in 1980"])
        after = num(d["Speakers in 2020"])
        if d["Language"] == "National language":
            national = (before, after)
        else:
            indigenous.append((d["Language"], before, after))
    assert national is not None and len(indigenous) == 3, (national, indigenous)
    assert national[1] > national[0], national
    losses = [(b - a) / b for _, b, a in indigenous]
    assert all(x > 0.75 for x in losses), losses
    assert [round(100 * x) for x in losses] == [77, 90, 93], losses
    return "lost more than three quarters"


def q29_divergence(table):
    """Classes, participants and participating countries all rise."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Online language classes offered"]),
                   num(rowdict(table, r)["Members participating in coordinated observances"]),
                   num(rowdict(table, r)["Countries with participating members"]))
                  for r in table["rows"])
    for col in (1, 2, 3):
        series = [r[col] for r in rows]
        assert all(series[i] < series[i + 1] for i in range(len(series) - 1)), (col, series)
    # Dispersal AND practice must both rise, which is what makes it divergence
    # rather than a community simply becoming more concentrated.
    assert rows[-1][3] > 4 * rows[0][3], rows
    assert rows[-1][2] > 20 * rows[0][2], rows
    return "sustaining a distinct practice"


def q30_both_outcomes(table):
    """International media consumption and local organizing both rise."""
    rows = []
    for row in table["rows"]:
        d = rowdict(table, row)
        rows.append((d["Decade"],
                     num(d["Households consuming internationally produced media weekly (%)"]),
                     num(d["Registered local cultural associations"])))
    media = [m for _, m, _ in rows]
    local = [l for _, _, l in rows]
    assert all(media[i] < media[i + 1] for i in range(len(media) - 1)), media
    assert all(local[i] < local[i + 1] for i in range(len(local) - 1)), local
    assert media[0] == 18 and media[-1] == 84, media
    assert local[-1] > 3 * local[0], local
    return "both rose sharply"


CLAIMS = [
 ("made, maintained, and changed by people",
  "EK SPS-3.A.3 states that cultural ideas and practices are socially constructed. The point of the phrase is that a practice persists because people keep doing and teaching it, which is also why it can change when they stop."),

 ("Urbanization and globalization",
  "EK SPS-3.A.3 names urbanization and globalization as its examples of large-scale processes. Colonialism and imperialism belong to the previous topic's statement, and convergence and divergence are outcomes named in EK SPS-3.A.4 rather than processes."),

 ("Media, technological change, politics, economics, and social relationships",
  "EK SPS-3.A.3 prints exactly this list of five channels through which processes come to bear on culture. Each distractor substitutes a plausible channel the statement does not name, and here the list is closed rather than illustrative."),

 ("arose from particular decisions and circumstances rather than from necessity",
  "EK SPS-3.A.3's social construction claim is about origin and maintenance rather than about value. Recognising contingency makes a practice a subject for explanation instead of something taken as given, and it says nothing about whether the practice is good."),

 ("household and neighbourhood processes as well as by worldwide ones",
  "EK SPS-3.A.3 writes 'both small-scale and large-scale processes', which is a deliberate pairing. A family deciding which language to speak at home and a global media industry are both changing culture, and neither account is complete alone."),

 ("smaller family sizes, new work rhythms, and different food-buying habits",
  "EK SPS-3.A.3 names urbanization among the large-scale processes changing cultural ideas and practices. Moving to a city changes the cost of children, the shape of the working day and the way food is obtained, and each reshapes daily practice."),

 ("places grow functionally closer while the distance between them is unchanged",
  "EK SPS-3.A.4 names time-space convergence among the communication technologies reshaping interaction, without defining it. It is the same phenomenon Topic 1.4 calls time-space compression, described from the side of the places rather than of the traveller."),

 ("Media, one of the five channels",
  "EK SPS-3.A.3 names media first among the five channels through which urbanization and globalization come to bear on culture. That the industry is also commercial does not displace the channel, since the question asks how the influence reaches people."),

 ("neighbourhood's families deciding together",
  "EK SPS-3.A.3 pairs small-scale with large-scale processes, and a neighbourhood establishing a durable practice is the small-scale case. The other options operate at national or global extent, which is the other half of that pairing."),

 ("Accelerated interaction, changed cultural practices, and both cultural convergence and divergence",
  "EK SPS-3.A.4 names three consequences in one sentence, and the third is itself a pair rather than a single outcome. A reading that stops at convergence omits half of what the statement asserts."),

 ("cultural ideas and practices are socially constructed",
  "EK SPS-3.A.3 asserts exactly this, and datable origins together with absence elsewhere are the standard evidence for it. Neither observation says anything about whether the practice in question is worth keeping."),

 ("state decision reached culture through the school system",
  "EK SPS-3.A.3 names politics among the five channels through which processes come to bear on culture, and EK SPS-3.A.4 names the loss of indigenous languages among the practices that change. A curriculum rule is politics acting on culture directly."),

 ("convergence and cultural divergence, together rather than as alternatives",
  "EK SPS-3.A.4 ends by naming convergence AND divergence, which asserts that both occur. The same networks that spread one set of practices everywhere also let dispersed communities find one another and sustain practices proximity could not."),

 ("changing practices unevenly within one population",
  "EK SPS-3.A.4 says communication technologies are reshaping and accelerating interactions and changing cultural practices, and nothing in that requires the change to be uniform. Access and receptiveness both vary by age, so one household can hold two patterns."),

 ("scattered minority using online networks",
  "EK SPS-3.A.4 names both convergence and divergence as effects of communication technology. Divergence appears where the technology sustains distinctiveness rather than dissolving it, which is exactly what a dispersed community's network does."),

 ("Its use is increasing",
  "EK SPS-3.A.4 names the increasing use of English as one of its two examples of changed cultural practice. The statement describes a trend rather than replacement, and overstating it would turn a defensible claim into a false one."),

 ("Economics, since the influence travels through employment and markets",
  "EK SPS-3.A.3 names economics among the five channels through which large-scale processes reach culture. Workplace norms spread because employment is where most adults spend their days and because firms compete for the same workers."),

 ("simultaneously make distant places more alike and allow dispersed groups",
  "EK SPS-3.A.4 names both outcomes in the same clause, which asserts that a single cause produces both. A network carrying a global product to a village also carries a minority's language lessons to its diaspora, and both effects are real."),

 ("names divergence alongside convergence",
  "EK SPS-3.A.4 names cultural convergence AND divergence as effects, and EK SPS-3.A.3 makes culture something people construct rather than passively receive. The erasure claim assumes an audience with no agency, which is what both statements deny."),

 ("including the loss of indigenous languages",
  "EK SPS-3.A.4 names the loss of indigenous languages as an example of changing cultural practice, and EK SPS-3.A.3's five channels are how the pressure is applied. Naming several channels together is more accurate than isolating one, since a language dies when it stops being useful in all of them."),

 ("someone they know and trust already has",
  "EK SPS-3.A.3 names social relationships among the five channels through which processes come to bear on culture. It is also the mechanism behind contagious diffusion in Topic 3.4: adoption travels along the links people actually have."),

 ("does not require proximity",
  "EK SPS-3.A.4 says communication technologies are reshaping and accelerating interactions among people, and this is what the reshaping consists of. Contact by proximity produces distance decay; contact by network produces ordering by connection instead."),

 ("shared national reference points weaken",
  "EK SPS-3.A.4 names convergence and divergence together, and this is a case where one change produces both at once. The same shift that lets a video reach a hundred countries removes the single bulletin that gave one country a common evening."),

 ("through streaming platforms, matched to media",
  "EK SPS-3.A.3's five channels are media, technological change, politics, economics and social relationships, and a streaming platform delivering music is the media case. Each other pairing attaches a case to a channel that does not carry it."),

 ("both greater similarity between places and new forms of distinctiveness",
  "EK SPS-3.A.3 supplies the scales and the five channels while EK SPS-3.A.4 supplies the paired outcome of convergence and divergence. Keeping both halves is what the two statements together assert, and dropping either produces a claim the CED does not make."),

 ("1,940 of 4,500 respondents",
  "Recomputed from the table: the five response categories map one to one onto EK SPS-3.A.3's five channels, they total 4,500, and the media category leads the next by more than half again. Every option names a real channel, so only the counts separate them.",
  q26_five_channels),

 ("from 3 to 58 percent",
  "Recomputed from the table: access runs 14, 41, 78 and 86 percent while daily international contact runs 3, 17, 49 and 58, rising together at every step with contact multiplying more than nineteenfold. The verifier also confirms access did not rise faster in every period and that contact never reaches 100.",
  q27_access_and_contact),

 ("lost more than three quarters",
  "Recomputed from the table: the national language rises from 22 to 38 million while the three indigenous languages lose 77, 90 and 93 percent of their speakers. EK SPS-3.A.4 names the loss of indigenous languages among the cultural practices these processes change.",
  q28_language_loss),

 ("sustaining a distinct practice",
  "Recomputed from the table: classes rise from 3 to 64, participants from 420 to 9,800 and participating countries from 6 to 31, so a community spreading across more countries is sustaining more shared practice rather than less. EK SPS-3.A.4 names divergence alongside convergence, and this is the divergence case.",
  q29_divergence),

 ("both rose sharply",
  "Recomputed from the table: international media consumption rises from 18 to 84 percent while registered local associations more than triple, so both curves move upward together. EK SPS-3.A.4 names convergence and divergence as effects of the same technologies, and two rising trends is what that pairing looks like in data.",
  q30_both_outcomes),
]

hg_check.check(g3_6, CLAIMS, per_topic=30, n_choices=5)
