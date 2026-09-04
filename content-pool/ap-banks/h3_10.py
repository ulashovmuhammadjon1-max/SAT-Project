r"""AP CHEMISTRY 3.10 Solubility.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.10.A: explain the relationship between the solubility of
ionic and molecular compounds in aqueous and nonaqueous solvents, and the
intermolecular interactions between particles.
Suggested skill 4.D, explain the degree to which a model or representation
describes the connection between particulate-level properties and macroscopic
properties.

Essential knowledge relied on, in the framework's own words -- this topic has
exactly one statement:

  3.10.A.1  Substances with similar intermolecular interactions tend to be
            miscible or soluble in one another.

WHAT THE SENTENCE SAYS AND WHAT IT WITHHOLDS. It names SIMILARITY, not strength:
two substances whose interactions are both strong but unlike each other are not
what it predicts will mix. And it says TEND TO, not will. Both readings are
easy to lose, so both are guarded: verify_h3_10.py refuses any key attributing
solubility to the absolute strength of a substance's own intermolecular forces,
and any key promising that similar interactions always dissolve. Each
misconception is offered as a distractor so a student meets it and rejects it,
and each check asserts it is offered, so neither can pass over an empty set.

THE IMPORTED STATEMENTS, all cited where used. The learning objective reaches
past this topic's one sentence to ionic and molecular compounds in aqueous and
nonaqueous solvents, so the items that go there name what they borrow:

  3.1.A.1  London dispersion forces arise from Coulombic interactions between
           temporary, fluctuating dipoles -- the interaction a molecule of
           carbon and hydrogen alone is left with.
  3.1.A.2  interactions between polar molecules are typically greater than those
           between nonpolar molecules of comparable size, and ion-dipole forces
           of attraction are present between ions and polar molecules and tend
           to be stronger than dipole-dipole forces.
  3.1.A.4  hydrogen bonding exists where hydrogen covalently bonded to N, O or F
           is attracted to the negative end of a dipole formed by N, O or F.

Nothing here uses a solubility-rules table, a solubility product, or any
numerical solubility relationship: those belong to units 4 and 7.

NO FIGURES. Every set of solubility data is carried as a table.

ARITHMETIC. The tabulated solubilities are recomputed and compared in
verify_h3_10.py, and the interaction-matching tables are recomputed by matching
the tabulated interaction of each substance against the solvent named in the
stem, rather than by trusting a remembered answer.

NOTATION. Plain prose; no math spans are needed in this module.
"""
TOPIC = ("3.10", "Solubility", 3)

_T_SOLUTES = dict(
    headers=["Solute", "Strongest intermolecular interaction its molecules can form"],
    rows=[["Solute 1", "London dispersion forces only"],
          ["Solute 2", "Hydrogen bonding"],
          ["Solute 3", "Dipole-dipole interactions"]])

_T_PAIRS = dict(
    headers=["Pair", "Interaction available to the first substance",
             "Interaction available to the second substance"],
    rows=[["Pair 1", "Hydrogen bonding", "Hydrogen bonding"],
          ["Pair 2", "London dispersion forces only", "Hydrogen bonding"],
          ["Pair 3", "Dipole-dipole interactions", "Dipole-dipole interactions"],
          ["Pair 4", "London dispersion forces only", "London dispersion forces only"]])

# Water is polar and forms hydrogen bonds; hexane is nonpolar and its molecules
# have only London dispersion forces available. Each stem using this table says
# so, so nothing rests on remembering it.
_T_SOLB = dict(
    headers=["Solute", "Solubility in water (g per 100 g of water)",
             "Solubility in hexane (g per 100 g of hexane)"],
    rows=[["Solute P", "36.0", "0.01"],
          ["Solute Q", "0.02", "28.0"],
          ["Solute R", "15.0", "14.0"]])

QUESTIONS = [

 dict(q="What does the framework say about substances with similar intermolecular "
        "interactions?",
      choices=[
        "They tend to be miscible or soluble in one another",
        "They tend to be insoluble in one another",
        "They react with one another rather than dissolving",
        "They are always identical substances",
        "The framework makes no claim about them"],
      ans=0,
      why="EK 3.10.A.1 is that sentence in full: substances with similar intermolecular "
          "interactions tend to be miscible or soluble in one another. It is a claim about "
          "mixing rather than about reacting."),

 dict(q="The framework says such substances TEND TO be miscible or soluble. What does that "
        "wording establish?",
      choices=[
        "A general expectation rather than a guarantee for every pair",
        "That every pair with similar interactions dissolves completely",
        "That no pair with similar interactions ever dissolves",
        "That solubility depends only on temperature",
        "That the claim applies only to pairs of liquids"],
      ans=0,
      why="EK 3.10.A.1's verb is tend to, which asserts a pattern without promising it holds "
          "in every case. Reading it as a guarantee makes a stronger claim than the sentence "
          "supports."),

 dict(q="According to the framework, what makes two substances likely to dissolve in one "
        "another?",
      choices=[
        "Their intermolecular interactions being similar to each other",
        "Their intermolecular forces both being strong, whether or not they are alike",
        "Their molar masses being close to each other",
        "Their melting points being close to each other",
        "Their being made of the same elements"],
      ans=0,
      why="EK 3.10.A.1 names SIMILAR intermolecular interactions. Two substances whose "
          "interactions are both strong but of different kinds are not what the sentence "
          "predicts will mix, and it says nothing at all about masses or melting points."),

 dict(q="A nonpolar solute whose molecules have only London dispersion forces available is "
        "added to a nonpolar solvent whose molecules also have only London dispersion forces "
        "available. What does the framework expect?",
      choices=[
        "They tend to be soluble in one another, because their interactions are similar",
        "They tend to be insoluble in one another, because London dispersion forces are weak",
        "They tend to be insoluble in one another, because neither is polar",
        "They react rather than dissolving",
        "Nothing can be expected without their molar masses"],
      ans=0,
      why="EK 3.1.A.1 leaves both substances with London dispersion forces as their "
          "interaction, so the two are alike, and EK 3.10.A.1 makes similarity the ground of "
          "the expectation. The absolute weakness of the forces is not what the sentence "
          "turns on."),

 dict(q="A polar solute is added to a polar solvent. What does the framework expect, and "
        "why?",
      choices=[
        "They tend to dissolve in one another, because both rely on interactions between "
        "polar molecules",
        "They tend not to dissolve in one another, because two polar substances repel each "
        "other",
        "They tend to dissolve in one another, because polar substances dissolve everything",
        "They tend not to dissolve in one another, because polar molecules interact only "
        "with ions",
        "Nothing can be expected, because polarity is not an intermolecular interaction"],
      ans=0,
      why="EK 3.1.A.2 makes dipole-dipole interactions the ones present between polar "
          "molecules and notes they are typically greater than those between nonpolar "
          "molecules of comparable size. Both substances therefore bring the same kind of "
          "interaction, which is the similarity EK 3.10.A.1 relies on."),

 dict(q="A nonpolar solute is added to a polar solvent. What does the framework expect, and "
        "why?",
      choices=[
        "Poor solubility, because the two substances' intermolecular interactions are not "
        "similar",
        "Poor solubility, because the solvent's intermolecular forces are too strong to allow "
        "any solute in",
        "High solubility, because the two substances' intermolecular interactions are not "
        "similar",
        "High solubility, because a polar solvent dissolves every solute",
        "Nothing can be expected, since only ionic solutes have predictable solubility"],
      ans=0,
      why="EK 3.1.A.1 leaves the nonpolar solute with London dispersion forces while "
          "EK 3.1.A.2 gives the polar solvent dipole-dipole interactions as well, so the two "
          "are unlike. EK 3.10.A.1 attaches its expectation of mixing to similarity, so "
          "unlike interactions carry the opposite expectation."),

 dict(q="A polar solute is added to a nonpolar solvent. What does the framework expect?",
      choices=[
        "Poor solubility, since the two substances' interactions are unlike each other",
        "High solubility, since the solute is polar and polarity aids dissolving",
        "High solubility, since the solvent has weak forces and is easy to enter",
        "Poor solubility, since the solute's own forces are strong",
        "A chemical reaction rather than dissolving"],
      ans=0,
      why="EK 3.10.A.1 turns on the similarity of the two substances' interactions, and here "
          "one relies on dipole-dipole interactions under EK 3.1.A.2 while the other has only "
          "London dispersion forces under EK 3.1.A.1. The absolute strength of either "
          "substance's own forces is not what the sentence names."),

 dict(q="An ionic solid is added to water. Which interaction does the framework make "
        "available between the solute's ions and the solvent's molecules?",
      choices=[
        "Ion-dipole forces of attraction",
        "Hydrogen bonding between the ions and the water molecules",
        "London dispersion forces only",
        "Covalent bonds between the ions and the water molecules",
        "No interaction at all, since ions and molecules cannot interact"],
      ans=0,
      why="EK 3.1.A.2 states that ion-dipole forces of attraction are present between ions "
          "and polar molecules and tend to be stronger than dipole-dipole forces. Water's "
          "molecules are polar, so that interaction is the one available, and EK 3.10.A.1 "
          "makes the availability of comparable interactions the ground of solubility."),

 dict(q="An ionic solid is added to a nonpolar solvent whose molecules have no dipole. What "
        "does the framework expect?",
      choices=[
        "Poor solubility, since no ion-dipole interaction is available",
        "High solubility, since ions dissolve in every solvent",
        "High solubility, since London dispersion forces act between all particles",
        "Poor solubility, since the ionic solid's own forces are strong",
        "A chemical reaction between the ions and the solvent"],
      ans=0,
      why="EK 3.1.A.2 places ion-dipole forces between ions and POLAR molecules, so a solvent "
          "with no dipole offers nothing comparable to the interactions holding the ionic "
          "solid together, and EK 3.10.A.1's expectation of mixing does not apply. What "
          "matters is the mismatch rather than the strength of the solid's own forces."),

 dict(q="A molecular solute whose molecules carry hydrogen covalently bonded to oxygen is "
        "added to water. What does the framework expect, and why?",
      choices=[
        "Good solubility, because both substances can take part in hydrogen bonding",
        "Good solubility, because the solute's molecules are larger than the water molecules",
        "Poor solubility, because hydrogen bonding holds each substance to itself",
        "Poor solubility, because water interacts only with ions",
        "A chemical reaction, because hydrogen bonds are covalent bonds"],
      ans=0,
      why="EK 3.1.A.4 makes hydrogen bonding the interaction available where hydrogen "
          "covalently bonded to nitrogen, oxygen or fluorine is attracted to the negative end "
          "of a dipole formed by one of those atoms, which describes both substances here. "
          "EK 3.10.A.1 then expects substances with such similar interactions to dissolve in "
          "one another."),

 dict(q="What connection does EK 3.10.A.1 draw, in the terms suggested skill 4.D uses?",
      choices=[
        "A particulate-level property, the intermolecular interactions, to a macroscopic "
        "property, solubility",
        "A macroscopic property, temperature, to another macroscopic property, solubility",
        "A particulate-level property, the number of protons, to a macroscopic property, "
        "colour",
        "Two macroscopic properties, density and mass",
        "Two particulate-level properties, bond length and bond angle"],
      ans=0,
      why="EK 3.10.A.1 predicts whether two substances mix, which is something observed of "
          "bulk samples, from the interactions between their particles. That is exactly the "
          "particulate-to-macroscopic connection suggested skill 4.D asks a student to "
          "explain."),

 dict(q="The tabulated solutes are each added to water, whose molecules form hydrogen bonds. "
        "Which is expected to be the most soluble?",
      table=_T_SOLUTES,
      choices=[
        "Solute 2",
        "Solute 1",
        "Solute 3",
        "All three equally",
        "It cannot be decided from intermolecular interactions"],
      ans=0,
      why="EK 3.10.A.1 expects substances with similar intermolecular interactions to be "
          "soluble in one another, and EK 3.1.A.4 names hydrogen bonding as a distinct kind "
          "of interaction. The tabulated solute whose own strongest interaction is the same "
          "kind as the solvent's is the one the sentence favours."),

 dict(q="The tabulated solutes are each added instead to a nonpolar solvent whose molecules "
        "have only London dispersion forces available. Which is expected to be the most "
        "soluble?",
      table=_T_SOLUTES,
      choices=[
        "Solute 1",
        "Solute 2",
        "Solute 3",
        "All three equally",
        "It cannot be decided from intermolecular interactions"],
      ans=0,
      why="EK 3.10.A.1's expectation follows similarity, and EK 3.1.A.1 makes London "
          "dispersion forces the interaction left to a molecule with no dipole. The tabulated "
          "solute matching the solvent on that count is the one the sentence favours."),

 dict(q="For which tabulated pair of substances does the framework NOT expect the two to be "
        "miscible?",
      table=_T_PAIRS,
      choices=[
        "Pair 2",
        "Pair 1",
        "Pair 3",
        "Pair 4",
        "The framework expects none of them to be miscible"],
      ans=0,
      why="EK 3.10.A.1 attaches its expectation to substances whose intermolecular "
          "interactions are SIMILAR, so the pair whose two entries name different kinds of "
          "interaction is the one the sentence does not cover."),

 dict(q="For how many of the tabulated pairs does the framework expect the two substances to "
        "be miscible?",
      table=_T_PAIRS,
      choices=[
        "Exactly three",
        "Exactly one",
        "Exactly two",
        "All four of them",
        "None of them"],
      ans=0,
      why="EK 3.10.A.1's expectation applies to each tabulated pair whose two entries name "
          "the same kind of intermolecular interaction, and the count is taken across the "
          "whole table."),

 dict(q="Water is polar and forms hydrogen bonds; hexane is nonpolar and its molecules have "
        "only London dispersion forces. Which tabulated solute has intermolecular "
        "interactions most like water's?",
      table=_T_SOLB,
      choices=[
        "Solute P",
        "Solute Q",
        "Solute R",
        "All three are equally like water",
        "The data cannot support such an inference"],
      ans=0,
      why="EK 3.10.A.1 makes similarity of intermolecular interactions the reason substances "
          "dissolve in one another, so the tabulated solute that dissolves far better in the "
          "hydrogen-bonding solvent than in the nonpolar one is the one whose own "
          "interactions most resemble the former's."),

 dict(q="Which tabulated solute dissolves to a comparable extent in both solvents?",
      table=_T_SOLB,
      choices=[
        "Solute R",
        "Solute P",
        "Solute Q",
        "All three do",
        "None of them does"],
      ans=0,
      why="The two tabulated solubilities are compared for each solute in turn, and one "
          "solute's two figures are close to each other while the other two differ by orders "
          "of magnitude. EK 3.10.A.1 makes a solute that resembles both solvents an "
          "unremarkable case rather than an impossible one, since its verb is tend to."),

 dict(q="Which tabulated solute is far more soluble in hexane, the nonpolar solvent, than in "
        "water?",
      table=_T_SOLB,
      choices=[
        "Solute Q",
        "Solute P",
        "Solute R",
        "All three are",
        "None of them is"],
      ans=0,
      why="The two tabulated figures are compared for each solute, and EK 3.10.A.1 lets the "
          "solvent a solute prefers indicate which set of intermolecular interactions its own "
          "resemble; here that is the nonpolar solvent's London dispersion forces, named in "
          "EK 3.1.A.1."),

 dict(q="Which kinds of compound and which kinds of solvent does this topic's learning "
        "objective cover?",
      choices=[
        "Ionic and molecular compounds, in aqueous and nonaqueous solvents",
        "Ionic compounds only, in aqueous solvents only",
        "Molecular compounds only, in nonaqueous solvents only",
        "Ionic compounds only, in any solvent",
        "Molecular compounds only, in water only"],
      ans=0,
      why="Learning objective 3.10.A names the solubility of ionic AND molecular compounds in "
          "aqueous AND nonaqueous solvents, and ties all of it to the intermolecular "
          "interactions between particles. Nothing in it restricts the claim to water."),

 dict(q="Two substances have similar intermolecular interactions but do not in fact mix. Does "
        "that contradict the framework?",
      choices=[
        "No, because the framework says such substances TEND TO be miscible or soluble",
        "Yes, because the framework says such substances always dissolve in one another",
        "Yes, because the framework allows no exceptions of any kind",
        "No, because the framework says nothing about substances with similar interactions",
        "No, because solubility is unrelated to intermolecular interactions"],
      ans=0,
      why="EK 3.10.A.1's verb is tend to, which states a general pattern rather than an "
          "exceptionless rule, so a single pair that does not follow it leaves the sentence "
          "standing. The framework does make the claim, so denying that it says anything is "
          "equally wrong."),

 dict(q="Two substances both have unusually strong intermolecular forces, but of different "
        "kinds. What does the framework expect?",
      choices=[
        "They are not expected to mix, since their interactions are not similar",
        "They are expected to mix, since both sets of forces are strong",
        "They are expected to mix, since strong forces always attract",
        "They are expected to react rather than mix",
        "Nothing can be expected, since the framework treats only weak forces"],
      ans=0,
      why="EK 3.10.A.1 names similarity of intermolecular interactions and not their absolute "
          "strength. Two substances that are each held together tightly, but in different "
          "ways, do not meet the condition the sentence states."),

 dict(q="A student says a substance dissolves in a given solvent because its own "
        "intermolecular forces are strong. Which correction matches the framework?",
      choices=[
        "What matters is whether its interactions are similar to the solvent's, not how "
        "strong they are on their own",
        "What matters is how strong its interactions are, and the student is right",
        "What matters is the molar mass of the solute rather than any interaction",
        "What matters is the temperature of the solvent rather than any interaction",
        "What matters is whether the two substances react, not whether they interact"],
      ans=0,
      why="EK 3.10.A.1 states the condition as similar intermolecular interactions between "
          "the two substances. Strength on its own says nothing about whether the solvent can "
          "offer the solute interactions comparable to the ones it already has."),

 dict(q="How does the framework rank ion-dipole forces against dipole-dipole forces?",
      choices=[
        "Ion-dipole forces tend to be the stronger of the two",
        "Dipole-dipole forces tend to be the stronger of the two",
        "The two are always exactly equal in strength",
        "Ion-dipole forces exist only in the absence of dipole-dipole forces",
        "The framework does not compare them"],
      ans=0,
      why="EK 3.1.A.2 says ion-dipole forces of attraction are present between ions and polar "
          "molecules and that these tend to be stronger than dipole-dipole forces. That "
          "comparison is what makes a polar solvent effective at surrounding ions."),

 dict(q="Two liquids can each take part in hydrogen bonding. What does the framework expect "
        "of a mixture of them?",
      choices=[
        "They tend to be miscible, because their intermolecular interactions are similar",
        "They tend to be immiscible, because hydrogen bonds hold each liquid to itself",
        "They tend to be immiscible, because hydrogen bonding is too strong to share",
        "They tend to react to form a new compound",
        "Nothing can be expected without their densities"],
      ans=0,
      why="EK 3.1.A.4 makes hydrogen bonding a single named kind of interaction, so two "
          "liquids that both take part in it bring similar interactions to the mixture, which "
          "is the condition EK 3.10.A.1 attaches its expectation of miscibility to."),

 dict(q="A hydrocarbon whose molecules contain only carbon and hydrogen is shaken with water. "
        "What does the framework expect?",
      choices=[
        "They tend not to mix, since one has only London dispersion forces while the other "
        "hydrogen bonds",
        "They tend to mix, since every liquid mixes with water eventually",
        "They tend to mix, since London dispersion forces act between all molecules",
        "They tend not to mix, since the hydrocarbon's forces are stronger than water's",
        "They react, since hydrogen is present in both"],
      ans=0,
      why="EK 3.1.A.4 requires hydrogen bonded to nitrogen, oxygen or fluorine for hydrogen "
          "bonding, which a molecule of carbon and hydrogen alone cannot offer, leaving it "
          "the London dispersion forces of EK 3.1.A.1. The two substances' interactions are "
          "therefore unlike, which is the reverse of EK 3.10.A.1's condition."),

 dict(q="To what degree does EK 3.10.A.1 explain solubility, in the terms suggested skill 4.D "
        "asks about?",
      choices=[
        "It connects a particulate-level property to a macroscopic one, as a tendency rather "
        "than as a rule",
        "It gives an exact numerical solubility for any pair of substances",
        "It explains solubility completely, with no exceptions",
        "It describes only macroscopic observations and says nothing about particles",
        "It applies only to substances that do not dissolve"],
      ans=0,
      why="EK 3.10.A.1 reasons from the interactions between particles to whether bulk "
          "samples mix, which is the particulate-to-macroscopic connection, and its verb is "
          "tend to, which is the limit on how far the model reaches. Judging both at once is "
          "what suggested skill 4.D asks for."),

 dict(q="Which of these does EK 3.10.A.1 NOT name as bearing on whether two substances "
        "dissolve in one another?",
      choices=[
        "The molar mass of each substance",
        "The intermolecular interactions of each substance",
        "The similarity of those interactions between the two substances",
        "Whether the two substances are miscible",
        "Whether one substance is soluble in the other"],
      ans=0,
      why="EK 3.10.A.1 mentions intermolecular interactions, their similarity, and the "
          "miscibility or solubility that follows, and nothing else. Molar mass belongs to "
          "other statements in the course and does not appear in this one."),

 dict(q="Two substances have very different intermolecular interactions. What does the "
        "framework lead a student to expect?",
      choices=[
        "They tend not to be soluble in one another",
        "They tend to be soluble in one another",
        "They tend to react with one another",
        "One will always dissolve in the other but not the reverse",
        "The framework supports no expectation either way"],
      ans=0,
      why="EK 3.10.A.1 attaches the expectation of mixing to substances whose intermolecular "
          "interactions are similar, so a pair that fails that condition carries the opposite "
          "expectation. The sentence is about dissolving rather than reacting."),

 dict(q="An ionic compound is added to a polar solvent that is not water. What does the "
        "framework allow?",
      choices=[
        "It may still dissolve, since a polar solvent can offer ion-dipole interactions to "
        "the ions",
        "It cannot dissolve, since only water dissolves ionic compounds",
        "It cannot dissolve, since ion-dipole forces exist only in aqueous solution",
        "It dissolves only if the solvent contains oxygen",
        "It dissolves only if the solvent is nonpolar"],
      ans=0,
      why="EK 3.1.A.2 places ion-dipole forces of attraction between ions and POLAR MOLECULES "
          "without restricting them to water, and learning objective 3.10.A explicitly covers "
          "nonaqueous solvents. EK 3.10.A.1 then makes the availability of comparable "
          "interactions the ground of the expectation."),

 dict(q="Which statement expresses EK 3.10.A.1 completely?",
      choices=[
        "Substances with similar intermolecular interactions tend to be miscible or soluble "
        "in one another",
        "Substances with strong intermolecular interactions are always soluble in one another",
        "Substances with different intermolecular interactions are always soluble in one "
        "another",
        "Substances of similar molar mass tend to be soluble in one another",
        "Substances tend to dissolve in one another only when they react"],
      ans=0,
      why="EK 3.10.A.1 is that sentence, and every part of it carries weight: similarity "
          "rather than strength, a tendency rather than a certainty, and mixing rather than "
          "reacting. Each rejected option changes one of those three."),
]
