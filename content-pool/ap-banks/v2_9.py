# AP U.S. GOVERNMENT AND POLITICS 2.9 The Role of the Judicial Branch -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.9.A: explain the role of LEGAL PRECEDENT in judicial
# decision making.
# Suggested skill for this topic (CED p. 69): 1.D, describe political
# principles, institutions, processes, policies and behaviors ILLUSTRATED IN
# DIFFERENT SCENARIOS IN CONTEXT. So most items here describe a court's
# situation and ask what it illustrates.
#
# Essential knowledge relied on:
#   EK 2.9.A.1 -- "STARE DECISIS (the legal doctrine under which courts follow
#     legal precedents when deciding cases with SIMILAR FACTS) plays an
#     important role in judicial decision making."
#   EK 2.9.A.2 -- "IDEOLOGICAL CHANGES in the composition of the Supreme Court
#     DUE TO PRESIDENTIAL APPOINTMENTS have led to the Court's ESTABLISHING NEW
#     OR REJECTING EXISTING precedents."
#
# THE TWO STATEMENTS PULL IN OPPOSITE DIRECTIONS, AND THAT IS THE TOPIC. One
# says courts follow what was decided before; the other says the Court's
# composition changes and precedents fall. A bank that teaches only the first
# leaves a student unable to explain any overruling; a bank that teaches only
# the second leaves them thinking precedent is decoration. Items 1 to 10 are
# stare decisis, items 11 to 18 are change, and items 27 to 30 ask how the two
# fit together.
#
# THE PHRASE "SIMILAR FACTS" IS LOAD-BEARING and items 4, 5 and 6 turn on it.
# EK 2.9.A.1's own parenthesis limits stare decisis to cases with similar facts,
# which is why DISTINGUISHING a case -- showing the facts differ -- is a court's
# ordinary alternative to following or overruling. A student who thinks the only
# options are "follow" and "overrule" has missed the move courts make most.
#
# WHAT EK 2.9.A.2 ATTRIBUTES THE CHANGE TO, precisely: ideological changes in
# COMPOSITION, due to PRESIDENTIAL APPOINTMENTS. Not to public opinion, not to
# individual justices changing their minds, and not to Congress. That causal
# chain is examinable and items 11 to 14 keep it intact.
#
# Documents the CED attaches to 2.9.A (p. 26-27): Federalist No. 78.
# Required cases the CED attaches to 2.9.A (p. 32-33): New York Times Co. v.
# United States. The CED's illustrative examples for this topic -- Martin v.
# Hunter's Lessee, the New Deal conflict, United States v. Nixon -- are marked
# NOT REQUIRED, so no item here depends on knowing any of them, and none is
# named.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 78 is quoted verbatim.
# Non-required cases are described in the stem with the facts a student needs,
# as the CED promises the exam will do (p. 29). Both tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; vote splits
# are written in words. The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.9", "The Role of the Judicial Branch", 2)

_PRECEDENT = ("In a hypothetical study of one high court's constitutional decisions, the table "
              "reports how the court disposed of the governing precedent in each of four "
              "decades.")
_PRECEDENT_TABLE = dict(
    headers=["Decade", "Followed the precedent", "Distinguished the case", "Overruled the precedent"],
    rows=[["First", "412", "58", "3"],
          ["Second", "389", "71", "6"],
          ["Third", "355", "94", "11"],
          ["Fourth", "331", "108", "9"]])

_COMPOSITION = ("In a hypothetical study, the table reports how many precedents a nine member "
                "high court rejected in each of three periods, alongside how many of its "
                "members had been appointed within the preceding decade.")
_COMPOSITION_TABLE = dict(
    headers=["Period", "Members appointed within the preceding decade", "Precedents rejected"],
    rows=[["First period", "1", "2"],
          ["Second period", "3", "5"],
          ["Third period", "6", "14"]])

QUESTIONS = [
 dict(q="According to the course framework, stare decisis is",
   choices=[
     "the legal doctrine under which courts follow legal precedents when deciding cases with similar facts",
     "the doctrine that courts may declare acts of the other branches unconstitutional",
     "the rule that a court may hear only cases within its jurisdiction",
     "the requirement that judges recuse themselves from cases involving personal interests",
     "the principle that Supreme Court decisions bind only the parties to the case"], ans=0,
   why="EK 2.9.A.1 gives this definition in its own parenthesis, and the phrase 'with similar facts' is part of it. The second option describes judicial review, which is EK 2.8.A.1's subject."),

 dict(q="According to the course framework, what role does stare decisis play?",
   choices=[
     "An important role in judicial decision making",
     "No role, since each case is decided on its own facts alone",
     "A role only in state courts and not in federal courts",
     "A role only in cases involving the Constitution",
     "A role that binds Congress as well as the courts"], ans=0,
   why="EK 2.9.A.1 says stare decisis 'plays an important role in judicial decision making,' without limiting it to a level of court or a category of case."),

 dict(q="Why does a doctrine of following past decisions make a legal system more useful to the people governed by it?",
   choices=[
     "People and institutions can predict how a rule will be applied and plan accordingly",
     "It guarantees that every decision will be correct",
     "It prevents any court from ever changing its mind",
     "It removes the need for legislatures to write statutes",
     "It ensures that judges will agree with public opinion"], ans=0,
   why="Predictability is what a doctrine of consistency buys, which is why EK 2.9.A.1 calls the role important. EK 2.9.A.2's own account of rejected precedents shows the doctrine does not prevent change."),

 dict(q="A court is asked to apply a precedent to a new case. Under the definition in the course framework, what must be true for stare decisis to govern?",
   choices=[
     "The facts of the new case must be similar to those of the decided case",
     "The two cases must arise in the same state",
     "The two cases must have been argued by the same lawyers",
     "The earlier case must have been decided unanimously",
     "The earlier case must have been decided within the past ten years"], ans=0,
   why="EK 2.9.A.1's parenthesis limits the doctrine to cases 'with similar facts,' which is the condition the item asks for. Nothing in the framework conditions precedent on unanimity, geography or age."),

 dict(q="A court concludes that an earlier decision does not control because the facts before it differ in a way the earlier rule depended on. What has the court done?",
   choices=[
     "Distinguished the case, which leaves the earlier precedent standing for its own facts",
     "Overruled the precedent, which removes it entirely",
     "Followed the precedent, since it referred to the earlier decision",
     "Exercised judicial review over the earlier decision",
     "Certified the question to the legislature for an answer"], ans=0,
   why="EK 2.9.A.1 makes similar facts the trigger for the doctrine, so a court finding the facts different declines to apply the precedent without disturbing it. Overruling is the different act EK 2.9.A.2 describes."),

 dict(q="What is the practical difference between distinguishing a case and overruling a precedent?",
   choices=[
     "Distinguishing leaves the earlier rule in force for cases like the earlier one; overruling withdraws the rule altogether",
     "Distinguishing withdraws the earlier rule; overruling leaves it in force",
     "Both remove the earlier rule, but only overruling requires a written opinion",
     "Both leave the earlier rule in force, but only distinguishing may be appealed",
     "There is no difference; the two terms describe the same act"], ans=0,
   why="A distinction narrows a precedent's reach by finding the facts unlike; an overruling rejects the rule itself. Collapsing the two makes EK 2.9.A.1 and EK 2.9.A.2 into a single indistinguishable claim."),

 dict(q="A lower court believes a Supreme Court precedent was wrongly decided but the facts before it are closely similar. What does stare decisis require?",
   choices=[
     "The lower court must follow the precedent even while disagreeing with it",
     "The lower court may disregard the precedent because it disagrees",
     "The lower court must refer the case to Congress",
     "The lower court must dismiss the case for lack of jurisdiction",
     "The lower court may overrule the Supreme Court's decision"], ans=0,
   why="EK 2.9.A.1's doctrine is that courts FOLLOW precedents in cases with similar facts, and a lower court's disagreement is not one of the doctrine's exceptions. Only the Supreme Court can reject its own precedent."),

 dict(q="Which of the following is the strongest argument for adhering to a precedent a court now considers mistaken?",
   choices=[
     "People have arranged their affairs in reliance on the rule, and changing it would upset settled expectations",
     "A court is never permitted to correct an error",
     "The earlier court was necessarily better informed",
     "Precedent is required by the text of Article III",
     "Overruling a precedent requires the consent of Congress"], ans=0,
   why="Reliance is the serious argument for adhering, and it follows from the predictability that makes EK 2.9.A.1's doctrine important. The other options assert prohibitions and requirements that do not exist."),

 dict(q="Which of the following is the strongest argument for rejecting a precedent a court considers mistaken?",
   choices=[
     "A rule that was wrong when decided continues to produce wrong outcomes for as long as it stands",
     "The court's current members were appointed more recently",
     "Public opinion has moved against the earlier decision",
     "The earlier decision was not unanimous",
     "Congress has criticized the earlier decision"], ans=0,
   why="The argument on the merits is that error compounds, which is what has to be weighed against reliance. Composition, opinion polls and congressional criticism explain WHY courts overrule without justifying it."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. What role would that decision play in a later case raising a similar question?",
   choices=[
     "It would be the governing precedent, which a court deciding a case with similar facts would be expected to follow",
     "It would be irrelevant, since each case is decided on its own facts alone",
     "It would bind Congress but not the courts",
     "It would apply only to the newspaper that was a party to it",
     "It would have to be re-ratified by the Senate before a later court could rely on it"], ans=0,
   why="EK 2.9.A.1's doctrine makes a decided case the governing rule for later cases with similar facts, which is precisely what a holding about prior restraint supplies for the next prior restraint case."),

 dict(q="According to the course framework, what has led the Supreme Court to establish new precedents or reject existing ones?",
   choices=[
     "Ideological changes in the composition of the Court due to presidential appointments",
     "Changes in public opinion measured by national surveys",
     "Instructions issued by Congress to the Court",
     "Constitutional amendments requiring the Court to reconsider",
     "The retirement of the Chief Justice in each generation"], ans=0,
   why="EK 2.9.A.2 names ideological changes in COMPOSITION, and attributes those changes to PRESIDENTIAL APPOINTMENTS. The framework does not attribute precedential change to opinion, Congress or amendment."),

 dict(q="EK 2.9.A.2 describes a causal chain. Which sequence states it correctly?",
   choices=[
     "Presidential appointments change the Court's composition, which changes its ideological balance, which leads to new or rejected precedents",
     "New precedents change the Court's composition, which leads presidents to make appointments",
     "Congress changes the Court's composition, which leads to new or rejected precedents",
     "Public opinion changes the Court's ideology, which leads presidents to make appointments",
     "Rejected precedents lead to constitutional amendments, which change the Court's composition"], ans=0,
   why="EK 2.9.A.2 runs from appointments to composition to ideological change to precedent. Each other option reverses a link or substitutes an actor the framework does not name."),

 dict(q="A president appoints three justices over one term, and within a decade the Court rejects several precedents it had reaffirmed for years. Which claim from the course framework does this best illustrate?",
   choices=[
     "That ideological changes in composition due to presidential appointments have led the Court to reject existing precedents",
     "That stare decisis plays no role in judicial decision making",
     "That the Court follows public opinion in constitutional cases",
     "That Congress may direct the Court to reconsider its decisions",
     "That precedents expire automatically after a fixed period"], ans=0,
   why="EK 2.9.A.2 is exactly this sequence. Note that it does not deny EK 2.9.A.1: precedent can play an important role and still be rejected when the composition of the deciding body changes."),

 dict(q="Which observation would most WEAKEN a claim that a particular overruling was caused by ideological change in the Court's composition?",
   choices=[
     "The justices who joined the overruling included several appointed by presidents of the party that had supported the earlier rule",
     "The Court's newest members joined the overruling",
     "The overruling followed a change in which party held the presidency",
     "The overruling was decided by a narrow margin",
     "The earlier precedent had stood for several decades"], ans=0,
   why="EK 2.9.A.2's mechanism is ideological change traceable to appointments, so the strongest rebuttal is a majority that crosses appointing-party lines. The other options are consistent with the composition explanation rather than against it."),

 dict(q="Why does the framework's account of precedential change make judicial appointments politically consequential?",
   choices=[
     "Because the rules a court will apply depend in part on who sits on it, an appointment is a decision about future law",
     "Because a justice may enact statutes once confirmed",
     "Because appointments determine which cases the Court is required to hear",
     "Because a newly appointed justice may reverse a decision without a case before the Court",
     "Because appointments set the number of seats on the Court"], ans=0,
   why="EK 2.9.A.2 links composition to precedent, and EK 2.5.A.2 adds that judicial appointments are the president's longest lasting influence. The other options describe powers no justice holds."),

 dict(q="A commentator says that because the Court sometimes overrules itself, precedent is meaningless. What is the most accurate response?",
   choices=[
     "Overrulings are rare relative to the number of cases decided, and the framework calls the role of precedent important while also recording that precedents are sometimes rejected",
     "The commentator is right, since the framework says precedent plays no role",
     "The Court has never overruled one of its own precedents",
     "Precedent binds only lower courts and has never applied to the Supreme Court",
     "The framework treats overruling as the ordinary way cases are decided"], ans=0,
   why="EK 2.9.A.1 and EK 2.9.A.2 are both in the framework and are not in conflict: a doctrine can shape most decisions while yielding in some. Treating exceptions as the rule is the error."),

 dict(q="A court must decide whether to follow a precedent, distinguish the case, or overrule the precedent. Which consideration belongs to the FIRST of those decisions under EK 2.9.A.1?",
   choices=[
     "Whether the facts before the court are similar to those of the decided case",
     "Whether the current members would have decided the earlier case the same way",
     "Whether the earlier decision remains popular",
     "Whether Congress has expressed a view on the earlier decision",
     "Whether the earlier decision was unanimous"], ans=0,
   why="EK 2.9.A.1's own condition is similar facts, which is the threshold question for whether the doctrine applies at all. The other considerations bear on whether to overrule, which is a later and different question."),

 dict(q="Read the following excerpt.\n\n“To avoid an arbitrary discretion in the courts, it is indispensable that they should be bound down by strict rules and precedents, which serve to define and point out their duty in every particular case that comes before them.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhat function does Hamilton assign to precedent in this passage?",
   choices=[
     "It constrains judges' discretion by fixing in advance what their duty is in a given case",
     "It allows judges to decide each case according to their own sense of justice",
     "It gives the legislature authority over how courts decide cases",
     "It requires that judges be elected rather than appointed",
     "It permits courts to disregard the Constitution when precedent conflicts with it"], ans=0,
   why="Hamilton's stated purpose is to avoid arbitrary discretion, and precedent does that by defining the judge's duty before the case arises. The passage is an argument for constraint, not for freedom."),

 dict(q="How does Federalist No. 78's argument about precedent relate to its argument for judicial independence?",
   choices=[
     "Independence makes judges free of political pressure, and precedent keeps that freedom from becoming personal discretion",
     "Independence and precedent are alternatives, and the Constitution adopted only one",
     "Precedent makes independence unnecessary, since the rules decide the cases",
     "Independence requires that judges disregard precedent",
     "Federalist No. 78 discusses independence but says nothing about precedent"], ans=0,
   why="The two arguments answer two different objections in the same paper: independence protects judges from the other branches, and being bound by rules and precedents protects litigants from the judges."),

 dict(q="A non-required case: a state supreme court holds that its own decision from thirty years earlier should no longer be followed, because the reasoning rested on an assumption later cases had abandoned. Which concept does this illustrate?",
   choices=[
     "Overruling a precedent, which the framework attributes in the Supreme Court's case to ideological changes in composition",
     "Distinguishing a case on its facts",
     "Exercising judicial review over a statute",
     "Applying stare decisis to a case with similar facts",
     "Certifying a question to the legislature"], ans=0,
   why="Rejecting the rule itself rather than confining it to its facts is overruling. EK 2.9.A.2 records that the Supreme Court's own rejections have followed ideological changes in composition due to presidential appointments."),

 dict(q=_PRECEDENT + " Which conclusion is best supported by the data?",
   table=_PRECEDENT_TABLE,
   choices=[
     "The court followed the governing precedent in the large majority of cases in every decade",
     "The court overruled more precedents than it followed in at least one decade",
     "The number of cases in which the court followed precedent rose across the four decades",
     "The court never distinguished a case in any decade",
     "Overrulings outnumbered distinctions in every decade"], ans=0,
   why="The followed column runs 412, 389, 355 and 331 against overrulings of 3, 6, 11 and 9, so following dominates throughout. Following falls rather than rises, and distinctions exceed overrulings by a wide margin in every decade."),

 dict(q=_PRECEDENT + " Which claim from the course framework do these data most directly support?",
   table=_PRECEDENT_TABLE,
   choices=[
     "That stare decisis plays an important role in judicial decision making",
     "That ideological changes in composition have led the court to reject precedents",
     "That courts may declare acts of the legislature unconstitutional",
     "That life tenure allows a court to function independent of the political climate",
     "That precedent binds the legislature as well as the courts"], ans=0,
   why="A table in which the court follows the governing precedent in between about three quarters and seven eighths of dispositions is EK 2.9.A.1's importance measured. The overruling column is far too small to be the table's main story."),

 dict(q=_PRECEDENT + " A student concludes from these data that the court became less willing to follow precedent over time. Which feature of the data most complicates that conclusion?",
   table=_PRECEDENT_TABLE,
   choices=[
     "Distinctions rose far more than overrulings did, and distinguishing a case leaves the precedent standing",
     "Overrulings rose in every decade without exception",
     "The number of cases following precedent rose in every decade",
     "The table reports no distinctions at all",
     "The table covers a single decade, so no trend can be observed"], ans=0,
   why="Distinctions rise from 58 to 108 while overrulings rise only from 3 to 9 and then fall, and a distinction respects the precedent rather than rejecting it. Reading a rise in distinctions as abandonment of precedent misreads what the column records."),

 dict(q=_COMPOSITION + " Which conclusion is best supported by the data?",
   table=_COMPOSITION_TABLE,
   choices=[
     "Both the number of recently appointed members and the number of precedents rejected rose across the three periods",
     "The number of recently appointed members rose while precedents rejected fell",
     "A majority of the court had been appointed within the preceding decade in every period",
     "The number of precedents rejected was the same in every period",
     "No precedents were rejected in any period"], ans=0,
   why="Recent appointments run 1, 3 and 6 and rejections run 2, 5 and 14, both rising. A majority of a nine member court is five, which only the third period reaches."),

 dict(q=_COMPOSITION + " Which claim from the course framework do these data most directly illustrate?",
   table=_COMPOSITION_TABLE,
   choices=[
     "That ideological changes in composition due to presidential appointments have led to the rejection of existing precedents",
     "That stare decisis plays an important role in judicial decision making",
     "That courts follow precedents when deciding cases with similar facts",
     "That the judiciary has neither force nor will but merely judgment",
     "That judicial review checks the power of the other branches"], ans=0,
   why="EK 2.9.A.2 links turnover in the Court's membership to the rejection of precedents, and the table pairs exactly those two quantities. The other options name statements these columns do not measure."),

 dict(q=_COMPOSITION + " A student concludes from these data that new appointments CAUSE precedents to be rejected. Which limitation of the data most undercuts that conclusion?",
   table=_COMPOSITION_TABLE,
   choices=[
     "The table records no information about the cases themselves, so it cannot show that turnover rather than the merits produced the rejections",
     "The table omits the number of precedents rejected, so no comparison is possible",
     "The table covers a single period, so no trend can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The two series move in opposite directions, which rules out any relationship"], ans=0,
   why="Two series rising together are consistent with the composition explanation and with a period in which many precedents were ripe for reconsideration for reasons unrelated to who sat on the court. Both columns and three periods are plainly present."),

 dict(q="Which statement best reconciles EK 2.9.A.1 and EK 2.9.A.2?",
   choices=[
     "Precedent governs most decisions, and changes in who decides account for the minority of cases in which it does not",
     "The two statements contradict each other, and only one can be true",
     "Precedent governs no decisions, and composition accounts for all of them",
     "Composition never affects outcomes, and precedent accounts for all of them",
     "The two statements describe different court systems"], ans=0,
   why="EK 2.9.A.1 calls the role of precedent important and EK 2.9.A.2 records that precedents are sometimes rejected, which are compatible claims about the ordinary case and the exception."),

 dict(q="A justice writes that she would have decided an earlier case differently but votes to follow it anyway. Which principle is she applying?",
   choices=[
     "Stare decisis, under which a court follows precedent in cases with similar facts even when its current members disagree with the earlier result",
     "Judicial review, under which a court may set aside acts of other branches",
     "Judicial activism, under which a court may overturn existing precedent",
     "Separation of powers, under which each branch exercises distinct functions",
     "Distinguishing, under which a court finds the facts materially different"], ans=0,
   why="Following a rule one would not have adopted is exactly what EK 2.9.A.1's doctrine asks, and it is what makes the doctrine a constraint rather than a preference. She is not distinguishing, since she treats the earlier case as controlling."),

 dict(q="Which question would best measure the strength of stare decisis in a particular court?",
   choices=[
     "In cases where a precedent squarely governs, how often does the court follow it rather than overruling it?",
     "How many cases does the court decide each year?",
     "How many justices sit on the court?",
     "How long are the court's opinions?",
     "How often does the court hear cases involving the federal government?"], ans=0,
   why="EK 2.9.A.1's doctrine is about what a court does when a precedent applies, so the measure has to condition on the precedent applying. Volume, size and opinion length measure other things."),

 dict(q="Which pair of facts, taken together, would best support an argument that a court's treatment of precedent had changed for reasons other than the merits of the cases?",
   choices=[
     "A sharp rise in overrulings that coincides with substantial turnover in membership, with no comparable change in the kinds of cases reaching the court",
     "A sharp rise in overrulings and a sharp rise in the number of cases filed",
     "Substantial turnover in membership and a decline in the length of opinions",
     "A rise in the number of distinctions and a rise in the number of cases followed",
     "A decline in overrulings and a decline in turnover"], ans=0,
   why="EK 2.9.A.2's mechanism is composition, so the argument needs turnover to coincide with the change AND the caseload to stay comparable, which is what rules out the merits explanation. Any one of those facts alone leaves the alternative open."),
]
