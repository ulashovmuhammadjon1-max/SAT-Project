# AP ENVIRONMENTAL SCIENCE 9.2 Reducing Ozone Depletion
# CED effective Fall 2026, Unit 9 Global Change. Enduring understanding STB-4, local and
# regional human activities can have impacts at the global level. Learning objective
# STB-4.B: describe chemicals used to substitute for chlorofluorocarbons (CFCs).
# Suggested skill 7.B, describe potential responses or approaches to environmental
# problems.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.B.1  Ozone depletion can be mitigated by replacing ozone-depleting chemicals
#              with substitutes that do not deplete the ozone layer. Hydrofluorocarbons
#              (HFCs) are one such replacement, but some are strong greenhouse gases.
#
# THAT IS THE WHOLE OF THIS TOPIC'S OWN CONTENT. One sentence with three parts: the
# strategy is REPLACEMENT, the named replacement is HFCs, and the caveat is that SOME of
# them are strong greenhouse gases. Every item here keys one of those three, or reasons
# from them, or reads its own table.
#
# NEIGHBOURING STATEMENTS CITED, and only where the item genuinely needs them:
#   STB-4.A.2  CFCs are an anthropogenic cause of stratospheric ozone depletion -- this
#              is what makes replacement a response to the stated cause.
#   STB-4.A.3  a decrease in stratospheric ozone increases the UV rays reaching the
#              surface, and exposure can lead to skin cancer and cataracts -- the harm
#              the mitigation is aimed at.
#   STB-4.C.1  the principal greenhouse gases include CFCs.
#   STB-4.D.1  carbon dioxide has a global warming potential of 1 and is the reference
#              for comparing greenhouse gases; CFCs have the highest GWP.
# Items 13, 14 and 26 lean on those; every one says so in verify_e9_2.py.
#
# ON SCOPE. Topic 9.1 keys the causes and consequences of the depletion itself and topic
# 9.3 keys the greenhouse gases and their potencies. No key here restates either as this
# topic's own content.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e9_2.py from that table alone.
#
# NOT KEYED: no treaty, no date, no named commercial refrigerant, and no claim that every
# hydrofluorocarbon is a strong greenhouse gas -- the framework says some are.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("9.2", "Reducing Ozone Depletion", 9)

_T_SUBS = dict(
    headers=["Compound available for a cooling system", "Does it deplete the ozone layer",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Chlorofluorocarbon A", "yes", "10900"],
          ["Hydrofluorocarbon B", "no", "1430"],
          ["Hydrofluorocarbon C", "no", "4.0"],
          ["Hydrocarbon D", "no", "3.0"]])

_T_PHASEOUT = dict(
    headers=["Period of the record",
             "Production of ozone depleting chemicals (thousands of tons per year)",
             "Springtime ozone column over the pole (Dobson units)"],
    rows=[["Period 1", "900", "160"],
          ["Period 2", "400", "180"],
          ["Period 3", "60", "215"],
          ["Period 4", "5.0", "245"]])

_T_RISE = dict(
    headers=["Decade of the record",
             "Use of chlorofluorocarbons (thousands of tons)",
             "Use of hydrofluorocarbons (thousands of tons)"],
    rows=[["Decade 1", "800", "5.0"],
          ["Decade 2", "300", "190"],
          ["Decade 3", "20", "520"]])

_T_GWP = dict(
    headers=["Refrigerant under consideration", "Mass that would be released (tons)",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Option 1", "10", "1400"],
          ["Option 2", "10", "4.0"],
          ["Option 3", "10", "150"]])

_T_CRITERIA = dict(
    headers=["Candidate replacement", "Ozone depleting potential",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Candidate W", "0.60", "1200"],
          ["Candidate X", "0", "3900"],
          ["Candidate Y", "0", "6.0"],
          ["Candidate Z", "0.90", "20"]])

_T_RECOVERY = dict(
    headers=["Period after the replacement program began",
             "Springtime ozone column (Dobson units)",
             "Ultraviolet index measured at the surface"],
    rows=[["Period 1", "170", "14"],
          ["Period 2", "200", "12"],
          ["Period 3", "240", "9.0"],
          ["Period 4", "280", "7.0"]])

QUESTIONS = [

 dict(q="How does the framework say ozone depletion can be mitigated?",
      choices=[
        "By replacing ozone depleting chemicals with substitutes that do not deplete the "
        "ozone layer",
        "By releasing additional ozone depleting chemicals at a slower rate",
        "By manufacturing ozone at the surface and releasing it into the air",
        "By reducing the amount of sunlight that reaches the stratosphere",
        "By treating the water in streams and rivers before it is discharged"],
      ans=0,
      why="STB-4.B.1 states that ozone depletion can be mitigated by replacing "
          "ozone-depleting chemicals with substitutes that do not deplete the ozone layer. "
          "Slower release, surface manufacture, shading and water treatment are not the "
          "strategy the framework names."),

 dict(q="What does the framework identify hydrofluorocarbons as?",
      choices=[
        "One replacement for ozone depleting chemicals",
        "The main cause of stratospheric ozone depletion",
        "A natural factor in the loss of polar ozone",
        "A method of treating sewage before discharge",
        "A disinfectant applied to drinking water"],
      ans=0,
      why="STB-4.B.1 states that hydrofluorocarbons are one such replacement for "
          "ozone-depleting chemicals. Chlorofluorocarbons are the anthropogenic cause named "
          "in STB-4.A.2, and the rejected options belong to other topics."),

 dict(q="Four compounds available for the same use are compared.",
      table=_T_SUBS,
      choices=[
        "Every compound other than the chlorofluorocarbon avoids depleting the ozone layer, "
        "yet one of those substitutes still carries a very large warming potential",
        "Every compound listed depletes the ozone layer",
        "None of the compounds listed carries any warming potential",
        "The chlorofluorocarbon is the only compound with a large warming potential",
        "The substitutes all carry warming potentials close to that of carbon dioxide"],
      ans=0,
      why="The ozone column marks only the chlorofluorocarbon as depleting, while one "
          "hydrofluorocarbon row carries a warming potential in the thousands. STB-4.B.1 "
          "states that hydrofluorocarbons are one such replacement but that some are strong "
          "greenhouse gases."),

 dict(q="What drawback does the framework attach to hydrofluorocarbons?",
      choices=[
        "Some of them are strong greenhouse gases",
        "All of them deplete the ozone layer as much as the chemicals they replace",
        "They cannot be used in any cooling system",
        "They break down into chlorofluorocarbons after release",
        "They are the main cause of respiratory illness near the ground"],
      ans=0,
      why="STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are "
          "strong greenhouse gases. It does not say they deplete ozone, that they are "
          "unusable, or that they convert into the chemicals they replaced."),

 dict(q="Which chemicals is this topic about replacing?",
      choices=[
        "Chlorofluorocarbons",
        "Nitrogen fertilizers",
        "Persistent organic pollutants used as pesticides",
        "Heavy metals used in electronics",
        "Disinfectants used in sewage treatment"],
      ans=0,
      why="Learning objective STB-4.B concerns chemicals used to substitute for "
          "chlorofluorocarbons, and STB-4.A.2 names chlorofluorocarbons as an anthropogenic "
          "cause of stratospheric ozone depletion. The rejected options are pollutants "
          "treated in other units."),

 dict(q="Production of ozone depleting chemicals and polar ozone were recorded over four "
        "periods.",
      table=_T_PHASEOUT,
      choices=[
        "As production of the ozone depleting chemicals fell across the periods, the "
        "springtime ozone column rose",
        "As production of the ozone depleting chemicals fell, the springtime ozone column "
        "fell with it",
        "Production rose across the four periods",
        "The springtime ozone column was the same in all four periods",
        "The period with the largest production had the largest ozone column"],
      ans=0,
      why="The production column falls at every step while the ozone column rises at every "
          "step. STB-4.B.1 makes replacing ozone-depleting chemicals the way depletion is "
          "mitigated, and STB-4.A.2 names those chemicals as a cause."),

 dict(q="Why does replacing a chemical count as mitigation of ozone depletion rather than "
        "as a treatment of its effects?",
      choices=[
        "It removes from use the chemicals that cause the depletion, so the loss of ozone "
        "is prevented rather than repaired",
        "It repairs the ozone that has already been lost from the stratosphere",
        "It reduces the ultraviolet radiation without changing any chemical in use",
        "It treats the skin conditions that follow increased ultraviolet exposure",
        "It cools the stratosphere so that ozone cannot be destroyed"],
      ans=0,
      why="STB-4.B.1 describes replacing ozone-depleting chemicals with substitutes that "
          "do not deplete the layer, and STB-4.A.2 names those chemicals as a cause of the "
          "depletion, so the response acts on the cause."),

 dict(q="What property must a substitute have in order to address the ozone problem, "
        "according to the framework?",
      choices=[
        "It must not deplete the ozone layer",
        "It must be cheaper than the chemical it replaces",
        "It must be a naturally occurring compound",
        "It must break down within a single day of release",
        "It must have no warming potential of any kind"],
      ans=0,
      why="STB-4.B.1 defines the strategy as replacing ozone-depleting chemicals with "
          "substitutes that do not deplete the ozone layer, which is the stated "
          "requirement. Price, natural origin and rapid breakdown are not mentioned, and "
          "the framework acknowledges that some substitutes are strong greenhouse gases."),

 dict(q="What tension does the framework itself point out in the replacement strategy?",
      choices=[
        "A substitute can solve the ozone problem while some substitutes contribute "
        "strongly to the greenhouse effect",
        "A substitute can solve the greenhouse problem while making ozone depletion worse",
        "A substitute always solves both problems at once",
        "A substitute always makes both problems worse",
        "The framework identifies no tension in the strategy"],
      ans=0,
      why="STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are "
          "strong greenhouse gases, so the ozone problem is addressed while a climate "
          "concern can remain."),

 dict(q="Use of two classes of compound was recorded across three decades.",
      table=_T_RISE,
      choices=[
        "The use of chlorofluorocarbons fell across the decades while the use of "
        "hydrofluorocarbons rose",
        "The use of both classes fell across the decades",
        "The use of both classes rose across the decades",
        "The use of chlorofluorocarbons rose while the use of hydrofluorocarbons fell",
        "Neither class changed in use across the decades"],
      ans=0,
      why="The chlorofluorocarbon column falls at every step while the hydrofluorocarbon "
          "column rises at every step. STB-4.B.1 names hydrofluorocarbons as one "
          "replacement for ozone-depleting chemicals."),

 dict(q="Why does the framework say that some hydrofluorocarbons are strong greenhouse "
        "gases rather than that all of them are?",
      choices=[
        "The compounds in that class differ from one another, so the caution applies to "
        "part of the class rather than to all of it",
        "The framework means that every compound in the class is a strong greenhouse gas",
        "The framework means that none of the compounds in the class is a greenhouse gas",
        "The framework means that the compounds become greenhouse gases only after they "
        "deplete ozone",
        "The framework means that only the compounds that deplete ozone are greenhouse "
        "gases"],
      ans=0,
      why="STB-4.B.1 says that hydrofluorocarbons are one such replacement, but some are "
          "strong greenhouse gases, which qualifies the claim to part of the class. "
          "Reading it as all or as none would misstate the sentence."),

 dict(q="A company selects a replacement solely because it does not deplete the ozone "
        "layer. What does the framework's statement suggest about that choice?",
      choices=[
        "It meets the ozone requirement but may still carry a strong greenhouse effect, "
        "which the framework warns about",
        "It meets both the ozone requirement and every climate concern automatically",
        "It fails the ozone requirement because only chlorofluorocarbons meet it",
        "It is irrelevant, since the framework recommends no replacement at all",
        "It guarantees that the compound has no effect on the atmosphere"],
      ans=0,
      why="STB-4.B.1 makes not depleting the ozone layer the requirement for a substitute "
          "and then adds that some replacements are strong greenhouse gases, so the one "
          "criterion does not settle the other."),

 dict(q="Why is a chlorofluorocarbon a concern for both problems at once?",
      choices=[
        "The framework names it as a cause of stratospheric ozone depletion and also "
        "includes it among the principal greenhouse gases",
        "The framework names it as a greenhouse gas but not as a cause of ozone depletion",
        "The framework names it as a cause of ozone depletion but excludes it from the "
        "greenhouse gases",
        "The framework treats it as harmless in both respects",
        "The framework treats it as a natural compound with no human source"],
      ans=0,
      why="STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of stratospheric "
          "ozone depletion and STB-4.C.1 includes chlorofluorocarbons among the principal "
          "greenhouse gases, so both apply to the same compounds."),

 dict(q="Three refrigerants are compared for the same release. Which release would have "
        "the largest effect on warming, and how large is it in carbon dioxide terms?",
      table=_T_GWP,
      choices=[
        "The first option, whose release is equivalent to 14,000 tons of carbon dioxide",
        "The first option, whose release is equivalent to 1,400 tons of carbon dioxide",
        "The second option, whose release is equivalent to 14,000 tons of carbon dioxide",
        "The third option, whose release is equivalent to 15,000 tons of carbon dioxide",
        "The second option, whose release is equivalent to 40 tons of carbon dioxide"],
      ans=0,
      why="Multiplying each mass by its warming potential gives the carbon dioxide "
          "equivalent of each release, and the largest product belongs to the first row. "
          "STB-4.D.1 makes carbon dioxide the reference against which other greenhouse "
          "gases are compared, and STB-4.B.1 is the reason a replacement's warming "
          "potential matters."),

 dict(q="Two substitutes both avoid depleting the ozone layer, but one has a much larger "
        "warming potential. What does the framework's account favor?",
      choices=[
        "The one with the smaller warming potential, since the framework warns that some "
        "replacements are strong greenhouse gases",
        "The one with the larger warming potential, since a stronger compound works better",
        "Either one equally, since the framework considers only ozone depletion",
        "Neither one, since the framework rejects all substitutes",
        "The one that depletes more ozone, since that is the tested option"],
      ans=0,
      why="STB-4.B.1 requires a substitute not to deplete the ozone layer and adds that "
          "some replacements are strong greenhouse gases, so between two compounds that "
          "both pass the first test the warning applies to the second property."),

 dict(q="What does the word mitigated mean in the framework's statement about ozone "
        "depletion?",
      choices=[
        "That the depletion is reduced by acting on what causes it",
        "That the depletion is measured more accurately",
        "That the depletion is reported to the public",
        "That the depletion is allowed to continue at its present rate",
        "That the ozone already lost is manufactured and replaced"],
      ans=0,
      why="STB-4.B.1 states that ozone depletion can be mitigated by replacing "
          "ozone-depleting chemicals with substitutes that do not deplete the layer, so "
          "mitigation here is a reduction achieved by removing the cause."),

 dict(q="Which evidence would best show that the replacement strategy is working?",
      choices=[
        "Production of the ozone depleting chemicals falls and the ozone column measured "
        "over the pole recovers",
        "Production of the ozone depleting chemicals falls and their price rises",
        "The number of companies making cooling systems increases",
        "The ozone measured in the air people breathe near the ground rises",
        "The number of scientific papers about ozone increases"],
      ans=0,
      why="STB-4.B.1 makes replacement the mitigation and STB-4.A.3 makes the state of the "
          "stratospheric ozone the quantity at stake, so falling production together with a "
          "recovering column is the evidence. Ground level ozone belongs to EIN-3.C.4."),

 dict(q="Four candidate replacements were scored on two properties.",
      table=_T_CRITERIA,
      choices=[
        "Only one candidate both avoids depleting the ozone layer and carries a small "
        "warming potential",
        "Every candidate avoids depleting the ozone layer",
        "No candidate avoids depleting the ozone layer",
        "The candidate with the largest warming potential is also the one that depletes "
        "the most ozone",
        "Every candidate that avoids depleting ozone also carries a small warming potential"],
      ans=0,
      why="Two candidates carry a nonzero ozone depleting potential, and of the two that do "
          "not, one carries a warming potential in the thousands. STB-4.B.1 requires a "
          "substitute not to deplete the ozone layer and warns that some replacements are "
          "strong greenhouse gases."),

 dict(q="Why would continuing to use the original ozone depleting chemicals not count as "
        "mitigation?",
      choices=[
        "The strategy the framework describes is to replace those chemicals, so continuing "
        "to use them leaves the cause in place",
        "Those chemicals do not cause any ozone depletion",
        "Those chemicals become substitutes after long use",
        "The framework treats continued use as the preferred approach",
        "The framework says the ozone layer recovers no matter what is used"],
      ans=0,
      why="STB-4.B.1 describes mitigation as replacing ozone-depleting chemicals with "
          "substitutes that do not deplete the layer, and STB-4.A.2 names those chemicals "
          "as a cause of the depletion."),

 dict(q="What human health consequence is the replacement strategy ultimately aimed at "
        "avoiding?",
      choices=[
        "The skin cancer and cataracts that can follow increased ultraviolet exposure at "
        "the surface",
        "The respiratory problems that follow elevated ozone near the ground",
        "The dysentery that follows untreated sewage in rivers",
        "The mesothelioma that follows exposure to asbestos",
        "The reproductive harm that follows a biomagnified pollutant"],
      ans=0,
      why="STB-4.A.3 states that a decrease in stratospheric ozone increases the "
          "ultraviolet rays reaching the surface and that exposure can lead to skin cancer "
          "and cataracts, and STB-4.B.1 is the response to that depletion. The rejected "
          "options are the health effects of unit 8 pollutants."),

 dict(q="Which test would a candidate substitute need to pass before the framework would "
        "call it a solution to ozone depletion?",
      choices=[
        "A demonstration that it does not deplete the ozone layer",
        "A demonstration that it costs less than the chemical it replaces",
        "A demonstration that it is used in more than one country",
        "A demonstration that it can be manufactured quickly",
        "A demonstration that it dissolves in water"],
      ans=0,
      why="STB-4.B.1 defines the substitute by the property of not depleting the ozone "
          "layer. Cost, distribution, manufacturing speed and solubility are not part of "
          "the framework's statement."),

 dict(q="Measurements were taken over four periods after a replacement program began.",
      table=_T_RECOVERY,
      choices=[
        "The springtime ozone column rose across the periods while the ultraviolet index "
        "at the surface fell",
        "Both the ozone column and the ultraviolet index rose across the periods",
        "Both the ozone column and the ultraviolet index fell across the periods",
        "The ozone column fell while the ultraviolet index rose",
        "Neither measurement changed across the periods"],
      ans=0,
      why="The ozone column rises at every step while the ultraviolet index falls at every "
          "step. STB-4.A.3 states that a decrease in stratospheric ozone increases the "
          "ultraviolet rays reaching the surface, so a recovery works the other way, and "
          "STB-4.B.1 is the mitigation that produces it."),

 dict(q="Which pairing of a compound with the framework's own description is correct?",
      choices=[
        "Hydrofluorocarbons, paired with being one replacement for ozone depleting "
        "chemicals",
        "Hydrofluorocarbons, paired with being an anthropogenic cause of ozone depletion",
        "Chlorofluorocarbons, paired with being a substitute that does not deplete ozone",
        "Chlorofluorocarbons, paired with having no effect on the greenhouse effect",
        "Hydrofluorocarbons, paired with being a natural factor in polar ozone loss"],
      ans=0,
      why="STB-4.B.1 names hydrofluorocarbons as one replacement, STB-4.A.2 names "
          "chlorofluorocarbons as an anthropogenic cause of depletion, and STB-4.C.1 "
          "includes chlorofluorocarbons among the principal greenhouse gases. Each rejected "
          "pairing crosses two of those."),

 dict(q="A policy solves one environmental problem while contributing to another. Which "
        "example from this topic fits that description?",
      choices=[
        "Replacing an ozone depleting chemical with a substitute that is itself a strong "
        "greenhouse gas",
        "Replacing an ozone depleting chemical with a substitute that affects neither the "
        "ozone layer nor the climate",
        "Continuing to use an ozone depleting chemical without any substitute",
        "Measuring the ozone column more often without changing any chemical",
        "Treating sewage before it enters a river"],
      ans=0,
      why="STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are "
          "strong greenhouse gases, which is a response to one problem that contributes to "
          "another."),

 dict(q="Which of the following does the framework NOT state in this topic?",
      choices=[
        "That every hydrofluorocarbon is a strong greenhouse gas",
        "That ozone depletion can be mitigated by replacing ozone depleting chemicals",
        "That a substitute should not deplete the ozone layer",
        "That hydrofluorocarbons are one such replacement",
        "That some hydrofluorocarbons are strong greenhouse gases"],
      ans=0,
      why="STB-4.B.1 says that some hydrofluorocarbons are strong greenhouse gases, not "
          "that all of them are. The four rejected options restate the sentence "
          "accurately."),

 dict(q="Why can a compound that does nothing to the ozone layer still matter for global "
        "change?",
      choices=[
        "A compound can act as a greenhouse gas without depleting ozone, and the framework "
        "warns that some replacements do exactly that",
        "Any compound that spares the ozone layer has no other atmospheric effect",
        "A compound can only affect the climate by first depleting ozone",
        "Greenhouse gases and ozone depleting chemicals are the same set of compounds",
        "The framework treats the two problems as one and the same"],
      ans=0,
      why="STB-4.B.1 warns that some replacements are strong greenhouse gases even though "
          "they do not deplete the ozone layer, so the two properties are separate. "
          "STB-4.C.1 lists the principal greenhouse gases, which include compounds that "
          "have nothing to do with ozone depletion."),

 dict(q="A company replaces its ozone depleting refrigerant and afterward reports that its "
        "contribution to warming has increased. Which framework statement explains that "
        "outcome?",
      choices=[
        "Hydrofluorocarbons are one replacement for ozone depleting chemicals, but some are "
        "strong greenhouse gases",
        "Ozone depletion is caused by natural factors as well as anthropogenic ones",
        "A decrease in stratospheric ozone increases the ultraviolet rays reaching the "
        "surface",
        "Exposure to ultraviolet rays can lead to skin cancer and cataracts",
        "The stratospheric ozone layer is important to the survival of life on Earth"],
      ans=0,
      why="STB-4.B.1 pairs the replacement with the warning that some of the replacements "
          "are strong greenhouse gases, which is precisely the reported outcome. The "
          "rejected statements concern the causes and consequences of the depletion "
          "itself."),

 dict(q="What would a replacement have to achieve in order to address both concerns the "
        "framework raises in this topic?",
      choices=[
        "It would have to leave the ozone layer undepleted and also avoid acting as a "
        "strong greenhouse gas",
        "It would have to deplete less ozone than the chemical it replaces while acting as "
        "a stronger greenhouse gas",
        "It would have to be a greenhouse gas so that it can be tracked",
        "It would have to be identical to the chemical it replaces",
        "It would have to be applied only in the stratosphere"],
      ans=0,
      why="STB-4.B.1 sets the ozone requirement and then names the greenhouse concern that "
          "some replacements raise, so satisfying both means passing both tests."),

 dict(q="An engineer must recommend a refrigerant. Which recommendation follows most "
        "directly from the framework's statement?",
      choices=[
        "A compound that does not deplete the ozone layer and whose warming potential is "
        "low",
        "A compound that depletes the ozone layer only slightly",
        "A compound whose warming potential is high but which is inexpensive",
        "The chlorofluorocarbon already in use, because its behavior is known",
        "Any compound at all, since the framework expresses no preference"],
      ans=0,
      why="STB-4.B.1 requires a substitute that does not deplete the ozone layer and warns "
          "that some replacements are strong greenhouse gases, so a low warming potential "
          "addresses the warning while the first property addresses the strategy."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Ozone depletion is mitigated by replacing the chemicals that cause it with "
        "substitutes that do not deplete the layer, and hydrofluorocarbons are one such "
        "replacement, though some of them are strong greenhouse gases",
        "Ozone depletion is mitigated by using more of the chemicals that cause it",
        "Every substitute for an ozone depleting chemical is free of any other "
        "environmental effect",
        "Hydrofluorocarbons deplete the ozone layer more than the chemicals they replace",
        "The framework describes no way of reducing ozone depletion"],
      ans=0,
      why="The keyed summary is STB-4.B.1 in full, with all three of its parts. Every "
          "rejected summary reverses the strategy, denies the stated caveat, misdescribes "
          "the replacement, or denies that a response exists."),
]
