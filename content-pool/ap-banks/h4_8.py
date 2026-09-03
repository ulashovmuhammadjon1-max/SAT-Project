# AP CHEMISTRY 4.8 Introduction to Acid-Base Reactions
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.8.A: identify species as Bronsted-Lowry acids, bases,
# and/or conjugate acid-base pairs, based on proton transfer involving those
# species. Suggested skill 1.B, describe the components of and quantitative
# information from models and representations.
#
# Essential knowledge relied on, in the framework's own words:
#   4.8.A.1  By definition, a Bronsted-Lowry acid is a proton donor and a
#            Bronsted-Lowry base is a proton acceptor.
#   4.8.A.2  Only in aqueous solutions, water plays an important role in many
#            acid-base reactions, as its molecular structure allows it to accept
#            protons from and donate protons to dissolved species.
#   4.8.A.3  When an acid or base ionizes in water, the conjugate acid-base pairs
#            can be identified and their relative strengths compared.
#
# THE EXCLUSION STATEMENT IS OBEYED AND CHECKED. "Lewis acid-base concepts will
# not be assessed on the AP Exam. The emphasis in AP Chemistry is on reactions in
# aqueous solution." Neither "Lewis acid" nor "Lewis base" appears anywhere in
# this module, and no key rests on electron-pair donation or acceptance;
# verify_h4_8.py fails the module if either phrase is reintroduced by an edit.
#
# ON RELATIVE STRENGTH. 4.8.A.3 allows the relative strengths of conjugate pairs
# to be compared, but Unit 8 owns Ka, Kb and pH. So every strength comparison
# here is made from data GIVEN in the item -- a percent ionization, or the stated
# direction a proton transfer runs -- and the reasoning is about protons being
# given up or held on to, never about a constant a student would have to recall.
#
# ON THE SPELLING. The CED prints "Bronsted-Lowry" with a slashed o. This module
# uses the plain ASCII spelling throughout so that a stem, a choice and an anchor
# cannot disagree on the character, which is the sort of difference a substring
# check does not survive.
#
# Topic 4.7 classifies whole reactions as acid-base, redox or precipitation.
# This module identifies the ROLE of each species within an acid-base reaction,
# which is what LO 4.8.A asks; no item here asks which class a reaction is in.
#
# NOTATION. Chemistry is not typeset; formulas and charges stay plain text.
TOPIC = ("4.8", "Introduction to Acid-Base Reactions", 4)

_T_IONIZATION = dict(
    headers=["Acid", "Percent of the acid ionized in 0.10 M aqueous solution"],
    rows=[["HA", "92"],
          ["HB", "14"],
          ["HD", "3.0"],
          ["HE", "0.40"]])

_T_PAIRS = dict(
    headers=["Species", "Formula obtained by removing one proton",
             "Formula obtained by adding one proton"],
    rows=[["H2O", "OH-", "H3O+"],
          ["NH3", "NH2-", "NH4+"],
          ["HCO3-", "CO3 2-", "H2CO3"],
          ["HSO4-", "SO4 2-", "H2SO4"]])

_T_ROLES = dict(
    headers=["Reaction in aqueous solution", "Species that loses a proton",
             "Species that gains a proton"],
    rows=[["HF + H2O gives F- + H3O+", "HF", "H2O"],
          ["NH3 + H2O gives NH4+ + OH-", "H2O", "NH3"],
          ["HCO3- + OH- gives CO3 2- + H2O", "HCO3-", "OH-"]])

_T_CANDIDATES = dict(
    headers=["Species", "Number of protons the species can donate",
             "Can the species accept a proton?"],
    rows=[["Cl-", "0", "Yes"],
          ["HSO4-", "1", "Yes"],
          ["NH4+", "1", "No"],
          ["H2PO4-", "2", "Yes"]])

QUESTIONS = [

 dict(q="By the definition used in this course, what is a Bronsted-Lowry acid?",
      choices=[
        "A proton donor",
        "A proton acceptor",
        "A species that raises the conductivity of any solution it enters",
        "A species that must contain oxygen in order to react",
        "A species that dissolves metals to release hydrogen gas"],
      ans=0,
      why="EK 4.8.A.1, verbatim: by definition, a Bronsted-Lowry acid is a "
          "proton donor and a Bronsted-Lowry base is a proton acceptor. Nothing "
          "in that definition refers to conductivity or to any particular "
          "element."),

 dict(q="By the definition used in this course, what is a Bronsted-Lowry base?",
      choices=[
        "A proton acceptor",
        "A proton donor",
        "A species that always contains a hydroxide ion",
        "A species that neutralizes any solid it comes into contact with",
        "A species that lowers the temperature of the solution it enters"],
      ans=0,
      why="EK 4.8.A.1, verbatim: a Bronsted-Lowry base is a proton acceptor. "
          "Containing hydroxide is one way to accept a proton but the definition "
          "does not require it, as ammonia accepting a proton shows."),

 dict(q="Hydrogen fluoride reacts with water according to HF + H2O → F- + H3O+. "
        "Which species acts as the acid, and why?",
      choices=[
        "HF, because it gives up a proton to the water molecule",
        "H2O, because it is present in the largest amount",
        "F-, because it carries a negative charge after the transfer",
        "H3O+, because it holds the greatest number of hydrogen atoms",
        "Both HF and H2O, because both contain hydrogen atoms"],
      ans=0,
      why="EK 4.8.A.1 makes a Bronsted-Lowry acid a proton donor. Comparing the "
          "two sides shows HF losing a hydrogen to become F- while the water "
          "gains one to become H3O+."),

 dict(q="In the reaction NH3 + H2O → NH4+ + OH-, which species acts as the base?",
      choices=[
        "NH3, because it accepts a proton from the water molecule",
        "H2O, because water is a base in every reaction it takes part in",
        "OH-, because it is the species left after the transfer",
        "NH4+, because it carries a positive charge",
        "Neither species, because no hydroxide was present at the start"],
      ans=0,
      why="EK 4.8.A.1 makes a Bronsted-Lowry base a proton acceptor. Ammonia "
          "gains a hydrogen to become the ammonium ion, so it is the acceptor "
          "and the water is the donor in this reaction."),

 dict(q="What is the conjugate base of the acid HNO2?",
      choices=["NO2-", "HNO3", "H2NO2+", "NO3-", "H3O+"],
      ans=0,
      why="A conjugate base is what remains after a Bronsted-Lowry acid donates "
          "the proton that EK 4.8.A.1 defines it by, so the pair differs by "
          "exactly one hydrogen and one unit of charge."),

 dict(q="What is the conjugate acid of the base HPO4 2-?",
      choices=["H2PO4-", "PO4 3-", "H3PO4", "HPO4-", "H2PO4 2-"],
      ans=0,
      why="A conjugate acid is what a Bronsted-Lowry base becomes after it "
          "accepts the proton EK 4.8.A.1 defines it by, so it holds one more "
          "hydrogen and its charge is one unit more positive."),

 dict(q="Water accepts a proton from hydrogen chloride in one reaction and "
        "donates a proton to ammonia in another. What does this show about "
        "water?",
      choices=[
        "Its molecular structure allows it to both accept protons from and "
        "donate protons to dissolved species",
        "It is a stronger acid than hydrogen chloride and a stronger base than "
        "ammonia",
        "It changes its molecular structure depending on what is dissolved in it",
        "It takes no part in either reaction and only carries the dissolved "
        "species",
        "It can accept a proton only when no other base is present in the "
        "solution"],
      ans=0,
      why="EK 4.8.A.2, near verbatim: water plays an important role in many "
          "acid-base reactions because its molecular structure allows it to "
          "accept protons from and donate protons to dissolved species. Its "
          "structure is the same in both cases."),

 dict(q="In the reaction HCN + H2O → CN- + H3O+, which two species form a "
        "conjugate acid-base pair?",
      choices=[
        "HCN and CN-",
        "HCN and H3O+",
        "H2O and CN-",
        "CN- and H3O+",
        "HCN and H2O"],
      ans=0,
      why="EK 4.8.A.3 has the conjugate acid-base pairs identified when an acid "
          "ionizes in water. A pair is the same species before and after one "
          "proton has moved, so the two members differ by exactly one hydrogen."),

 dict(q="The hydrogen carbonate ion, HCO3-, reacts with hydrochloric acid to give "
        "H2CO3 and with sodium hydroxide to give CO3 2-. What does this behavior "
        "show?",
      choices=[
        "The ion can act as a proton acceptor in one reaction and a proton donor "
        "in the other",
        "The ion is a stronger acid than it is a base in every solution",
        "The ion is neither an acid nor a base, since it does not behave the "
        "same way in both reactions",
        "The ion breaks apart into carbon dioxide before either reaction can "
        "occur",
        "The ion must contain two ionizable hydrogen atoms in order to do both"],
      ans=0,
      why="EK 4.8.A.1 defines an acid as a proton donor and a base as a proton "
          "acceptor. Gaining a hydrogen to become H2CO3 is acceptance and losing "
          "one to become the carbonate ion is donation, so both roles are "
          "available to the same species."),

 dict(q="Which of the following is a conjugate acid-base pair?",
      choices=[
        "H2SO4 and HSO4-",
        "H2SO4 and SO4 2-",
        "H3O+ and OH-",
        "NH4+ and NH2-",
        "HCl and NaCl"],
      ans=0,
      why="A conjugate pair under EK 4.8.A.3 consists of two species differing "
          "by exactly one transferred proton, which changes the count of "
          "hydrogen atoms by one and the charge by one unit."),

 dict(q="A student claims that H3O+ and OH- form a conjugate acid-base pair. Why "
        "is this incorrect?",
      choices=[
        "They differ by two protons rather than one, so neither becomes the "
        "other in a single transfer",
        "They differ in charge, and the members of a conjugate pair must carry "
        "the same charge",
        "Neither of them can act as an acid or a base, since both come from "
        "water",
        "They can never be present in the same solution at the same time",
        "A conjugate pair must contain a species with no charge at all"],
      ans=0,
      why="EK 4.8.A.3 identifies conjugate pairs from the ionization of an acid "
          "or base, and a pair is related by the transfer of a single proton. "
          "Converting the hydronium ion to hydroxide requires two hydrogens to "
          "be removed."),

 dict(q="The table shows, for three aqueous reactions, which species loses a "
        "proton and which gains one. In which reaction does water act as a "
        "Bronsted-Lowry acid?",
      table=_T_ROLES,
      choices=[
        "The reaction of ammonia with water, because water is the species that "
        "loses a proton there",
        "The reaction of hydrogen fluoride with water, because water is one of "
        "the reactants",
        "The reaction of the hydrogen carbonate ion with hydroxide, because "
        "water appears among the products",
        "All three reactions, because water is an acid whenever it is present",
        "None of the three, because water is a solvent rather than a reactant"],
      ans=0,
      why="EK 4.8.A.1 makes an acid the proton donor, and the table names the "
          "donor for each reaction directly. Water is listed as the donor in "
          "exactly one of the three rows."),

 dict(q="The table gives the percentage of each acid that ionizes in 0.10 M "
        "aqueous solution. Which acid gives up protons most readily?",
      table=_T_IONIZATION,
      choices=[
        "HA, because the largest fraction of it has donated a proton to water",
        "HE, because the smallest fraction of it has ionized",
        "HD, because its percentage lies between the two extremes",
        "HB, because its percentage is closest to the average of the four",
        "All four equally, because each was prepared at the same concentration"],
      ans=0,
      why="EK 4.8.A.1 makes an acid a proton donor, and EK 4.8.A.3 allows "
          "relative strengths to be compared when an acid ionizes in water. The "
          "larger the ionized fraction at the same concentration, the more "
          "readily that acid has given up its proton."),

 dict(q="Using the same table of percent ionization, which conjugate base holds a "
        "proton most tightly?",
      table=_T_IONIZATION,
      choices=[
        "The conjugate base of HE, because HE gave up its proton least readily "
        "of the four",
        "The conjugate base of HA, because HA ionized to the greatest extent",
        "The conjugate base of HD, because its acid ionized to an intermediate "
        "extent",
        "The conjugate base of HB, because its percentage is a whole number",
        "They all hold a proton equally tightly, because each pair differs by "
        "one proton"],
      ans=0,
      why="EK 4.8.A.3 allows the relative strengths of conjugate pairs to be "
          "compared. An acid that has parted with its proton least readily is "
          "one whose conjugate base is the one most inclined to keep a proton "
          "once it has one."),

 dict(q="In the reaction HSO4- + H2O → SO4 2- + H3O+, identify the acid on each "
        "side of the equation.",
      choices=[
        "HSO4- on the left and H3O+ on the right, since each is the species that "
        "can donate a proton",
        "H2O on the left and SO4 2- on the right, since each is the species that "
        "can accept a proton",
        "HSO4- on the left and SO4 2- on the right, since sulfur appears in both",
        "H2O on the left and H3O+ on the right, since both contain oxygen",
        "There is an acid only on the left, because the products of an acid-base "
        "reaction are neutral"],
      ans=0,
      why="EK 4.8.A.1 makes an acid a proton donor. Reading the equation in "
          "reverse shows the hydronium ion able to hand a proton to the sulfate "
          "ion, so each direction has its own donor."),

 dict(q="Which species listed cannot act as a Bronsted-Lowry acid under any "
        "circumstances?",
      choices=[
        "Cl-, because it contains no hydrogen atom to donate",
        "HSO4-, because it carries a negative charge",
        "H2O, because it is the solvent rather than a solute",
        "NH4+, because it carries a positive charge",
        "H2PO4-, because it already holds two hydrogen atoms"],
      ans=0,
      why="EK 4.8.A.1 defines a Bronsted-Lowry acid as a proton donor. A species "
          "with no hydrogen atom at all has no proton available to donate, while "
          "charge alone prevents nothing."),

 dict(q="The table lists four species with the number of protons each can donate "
        "and whether it can accept one. Which species can act ONLY as a base?",
      table=_T_CANDIDATES,
      choices=[
        "Cl-, because the table gives it no proton to donate while it can still "
        "accept one",
        "HSO4-, because the table shows that it can both donate and accept",
        "NH4+, because the table shows that it cannot accept a proton",
        "H2PO4-, because it can donate more protons than any other species "
        "listed",
        "None of them, because every species in the table can donate at least "
        "one proton"],
      ans=0,
      why="EK 4.8.A.1 makes donating a proton the mark of an acid and accepting "
          "one the mark of a base. Acting only as a base requires the table to "
          "record no proton available to donate and acceptance still possible, "
          "which one row does."),

 dict(q="Sulfuric acid loses protons in two steps: H2SO4 gives HSO4-, and HSO4- "
        "gives SO4 2-. How many conjugate acid-base pairs are represented among "
        "these three species?",
      choices=[
        "Two, because each adjacent species differs from the next by one proton",
        "One, because all three species contain sulfur and oxygen",
        "Three, because any two of the three species make a pair",
        "None, because a conjugate pair cannot include a species carrying two "
        "negative charges",
        "Two, because the first and last species differ by exactly two protons"],
      ans=0,
      why="EK 4.8.A.3 identifies conjugate pairs from an ionization. A pair is "
          "related by a single proton transfer, so the first species pairs with "
          "the second and the second with the third, while the first and third "
          "differ by two."),

 dict(q="Ammonium ion reacts with hydroxide ion according to NH4+ + OH- → NH3 + "
        "H2O. Which species is the Bronsted-Lowry base among the reactants?",
      choices=[
        "OH-, because it accepts the proton released by the ammonium ion",
        "NH4+, because it releases a hydrogen atom",
        "NH3, because ammonia is a base in aqueous solution",
        "H2O, because it appears among the products",
        "Both reactants, because both contain hydrogen atoms"],
      ans=0,
      why="EK 4.8.A.1 makes a base a proton acceptor. The hydroxide ion gains a "
          "hydrogen to become water, and ammonia is a product here rather than a "
          "reactant."),

 dict(q="The table shows, for four species, what each becomes when one proton is "
        "removed and when one is added. Which species has BOTH a conjugate base "
        "and a conjugate acid listed, and what does that show?",
      table=_T_PAIRS,
      choices=[
        "All four, which shows that each of them can act either as a proton "
        "donor or as a proton acceptor",
        "Only H2O, which shows that water is the only species able to act in "
        "both roles",
        "Only the two ions, which shows that a charge is required in order to "
        "act in both roles",
        "None of them, which shows that a species can occupy only one role",
        "Only NH3, which shows that a species must be neutral to act in both "
        "roles"],
      ans=0,
      why="EK 4.8.A.1 makes donating a proton the mark of an acid and accepting "
          "one the mark of a base, and every row of the table gives a formula "
          "for both operations. EK 4.8.A.2 makes water one such species rather "
          "than the only one."),

 dict(q="An acid HX ionizes in water so that nearly every HX molecule has "
        "transferred its proton. Which statement about the resulting solution is "
        "best supported?",
      choices=[
        "It contains far more X- than HX, because the proton transfer has gone "
        "nearly to completion",
        "It contains far more HX than X-, because ionization consumes X-",
        "It contains equal amounts of HX and X-, because a conjugate pair is "
        "always present in equal amounts",
        "It contains no water molecules, because they have all accepted protons",
        "It contains X- but no hydronium ion, because only one product can form"],
      ans=0,
      why="EK 4.8.A.3 has the conjugate pair identified when an acid ionizes in "
          "water. If almost every molecule has donated its proton, almost all of "
          "the acid is present as its conjugate base and an equal number of "
          "protons has been accepted by water."),

 dict(q="How many conjugate acid-base pairs appear in the equation HF + H2O → F- "
        "+ H3O+, and which species make them up?",
      choices=[
        "Two pairs: hydrogen fluoride with fluoride, and water with hydronium",
        "One pair: hydrogen fluoride with fluoride, since only one proton moved",
        "One pair: hydrogen fluoride with hydronium, since both contain the "
        "transferred proton",
        "Four pairs, since every species in the equation pairs with every other "
        "one",
        "No pairs, since a conjugate pair requires both members to appear on the "
        "same side of the equation"],
      ans=0,
      why="EK 4.8.A.3 has conjugate pairs identified when an acid ionizes in "
          "water. One proton moves, but it leaves a donor behind and arrives at "
          "an acceptor, so the donor with what it became and the acceptor with "
          "what it became are two separate pairs."),

 dict(q="Two species differ by exactly one hydrogen atom, and their charges are "
        "-1 and -2. Which conclusion is best supported?",
      choices=[
        "They are a conjugate pair, with the more negative species the base of "
        "the two",
        "They are a conjugate pair, with the more negative species the acid of "
        "the two",
        "They cannot be a conjugate pair, because both carry a negative charge",
        "They cannot be a conjugate pair, because a proton carries no charge",
        "They are a conjugate pair only if one of them is derived from water"],
      ans=0,
      why="EK 4.8.A.3 identifies conjugate pairs by a single proton transfer. "
          "Removing a proton takes away one positive charge, so the species with "
          "the more negative charge is the one that has already given the proton "
          "up and is therefore the acceptor of the two."),

 dict(q="In the reaction CH3COOH + NH3 → CH3COO- + NH4+, which pair of statements "
        "correctly assigns the roles?",
      choices=[
        "The acetic acid donates a proton and the ammonia accepts it",
        "The ammonia donates a proton and the acetic acid accepts it",
        "Both species donate a proton to one another simultaneously",
        "Neither species donates a proton, because no water is present",
        "The acetate ion donates a proton to the ammonium ion"],
      ans=0,
      why="EK 4.8.A.1 defines the two roles by proton donation and acceptance. "
          "Comparing the two sides shows the acid losing a hydrogen to become "
          "the acetate ion and the ammonia gaining one to become the ammonium "
          "ion."),

 dict(q="What relationship must hold between the members of any conjugate "
        "acid-base pair?",
      choices=[
        "They differ by exactly one proton, so one hydrogen atom and one unit of "
        "positive charge separate them",
        "They differ by exactly one electron, so their charges differ by one "
        "unit",
        "They contain the same number of hydrogen atoms but different charges",
        "They contain different elements but the same total charge",
        "One must be neutral and the other must carry a charge"],
      ans=0,
      why="EK 4.8.A.3 identifies conjugate pairs from a proton transfer, and a "
          "proton is a hydrogen nucleus carrying one positive charge. Both the "
          "hydrogen count and the charge therefore shift by exactly one."),

 dict(q="A student is told that the reaction HD + H2O → D- + H3O+ proceeds only "
        "slightly to the right, while HA + H2O → A- + H3O+ proceeds nearly "
        "completely. Which comparison of the two conjugate bases follows?",
      choices=[
        "D- accepts a proton more readily than A- does, because HD gives its "
        "proton up less readily than HA",
        "A- accepts a proton more readily than D- does, because HA is the more "
        "extensively ionized acid",
        "The two conjugate bases accept protons equally readily, because both "
        "come from an acid reacting with water",
        "Neither conjugate base can accept a proton, because each already lost "
        "one",
        "The comparison cannot be made without knowing the concentrations of the "
        "two acids"],
      ans=0,
      why="EK 4.8.A.3 allows the relative strengths of conjugate pairs to be "
          "compared. An acid that mostly keeps its proton is one whose conjugate "
          "base takes a proton back readily, which is what the stated extents of "
          "reaction describe."),

 dict(q="Hydrogen bromide is dissolved in water. Which equation correctly shows "
        "the proton transfer, with the roles correctly assigned?",
      choices=[
        "HBr + H2O gives Br- + H3O+, with HBr the donor and water the acceptor",
        "HBr + H2O gives HBrO + H2, with HBr the acceptor and water the donor",
        "HBr + H2O gives H2Br+ + OH-, with water the donor and HBr the acceptor",
        "HBr + H2O gives Br- + H2 + O, with the water molecule splitting into "
        "separate atoms",
        "HBr does not react with water, because both species contain hydrogen"],
      ans=0,
      why="EK 4.8.A.1 makes the donor the acid and the acceptor the base, and EK "
          "4.8.A.2 has water accept protons from dissolved species. Atoms and "
          "charge must also balance, which rules out the equations that create "
          "or destroy atoms."),

 dict(q="Which observation would show that a dissolved species had acted as a "
        "Bronsted-Lowry base?",
      choices=[
        "The species is found to hold one more hydrogen atom after the reaction "
        "than before it",
        "The species is found to hold one fewer hydrogen atom after the reaction "
        "than before it",
        "The species is found to have dissolved completely in the water",
        "The species is found to have raised the temperature of the solution",
        "The species is found to have formed a solid with another dissolved ion"],
      ans=0,
      why="EK 4.8.A.1 makes a base a proton acceptor. A proton is a hydrogen "
          "nucleus, so accepting one shows up as one more hydrogen atom on the "
          "species than it carried before."),

 dict(q="The dihydrogen phosphate ion, H2PO4-, is placed in water. Which pair of "
        "products could result from H2PO4- acting as a base, and from it acting "
        "as an acid, respectively?",
      choices=[
        "H3PO4 as the base product, and HPO4 2- as the acid product",
        "HPO4 2- as the base product, and H3PO4 as the acid product",
        "PO4 3- as the base product, and H3PO4 as the acid product",
        "H3PO4 as the base product, and PO4 3- as the acid product",
        "H2PO4- cannot act in both ways, so no such pair exists"],
      ans=0,
      why="EK 4.8.A.1 makes acceptance of a proton the mark of a base and "
          "donation the mark of an acid. Accepting adds one hydrogen and one "
          "unit of positive charge; donating removes one of each."),

 dict(q="Which statement about the role of water in an aqueous acid-base reaction "
        "is supported by the course framework?",
      choices=[
        "Water may take part directly, accepting a proton in one reaction and "
        "donating a proton in another",
        "Water always takes part as a proton acceptor and never as a proton "
        "donor",
        "Water never takes part directly and serves only to keep the solutes "
        "apart",
        "Water takes part only when neither solute contains a hydrogen atom",
        "Water takes part only when the solution is warmer than room temperature"],
      ans=0,
      why="EK 4.8.A.2 states that water plays an important role in many "
          "acid-base reactions, as its molecular structure allows it to accept "
          "protons from and donate protons to dissolved species. Both roles are "
          "named in the statement itself."),
]
