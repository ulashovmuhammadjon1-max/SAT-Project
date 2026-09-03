# AP CHEMISTRY 4.9 Oxidation-Reduction (Redox) Reactions
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.9.A: represent a balanced redox reaction equation using
# half-reactions. Suggested skill 5.E, determine a balanced chemical equation for
# a given chemical phenomenon.
#
# Essential knowledge relied on, in the framework's own words:
#   4.9.A.1  Balanced chemical equations for redox reactions can be constructed
#            from half-reactions.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, THIRTY QUESTIONS. 4.9.A.1 is a single
# sentence and the learning objective is a SKILL: construct the balanced
# equation. So this module is the skill, exercised on different pairs of
# half-reactions, plus the three facts the construction rests on and nothing
# else -- electrons appear on the side that says whether the half-reaction is
# oxidation or reduction, a half-reaction is balanced only when both atoms and
# charge balance, and the two half-reactions must be scaled until the electrons
# lost equal the electrons gained so that none survives into the overall
# equation.
#
# EVERY HALF-REACTION A STUDENT IS ASKED TO USE IS PRINTED IN THE STEM. No item
# asks a student to recall a standard half-reaction, an electrode potential or a
# solubility fact. Where an item works in acidic solution the H+ and H2O are
# already in the printed half-reaction, so the item is the COMBINATION step that
# 4.9.A.1 names, not an unstated balancing convention.
#
# THE EXCLUSION IN 4.7 IS COURSE-WIDE AND IS OBEYED HERE TOO: the terms
# "reducing agent" and "oxidizing agent" appear nowhere in this module, and
# verify_h4_9.py fails if an edit reintroduces either.
#
# Topic 4.7 classifies reactions and assigns oxidation numbers; this module
# constructs balanced equations from half-reactions, which is what LO 4.9.A asks.
#
# NOTATION. Chemistry is not typeset; equations and charges stay plain text.
TOPIC = ("4.9", "Oxidation-Reduction (Redox) Reactions", 4)

_T_HALF = dict(
    headers=["Half-reaction", "Electrons appearing in it",
             "Side on which the electrons appear"],
    rows=[["Zn gives Zn2+ + 2 e-", "2", "Product side"],
          ["Cu2+ + 2 e- gives Cu", "2", "Reactant side"],
          ["Al gives Al3+ + 3 e-", "3", "Product side"],
          ["Ag+ + e- gives Ag", "1", "Reactant side"]])

_T_CHARGE = dict(
    headers=["Candidate half-reaction", "Total charge on the reactant side",
             "Total charge on the product side"],
    rows=[["I: Fe3+ + e- gives Fe2+", "+2", "+2"],
          ["II: Cu2+ + e- gives Cu", "+1", "0"],
          ["III: 2 I- gives I2 + 2 e-", "-2", "-2"],
          ["IV: Cr3+ + 2 e- gives Cr", "+1", "0"]])

_T_ELECTRONS = dict(
    headers=["Pair of half-reactions", "Electrons in the oxidation half",
             "Electrons in the reduction half"],
    rows=[["Zinc with copper(II)", "2", "2"],
          ["Aluminum with copper(II)", "3", "2"],
          ["Iron(II) with permanganate", "1", "5"],
          ["Tin(II) with iron(III)", "2", "1"]])

_T_ATOMS = dict(
    headers=["Species in the acidic half-reaction",
             "Oxygen atoms on the reactant side",
             "Oxygen atoms on the product side"],
    rows=[["MnO4- gives Mn2+", "4", "0"],
          ["Cr2O7 2- gives 2 Cr3+", "7", "0"],
          ["SO4 2- gives SO2", "4", "2"]])

QUESTIONS = [

 dict(q="In a half-reaction that represents oxidation, where do the electrons "
        "appear, and why?",
      choices=[
        "On the product side, because oxidation is the loss of electrons by the "
        "species written on the reactant side",
        "On the reactant side, because the species must take in electrons before "
        "it can react",
        "On both sides in equal numbers, so that they cancel within the "
        "half-reaction itself",
        "On neither side, because electrons are never written in a "
        "half-reaction",
        "On whichever side balances the number of atoms, since charge is not "
        "considered"],
      ans=0,
      why="EK 4.9.A.1 has balanced redox equations constructed from "
          "half-reactions, and a half-reaction shows what one species does with "
          "electrons. A species that is oxidized releases them, so they are "
          "written among what the half-reaction produces."),

 dict(q="Which of the following is a reduction half-reaction?",
      choices=[
        "Cu2+ + 2 e- gives Cu",
        "Zn gives Zn2+ + 2 e-",
        "2 I- gives I2 + 2 e-",
        "Fe2+ gives Fe3+ + e-",
        "H2 gives 2 H+ + 2 e-"],
      ans=0,
      why="Reduction is the gain of electrons, so the electrons appear among the "
          "reactants of the half-reaction. Only one of the five writes the "
          "electrons on that side; the other four write them as products, which "
          "makes them oxidation halves."),

 dict(q="Zinc metal and copper(II) ions react. Given the half-reactions Zn gives "
        "Zn2+ + 2 e- and Cu2+ + 2 e- gives Cu, what is the balanced overall "
        "equation?",
      choices=[
        "Zn + Cu2+ gives Zn2+ + Cu",
        "Zn + Cu2+ + 2 e- gives Zn2+ + Cu + 2 e-",
        "2 Zn + Cu2+ gives 2 Zn2+ + Cu",
        "Zn + 2 Cu2+ gives Zn2+ + 2 Cu",
        "Zn2+ + Cu gives Zn + Cu2+"],
      ans=0,
      why="EK 4.9.A.1 builds the balanced equation from the half-reactions. Both "
          "halves already involve two electrons, so they add directly and the "
          "electrons cancel, leaving no electrons in the overall equation."),

 dict(q="Aluminum reacts with copper(II) ions. Given Al gives Al3+ + 3 e- and "
        "Cu2+ + 2 e- gives Cu, by what factors must the two half-reactions be "
        "multiplied before they are added?",
      choices=[
        "The aluminum half by 2 and the copper half by 3, giving six electrons "
        "in each",
        "The aluminum half by 3 and the copper half by 2, giving nine and four "
        "electrons",
        "Both halves by 6, so that each involves eighteen electrons",
        "Neither half, because the electrons already cancel as written",
        "The aluminum half by 3 alone, because it is the half with the larger "
        "number of electrons"],
      ans=0,
      why="EK 4.9.A.1 constructs the overall equation from half-reactions, which "
          "requires the electrons lost to equal the electrons gained. The "
          "smallest common multiple of three and two is six, so each half must "
          "be scaled to that number."),

 dict(q="Using the half-reactions Al gives Al3+ + 3 e- and Cu2+ + 2 e- gives Cu, "
        "what is the balanced overall equation?",
      choices=[
        "2 Al + 3 Cu2+ gives 2 Al3+ + 3 Cu",
        "3 Al + 2 Cu2+ gives 3 Al3+ + 2 Cu",
        "Al + Cu2+ gives Al3+ + Cu",
        "6 Al + 6 Cu2+ gives 6 Al3+ + 6 Cu",
        "2 Al + 3 Cu2+ + 6 e- gives 2 Al3+ + 3 Cu + 6 e-"],
      ans=0,
      why="EK 4.9.A.1 has the balanced equation constructed from the "
          "half-reactions after scaling each to a common electron count. Six "
          "electrons requires two aluminum atoms and three copper(II) ions, and "
          "no electrons remain in the sum."),

 dict(q="How many electrons are transferred in the balanced equation formed from "
        "Al gives Al3+ + 3 e- and Cu2+ + 2 e- gives Cu?",
      choices=["6", "5", "3", "2", "12"],
      ans=0,
      why="EK 4.9.A.1 requires the two half-reactions to be scaled until the "
          "electrons lost equal the electrons gained. That common number is the "
          "smallest value divisible by both three and two."),

 dict(q="The table lists four candidate half-reactions with the total charge on "
        "each side. Which candidates are correctly balanced with respect to "
        "charge?",
      table=_T_CHARGE,
      choices=[
        "I and III only, because in each of them the two sides carry the same "
        "total charge",
        "II and IV only, because in each of them the reactant side carries the "
        "larger charge",
        "All four, because every candidate shows a species gaining or losing "
        "electrons",
        "None of them, because a half-reaction cannot balance charge on its own",
        "I and II only, because both involve an ion with a charge of positive "
        "two"],
      ans=0,
      why="EK 4.9.A.1 has balanced equations constructed from half-reactions, "
          "and a half-reaction is not usable until charge balances as well as "
          "atoms. The table gives both totals directly, so the check is a "
          "comparison of the two columns."),

 dict(q="A student writes Cu2+ + e- gives Cu as a half-reaction. What is wrong "
        "with it?",
      choices=[
        "The charge does not balance, because the left side totals positive one "
        "and the right side is neutral",
        "The atoms do not balance, because there is one copper on the left and "
        "none on the right",
        "Electrons may not appear in a half-reaction at all",
        "Copper(II) ions cannot be reduced under any circumstances",
        "Nothing is wrong with it, because one electron is enough to neutralize "
        "any ion"],
      ans=0,
      why="EK 4.9.A.1 makes half-reactions the building blocks of a balanced "
          "equation, and both atoms and charge must balance in each. One "
          "electron leaves the ion one unit short of neutral, so two are "
          "required."),

 dict(q="In acidic solution the permanganate half-reaction is MnO4- + 8 H+ + 5 e- "
        "gives Mn2+ + 4 H2O. Which check confirms that its charge is balanced?",
      choices=[
        "Negative one plus eight positive charges minus five electron charges "
        "gives positive two, matching the manganese ion",
        "Negative one plus eight positive charges gives positive seven, matching "
        "the seven atoms of hydrogen and manganese",
        "The five electrons balance the five oxygen atoms carried by the "
        "permanganate ion",
        "The water molecules are neutral, so the charge on the product side "
        "cannot be determined",
        "Charge does not need to be balanced in a half-reaction written for "
        "acidic solution"],
      ans=0,
      why="EK 4.9.A.1 requires a usable half-reaction to balance both atoms and "
          "charge. Summing the charges on the reactant side, including the "
          "negative charge each electron carries, must give the total charge on "
          "the product side."),

 dict(q="Permanganate oxidizes iron(II) in acidic solution. Given MnO4- + 8 H+ + "
        "5 e- gives Mn2+ + 4 H2O and Fe2+ gives Fe3+ + e-, how many iron(II) ions "
        "appear in the balanced overall equation?",
      choices=["5", "1", "8", "4", "2"],
      ans=0,
      why="EK 4.9.A.1 constructs the balanced equation by scaling the "
          "half-reactions to a common electron count. The permanganate half "
          "consumes five electrons and the iron half releases one, so the iron "
          "half must be multiplied to match."),

 dict(q="Using MnO4- + 8 H+ + 5 e- gives Mn2+ + 4 H2O together with Fe2+ gives "
        "Fe3+ + e-, what is the balanced overall equation?",
      choices=[
        "MnO4- + 5 Fe2+ + 8 H+ gives Mn2+ + 5 Fe3+ + 4 H2O",
        "MnO4- + Fe2+ + 8 H+ gives Mn2+ + Fe3+ + 4 H2O",
        "5 MnO4- + Fe2+ + 40 H+ gives 5 Mn2+ + Fe3+ + 20 H2O",
        "MnO4- + 5 Fe2+ + 8 H+ + 5 e- gives Mn2+ + 5 Fe3+ + 4 H2O + 5 e-",
        "MnO4- + 5 Fe3+ + 8 H+ gives Mn2+ + 5 Fe2+ + 4 H2O"],
      ans=0,
      why="EK 4.9.A.1 has the overall equation constructed from the "
          "half-reactions once the electrons match. Multiplying the iron half by "
          "five and adding leaves five electrons on each side, which cancel, and "
          "the hydrogen and oxygen counts come from the printed half-reaction."),

 dict(q="In acidic solution the dichromate half-reaction is Cr2O7 2- + 14 H+ + 6 "
        "e- gives 2 Cr3+ + 7 H2O. How many electrons does one dichromate ion "
        "take in?",
      choices=["6", "2", "3", "7", "14"],
      ans=0,
      why="EK 4.9.A.1 makes the half-reaction the unit from which the balanced "
          "equation is built, and the number of electrons is written into it. "
          "The printed half-reaction states the number directly."),

 dict(q="Dichromate oxidizes iron(II) in acidic solution. Given Cr2O7 2- + 14 H+ "
        "+ 6 e- gives 2 Cr3+ + 7 H2O and Fe2+ gives Fe3+ + e-, how many iron(II) "
        "ions appear in the balanced overall equation?",
      choices=["6", "2", "3", "14", "7"],
      ans=0,
      why="EK 4.9.A.1 requires the electrons released by the oxidation half to "
          "equal the electrons taken in by the reduction half. The dichromate "
          "half takes six and each iron(II) ion releases one."),

 dict(q="Why must the electrons cancel completely when two half-reactions are "
        "added together?",
      choices=[
        "Because every electron released by one species is taken up by the "
        "other, so none is left over in the overall equation",
        "Because electrons are too small to appear in a chemical equation",
        "Because the two half-reactions always involve the same number of "
        "electrons before scaling",
        "Because an overall equation may show charge but never show a particle",
        "Because electrons are consumed by the solvent before the reaction is "
        "complete"],
      ans=0,
      why="EK 4.9.A.1 constructs the balanced equation from half-reactions. The "
          "half-reactions are two accounts of the same single transfer, so once "
          "they are scaled to the same electron count the electrons written on "
          "opposite sides are the same electrons and cancel."),

 dict(q="What must be true of a correctly balanced overall redox equation built "
        "from half-reactions?",
      choices=[
        "The atoms of every element and the total charge are the same on both "
        "sides, and no electrons appear",
        "The atoms balance but the charge need not, because ions carry charge "
        "into solution",
        "The charge balances but the atoms need not, because electrons carry "
        "mass away",
        "Electrons appear on the product side to show that a transfer occurred",
        "The number of species on each side must be equal"],
      ans=0,
      why="EK 4.9.A.1 constructs the balanced equation from half-reactions, each "
          "of which is itself balanced for atoms and charge. Adding two balanced "
          "expressions preserves both, and the matched electrons cancel."),

 dict(q="The overall equation 2 Ag+ + Cu gives 2 Ag + Cu2+ is to be separated "
        "into half-reactions. Which pair is correct?",
      choices=[
        "Cu gives Cu2+ + 2 e-, and 2 Ag+ + 2 e- gives 2 Ag",
        "Cu + 2 e- gives Cu2+, and 2 Ag+ gives 2 Ag + 2 e-",
        "Cu gives Cu2+ + e-, and Ag+ + e- gives Ag",
        "2 Cu gives 2 Cu2+ + 4 e-, and Ag+ + e- gives Ag",
        "Cu gives Cu2+, and 2 Ag+ gives 2 Ag, with no electrons in either"],
      ans=0,
      why="EK 4.9.A.1 has the balanced equation and its half-reactions related "
          "by construction. Copper goes from zero to positive two, releasing two "
          "electrons, and the two silver ions each take one, so the electron "
          "counts match and add back to the given equation."),

 dict(q="The table gives four pairs of half-reactions with the electron count in "
        "each half. For which pair do the two halves combine with no scaling at "
        "all?",
      table=_T_ELECTRONS,
      choices=[
        "The zinc with copper(II) pair, because both halves already involve the "
        "same number of electrons",
        "The aluminum with copper(II) pair, because three and two have no common "
        "factor",
        "The iron(II) with permanganate pair, because one electron divides "
        "evenly into five",
        "The tin(II) with iron(III) pair, because two is twice one",
        "None of the pairs, because every combination requires scaling"],
      ans=0,
      why="EK 4.9.A.1 requires the electrons lost to equal the electrons gained "
          "before the halves are added. Only a pair whose two tabulated counts "
          "are already equal needs no multiplier on either half."),

 dict(q="Tin(II) is oxidized by iron(III): Sn2+ gives Sn4+ + 2 e- and Fe3+ + e- "
        "gives Fe2+. What is the balanced overall equation?",
      choices=[
        "Sn2+ + 2 Fe3+ gives Sn4+ + 2 Fe2+",
        "2 Sn2+ + Fe3+ gives 2 Sn4+ + Fe2+",
        "Sn2+ + Fe3+ gives Sn4+ + Fe2+",
        "Sn2+ + 2 Fe3+ + 2 e- gives Sn4+ + 2 Fe2+ + 2 e-",
        "Sn4+ + 2 Fe2+ gives Sn2+ + 2 Fe3+"],
      ans=0,
      why="EK 4.9.A.1 scales the halves to a common electron count before "
          "adding. The tin half releases two electrons and each iron(III) ion "
          "takes one, so the iron half is doubled and the electrons then cancel."),

 dict(q="The half-reaction 2 I- gives I2 + 2 e- is written for the oxidation of "
        "iodide. Which statement about it is correct?",
      choices=[
        "It balances both atoms and charge, with negative two on each side once "
        "the electrons are counted",
        "It balances atoms but not charge, because the left side is negative and "
        "the right side is neutral",
        "It balances charge but not atoms, because two iodide ions cannot give "
        "one molecule",
        "It is a reduction half-reaction, because the iodide ions are consumed",
        "It cannot be a half-reaction, because no oxygen atoms appear in it"],
      ans=0,
      why="EK 4.9.A.1 makes a usable half-reaction one balanced for both atoms "
          "and charge. Two iodine atoms appear on each side, and the two "
          "electrons written as products carry the same total negative charge "
          "the two iodide ions did."),

 dict(q="The table gives the number of oxygen atoms on each side of three "
        "half-reaction skeletons written for acidic solution. Which species must "
        "be added, and to which side, in order to balance the oxygen atoms?",
      table=_T_ATOMS,
      choices=[
        "Water molecules on the product side, one for each oxygen atom the "
        "reactant side holds in excess",
        "Water molecules on the reactant side, one for each oxygen atom the "
        "reactant side holds in excess",
        "Oxygen molecules on the product side, one for every two excess oxygen "
        "atoms",
        "Hydroxide ions on the product side, one for each excess oxygen atom",
        "Nothing, because oxygen atoms in a half-reaction do not need to balance"],
      ans=0,
      why="EK 4.9.A.1 makes a balanced half-reaction the building block, so the "
          "atoms of every element must balance in it. Each row shows more oxygen "
          "on the reactant side than the product side, and in acidic solution "
          "the species available to carry that oxygen is water."),

 dict(q="A student adds two half-reactions and obtains an equation with 3 e- on "
        "the reactant side and 2 e- on the product side. What has gone wrong?",
      choices=[
        "The halves were added before being scaled to a common electron count, "
        "so the electrons did not cancel",
        "The halves were scaled correctly but the atoms were miscounted",
        "Nothing has gone wrong, since a difference of one electron is within "
        "tolerance",
        "The student reversed one of the half-reactions, which always leaves "
        "electrons behind",
        "The student used a reduction half where an oxidation half was needed, "
        "which cannot be corrected"],
      ans=0,
      why="EK 4.9.A.1 constructs the balanced equation from half-reactions, and "
          "that construction requires the electrons lost to equal the electrons "
          "gained. Unequal counts are exactly what remains when the scaling step "
          "has been skipped."),

 dict(q="Hydrogen gas is oxidized to hydrogen ions. Which half-reaction "
        "represents that correctly?",
      choices=[
        "H2 gives 2 H+ + 2 e-",
        "H2 + 2 e- gives 2 H+",
        "2 H+ + 2 e- gives H2",
        "H2 gives 2 H+ + e-",
        "H+ gives H2 + e-"],
      ans=0,
      why="Oxidation is the loss of electrons, so they belong among the products, "
          "and EK 4.9.A.1 requires atoms and charge to balance: two hydrogen "
          "atoms on each side, and two units of positive charge offset by two "
          "electrons."),

 dict(q="In the balanced equation 3 Cu + 8 H+ + 2 NO3- gives 3 Cu2+ + 2 NO + 4 "
        "H2O, how many electrons are transferred in total?",
      choices=["6", "3", "2", "8", "4"],
      ans=0,
      why="EK 4.9.A.1 relates the balanced equation to the half-reactions it was "
          "built from. Each copper atom goes from zero to positive two, and "
          "three copper atoms appear, so that is the total number of electrons "
          "the reduction half must have taken in."),

 dict(q="The table lists four half-reactions with the number of electrons in each "
        "and the side on which they appear. Which two would combine to give a "
        "balanced overall equation with the smallest whole-number coefficients?",
      table=_T_HALF,
      choices=[
        "The zinc half with the copper(II) half, since both involve two "
        "electrons and need no scaling",
        "The aluminum half with the copper(II) half, since three and two are "
        "the smallest numbers listed",
        "The zinc half with the aluminum half, since both write their electrons "
        "on the product side",
        "The copper(II) half with the silver half, since both write their "
        "electrons on the reactant side",
        "Any two of them, since every pair combines with the same coefficients"],
      ans=0,
      why="EK 4.9.A.1 requires one half to release the electrons the other takes "
          "in, so the pair must have electrons on opposite sides, and equal "
          "counts avoid any multiplier. The table supplies both the counts and "
          "the sides."),

 dict(q="Which statement correctly describes what a half-reaction represents?",
      choices=[
        "The change undergone by one of the two species, written with the "
        "electrons it loses or gains",
        "Half of the total number of atoms taking part in the reaction",
        "The first half of the reaction in time, before the products appear",
        "The portion of the reaction that occurs in solution rather than at a "
        "surface",
        "An equation in which only atoms are balanced and charge is ignored"],
      ans=0,
      why="EK 4.9.A.1 has balanced redox equations constructed from "
          "half-reactions, which is only possible if each half-reaction is a "
          "complete, balanced account of what one species does with electrons."),

 dict(q="Silver ions are reduced by zinc metal. Given Ag+ + e- gives Ag and Zn "
        "gives Zn2+ + 2 e-, how many silver ions appear in the balanced overall "
        "equation?",
      choices=["2", "1", "3", "4", "6"],
      ans=0,
      why="EK 4.9.A.1 requires the electrons gained to equal the electrons lost. "
          "Zinc releases two electrons and each silver ion takes one, so the "
          "silver half must be scaled to match."),

 dict(q="A half-reaction is reversed so that a reduction becomes an oxidation. "
        "What happens to the electrons?",
      choices=[
        "They move to the other side of the equation, keeping the same "
        "coefficient",
        "They keep their side of the equation but their coefficient is halved",
        "They disappear, since a reversed half-reaction involves no transfer",
        "Their coefficient is doubled, because the direction of transfer has "
        "changed",
        "They appear on both sides, one set for each direction"],
      ans=0,
      why="A half-reaction written in reverse describes the same species doing "
          "the opposite thing with the same electrons, so the count is unchanged "
          "and only the side moves. EK 4.9.A.1 relies on being able to write "
          "either direction when building the overall equation."),

 dict(q="Which pair of half-reactions could NOT be combined into an overall redox "
        "equation as written?",
      choices=[
        "Zn gives Zn2+ + 2 e- together with Cu gives Cu2+ + 2 e-",
        "Zn gives Zn2+ + 2 e- together with Cu2+ + 2 e- gives Cu",
        "Al gives Al3+ + 3 e- together with Ag+ + e- gives Ag",
        "Fe2+ gives Fe3+ + e- together with Cu2+ + 2 e- gives Cu",
        "2 I- gives I2 + 2 e- together with Cl2 + 2 e- gives 2 Cl-"],
      ans=0,
      why="EK 4.9.A.1 builds the overall equation by matching electrons "
          "released against electrons taken in. Two halves that both write their "
          "electrons as products have nothing to receive them, so adding them "
          "leaves electrons in the result."),

 dict(q="After scaling and adding two half-reactions, a student finds four water "
        "molecules on the reactant side and one on the product side. What should "
        "the final equation show?",
      choices=[
        "Three water molecules on the reactant side and none on the product side",
        "Four water molecules on the reactant side and one on the product side, "
        "left as they are",
        "Five water molecules on the reactant side, since the two counts add",
        "One water molecule on each side, since the smaller count is kept",
        "No water at all, since water is the solvent and is never written"],
      ans=0,
      why="EK 4.9.A.1 produces one balanced equation from the sum of the "
          "half-reactions, and a species appearing on both sides is present in "
          "excess on one of them. Cancelling the common amount leaves the net "
          "number on the side that had more."),

 dict(q="Why is constructing a redox equation from half-reactions more reliable "
        "than balancing it by inspection?",
      choices=[
        "Because each half-reaction forces the electron count and the charge to "
        "be accounted for explicitly",
        "Because half-reactions do not require the atoms of each element to "
        "balance",
        "Because a half-reaction can be written without knowing what the "
        "products are",
        "Because balancing by inspection cannot be done for any equation "
        "involving ions",
        "Because half-reactions always give coefficients smaller than those "
        "found by inspection"],
      ans=0,
      why="EK 4.9.A.1 states that balanced chemical equations for redox "
          "reactions can be constructed from half-reactions. Writing each half "
          "separately makes the electrons an explicit quantity that must match, "
          "which inspection of the overall equation leaves implicit."),
]
