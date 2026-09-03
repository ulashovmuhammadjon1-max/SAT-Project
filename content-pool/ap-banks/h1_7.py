r"""AP CHEMISTRY 1.7 Periodic Trends.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.7.A: explain the relationship between trends in atomic
properties of elements and electronic structure and periodicity.
Suggested skill 4.A, predict and/or explain chemical properties or phenomena
using given chemical theories, models, and representations.

Essential knowledge relied on, in the framework's own words:

  1.7.A.1  The organization of the periodic table is based on patterns of
           recurring properties of the elements, which are explained by
           patterns of ground-state electron configurations and the presence of
           completely or partially filled shells (and subshells) of electrons
           in atoms.

           Exclusion Statement: Writing the electron configuration of elements
           that are exceptions to the aufbau principle will not be assessed on
           the AP Exam.

  1.7.A.2  Trends in atomic properties within the periodic table (periodicity)
           can be predicted by the position of the element on the periodic
           table and qualitatively understood using Coulomb's law, the shell
           model, and the concepts of shielding and effective nuclear charge.
           These properties include: i. Ionization energy, ii. Atomic and ionic
           radii, iii. Electron affinity, iv. Electronegativity.

  1.7.A.3  The periodicity (in 1.7.A.2) is useful to predict/estimate values of
           properties in the absence of data.

HOW THIS TOPIC IS KEPT DISTINCT FROM 1.5 AND 1.6. Topic 1.5 applies Coulomb's
law to subshells of one atom and writes configurations from electron counts;
1.6 reads a configuration back out of a spectrum. Everything here starts from
an element's POSITION in the periodic table, which is what EK 1.7.A.2 says
periodicity is predicted by and what neither of the other two topics uses. No
item here reads a spectrum, and no item here asks for a configuration to be
written out.

ON THE DATA, AND ON THE TWO DIPS. The period 3 ionization energy table is
printed COMPLETE, including the two places where the value falls rather than
rises. Trimming those rows would have made a cleaner-looking trend and taught a
falsehood: EK 1.7.A.1 traces recurring properties to completely or partially
filled shells AND SUBSHELLS, which is exactly where those two departures come
from. So the items ask what the data support -- which element is largest, and
whether the trend rises overall -- and never ask a student to interpolate
across a dip. Every other table used for a prediction item (items 9, 21, 27) is
checked to be strictly monotonic before an estimate is keyed to it.

ON THE EXCLUSION. No item writes or asks for the configuration of an element
that is an exception to the Aufbau principle; chromium and copper appear
nowhere in this module.

NOTATION. Plain prose with tabulated numbers. Element symbols and ion charges
are written out in words or as plain text (a sodium ion, a chloride ion), never
as a superscript outside a span.
"""
TOPIC = ("1.7", "Periodic Trends", 1)

_T_RAD_PERIOD = dict(
    headers=["Element (second row, left to right)", "Atomic radius (picometers)"],
    rows=[["Lithium", "152"], ["Beryllium", "112"], ["Boron", "85"],
          ["Carbon", "77"], ["Nitrogen", "75"], ["Oxygen", "73"], ["Fluorine", "72"]])

_T_RAD_GROUP = dict(
    headers=["Element (first column, top to bottom)", "Atomic radius (picometers)"],
    rows=[["Lithium", "152"], ["Sodium", "186"], ["Potassium", "227"],
          ["Rubidium", "248"]])

_T_IE_GROUP = dict(
    headers=["Element (first column, top to bottom)",
             "First ionization energy (kilojoules per mole)"],
    rows=[["Lithium", "520"], ["Sodium", "496"], ["Potassium", "419"],
          ["Rubidium", "403"]])

_T_IE_GAP = dict(
    headers=["Element (first column, top to bottom)",
             "First ionization energy (kilojoules per mole)"],
    rows=[["Lithium", "520"], ["Sodium", "496"], ["Rubidium", "403"],
          ["Cesium", "376"]])

_T_IE_PERIOD3 = dict(
    headers=["Element (third row, left to right)",
             "First ionization energy (kilojoules per mole)"],
    rows=[["Sodium", "496"], ["Magnesium", "738"], ["Aluminum", "578"],
          ["Silicon", "786"], ["Phosphorus", "1012"], ["Sulfur", "1000"],
          ["Chlorine", "1251"], ["Argon", "1521"]])

_T_EN_PERIOD = dict(
    headers=["Element (third row, left to right)", "Electronegativity"],
    rows=[["Sodium", "0.9"], ["Magnesium", "1.2"], ["Aluminum", "1.5"],
          ["Silicon", "1.8"], ["Phosphorus", "2.1"], ["Sulfur", "2.5"],
          ["Chlorine", "3.0"]])

_T_EN_GROUP = dict(
    headers=["Element (seventeenth column, top to bottom)", "Electronegativity"],
    rows=[["Fluorine", "4.0"], ["Chlorine", "3.0"], ["Bromine", "2.8"],
          ["Iodine", "2.5"]])

_T_ISO = dict(
    headers=["Species", "Protons in the nucleus", "Electrons", "Radius (picometers)"],
    rows=[["Oxide ion", "8", "10", "140"], ["Fluoride ion", "9", "10", "133"],
          ["Sodium ion", "11", "10", "98"], ["Magnesium ion", "12", "10", "72"]])

_T_ATOM_ION = dict(
    headers=["Species", "Electrons", "Radius (picometers)"],
    rows=[["Sodium atom", "11", "186"], ["Sodium ion", "10", "98"],
          ["Chlorine atom", "17", "99"], ["Chloride ion", "18", "181"]])

_T_ZEFF = dict(
    headers=["Element (second row, left to right)", "Protons in the nucleus",
             "Core electrons", "Valence electrons"],
    rows=[["Lithium", "3", "2", "1"], ["Carbon", "6", "2", "4"],
          ["Oxygen", "8", "2", "6"], ["Fluorine", "9", "2", "7"]])

QUESTIONS = [

 dict(q="On what is the organization of the periodic table based?",
      choices=[
        "Patterns of recurring properties of the elements, which are explained by "
        "patterns of ground-state electron configurations and by which shells and "
        "subshells are completely or partially filled.",
        "The order in which the elements were discovered, so that older elements appear "
        "first.",
        "The masses of the elements alone, with no reference to their electrons.",
        "The number of neutrons in the most common isotope of each element.",
        "The temperature at which each element melts, with the lowest melting points "
        "placed together."],
      ans=0,
      why="EK 1.7.A.1, near verbatim: the organization of the periodic table is based on "
          "patterns of recurring properties of the elements, which are explained by "
          "patterns of ground-state electron configurations and the presence of "
          "completely or partially filled shells and subshells of electrons in atoms."),

 dict(q="Which set of properties does the framework list as showing periodicity that "
        "can be predicted from an element's position in the periodic table?",
      choices=[
        "Ionization energy, atomic and ionic radii, electron affinity, and "
        "electronegativity.",
        "Melting point, boiling point, density, and hardness.",
        "Atomic mass, isotopic abundance, molar mass, and formula mass.",
        "Bond length, bond energy, bond order, and molecular geometry.",
        "Specific heat capacity, thermal conductivity, color, and magnetic behavior."],
      ans=0,
      why="EK 1.7.A.2 names exactly these four: ionization energy, atomic and ionic "
          "radii, electron affinity, and electronegativity. The other lists contain "
          "real properties, but the framework does not assign their periodicity to this "
          "learning objective."),

 dict(q="The table gives the atomic radii of the elements of the second row of the "
        "periodic table, in order from left to right. What does the trend show?",
      table=_T_RAD_PERIOD,
      choices=[
        "The atomic radius decreases steadily from left to right across the row.",
        "The atomic radius increases steadily from left to right across the row.",
        "The atomic radius rises to a maximum in the middle of the row and then falls.",
        "The atomic radius is the same for every element in the row.",
        "The atomic radius changes without any consistent direction across the row."],
      ans=0,
      why="EK 1.7.A.2 makes atomic radius one of the properties whose trend is predicted "
          "by position in the table, and every tabulated value here is smaller than the "
          "one before it as the row is read from left to right."),

 dict(q="Why does the atomic radius decrease from left to right across a row of the "
        "periodic table?",
      choices=[
        "The nuclear charge rises while the added electrons enter the same shell, so "
        "the effective nuclear charge on the valence electrons rises and pulls them "
        "closer.",
        "Electrons are removed one at a time across the row, so fewer electrons occupy "
        "less space.",
        "A new shell is added at every step, and each new shell is smaller than the one "
        "before it.",
        "The number of neutrons rises, and neutrons attract electrons toward the "
        "nucleus.",
        "The shielding by core electrons increases sharply across the row and pulls the "
        "valence electrons inward."],
      ans=0,
      why="EK 1.7.A.2 says trends are understood qualitatively using Coulomb's law, the "
          "shell model, and the concepts of shielding and effective nuclear charge. "
          "Across a row the core stays the same while protons are added, so the "
          "effective nuclear charge grows and EK 1.5.A.2 makes the attraction stronger. "
          "Neutrons are uncharged by EK 1.5.A.1."),

 dict(q="The table gives the atomic radii of the elements of the first column of the "
        "periodic table, read from top to bottom. Which explanation of the trend is "
        "correct?",
      table=_T_RAD_GROUP,
      choices=[
        "The radius increases because each element down the column has its valence "
        "electron in a shell farther from the nucleus, shielded by more core electrons.",
        "The radius increases because each element down the column has fewer protons "
        "than the one above it.",
        "The radius decreases because the nuclear charge grows down the column.",
        "The radius increases because the valence electrons of every element in the "
        "column occupy the same shell.",
        "The radius stays the same because every element in the column has one valence "
        "electron."],
      ans=0,
      why="The tabulated radii grow down the column, and EK 1.7.A.2 explains such trends "
          "with the shell model, shielding and effective nuclear charge: a valence "
          "electron in a higher shell is farther out and screened by more core "
          "electrons, which by EK 1.5.A.2 weakens the attraction holding it in."),

 dict(q="The table gives first ionization energies for the elements of the first column "
        "of the periodic table, from top to bottom. What trend do the data show, and "
        "why?",
      table=_T_IE_GROUP,
      choices=[
        "The ionization energy falls down the column, because the valence electron lies "
        "farther from the nucleus and is more shielded.",
        "The ionization energy rises down the column, because each element has more "
        "protons than the one above it.",
        "The ionization energy falls down the column, because each element has fewer "
        "electrons than the one above it.",
        "The ionization energy is constant down the column, because every element has "
        "one valence electron.",
        "The ionization energy rises down the column, because the atoms become larger "
        "and hold their electrons better."],
      ans=0,
      why="Every tabulated value is smaller than the one above it, and EK 1.7.A.2 makes "
          "ionization energy one of the properties understood through Coulomb's law, "
          "the shell model and shielding: a more distant, better-screened valence "
          "electron is held less firmly and so comes off more easily."),

 dict(q="Using the tabulated first ionization energies for the third row of the periodic "
        "table, which element has the largest first ionization energy, and what is the "
        "overall pattern across the row?",
      table=_T_IE_PERIOD3,
      choices=[
        "Argon has the largest, and the values rise overall from left to right although "
        "not at every single step.",
        "Sodium has the largest, and the values fall steadily from left to right.",
        "Argon has the largest, and the values rise at every single step from left to "
        "right.",
        "Phosphorus has the largest, because it lies at the middle of the row.",
        "There is no overall pattern, because the values rise and fall without "
        "direction."],
      ans=0,
      why="The largest tabulated value belongs to the element farthest right, and the "
          "value at the right end is far above the value at the left end, so the row "
          "rises overall. Two steps in the table nevertheless go down, which is why the "
          "claim of a rise at every step is false on the same data."),

 dict(q="Two of the steps in that same table of first ionization energies go down "
        "rather than up. Which statement is the best account of why departures from a "
        "smooth trend are expected at all?",
      table=_T_IE_PERIOD3,
      choices=[
        "Recurring properties are explained by which shells and subshells are "
        "completely or partially filled, so the trend can break where a subshell is "
        "newly begun or newly half filled.",
        "Departures are measurement errors and have no chemical explanation.",
        "Departures occur wherever a new shell begins, which happens twice within a "
        "single row.",
        "Departures occur because the number of neutrons does not increase regularly "
        "across a row.",
        "Departures show that ionization energy is not actually a periodic property."],
      ans=0,
      why="EK 1.7.A.1 traces recurring properties to patterns of ground-state electron "
          "configurations AND to the presence of completely or partially filled shells "
          "and subshells, which is what makes a subshell boundary a place where a trend "
          "can break. A new shell begins only at the start of a row, so it cannot "
          "explain a break inside one."),

 dict(q="The table omits potassium, which sits between sodium and rubidium in the first "
        "column. Using periodicity, which is the best estimate of the first ionization "
        "energy of potassium?",
      table=_T_IE_GAP,
      choices=[
        "About 420 kilojoules per mole, between the values for sodium and rubidium.",
        "About 560 kilojoules per mole, above the value for sodium.",
        "About 350 kilojoules per mole, below the value for cesium.",
        "About 900 kilojoules per mole, since potassium is a larger atom.",
        "No estimate is possible, because the value has not been measured."],
      ans=0,
      why="EK 1.7.A.3 states that periodicity is useful to predict or estimate values of "
          "properties in the absence of data, and the tabulated column falls steadily "
          "from top to bottom, so a missing member must lie between its neighbors. Any "
          "estimate outside that interval contradicts the trend the table itself shows."),

 dict(q="An element's ion has a smaller radius than the neutral atom it came from. What "
        "kind of ion is it, and why?",
      table=_T_ATOM_ION,
      choices=[
        "A positive ion, because losing an electron leaves the same nuclear charge "
        "acting on fewer electrons, drawing them in.",
        "A negative ion, because gaining an electron adds mass and compresses the atom.",
        "A positive ion, because losing an electron also removes a proton from the "
        "nucleus.",
        "A negative ion, because the added electron enters an inner shell.",
        "Either kind of ion, because the charge has no bearing on radius."],
      ans=0,
      why="The tabulated radii show the species with fewer electrons than its atom to be "
          "the smaller one and the species with more electrons to be the larger. EK "
          "1.7.A.2 lists ionic radius among the periodic properties, and EK 1.5.A.2 "
          "supplies the reason: an unchanged nuclear charge shared among fewer electrons "
          "pulls each one harder."),

 dict(q="Using the same table, why is the chloride ion so much larger than the chlorine "
        "atom?",
      table=_T_ATOM_ION,
      choices=[
        "The added electron increases the repulsion among the electrons while the "
        "nuclear charge stays the same, so the electron cloud expands.",
        "The added electron increases the nuclear charge, which pushes the other "
        "electrons outward.",
        "The added electron occupies an entirely new shell farther from the nucleus.",
        "The added electron removes the shielding provided by the core electrons.",
        "The added electron increases the mass of the ion, and heavier species are "
        "always larger."],
      ans=0,
      why="The tabulated radius rises when an electron is added at unchanged nuclear "
          "charge. EK 1.7.A.2 explains ionic radius through Coulomb's law and the shell "
          "model, and adding an electron to a partly filled subshell does not open a new "
          "shell; it spreads the same nuclear attraction over one more electron."),

 dict(q="The four species in the table all have ten electrons. What accounts for the "
        "order of their radii?",
      table=_T_ISO,
      choices=[
        "The radius falls as the number of protons rises, because a larger nuclear "
        "charge draws the same ten electrons in more tightly.",
        "The radius falls as the number of protons rises, because the extra protons "
        "occupy space inside the ion.",
        "The radius rises as the number of protons rises, because more protons repel "
        "one another.",
        "The radius depends only on the charge of the ion and not on the nuclear charge.",
        "The four radii should be equal, because all four species have the same number "
        "of electrons."],
      ans=0,
      why="Every species has the same electron count, so the electron count cannot "
          "explain the difference, and the tabulated radius falls as the tabulated "
          "proton count rises. EK 1.5.A.2 makes a larger positive charge a stronger "
          "attraction, and EK 1.7.A.2 lists ionic radius among the periodic properties."),

 dict(q="What is meant by the effective nuclear charge experienced by a valence "
        "electron?",
      choices=[
        "The net attraction it feels from the nucleus once the screening effect of the "
        "other electrons is taken into account.",
        "The total number of protons in the nucleus, with no correction of any kind.",
        "The charge on the ion the atom will form when it reacts.",
        "The total charge of all the electrons in the atom taken together.",
        "The number of neutrons in the nucleus, since neutrons dilute the nuclear "
        "charge."],
      ans=0,
      why="EK 1.7.A.2 names shielding and effective nuclear charge as the concepts "
          "through which the trends are understood, and shielding is what separates the "
          "effective charge from the bare proton count. Neutrons carry no charge by EK "
          "1.5.A.1 and so do not enter."),

 dict(q="The table lists the proton count and the numbers of core and valence electrons "
        "for four elements of the second row. Which element's valence electrons "
        "experience the largest effective nuclear charge?",
      table=_T_ZEFF,
      choices=["Fluorine", "Lithium", "Carbon", "Oxygen",
               "All four are equal, because all four have the same number of core "
               "electrons"],
      ans=0,
      why="The tabulated core electron count is the same for every row, so the screening "
          "is comparable and the effective nuclear charge rises with the proton count. "
          "That is the qualitative reasoning EK 1.7.A.2 prescribes, and the constant "
          "core is what makes it valid here."),

 dict(q="The table gives electronegativity values across the third row of the periodic "
        "table. What trend do they show?",
      table=_T_EN_PERIOD,
      choices=[
        "Electronegativity increases from left to right across the row.",
        "Electronegativity decreases from left to right across the row.",
        "Electronegativity is highest in the middle of the row.",
        "Electronegativity is the same for every element in the row.",
        "Electronegativity increases and then decreases across the row."],
      ans=0,
      why="EK 1.7.A.2 lists electronegativity among the properties whose periodicity is "
          "predicted by position in the table, and every tabulated value here exceeds "
          "the one to its left."),

 dict(q="The table gives electronegativity values down the seventeenth column of the "
        "periodic table. Which statement about the trend and its cause is correct?",
      table=_T_EN_GROUP,
      choices=[
        "Electronegativity falls down the column, because the bonding electrons are "
        "held farther from the nucleus and are more shielded.",
        "Electronegativity rises down the column, because the nuclear charge grows.",
        "Electronegativity falls down the column, because the atoms have fewer valence "
        "electrons lower down.",
        "Electronegativity is unchanged down the column, because every element in it "
        "has seven valence electrons.",
        "Electronegativity rises down the column, because larger atoms attract "
        "electrons more strongly."],
      ans=0,
      why="Every tabulated value is smaller than the one above it, and EK 1.7.A.2 has "
          "the trend understood through Coulomb's law, the shell model and shielding: "
          "greater distance and more screening weaken the pull on a shared electron. "
          "Every element in the column has the same number of valence electrons, which "
          "is why that cannot be the cause."),

 dict(q="Two elements sit in the same row of the periodic table, one near the left edge "
        "and one near the right edge. Which is expected to have the larger first "
        "ionization energy, and why?",
      choices=[
        "The one on the right, because its valence electrons feel a larger effective "
        "nuclear charge at a comparable distance.",
        "The one on the left, because it has fewer electrons in total to hold on to.",
        "The one on the left, because it has more shells of electrons.",
        "The one on the right, because it has more neutrons in its nucleus.",
        "Neither, because ionization energy depends only on which row an element "
        "occupies."],
      ans=0,
      why="EK 1.7.A.2 makes ionization energy predictable from position and understood "
          "through effective nuclear charge and the shell model. Across a row the "
          "valence shell does not change while protons are added, so the effective "
          "charge rises and, by EK 1.5.A.2, the valence electron is held more firmly."),

 dict(q="Why do the elements of a single column of the periodic table show similar "
        "chemical behavior?",
      choices=[
        "Because they have the same number of valence electrons, so their ground-state "
        "configurations repeat the same outer pattern.",
        "Because they have the same number of protons in their nuclei.",
        "Because they have the same total number of electrons.",
        "Because they have the same atomic radius.",
        "Because they have the same number of neutrons in their most common isotopes."],
      ans=0,
      why="EK 1.7.A.1 traces the recurring properties on which the table is organized to "
          "patterns of ground-state electron configurations, and it is the outer part of "
          "that pattern that repeats down a column. Proton and electron totals differ "
          "from one member of a column to the next."),

 dict(q="Electron affinity concerns the energy change when an atom gains an electron. "
        "Based on periodicity, which element would be expected to release the most "
        "energy on gaining one electron?",
      choices=[
        "An element near the right of a row, one electron short of a filled subshell.",
        "An element at the far left of a row, with one valence electron.",
        "An element in the middle of a row, with a half-filled subshell.",
        "An element in the last column of a row, with a completely filled subshell.",
        "The elements of a row are all alike in this respect, since electron affinity "
        "does not vary with position."],
      ans=0,
      why="EK 1.7.A.2 lists electron affinity among the properties predicted by position "
          "and understood through effective nuclear charge, and EK 1.7.A.1 makes a "
          "completely filled subshell part of the explanation of recurring properties. "
          "An atom that both feels a large effective nuclear charge and can complete a "
          "subshell releases the most on gaining an electron; one whose subshells are "
          "already complete has nowhere to put it."),

 dict(q="A newly synthesized element is placed below cesium in the first column of the "
        "periodic table, and no measurement of its atomic radius exists. Using the "
        "tabulated radii, what can reasonably be said about it?",
      table=_T_RAD_GROUP,
      choices=[
        "Its atomic radius should be larger than that of every element listed, since "
        "the radius grows steadily down this column.",
        "Its atomic radius should be smaller than that of every element listed, since "
        "heavier atoms are more compact.",
        "Its atomic radius should equal that of rubidium, since both lie in the same "
        "column.",
        "Its atomic radius should lie between those of lithium and sodium.",
        "Nothing can be said, since periodicity does not permit estimates without "
        "measurements."],
      ans=0,
      why="EK 1.7.A.3 states that periodicity is useful to predict or estimate values of "
          "properties in the absence of data, and the tabulated column rises steadily "
          "from top to bottom, so an element placed below the last one should continue "
          "that rise."),

 dict(q="A student says that atomic radius must increase from left to right across a "
        "row, because electrons are being added and more electrons take up more room. "
        "Using the tabulated radii, evaluate the claim.",
      table=_T_RAD_PERIOD,
      choices=[
        "The claim is wrong: the tabulated radii shrink across the row, because the "
        "added electrons enter the same shell while the nuclear charge grows.",
        "The claim is right: the tabulated radii grow across the row, as the student "
        "predicted.",
        "The claim is wrong: the tabulated radii shrink because electrons are removed "
        "rather than added across a row.",
        "The claim is right in direction but wrong in magnitude, since the radii grow "
        "only very slightly.",
        "The claim cannot be evaluated, since atomic radius is not a periodic property."],
      ans=0,
      why="The tabulated values fall from left to right, so the prediction is refuted by "
          "the data itself. EK 1.7.A.2 supplies the correct reasoning: the added "
          "electrons go into the SAME shell while protons accumulate, so the effective "
          "nuclear charge rises and pulls the shell inward."),

 dict(q="Why does the effective nuclear charge experienced by a valence electron rise "
        "much more sharply across a row than it does down a column?",
      choices=[
        "Because across a row protons are added while the core that screens them stays "
        "the same, whereas down a column each new shell brings a larger screening core "
        "as well as more protons.",
        "Because across a row the number of neutrons rises faster than down a column.",
        "Because down a column the nuclear charge does not change at all.",
        "Because across a row the valence electrons are removed one at a time.",
        "Because down a column the valence electrons enter the same shell each time."],
      ans=0,
      why="EK 1.7.A.2 has these trends understood through shielding and effective "
          "nuclear charge. Along a row the screening core is unchanged, so each added "
          "proton is felt almost fully; down a column the added protons arrive together "
          "with a larger core, and the valence shell moves outward as well."),

 dict(q="Which of the following pairs is correctly ordered by increasing atomic radius, "
        "given that both elements lie in the same row of the periodic table and that "
        "the second lies to the left of the first?",
      choices=[
        "The element on the right is smaller, so the pair runs from the right-hand "
        "element to the left-hand one.",
        "The element on the right is larger, so the pair runs from the left-hand "
        "element to the right-hand one.",
        "The two are equal in radius, since they occupy the same row.",
        "The order depends on how many neutrons each nucleus contains.",
        "The order cannot be predicted from position within a row."],
      ans=0,
      why="EK 1.7.A.2 makes atomic radius predictable from position, and the radius "
          "shrinks from left to right along a row as the effective nuclear charge rises "
          "on an unchanged valence shell. Ordering by increasing radius therefore runs "
          "from right to left."),

 dict(q="Which of these comparisons of ionization energy is correctly explained by "
        "Coulomb's law and the shell model?",
      choices=[
        "The element lower in a column has the smaller first ionization energy, because "
        "its valence electron sits farther from the nucleus.",
        "The element lower in a column has the larger first ionization energy, because "
        "it has more protons.",
        "The element farther left in a row has the larger first ionization energy, "
        "because it has fewer electrons.",
        "Two elements in different rows and different columns cannot be compared at all.",
        "Ionization energy depends on the number of neutrons, so no comparison based on "
        "position is valid."],
      ans=0,
      why="EK 1.7.A.2 has ionization energy predicted by position and understood through "
          "Coulomb's law, the shell model and shielding. Down a column the valence "
          "electron occupies a shell farther out and is better screened, and by EK "
          "1.5.A.2 a greater separation means a weaker hold."),

 dict(q="An element has not yet been isolated in quantity, so none of its atomic "
        "properties has been measured. Which of the following does the framework say "
        "periodicity is useful for in that situation?",
      choices=[
        "Predicting or estimating values of its properties in the absence of data.",
        "Determining the exact values of its properties without any uncertainty.",
        "Establishing how many isotopes of the element exist in nature.",
        "Deciding whether the element can be synthesized at all.",
        "Nothing, since periodicity applies only to elements whose properties are "
        "already known."],
      ans=0,
      why="EK 1.7.A.3, near verbatim: the periodicity is useful to predict or estimate "
          "values of properties in the absence of data. An estimate is not an exact "
          "value, and isotopic abundance is what a mass spectrum supplies under EK "
          "1.2.A.1."),

 dict(q="Two atoms in the same row of the periodic table are compared. The first is "
        "described as having a larger effective nuclear charge acting on its valence "
        "electrons. Which set of properties should the first atom show, relative to the "
        "second?",
      choices=[
        "A smaller atomic radius and a larger first ionization energy.",
        "A larger atomic radius and a larger first ionization energy.",
        "A smaller atomic radius and a smaller first ionization energy.",
        "A larger atomic radius and a smaller first ionization energy.",
        "The same radius and the same first ionization energy, since both lie in one "
        "row."],
      ans=0,
      why="EK 1.7.A.2 makes both properties functions of the same underlying attraction, "
          "and EK 1.5.A.2 makes a larger effective charge a stronger pull. A stronger "
          "pull draws the valence shell in and makes an electron harder to remove, so "
          "the two properties must move in opposite directions."),

 dict(q="The table gives electronegativities for four members of the seventeenth column. "
        "A fifth member lies below iodine and has not been measured. What is the best "
        "estimate of its electronegativity?",
      table=_T_EN_GROUP,
      choices=[
        "Below 2.5, continuing the fall down the column.",
        "Above 4.0, since it is the heaviest member of the column.",
        "Exactly 2.5, since the values level off at the bottom of a column.",
        "Between 2.8 and 3.0, since the last two values are close together.",
        "No estimate is justified, since electronegativity is not periodic."],
      ans=0,
      why="EK 1.7.A.3 licenses an estimate in the absence of data, and every tabulated "
          "value falls below the one above it, so continuing the column downward "
          "continues the fall. Any estimate that reverses the direction the table shows "
          "contradicts the data used to make it."),

 dict(q="A sodium ion and a magnesium ion both have ten electrons, but the magnesium ion "
        "is smaller. Which statement explains this without appealing to the number of "
        "electrons?",
      table=_T_ISO,
      choices=[
        "The magnesium ion has one more proton, so the same ten electrons feel a "
        "stronger attraction and are drawn closer.",
        "The magnesium ion has one fewer proton, so it holds its electrons in a tighter "
        "shell.",
        "The magnesium ion carries a larger charge, and charge itself occupies less "
        "volume.",
        "The magnesium ion has fewer core electrons, so there is less to shield.",
        "The magnesium ion has more neutrons, and neutrons pull the electrons inward."],
      ans=0,
      why="The tabulated electron counts are identical, so the difference must come from "
          "the nucleus, and the tabulated proton counts differ by one. EK 1.5.A.2 makes "
          "the larger positive charge a stronger attraction on the same electrons, and "
          "neutrons are uncharged by EK 1.5.A.1."),

 dict(q="Which observation would most directly support the claim that the properties "
        "used to organize the periodic table are RECURRING rather than simply "
        "increasing with atomic number?",
      choices=[
        "A property rises across one row, drops sharply at the start of the next, and "
        "then rises across that row as well.",
        "A property rises steadily with atomic number from the first element to the "
        "last.",
        "A property has the same value for every element in the table.",
        "A property varies from sample to sample of the same element.",
        "A property depends on the number of neutrons rather than the number of "
        "protons."],
      ans=0,
      why="EK 1.7.A.1 bases the table's organization on patterns of RECURRING "
          "properties, explained by the repeating pattern of ground-state "
          "configurations. A quantity that resets at the start of each row and then "
          "repeats its behavior is exactly what recurrence looks like, while a quantity "
          "rising monotonically with atomic number shows no recurrence at all."),

 dict(q="Two elements lie in the same column, one directly above the other. Which "
        "comparison of their valence electrons is correct?",
      choices=[
        "Both have the same number of valence electrons, but the lower element's are in "
        "a shell farther from the nucleus.",
        "Both have the same number of valence electrons in the same shell.",
        "The lower element has more valence electrons, in a shell farther from the "
        "nucleus.",
        "The lower element has fewer valence electrons, which is why it is more "
        "reactive.",
        "The comparison depends on the number of neutrons in each nucleus."],
      ans=0,
      why="EK 1.7.A.1 traces the table's columns to repeating patterns of ground-state "
          "configurations, which is what gives members of one column the same valence "
          "count, while each successive member of a column occupies one more shell. EK "
          "1.7.A.2 then uses that greater distance to explain the property trends down "
          "the column."),
]
