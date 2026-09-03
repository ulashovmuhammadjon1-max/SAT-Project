r"""AP CHEMISTRY 1.2 Mass Spectra of Elements.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.2.A: explain the quantitative relationship between the
mass spectrum of an element and the masses of the element's isotopes.
Suggested skill 5.D, identify information presented graphically to solve a
problem.

Essential knowledge relied on, in the framework's own words:

  1.2.A.1  The mass spectrum of a sample containing a single element can be
           used to determine the identity of the isotopes of that element and
           the relative abundance of each isotope in nature.
  1.2.A.2  The average atomic mass of an element can be estimated from the
           weighted average of the isotopic masses using the mass of each
           isotope and its relative abundance.

           Exclusion Statement: Interpreting mass spectra of samples containing
           multiple elements or peaks arising from species other than singly
           charged monatomic ions will not be assessed on the AP Exam.

ON THE EXCLUSION. Every spectrum in this topic is of a sample containing a
single element, and every peak is stated to be a singly charged monatomic ion.
No item asks a student to disentangle two elements or to reason about a
fragment or a doubly charged peak. That is the framework's boundary and it is
kept.

ON FIGURES. SCIENCE_BRIEF.md forbids referring to a picture the bank cannot
show, and a mass spectrum is a picture. Every spectrum here is therefore
printed as a table of mass-to-charge ratio against relative peak height, and
each item asks its question of the table. Nothing says "the spectrum shown".

ON ISOTOPES AND NEUTRONS. Item 17 is the only place the bank says what makes
two isotopes differ. It chains EK 1.2.A.1, which puts several isotopes of one
element in one spectrum at different masses, to EK 1.5.A.1, which states that
the nucleus is made of protons and neutrons. The number of protons fixes the
element, so a mass difference within one element has to sit in the neutrons.
Both codes are cited in the claim.

NOTATION. Hand-written spans per SCIENCE_BRIEF.md; percentages and masses are
plain prose, and only genuine scientific notation is typeset.
"""
TOPIC = ("1.2", "Mass Spectra of Elements", 1)

_H = ["Mass-to-charge ratio of the peak", "Relative peak height (percent of all peaks)"]

_T_X = dict(headers=_H, rows=[["10.0", "20.0"], ["11.0", "80.0"]])

_T_Q = dict(headers=_H, rows=[["24.0", "79.0"], ["25.0", "10.0"], ["26.0", "11.0"]])

_T_CU = dict(headers=_H, rows=[["63.0", "69.0"], ["65.0", "31.0"]])

_T_CL = dict(headers=_H, rows=[["35.0", "75.0"], ["37.0", "25.0"]])

_T_LI = dict(headers=_H, rows=[["6.0", "7.5"], ["7.0", "92.5"]])

_T_BR = dict(headers=_H, rows=[["79.0", "50.0"], ["81.0", "50.0"]])

_T_SI = dict(headers=_H, rows=[["28.0", "92.0"], ["29.0", "5.0"], ["30.0", "3.0"]])

_T_HEIGHTS = dict(
    headers=["Mass-to-charge ratio of the peak", "Peak height (arbitrary units)"],
    rows=[["20.0", "3.00"], ["22.0", "1.00"]])

_T_TWO = dict(
    headers=["Element", "Mass-to-charge ratio of the peak",
             "Relative peak height (percent of that element's peaks)"],
    rows=[["Element G", "69.0", "60.0"],
          ["Element G", "71.0", "40.0"],
          ["Element J", "107.0", "50.0"],
          ["Element J", "109.0", "50.0"]])

_T_CANDIDATES = dict(
    headers=["Candidate element", "Average atomic mass (atomic mass units)"],
    rows=[["Candidate 1", "10.8"], ["Candidate 2", "24.3"], ["Candidate 3", "35.5"],
          ["Candidate 4", "63.5"], ["Candidate 5", "80.0"]])

_T_THREE_SPECTRA = dict(
    headers=["Spectrum", "Lighter peak: mass and relative height",
             "Heavier peak: mass and relative height"],
    rows=[["Spectrum 1", "6.0 at 7.5 percent", "7.0 at 92.5 percent"],
          ["Spectrum 2", "63.0 at 69.0 percent", "65.0 at 31.0 percent"],
          ["Spectrum 3", "35.0 at 75.0 percent", "37.0 at 25.0 percent"]])

QUESTIONS = [

 dict(q="A sample containing a single element is analyzed and every peak recorded is a "
        "singly charged monatomic ion. Which two pieces of information about the "
        "element can the resulting mass spectrum supply?",
      choices=[
        "The identity of the isotopes of that element and the relative abundance of "
        "each isotope in nature.",
        "The number of valence electrons of the element and the charge it forms in "
        "ionic compounds.",
        "The identity of the element and the temperature at which the sample was "
        "vaporized.",
        "The number of covalent bonds the element forms and the geometry of the "
        "resulting molecule.",
        "The volume occupied by one mole of the element and the density of the solid."],
      ans=0,
      why="EK 1.2.A.1 states that the mass spectrum of a sample containing a single "
          "element can be used to determine the identity of the isotopes of that "
          "element and the relative abundance of each isotope in nature. Nothing about "
          "bonding, geometry or bulk properties is available from it."),

 dict(q="The table records the mass spectrum of a sample of element X, in which every "
        "peak is a singly charged monatomic ion. What is the average atomic mass of "
        "element X?",
      table=_T_X,
      choices=["10.8 atomic mass units", "10.5 atomic mass units",
               "11.0 atomic mass units", "10.2 atomic mass units",
               "21.0 atomic mass units"],
      ans=0,
      why="EK 1.2.A.2 defines the average atomic mass as the weighted average of the "
          "isotopic masses using each mass and its relative abundance, so the value is "
          "0.200 times 10.0 plus 0.800 times 11.0. Averaging the two masses without "
          "weighting them gives the rejected 10.5."),

 dict(q="Element Q gives the mass spectrum recorded in the table. Which isotope of "
        "element Q is the most abundant in nature?",
      table=_T_Q,
      choices=["The isotope of mass 24.0, whose peak is the tallest",
               "The isotope of mass 26.0, whose peak is the tallest",
               "The isotope of mass 25.0, because it lies between the other two",
               "The isotope of mass 26.0, because the heaviest isotope is always the "
               "most abundant",
               "The three isotopes are equally abundant, because each produces a peak"],
      ans=0,
      why="EK 1.2.A.1 makes the spectrum a record of the relative abundance of each "
          "isotope in nature, and the tabulated height of that abundance is largest "
          "for the lightest of the three peaks here. Nothing makes the heaviest "
          "isotope the most common."),

 dict(q="A student is shown the tabulated spectrum of element Z below and is asked, "
        "without doing any arithmetic, where the average atomic mass must lie. Which "
        "answer is correct and correctly reasoned?",
      table=_T_CU,
      choices=[
        "Between 63.0 and 65.0 but nearer 63.0, because the lighter isotope is the "
        "more abundant of the two.",
        "Between 63.0 and 65.0 but nearer 65.0, because the heavier isotope always "
        "contributes more mass.",
        "Exactly 64.0, because that is the midpoint of the two isotopic masses.",
        "Below 63.0, because averaging always lowers a set of values.",
        "Above 65.0, because the abundances add to more than one hundred."],
      ans=0,
      why="A weighted average as defined in EK 1.2.A.2 is pulled toward the value "
          "carrying the greater weight, so the more abundant isotope determines which "
          "end of the range the answer sits near. The midpoint answer is the "
          "unweighted average, which the framework does not use."),

 dict(q="How many different isotopes of element Q are present in the sample whose "
        "spectrum is recorded in this table, and what feature of the data shows it?",
      table=_T_Q,
      choices=["Three, because the sample gives three separate peaks",
               "Two, because only two of the peaks are tall enough to matter",
               "One, because the sample contains a single element",
               "Six, because each isotope produces two peaks",
               "The number cannot be determined from relative heights alone"],
      ans=0,
      why="EK 1.2.A.1 makes each peak in a single-element spectrum the record of one "
          "isotope, so the count of peaks is the count of isotopes. The stem states "
          "the sample holds one element, which fixes the number of elements and not "
          "the number of isotopes."),

 dict(q="Using the tabulated spectrum of element R, calculate the average atomic mass "
        "of the element.",
      table=_T_CL,
      choices=["35.5 atomic mass units", "36.0 atomic mass units",
               "35.0 atomic mass units", "36.5 atomic mass units",
               "72.0 atomic mass units"],
      ans=0,
      why="EK 1.2.A.2's weighted average is 0.750 times 35.0 plus 0.250 times 37.0. "
          "The unweighted mean of the two isotopic masses would be the rejected 36.0, "
          "and summing the masses gives the rejected 72.0."),

 dict(q="Most elements have an average atomic mass that is not close to a whole "
        "number. Which explanation best accounts for this?",
      choices=[
        "The value is a weighted average over isotopes of different masses, so it "
        "generally falls between whole-number isotopic masses rather than on one.",
        "Every atom of an element has a slightly different mass, so no whole number "
        "could describe the element.",
        "The mass of an atom changes continuously as the sample is heated in the "
        "instrument.",
        "Atomic masses are measured in grams, which never give whole numbers for "
        "single atoms.",
        "The electrons contribute a fractional amount of mass that varies from atom to "
        "atom."],
      ans=0,
      why="EK 1.2.A.2 defines the reported average atomic mass as a weighted average of "
          "the isotopic masses, and a weighted average of two or more different values "
          "lands between them unless one abundance is one hundred percent."),

 dict(q="An element has exactly two isotopes, of masses 35.0 and 37.0 atomic mass "
        "units, and its average atomic mass is reported as 35.5 atomic mass units. "
        "What does that value alone establish about the two abundances?",
      choices=[
        "The isotope of mass 35.0 is the more abundant, because the average lies much "
        "nearer its mass.",
        "The isotope of mass 37.0 is the more abundant, because the average lies above "
        "35.0.",
        "The two isotopes are present in equal amounts, because the average lies "
        "between them.",
        "The abundances cannot be compared without knowing the size of the sample.",
        "The isotope of mass 37.0 is the more abundant, because heavier isotopes are "
        "always favored in nature."],
      ans=0,
      why="A weighted average under EK 1.2.A.2 sits closer to the mass carrying the "
          "larger weight, and 35.5 is one quarter of the way from 35.0 to 37.0. Sample "
          "size cancels out of a weighted average, so it is not needed."),

 dict(q="In a mass spectrum of a single element, what does the height of a peak "
        "represent?",
      choices=[
        "The relative abundance in nature of the isotope that produced the peak.",
        "The mass of the isotope that produced the peak.",
        "The charge carried by the ion that produced the peak.",
        "The energy required to remove an electron from that isotope.",
        "The number of protons in the nucleus of that isotope."],
      ans=0,
      why="EK 1.2.A.1 states that the spectrum determines the identity of the isotopes "
          "and the relative abundance of each. The position of a peak carries the mass "
          "information; its height carries the abundance information."),

 dict(q="Element T gives the tabulated spectrum below. What is the average atomic mass "
        "of element T?",
      table=_T_LI,
      choices=["6.9 atomic mass units", "6.5 atomic mass units",
               "6.1 atomic mass units", "7.0 atomic mass units",
               "13.0 atomic mass units"],
      ans=0,
      why="The weighted average of EK 1.2.A.2 is 0.075 times 6.0 plus 0.925 times 7.0, "
          "which is 6.925 and rounds to 6.9. Because the heavier isotope carries almost "
          "all the abundance, the answer must sit just below 7.0."),

 dict(q="A sample of a single element gives two peaks of exactly equal height, at 79.0 "
        "and 81.0 atomic mass units. What is the average atomic mass of this element?",
      table=_T_BR,
      choices=["80.0 atomic mass units", "79.0 atomic mass units",
               "81.0 atomic mass units", "160.0 atomic mass units",
               "The value cannot be found, because neither isotope is more abundant"],
      ans=0,
      why="When the weights in EK 1.2.A.2's weighted average are equal, the weighted "
          "average reduces to the ordinary mean of the two isotopic masses. Equal "
          "abundances make the calculation easier, not impossible."),

 dict(q="The abundances of the two isotopes of an element are reported as fractions "
        "rather than percentages: 0.600 at 69.0 atomic mass units and 0.400 at 71.0 "
        "atomic mass units. What is the average atomic mass?",
      choices=["69.8 atomic mass units", "70.0 atomic mass units",
               "70.2 atomic mass units", "69.0 atomic mass units",
               "140.0 atomic mass units"],
      ans=0,
      why="EK 1.2.A.2's weighted average takes the same form whether the weights are "
          "written as fractions or percentages: 0.600 times 69.0 plus 0.400 times 71.0 "
          "is 69.8. Swapping the two weights gives the rejected 70.2."),

 dict(q="An element has three isotopes with masses \\(m_1\\), \\(m_2\\) and \\(m_3\\) "
        "and fractional abundances \\(f_1\\), \\(f_2\\) and \\(f_3\\) that sum to one. "
        "Which expression gives the average atomic mass?",
      choices=[
        "\\(f_1 m_1 + f_2 m_2 + f_3 m_3\\)",
        "\\(\\frac{m_1 + m_2 + m_3}{3}\\)",
        "\\(\\frac{f_1 + f_2 + f_3}{m_1 + m_2 + m_3}\\)",
        "\\((m_1 + m_2 + m_3)(f_1 + f_2 + f_3)\\)",
        "\\(\\frac{m_1}{f_1} + \\frac{m_2}{f_2} + \\frac{m_3}{f_3}\\)"],
      ans=0,
      why="EK 1.2.A.2 defines the average atomic mass as the weighted average of the "
          "isotopic masses using the mass of each isotope and its relative abundance, "
          "which is the sum of each mass multiplied by its own fractional abundance. "
          "The unweighted mean discards the abundance data entirely."),

 dict(q="A second sample of the same element is found in which the heavier isotope is "
        "more abundant than it was in the first sample, while the isotopic masses are "
        "unchanged. Compared with the first sample, the average atomic mass calculated "
        "from the second spectrum will be",
      choices=[
        "larger, because more of the weight in the average now sits on the larger mass.",
        "smaller, because a larger abundance always divides the average by a larger "
        "number.",
        "unchanged, because the isotopic masses themselves have not changed.",
        "unchanged, because average atomic mass is a property of the element and never "
        "of the sample.",
        "impossible to compare without knowing the total mass of each sample."],
      ans=0,
      why="In the weighted average of EK 1.2.A.2 each isotopic mass is multiplied by "
          "its own abundance, so shifting weight onto the heavier isotope raises the "
          "result. The rejected options treat the abundances as if they did not enter "
          "the calculation."),

 dict(q="The table records the spectra of two separate single-element samples. Which "
        "element has the larger average atomic mass, and how can that be seen without "
        "completing both calculations?",
      table=_T_TWO,
      choices=[
        "Element J, because both of its peaks lie at higher mass than either peak of "
        "element G.",
        "Element G, because its two peaks differ more in relative height than element "
        "J's do.",
        "Element G, because its most abundant peak carries the larger share of the "
        "total.",
        "Element J, because equal abundances always produce a larger weighted average "
        "than unequal ones.",
        "The two averages must be equal, because each element contributes two peaks."],
      ans=0,
      why="A weighted average under EK 1.2.A.2 always lies between the smallest and "
          "largest value being averaged, so an element whose isotopic masses are all "
          "larger must have the larger average. Relative heights decide where in a "
          "range the average sits, not which range it sits in."),

 dict(q="A student calculates an average atomic mass of 24.3 atomic mass units from a "
        "single-element spectrum and wants to identify the element. Using the table of "
        "candidates, which is the best match?",
      table=_T_CANDIDATES,
      choices=["Candidate 2", "Candidate 1", "Candidate 3", "Candidate 4",
               "Candidate 5"],
      ans=0,
      why="EK 1.2.A.2 makes the weighted average of the isotopic masses an estimate of "
          "the element's average atomic mass, so the identification is made by matching "
          "that computed value against the tabulated averages."),

 dict(q="Two peaks in a single-element spectrum lie at different mass-to-charge ratios, "
        "and both arise from singly charged monatomic ions. What must differ between "
        "the two kinds of atom that produced them?",
      choices=[
        "The number of neutrons in the nucleus, since the number of protons fixes which "
        "element it is.",
        "The number of protons in the nucleus, since protons carry nearly all the mass.",
        "The number of electrons outside the nucleus, since electrons determine the "
        "mass of an atom.",
        "The charge on the ion, since a heavier particle must carry a larger charge.",
        "Nothing at all, since all atoms of one element are identical in every respect."],
      ans=0,
      why="EK 1.2.A.1 places several isotopes of one element at different masses in one "
          "spectrum, and EK 1.5.A.1 states that the nucleus is made of protons and "
          "neutrons. Since the proton count is what makes the sample a single element, "
          "the mass difference has to lie in the neutrons; the stem fixes the charge as "
          "the same for both peaks."),

 dict(q="In the sample whose spectrum is tabulated here, about how many atoms out of "
        "every one thousand are the isotope of mass 25.0?",
      table=_T_Q,
      choices=["About 100 atoms", "About 10 atoms", "About 250 atoms",
               "About 790 atoms", "About 1 atom"],
      ans=0,
      why="EK 1.2.A.1 makes the tabulated height the relative abundance of that isotope "
          "in nature, and ten percent of one thousand atoms is one hundred. Reading the "
          "percentage as a count directly gives the rejected value of ten."),

 dict(q="For any mass spectrum of a sample of a single element in which relative "
        "abundances are reported as percentages, what must be true of those "
        "percentages?",
      choices=[
        "They must add to one hundred percent across all the peaks of that element.",
        "They must each be larger than fifty percent, since every isotope is common.",
        "They must be equal to one another, since all isotopes of an element behave "
        "alike.",
        "They must add to the average atomic mass of the element.",
        "They must decrease steadily as the mass-to-charge ratio increases."],
      ans=0,
      why="A relative abundance as used in EK 1.2.A.1 is a share of the whole sample, "
          "so the shares of all the isotopes present exhaust the sample. That is also "
          "what makes the weighted average of EK 1.2.A.2 come out on the same scale as "
          "the individual masses."),

 dict(q="A previously unnoticed isotope of an element is found, present at only 0.01 "
        "percent abundance, with a mass far above the other isotopes. What is the most "
        "likely effect on the accepted average atomic mass of the element?",
      choices=[
        "A very small increase, because the new mass enters the average with a very "
        "small weight.",
        "A very large increase, because the new isotope is much heavier than the "
        "others.",
        "No change at all, because average atomic mass depends only on the most "
        "abundant isotope.",
        "A decrease, because adding another isotope divides the total among more "
        "values.",
        "The average atomic mass becomes undefined, because the abundances no longer "
        "add to one hundred."],
      ans=0,
      why="Each isotopic mass enters the weighted average of EK 1.2.A.2 multiplied by "
          "its own abundance, so a very small abundance can only shift the result very "
          "slightly however extreme the mass is."),

 dict(q="A student reports the average atomic mass of the element whose spectrum is "
        "tabulated as 64.0 atomic mass units, obtained by adding the two isotopic "
        "masses and dividing by two. What is wrong with the method?",
      table=_T_CU,
      choices=[
        "It ignores the abundances, and the correct weighted value is about 63.6 "
        "instead.",
        "It ignores the abundances, and the correct weighted value is about 64.4 "
        "instead.",
        "It uses the wrong isotopic masses, which should have been read from the peak "
        "heights.",
        "It divides by the wrong number, and dividing by the number of peak heights "
        "would fix it.",
        "Nothing is wrong; the unweighted mean is what EK 1.2.A.2 calls the average "
        "atomic mass."],
      ans=0,
      why="EK 1.2.A.2 calls for a weighted average using the mass of each isotope and "
          "its relative abundance, so the more abundant lighter isotope must pull the "
          "result below the midpoint of the two masses."),

 dict(q="An element has exactly two isotopes. The lighter has a mass of 10.0 atomic "
        "mass units and an abundance of 20.0 percent, and the average atomic mass of "
        "the element is 10.8 atomic mass units. What is the mass of the heavier "
        "isotope?",
      choices=["11.0 atomic mass units", "10.8 atomic mass units",
               "12.0 atomic mass units", "13.0 atomic mass units",
               "It cannot be determined without the abundance of the heavier isotope"],
      ans=0,
      why="The abundances must exhaust the sample, so the heavier isotope is at 80.0 "
          "percent, and EK 1.2.A.2's weighted average gives 10.8 equal to 0.200 times "
          "10.0 plus 0.800 times the unknown mass, which leaves 11.0."),

 dict(q="Three single-element spectra are summarized in the table. In which one does "
        "the average atomic mass lie closest to the mass of its own heavier peak?",
      table=_T_THREE_SPECTRA,
      choices=["Spectrum 1", "Spectrum 2", "Spectrum 3",
               "All three are equally close, because each has exactly two peaks",
               "None of them, because a weighted average always lies at the midpoint"],
      ans=0,
      why="A weighted average under EK 1.2.A.2 sits nearest the mass carrying the "
          "largest abundance, and only one of the three spectra puts the bulk of its "
          "abundance on the heavier peak."),

 dict(q="EK 1.2.A.1 describes the abundances obtained from a mass spectrum as relative "
        "abundances in nature. Why does that qualification matter for the average "
        "atomic mass listed for an element?",
      choices=[
        "Because the listed value describes elements as they are naturally found, so it "
        "depends on how common each isotope is rather than on the isotopic masses "
        "alone.",
        "Because natural samples contain no isotopes, so the listed value refers only "
        "to laboratory-made atoms.",
        "Because abundances measured in nature are always equal for every isotope of "
        "an element.",
        "Because the listed value is the mass of the single naturally occurring isotope "
        "of the element.",
        "Because natural abundance determines the mass of each isotope rather than its "
        "share of the sample."],
      ans=0,
      why="EK 1.2.A.1 ties the abundance obtained from the spectrum to the isotope's "
          "occurrence in nature, and EK 1.2.A.2 then uses exactly those abundances as "
          "the weights. Abundance is a share of a sample and does not set the mass of "
          "any isotope."),

 dict(q="For an element with several isotopes, how does the average atomic mass compare "
        "with the mass of its single most abundant isotope?",
      choices=[
        "It is usually close to that isotope's mass but shifted toward the masses of "
        "the others.",
        "It is always exactly equal to that isotope's mass.",
        "It is always smaller than that isotope's mass, because averaging reduces "
        "values.",
        "It is always larger than that isotope's mass, because the other isotopes add "
        "to it.",
        "It bears no relation to that isotope's mass, since all isotopes count equally."],
      ans=0,
      why="The largest weight in the weighted average of EK 1.2.A.2 belongs to the most "
          "abundant isotope, so the result sits near that mass; the remaining "
          "abundances pull it toward whichever masses they carry, which may be above or "
          "below."),

 dict(q="An element gives two peaks of nearly but not exactly equal height, at 106.0 "
        "and 108.0 atomic mass units, with the lighter peak slightly the taller. Which "
        "value is the best estimate of its average atomic mass?",
      choices=["106.9 atomic mass units", "107.5 atomic mass units",
               "108.0 atomic mass units", "105.0 atomic mass units",
               "214.0 atomic mass units"],
      ans=0,
      why="Nearly equal weights in EK 1.2.A.2's weighted average put the result near "
          "the midpoint of 107.0, and the slight excess on the lighter peak moves it a "
          "little below that midpoint rather than above it."),

 dict(q="A spectrum of a single element is reported as raw peak heights in arbitrary "
        "units rather than as percentages, as shown. What is the relative abundance of "
        "the isotope of mass 20.0?",
      table=_T_HEIGHTS,
      choices=["75.0 percent", "30.0 percent", "60.0 percent", "25.0 percent",
               "3.00 percent"],
      ans=0,
      why="EK 1.2.A.1 makes the peak height proportional to the number of atoms of that "
          "isotope, so a relative abundance is a height divided by the total height of "
          "all the peaks. Reading the raw height as a percentage directly gives the "
          "rejected 3.00."),

 dict(q="Using the same raw peak heights, what is the average atomic mass of that "
        "element?",
      table=_T_HEIGHTS,
      choices=["20.5 atomic mass units", "21.0 atomic mass units",
               "20.0 atomic mass units", "21.5 atomic mass units",
               "42.0 atomic mass units"],
      ans=0,
      why="Converting the heights to fractional abundances of 0.750 and 0.250 and "
          "applying the weighted average of EK 1.2.A.2 gives 0.750 times 20.0 plus "
          "0.250 times 22.0. The unweighted mean of the two masses would be the "
          "rejected 21.0."),

 dict(q="Element V gives the tabulated spectrum below, in which one isotope accounts "
        "for almost all of the sample. Which statement about its average atomic mass is "
        "best supported by the data?",
      table=_T_SI,
      choices=[
        "It is slightly above 28.0, because the two heavier isotopes together hold only "
        "a small share of the sample.",
        "It is slightly below 28.0, because the lightest isotope dominates and drags "
        "the value down.",
        "It is close to 29.0, because that is the middle of the three isotopic masses.",
        "It is exactly 29.0, because the three isotopic masses are evenly spaced.",
        "It is above 30.0, because all three isotopes contribute their full masses."],
      ans=0,
      why="The weighted average of EK 1.2.A.2 is anchored near the mass holding almost "
          "all the abundance and can only be pulled upward by isotopes heavier than it. "
          "Since both remaining isotopes are heavier, the result must exceed 28.0 "
          "slightly."),

 dict(q="A student examines a single-element spectrum with a tall peak at 11.0 and a "
        "short peak at 10.0 atomic mass units, and concludes that the element has an "
        "atomic mass of exactly 11.0 atomic mass units. Which evaluation of that "
        "conclusion is correct?",
      choices=[
        "It is wrong, because 11.0 is the mass of one isotope while the element's "
        "average atomic mass must include the lighter isotope as well.",
        "It is wrong, because the mass of an element is always read from its shortest "
        "peak rather than its tallest.",
        "It is correct, because the tallest peak by definition gives the atomic mass of "
        "the element.",
        "It is correct, because the shorter peak represents an impurity rather than an "
        "isotope of the element.",
        "It cannot be evaluated, because a two-peak spectrum gives no information about "
        "atomic mass."],
      ans=0,
      why="EK 1.2.A.1 assigns every peak of a single-element spectrum to an isotope of "
          "that element, so the short peak is not an impurity, and EK 1.2.A.2 requires "
          "both isotopic masses to enter the average. The reported average must "
          "therefore fall between the two peak positions."),
]
