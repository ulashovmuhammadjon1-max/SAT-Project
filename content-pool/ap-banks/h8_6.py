# AP CHEMISTRY 8.6 Molecular Structure of Acids and Bases
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.6.A: explain the relationship between the strength of an acid or
# base and the structure of the molecule or ion. Suggested skill 6.C, support a claim with
# evidence from representations or models at the particulate level, such as the structure
# of atoms and/or molecules.
#
# Essential knowledge relied on, in the framework's own words -- one statement with five
# lettered sub-points, and every key below is one of them:
#   8.6.A.1  The protons on a molecule that will participate in acid-base reactions, and
#            the relative strength of these protons, can be inferred from the molecular
#            structure.
#            i.   Strong acids (such as HCl, HBr, HI, HClO4, H2SO4, and HNO3) have very
#                 weak conjugate bases that are stabilized by electronegativity, inductive
#                 effects, resonance, or some combination thereof.
#            ii.  Carboxylic acids are one common class of weak acid.
#            iii. Strong bases (such as group I and II hydroxides) have very weak
#                 conjugate acids.
#            iv.  Common weak bases include nitrogenous bases such as ammonia as well as
#                 carboxylate ions.
#            v.   Electronegative elements tend to stabilize the conjugate base relative to
#                 the conjugate acid, and so increase acid strength.
#
# SCOPE. h8_2.py owns pH arithmetic for the strong acids and bases and owns IDENTIFYING a
# solute as strong from the framework's list; h8_3.py owns Ka, Kb and percent ionization.
# So no item below computes a pH, and none is handed an ionization constant and asked to
# convert it. What this module owns is the argument from STRUCTURE to strength: which
# proton is acidic, why a conjugate base is stabilized, and what an electronegative
# substituent does to it. verify_h8_6.py asserts both boundaries.
#
# THE DATA, and why it is presented as a student's measurements rather than as fact. The
# two tables report pKa values for a series of acids differing in one structural feature.
# They are given as readings taken in a described experiment, so no key rests on this bank
# asserting a literature value; what the items ask for is the TREND, which is what EK
# 8.6.A.1.v is about, and verify_h8_6.py recomputes the trend from the table alone and
# asserts it is monotonic in the structural variable.
#
# NOTATION. export_units.py does not typeset Chemistry. Formulas stay plain text (NH3,
# CH3COOH, Ca(OH)2, CH3COO-) and no span is needed anywhere in this module.
TOPIC = ("8.6", "Molecular Structure of Acids and Bases", 8)

_T_CHLORINE = dict(
    headers=["Acid", "Chlorine atoms on the carbon bearing the acidic group",
             "pKa measured by the student"],
    rows=[["J", "0", "4.8"],
          ["L", "1", "2.9"],
          ["M", "2", "1.3"],
          ["N", "3", "0.7"]])

_T_DISTANCE = dict(
    headers=["Acid", "Carbon atoms between the chlorine and the acidic group",
             "pKa measured by the student"],
    rows=[["P", "0", "2.9"],
          ["R", "1", "4.1"],
          ["S", "2", "4.5"]])

_T_SUBSTANCES = dict(
    headers=["Substance", "How the framework describes it"],
    rows=[["NaOH", "a group I hydroxide"],
          ["Ca(OH)2", "a group II hydroxide"],
          ["NH3", "a nitrogenous base"],
          ["CH3COO-", "a carboxylate ion"]])

QUESTIONS = [

 dict(q="According to the framework, what can be inferred from the structure of a molecule "
        "about its behaviour in acid-base reactions?",
      choices=[
        "Which protons will participate, and the relative strength of those protons",
        "The exact value of the ionization constant",
        "The concentration at which the acid will be supplied",
        "The temperature at which the acid will ionize completely",
        "The colour the solution will take on"],
      ans=0,
      why="EK 8.6.A.1 states that the protons on a molecule that will participate in "
          "acid-base reactions, and the relative strength of these protons, can be "
          "inferred from the molecular structure. A relative comparison is what structure "
          "supports; an exact constant comes from measurement under EK 8.3.A.2."),

 dict(q="The framework says the strong acids have very weak conjugate bases. What does it "
        "say stabilizes those conjugate bases?",
      choices=[
        "Electronegativity, inductive effects, resonance, or some combination of these",
        "Hydrogen bonding to the solvent alone",
        "The large size of the anion alone",
        "The high concentration at which strong acids are usually supplied",
        "The absence of any lone pairs on the anion"],
      ans=0,
      why="EK 8.6.A.1.i names electronegativity, inductive effects, resonance, or some "
          "combination thereof as what stabilizes the very weak conjugate bases of the "
          "strong acids. The other influences listed are not the ones the framework "
          "raises here."),

 dict(q="Which common class of weak acid does the framework name?",
      choices=["Carboxylic acids", "Mineral acids", "Hydrogen halides",
               "Metal hydroxides", "Nitrogenous bases"],
      ans=0,
      why="EK 8.6.A.1.ii states that carboxylic acids are one common class of weak acid. "
          "Nitrogenous compounds appear in the framework as weak BASES under EK 8.6.A.1.iv, "
          "and metal hydroxides appear as strong bases under EK 8.6.A.1.iii."),

 dict(q="Which substances does the framework offer as its examples of strong bases?",
      choices=["Group I and group II hydroxides", "Nitrogenous bases such as ammonia",
               "Carboxylate ions", "Carboxylic acids", "The conjugate bases of the strong "
               "acids"],
      ans=0,
      why="EK 8.6.A.1.iii names group I and II hydroxides as its examples of strong bases. "
          "Ammonia and carboxylate ions are given in EK 8.6.A.1.iv as common WEAK bases, "
          "and the conjugate bases of the strong acids are described as very weak by EK "
          "8.6.A.1.i."),

 dict(q="What does the framework say about the conjugate acids of the strong bases?",
      choices=[
        "They are very weak",
        "They are very strong",
        "They are of moderate strength",
        "They do not exist, because a strong base has no conjugate acid",
        "They are the same substances as the strong acids"],
      ans=0,
      why="EK 8.6.A.1.iii states that strong bases, such as group I and II hydroxides, have "
          "very weak conjugate acids. Every acid-base pair has both members, so a strong "
          "base certainly has a conjugate acid; what the framework says is that it is a "
          "feeble one."),

 dict(q="Which two kinds of species does the framework list as common weak bases?",
      choices=[
        "Nitrogenous bases such as ammonia, and carboxylate ions",
        "Group I hydroxides and group II hydroxides",
        "Carboxylic acids and hydrogen halides",
        "The conjugate bases of HCl and HNO3",
        "Nitrogenous bases such as ammonia, and group I hydroxides"],
      ans=0,
      why="EK 8.6.A.1.iv states that common weak bases include nitrogenous bases such as "
          "ammonia as well as carboxylate ions. Group I hydroxides are the framework's "
          "example of a STRONG base under EK 8.6.A.1.iii, so pairing one with ammonia mixes "
          "the two categories."),

 dict(q="What effect does the framework attribute to electronegative elements in an acid "
        "molecule?",
      choices=[
        "They stabilize the conjugate base relative to the conjugate acid, increasing acid "
        "strength",
        "They stabilize the conjugate acid relative to the conjugate base, decreasing acid "
        "strength",
        "They increase the concentration of the acid without changing its strength",
        "They prevent the proton from leaving the molecule at all",
        "They make the substance a base rather than an acid"],
      ans=0,
      why="EK 8.6.A.1.v states that electronegative elements tend to stabilize the "
          "conjugate base relative to the conjugate acid, and so increase acid strength. "
          "The direction matters: stabilizing what is left behind after the proton departs "
          "is what makes the proton easier to lose."),

 dict(q="A student measures the pKa of four acids that differ only in how many chlorine "
        "atoms sit on the carbon bearing the acidic group. What trend do the measurements "
        "show?",
      table=_T_CHLORINE,
      choices=[
        "The pKa falls as more chlorine atoms are added",
        "The pKa rises as more chlorine atoms are added",
        "The pKa is unaffected by the number of chlorine atoms",
        "The pKa falls and then rises again",
        "The pKa changes only when three chlorine atoms are present"],
      ans=0,
      why="Reading the tabulated pKa values against the tabulated chlorine counts shows a "
          "steady fall at every step. EK 8.6.A.1.v gives the reason: the electronegative "
          "chlorine atoms stabilize the conjugate base and so increase acid strength, and a "
          "stronger acid has the lower pKa under EK 8.3.A.2."),

 dict(q="Using the same set of four measured acids, which one is the strongest acid?",
      table=_T_CHLORINE,
      choices=["Acid N", "Acid J", "Acid L", "Acid M",
               "They are equally strong, since they differ only in chlorine"],
      ans=0,
      why="EK 8.3.A.2 makes pKa the negative logarithm of the ionization constant, so the "
          "smallest tabulated pKa belongs to the largest constant and therefore to the "
          "strongest acid. EK 8.6.A.1.v explains why that acid is the one with the most "
          "electronegative atoms next to the acidic group."),

 dict(q="Which statement from the framework does the chlorine series most directly "
        "illustrate?",
      table=_T_CHLORINE,
      choices=[
        "Electronegative elements stabilize the conjugate base and so increase acid strength",
        "Carboxylic acids are one common class of weak acid",
        "Strong bases have very weak conjugate acids",
        "Common weak bases include nitrogenous bases such as ammonia",
        "Strong acids ionize completely in aqueous solution"],
      ans=0,
      why="EK 8.6.A.1.v is the statement about electronegative elements, and the tabulated "
          "series changes exactly one thing -- the number of electronegative atoms -- while "
          "the pKa falls. The other statements are true but are about other structural "
          "families or about a different property."),

 dict(q="A second student measures three acids that carry one chlorine atom at different "
        "distances from the acidic group. What do the measurements show?",
      table=_T_DISTANCE,
      choices=[
        "The acid is stronger when the chlorine sits closer to the acidic group",
        "The acid is stronger when the chlorine sits further from the acidic group",
        "The distance of the chlorine makes no difference to the strength",
        "The acid is strongest when the chlorine is one carbon away",
        "The measurements show no pattern at all"],
      ans=0,
      why="The tabulated pKa rises steadily as the chlorine is moved away, and a higher pKa "
          "is a weaker acid under EK 8.3.A.2. EK 8.6.A.1.i names inductive effects among "
          "the influences that stabilize a conjugate base, and an influence transmitted "
          "through bonds weakens with distance."),

 dict(q="Using the same three measured acids, which acid has the most stabilized conjugate "
        "base?",
      table=_T_DISTANCE,
      choices=["Acid P", "Acid R", "Acid S", "All three are stabilized equally",
               "The one with the largest tabulated pKa"],
      ans=0,
      why="EK 8.6.A.1.v ties a more stabilized conjugate base to a stronger acid, and EK "
          "8.3.A.2 makes the strongest acid the one with the smallest pKa. The tabulated "
          "values identify a single acid, and it is the one whose electronegative atom sits "
          "nearest the acidic group."),

 dict(q="Why is ammonia described by the framework as a base rather than as an acid?",
      choices=[
        "It is a nitrogenous base, the framework's own example of a common weak base",
        "It contains no hydrogen atoms to donate",
        "It is a group I hydroxide",
        "It is the conjugate base of a strong acid",
        "It contains an electronegative element, which always produces a base"],
      ans=0,
      why="EK 8.6.A.1.iv names nitrogenous bases such as ammonia among the common weak "
          "bases. Ammonia does contain hydrogen atoms, and EK 8.6.A.1.v attaches an "
          "electronegative element to increased ACID strength, so neither of those "
          "reasons would work."),

 dict(q="What is the conjugate base formed when a carboxylic acid donates its proton?",
      choices=["A carboxylate ion", "A nitrogenous base", "A hydroxide ion",
               "A hydronium ion", "Another carboxylic acid"],
      ans=0,
      why="EK 8.6.A.1.ii makes carboxylic acids a common class of weak acid and EK "
          "8.6.A.1.iv names carboxylate ions among the common weak bases, which is the "
          "pairing of an acid with what is left after the proton leaves. Hydroxide belongs "
          "to the strong bases of EK 8.6.A.1.iii."),

 dict(q="How does resonance stabilize the conjugate base of an acid?",
      choices=[
        "The negative charge is spread over more than one atom rather than held on one",
        "The negative charge is concentrated onto the single most electronegative atom",
        "The conjugate base gains an additional proton",
        "The conjugate base is converted into a neutral molecule",
        "The conjugate base is prevented from interacting with the solvent"],
      ans=0,
      why="EK 8.6.A.1.i names resonance among the influences that stabilize a very weak "
          "conjugate base, and resonance is the delocalization of charge across more than "
          "one atom. Concentrating charge on one atom is the opposite of what makes the "
          "anion more stable."),

 dict(q="Two acids differ only in that one carries a fluorine atom next to the acidic "
        "group and the other carries a hydrogen atom there. Which is the stronger acid, and "
        "why?",
      choices=[
        "The fluorinated acid, because the electronegative fluorine stabilizes the "
        "conjugate base",
        "The fluorinated acid, because fluorine adds a second acidic proton",
        "The other acid, because fluorine holds the proton more tightly",
        "The other acid, because fluorine destabilizes the conjugate base",
        "Neither, because a single substituent cannot change acid strength"],
      ans=0,
      why="EK 8.6.A.1.v states that electronegative elements tend to stabilize the "
          "conjugate base relative to the conjugate acid and so increase acid strength. "
          "Fluorine is not itself an acidic proton, and the framework gives the effect in "
          "the direction of greater, not lesser, strength."),

 dict(q="In the molecule CH3COOH, which hydrogen atom participates in acid-base reactions?",
      choices=[
        "The one bonded to oxygen",
        "One of the three bonded to the carbon at the left end",
        "All four, since they are all hydrogen atoms",
        "None, since carbon compounds are not acids",
        "Whichever one is nearest the surface of the solution"],
      ans=0,
      why="EK 8.6.A.1 says the protons that will participate can be inferred from the "
          "structure, and EK 8.6.A.1.ii and iv pair a carboxylic acid with the carboxylate "
          "ion as its conjugate base, which is what remains after the hydrogen on oxygen "
          "departs. The hydrogens on carbon are not lost in these reactions."),

 dict(q="Which comparison between an acid and its conjugate base does the framework make "
        "for the strong acids?",
      choices=[
        "A strong acid has a very weak conjugate base",
        "A strong acid has a very strong conjugate base",
        "A strong acid has a conjugate base of the same strength",
        "A strong acid has no conjugate base",
        "A strong acid has a conjugate base that is itself a strong acid"],
      ans=0,
      why="EK 8.6.A.1.i states that the strong acids have very weak conjugate bases, "
          "stabilized by electronegativity, inductive effects, resonance, or some "
          "combination. A stabilized anion has little tendency to take a proton back, "
          "which is what being a weak base means."),

 dict(q="The table describes four substances in the framework's own terms. Which of them "
        "does the framework classify as strong bases?",
      table=_T_SUBSTANCES,
      choices=[
        "The group I hydroxide and the group II hydroxide",
        "The nitrogenous base and the carboxylate ion",
        "The group I hydroxide and the nitrogenous base",
        "All four of them",
        "Only the group II hydroxide"],
      ans=0,
      why="EK 8.6.A.1.iii names group I and II hydroxides as strong bases, and EK "
          "8.6.A.1.iv names nitrogenous bases and carboxylate ions as common WEAK bases. "
          "The table's descriptions place exactly two of the four substances in the first "
          "category."),

 dict(q="Using the same four substances, which are the weak bases?",
      table=_T_SUBSTANCES,
      choices=[
        "The nitrogenous base and the carboxylate ion",
        "The group I hydroxide and the group II hydroxide",
        "The carboxylate ion and the group II hydroxide",
        "Only the nitrogenous base",
        "None of them, since all four contain oxygen or nitrogen"],
      ans=0,
      why="EK 8.6.A.1.iv lists nitrogenous bases such as ammonia and carboxylate ions among "
          "the common weak bases, and the tabulated descriptions match exactly two of the "
          "four substances to those categories. Containing an electronegative element does "
          "not by itself make a substance a base."),

 dict(q="A chemist wants to make a carboxylic acid stronger by changing its structure. "
        "Which change does the framework support?",
      choices=[
        "Attaching electronegative atoms near the acidic group",
        "Attaching electronegative atoms as far from the acidic group as possible",
        "Removing the oxygen atoms from the acidic group",
        "Adding a group I metal to the molecule",
        "Increasing the concentration at which the acid is used"],
      ans=0,
      why="EK 8.6.A.1.v says electronegative elements stabilize the conjugate base and so "
          "increase acid strength, and EK 8.6.A.1.i names inductive effects, which are "
          "transmitted through bonds and therefore weaken with distance. Concentration is "
          "not strength, a distinction EK 8.3.A.1 rests on."),

 dict(q="Why does the framework describe the conjugate base of a strong acid as very weak?",
      choices=[
        "Because it is stabilized, and a stabilized anion has little tendency to take a "
        "proton back",
        "Because it is present in only a small concentration",
        "Because it carries no charge",
        "Because it is a solid and cannot react",
        "Because it is destabilized by the electronegative atoms it contains"],
      ans=0,
      why="EK 8.6.A.1.i pairs the very weak conjugate bases of the strong acids with the "
          "stabilization supplied by electronegativity, inductive effects and resonance. "
          "The conjugate base of a strong acid is in fact present in a LARGE concentration, "
          "since the acid ionizes completely, so its concentration is not the reason."),

 dict(q="Which structural feature would you look for to decide whether a molecule is "
        "likely to be a weak acid rather than a weak base?",
      choices=[
        "An acidic group of the kind carboxylic acids carry, rather than a basic nitrogen",
        "A nitrogen atom with a lone pair, rather than an acidic group",
        "The total number of atoms in the molecule",
        "Whether the molecule contains any oxygen at all",
        "Whether the molecule is larger than a water molecule"],
      ans=0,
      why="EK 8.6.A.1 says the structure identifies which protons take part, and EK "
          "8.6.A.1.ii and iv sort the two families: carboxylic acids are a common class of "
          "weak acid, while nitrogenous compounds such as ammonia are common weak bases. "
          "Size and the mere presence of oxygen sort nothing."),

 dict(q="An acid with a single acidic proton is compared with one whose acidic proton sits "
        "next to three electronegative atoms. Which conjugate base is more stable, and what "
        "follows?",
      choices=[
        "The second, so the second acid is the stronger",
        "The second, so the second acid is the weaker",
        "The first, so the first acid is the stronger",
        "The first, so the second acid is the stronger",
        "Neither, since stability of a conjugate base is unrelated to acid strength"],
      ans=0,
      why="EK 8.6.A.1.v ties stabilization of the conjugate base by electronegative "
          "elements directly to increased acid strength, so the more stabilized anion "
          "belongs to the stronger acid. Both halves of the answer have to point the same "
          "way for it to match the framework."),

 dict(q="Why can the relative strength of two protons in the same molecule be discussed at "
        "all, according to the framework?",
      choices=[
        "Because the molecular structure around each proton differs, and structure "
        "determines relative strength",
        "Because every proton in a molecule has the same strength",
        "Because the strength of a proton depends only on the concentration of the solution",
        "Because a molecule can hold only one acidic proton",
        "Because the strength of a proton is fixed by the temperature"],
      ans=0,
      why="EK 8.6.A.1 states that the protons that will participate AND the relative "
          "strength of these protons can be inferred from the molecular structure, which "
          "presupposes that different protons in one molecule can differ. Concentration and "
          "temperature are not structural features."),

 dict(q="Which of the following is NOT among the influences the framework names as "
        "stabilizing the conjugate base of a strong acid?",
      choices=[
        "The molar mass of the anion",
        "Electronegativity",
        "Inductive effects",
        "Resonance",
        "A combination of electronegativity and resonance"],
      ans=0,
      why="EK 8.6.A.1.i lists electronegativity, inductive effects, resonance, or some "
          "combination thereof, and molar mass is not among them. A heavy anion is not "
          "thereby a stable one, and the framework offers no mass-based rule."),

 dict(q="Sodium hydroxide and ammonia are both bases. What does the framework say "
        "distinguishes them?",
      choices=[
        "The hydroxide is a strong base while ammonia is a common weak base",
        "Ammonia is a strong base while the hydroxide is a common weak base",
        "Both are strong bases, since both accept protons",
        "Both are weak bases, since neither is a hydroxide of group II",
        "Neither is a base, since both contain hydrogen"],
      ans=0,
      why="EK 8.6.A.1.iii names group I and II hydroxides as strong bases and EK 8.6.A.1.iv "
          "names nitrogenous bases such as ammonia among the common weak bases, so the two "
          "substances fall on opposite sides of the framework's own division."),

 dict(q="Calcium hydroxide is a hydroxide of a group II metal. How does the framework "
        "classify it, and what follows about its conjugate acid?",
      choices=[
        "A strong base, whose conjugate acid is very weak",
        "A strong base, whose conjugate acid is very strong",
        "A weak base, whose conjugate acid is very strong",
        "A weak base, whose conjugate acid is also weak",
        "Neither a strong nor a weak base, since it contains two hydroxide groups"],
      ans=0,
      why="EK 8.6.A.1.iii names group I and II hydroxides as its examples of strong bases "
          "and states in the same sentence that strong bases have very weak conjugate "
          "acids. The number of hydroxide groups affects the stoichiometry, not the "
          "classification."),

 dict(q="Using the tabulated chlorine series, what would you predict for a fifth acid in "
        "the same family carrying four electronegative atoms next to the acidic group?",
      table=_T_CHLORINE,
      choices=[
        "A pKa below the smallest tabulated value, since it would be a stronger acid still",
        "A pKa above the largest tabulated value, since it would be a weaker acid",
        "A pKa equal to the average of the tabulated values",
        "The same pKa as the acid with three such atoms",
        "A pKa that cannot be predicted, since the tabulated values show no pattern"],
      ans=0,
      why="The tabulated pKa falls at every step as electronegative atoms are added, which "
          "EK 8.6.A.1.v explains as increasing stabilization of the conjugate base and "
          "therefore increasing acid strength. Continuing the trend means continuing "
          "downward past the smallest tabulated value."),

 dict(q="Summarise the relationship the framework draws between conjugate base stability "
        "and acid strength.",
      choices=[
        "The more stabilized the conjugate base, the stronger the acid",
        "The more stabilized the conjugate base, the weaker the acid",
        "The stability of the conjugate base has no bearing on acid strength",
        "The stability of the conjugate base fixes the concentration of the acid",
        "The more stabilized the conjugate base, the more slowly the acid ionizes"],
      ans=0,
      why="EK 8.6.A.1.v states that electronegative elements stabilize the conjugate base "
          "relative to the conjugate acid and so increase acid strength, and EK 8.6.A.1.i "
          "makes the same connection for the strong acids by way of their very weak "
          "conjugate bases. Nothing in the framework here concerns rate or concentration."),

]
