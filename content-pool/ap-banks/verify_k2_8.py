"""Key audit for AP COMPARATIVE GOVERNMENT 2.8 Judicial Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
PAU-3.G.1's nine sub-points, one country at a time:
  .a China: RULE BY LAW instead of rule of law; the judicial system is SUBSERVIENT
     to the Communist Party, which CONTROLS MOST JUDICIAL APPOINTMENTS
  .b Iran: the judiciary's MAJOR FUNCTION is a legal system BASED ON RELIGIOUS LAW;
     judges TRAINED IN ISLAMIC SHARIA LAW; the head of the judiciary is APPOINTED
     BY THE SUPREME LEADER and may nominate HALF the Guardian Council with Majles
     approval
  .c Mexico: judiciary IN TRANSITION; Supreme Court holds JUDICIAL REVIEW;
     amendments implemented WITH THE INTENT of more independence and effectiveness
  .d Mexico: magistrates NOMINATED BY THE PRESIDENT, APPROVED BY THE SENATE, term of
     15 YEARS
  .e Nigeria: JUDICIAL REVIEW; an effort to REESTABLISH LEGITIMACY AND INDEPENDENCE
     BY REDUCING CORRUPTION; Islamic Sharia Courts in the north UNDER FEDERALISM
  .f Nigeria: judges RECOMMENDED BY A JUDICIAL COUNCIL, APPOINTED BY THE PRESIDENT,
     CONFIRMED BY THE SENATE
  .g Russia: the government USES THE JUDICIAL SYSTEM TO TARGET OPPOSITION; the
     courts hold judicial review CONSTITUTIONALLY but it HAS NOT BEEN USED to limit
     the governing branches
  .h Russia: judges NOMINATED BY THE PRESIDENT, APPROVED BY THE FEDERATION COUNCIL
  .i United Kingdom: COMMON LAW enforcing the RULE OF LAW; the Supreme Court is the
     FINAL COURT OF APPEALS, PROTECTS HUMAN AND CIVIL RIGHTS AND LIBERTIES, and
     RULES ON DEVOLUTION DISPUTES

TWO DISTINCTIONS KEYED RATHER THAN GLOSSED
------------------------------------------
1. RULE BY LAW is not RULE OF LAW. PAU-3.G.1.a marks the difference in a
   parenthesis and PAU-1.B.1.a supplies what the rule of law means. Item 1 keys it.
2. PAU-3.G.1.g says in ONE sentence that Russia's courts hold judicial review
   constitutionally and that the power has not been used against the governing
   branches. An item asking simply 'do Russia's courts have judicial review' would
   therefore have two defensible answers, so items 12 and 27 make the question
   specify which half is meant, and item 20 puts the same distinction into data.

Mexico's 15-year term is one of the framework's very few precise institutional
numbers (AP_COMP_GOV_CED.md note 9); item 7 keys the figure and item 26 keys its
rarity, listing the handful of others rather than implying it stands alone.

DATA ITEMS
----------
Items 20-22 use a hypothetical judicial-review record, chosen because holding a
power and exercising it come apart in exactly the way PAU-3.G.1.g describes.
Items 23-25 use a four-row appointment matrix whose rows differ by one stage each,
so the three routes the framework prints can be told apart.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_8

STRUCK = "Laws or executive acts struck down, 2000-2020"
CASES = "Cases brought against the government, 2000-2020"
AGAINST = "Share of those cases decided against the government (percent)"
ROUTE = "How members reach the bench"


def _jrev(table):
    return {lab: (cg.cell(table, lab, STRUCK), cg.cell(table, lab, CASES), cg.cell(table, lab, AGAINST))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _jrev(table)
    assert v["Court II"][0] == 0, f"the keyed row must have struck down nothing; it reads {v['Court II'][0]}"
    assert v["Court II"][2] == min(x[2] for x in v.values()) == 2, \
        "the keyed row must also hold the smallest share decided against the government"
    assert v["Court II"][1] > 0, \
        "the keyed row must still HEAR cases against the government, since holding the power is not the issue"
    for lab in ("Court I", "Court III"):
        assert v[lab][0] > 0, f"{lab} must have struck something down, or the contrast disappears"
    return "one row hears 96 cases against the government, strikes down nothing, and decides 2 percent against it"


def q21(table, item):
    v = _jrev(table)
    assert v["Court I"][0] == max(x[0] for x in v.values()) == 41, "the keyed row must lead on laws struck down"
    assert v["Court I"][2] == max(x[2] for x in v.values()) == 28, \
        "the keyed row must also lead on the share decided against the government"
    assert v["Court III"][2] < v["Court I"][2] and v["Court III"][0] > 0, \
        "the rejected middle row must have struck something down on a smaller share, as its option says"
    return "one row leads both on laws struck down, 41, and on the share decided against the government, 28 percent"


def q22(table, item):
    col = cg.col(table, STRUCK)
    total = sum(col)
    assert total == 58, f"the keyed total recomputes to {total}"
    assert max(col) == 41 and sorted(col)[1] == 17, "the 41 and 17 distractors must be single rows"
    assert 41 - 17 == 24, "the 24 distractor must be the difference between two rows"
    assert sum(cg.col(table, CASES)) == 610, "the 610 distractor must be the total of a different column"
    return f"the struck-down column reads {col} and sums to {total:.0f}; every distractor is a row, a difference, or another column's total"


def _appt(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q23(table, item):
    v = _appt(table)
    r = v["Court W"]
    assert "nominated by the head of state" in r and "elected upper chamber" in r and "15 years" in r, \
        f"the keyed row reads {r!r}"
    for lab in ("Court X", "Court Y", "Court Z"):
        assert "15 years" not in v[lab], f"{lab} must not also state a 15-year term"
    return "one row alone pairs nomination by the head of state, approval by an ELECTED upper chamber, and a 15-year term"


def q24(table, item):
    v = _appt(table)
    r = v["Court X"]
    assert "judicial council" in r and "confirmed by the elected upper chamber" in r, f"the keyed row reads {r!r}"
    for lab in ("Court W", "Court Y", "Court Z"):
        assert "judicial council" not in v[lab], f"{lab} must not also involve a judicial council"
    return "one row alone inserts a judicial council's recommendation before the head of state and an elected chamber's confirmation after"


def q25(table, item):
    v = _appt(table)
    r = v["Court Y"]
    assert "appointed upper chamber" in r, f"the keyed row reads {r!r}"
    assert "elected upper chamber" in v["Court W"] and "elected upper chamber" in v["Court X"], \
        "the two rejected chamber routes must be ELECTED, which is what separates them from the key"
    assert "judicial council" not in r, "the keyed row must have no council stage"
    return "one row alone routes approval through an APPOINTED upper chamber rather than an elected one"


CLAIMS = [
 ("subservient to the decisions of the governing party",
  "EK PAU-3.G.1.a states that in China rule by law, instead of rule of law, means the judicial system is subservient to the decisions of the Chinese Communist Party. EK PAU-1.B.1.a defines the rule of law as governance by law rather than by arbitrary decisions of individual officials, which is the contrast the parenthesis draws."),
 ("the Chinese Communist Party",
  "EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments, alongside the judicial system's subservience to its decisions. EK PAU-4.A.2 explains that only that party may control governing power."),
 ("based on religious law",
  "EK PAU-3.G.1.b states that the Iranian judiciary's major function is to ensure the legal system is based on religious law. Devolution disputes belong to the United Kingdom's Supreme Court under EK PAU-3.G.1.i and confirming ministers to the Majles under EK PAU-3.E.1.b."),
 ("training in Islamic Sharia law",
  "EK PAU-3.G.1.b states that because the judiciary's major function is a legal system based on religious law, judges must be trained in Islamic Sharia law. The rejected qualifications describe appointment routes in other course countries."),
 ("nominate half of the Guardian Council with approval",
  "EK PAU-3.G.1.b states that the head of the judiciary is appointed by the Supreme Leader and can nominate half of the Guardian Council with approval by the Majles, and EK PAU-3.C.2.b has the Supreme Leader appointing the other half. Half in both places, never the whole body."),
 ("in transition",
  "EK PAU-3.G.1.c states that the Mexican judiciary is in transition, that the Supreme Court has the power of judicial review, and that subsequent constitutional amendments have been implemented with the intent of making the system more independent and effective. The rejected descriptions belong to China, Russia, Iran and the United Kingdom."),
 ("term of 15 years",
  "EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are nominated by the president and approved by the Senate for a term of 15 years. The judicial council route belongs to Nigeria under EK PAU-3.G.1.f and the appointed upper chamber to Russia under EK PAU-3.G.1.h."),
 ("reestablish its legitimacy and independence",
  "EK PAU-3.G.1.e states that the Nigerian judiciary has the power of judicial review and that an effort has been made to reestablish its legitimacy and independence by reducing corruption. EK PAU-1.C.3 supplies the connection between judicial independence and corruption control."),
 ("system of federalism",
  "EK PAU-3.G.1.e states that under the system of federalism, Islamic Sharia Courts have been established in the north of Nigeria, and EK PAU-2.A.1 lists Nigeria among the federal states. A legal order differing by region is what dividing power among levels makes possible."),
 ("recommended by a judicial council",
  "EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate. The three-stage route is what distinguishes it from Mexico's two-stage route at EK PAU-3.G.1.d."),
 ("target opposition",
  "EK PAU-3.G.1.g states that Russia's government uses the judicial system to target opposition. The same statement retains the courts' constitutional power of judicial review, so the framework is not describing that power's abolition."),
 ("has not been used to limit the authority",
  "EK PAU-3.G.1.g states both halves in one sentence: although constitutionally the courts have the power of judicial review, this power has not been used to limit the authority of the governing branches. Keying only one half would leave the other defensible."),
 ("approved by the Federation Council",
  "EK PAU-3.G.1.h states that Russia's judges are nominated by the president and approved by the Federation Council, which EK PAU-3.E.1.e describes as appointed rather than elected. The Duma's confirming role is over the prime minister, not judges."),
 ("common law, to enforce the rule of law",
  "EK PAU-3.G.1.i states that the United Kingdom's judicial system uses common law to enforce the rule of law, and EK PAU-1.B.1.a makes adherence to the rule of law one of the framework's indicators of a regime's place on the democratic-authoritarian scale."),
 ("final court of appeals",
  "EK PAU-3.G.1.i names serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes as major functions of the United Kingdom's Supreme Court. The rejected sets belong to Iran's Guardian Council, Russia's Federation Council and Iran's head of the judiciary."),
 ("only in the third is that power described as not having been used",
  "EK PAU-3.G.1.c gives Mexico's Supreme Court judicial review, EK PAU-3.G.1.e gives Nigeria's judiciary the same, and EK PAU-3.G.1.g gives Russia's courts the power constitutionally while stating it has not been used to limit the governing branches."),
 ("only one inserts a judicial council's recommendation",
  "EK PAU-3.G.1.d has Mexico's magistrates nominated by the president and approved by the Senate, while EK PAU-3.G.1.f has Nigeria's judges recommended by a judicial council, appointed by the president and confirmed by the Senate. EK PAU-3.E.1.c and EK PAU-3.E.1.d describe both Senates as elected."),
 ("one of those chambers is elected and the other appointed",
  "EK PAU-3.G.1.d has Mexico's president nominating and the Senate approving and EK PAU-3.G.1.h has Russia's president nominating and the Federation Council approving. EK PAU-3.E.1.c calls that Senate elected and EK PAU-3.E.1.e calls the Federation Council appointed, which is where the routes part."),
 ("the other exists chiefly to ensure the legal system rests on religious law",
  "EK PAU-3.G.1.a states that China's judicial system is subservient to the decisions of the Communist Party, and EK PAU-3.G.1.b that the Iranian judiciary's major function is a legal system based on religious law. Both are constrained, and by different things."),
 ("struck down nothing in twenty years",
  "EK PAU-3.G.1.g describes courts holding judicial review constitutionally without using it against the governing branches. Recomputed in q20 above: one row hears such cases, strikes down nothing, and decides the smallest share against the government, so holding a power and exercising it come apart."),
 ("struck down the most laws or acts",
  "EK PAU-3.G.1.c and EK PAU-3.G.1.e describe judiciaries holding the power of judicial review, and exercising it means deciding against the government at least sometimes. Recomputed in q21 above: one row leads on both measures at once."),
 ("58",
  "Recomputed in q22 above by summing the struck-down column. Every distractor is a single row, the difference between two rows, or the total of a different column."),
 ("for a term of 15 years",
  "EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are nominated by the president and approved by the Senate for a term of 15 years, and EK PAU-3.E.1.c describes that Senate as elected. Recomputed in q23 above: one row carries all three features, and the framework does state this term length."),
 ("confirmed by the elected upper chamber",
  "EK PAU-3.G.1.f states that Nigeria's judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, which EK PAU-3.E.1.d describes as elected. Recomputed in q24 above: only one row carries the council stage."),
 ("approved by an appointed upper chamber",
  "EK PAU-3.G.1.h states that Russia's judges are nominated by the president and approved by the Federation Council, which EK PAU-3.E.1.e describes as appointed. Recomputed in q25 above: the two rejected chamber routes are elected, which is what separates them from the key."),
 ("very few precise numbers",
  "EK PAU-3.G.1.d prints the 15-year figure, and the framework's other precise numbers in these units are few -- Iran's two 4-year presidential terms, China's at least 55 recognized ethnic minorities, Nigeria's more than 250 ethnic groups and 36 states, and ethnic Russians at more than 80 percent. All are course content rather than optional activities."),
 ("depends on which is being asked",
  "EK PAU-3.G.1.g states both halves in one sentence, so a question about the power on paper and a question about the power in practice have different answers. It is the same form-against-practice split EK PAU-3.E.1.a and EK PAU-3.F.1.a draw for China's legislature."),
 ("recommendation stage that precedes",
  "EK PAU-3.G.1.f states that Nigeria's judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, so the council acts before the president rather than replacing a stage. EK PAU-3.G.1.e connects that structure to the effort to reestablish the judiciary's legitimacy and independence."),
 ("governing party controls most judicial appointments",
  "EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments, and EK PAU-4.A.2 makes that party the only one permitted to control governing power. The rejected descriptions run through a head of state, a legislature or a judicial council, which are state institutions."),
 ("differ in function and in how judges are appointed",
  "EK PAU-3.G.1 opens by stating that judiciaries in course countries have different functions and use various methods to appoint judges, and its nine sub-points run from subservience to a party, through a religious mission, to judicial review and common law enforcement of the rule of law."),
]

cg.check(k2_8, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
