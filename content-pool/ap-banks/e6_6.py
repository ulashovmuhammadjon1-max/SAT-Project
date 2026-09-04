# AP ENVIRONMENTAL SCIENCE 6.6 Nuclear Power
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.G, describe the use of nuclear energy in power generation; and
# ENG-3.H, describe the effects of the use of nuclear energy on the environment.
# Suggested skill 2.B, explain relationships between different characteristics of
# environmental concepts, processes, or models represented visually, in theoretical and in
# applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.G.1  Nuclear power is generated through fission, where atoms of Uranium-235,
#              which are stored in fuel rods, are split into smaller parts after being
#              struck by a neutron. Nuclear fission releases a large amount of heat, which
#              is used to generate steam, which powers a turbine and generates electricity.
#   ENG-3.G.2  Radioactivity occurs when the nucleus of a radioactive isotope loses energy
#              by emitting radiation.
#   ENG-3.G.3  Uranium-235 remains radioactive for a long time, which leads to the problems
#              associated with the disposal of nuclear waste.
#   ENG-3.G.4  Nuclear power generation is a nonrenewable energy source. Nuclear power is
#              considered a cleaner energy source because it does not produce air
#              pollutants, but it does release thermal pollution and hazardous solid waste.
#   ENG-3.H.1  Three Mile Island, Chernobyl, and Fukushima are three cases where accidents
#              or natural disasters led to the release of radiation. These releases have had
#              short- and long-term impacts on the environment.
#   ENG-3.H.2  A radioactive element's half-life can be used to calculate a variety of
#              things, including the rate of decay and the radioactivity level at specific
#              points in time.
#
# FISSION AND FUSION ARE THE SWAP THIS TOPIC INVITES. The framework says FISSION and says
# the atoms are SPLIT INTO SMALLER PARTS; it never mentions fusion. The obvious distractor
# keeps the reactor and joins the atoms instead, so every anchor about the process carries
# BOTH clauses -- the name and the direction -- and never the word fission alone.
#
# CLEANER AND NONRENEWABLE IN THE SAME SENTENCE. ENG-3.G.4 makes three claims at once:
# nuclear power generation is NONRENEWABLE; it is considered CLEANER BECAUSE IT DOES NOT
# PRODUCE AIR POLLUTANTS; and it DOES RELEASE THERMAL POLLUTION AND HAZARDOUS SOLID WASTE.
# Dropping any one of the three is the commonest way to get this statement wrong, so the
# items that key it carry the qualification as well as the claim.
#
# WHAT IS NOT KEYED. The framework names three accident sites and says the releases had
# short- and long-term impacts. It gives no dates, no countries, no doses and no cause for
# any individual case beyond "accidents or natural disasters", so no item asks for one and
# no table is labelled with a real site. ENG-3.H.2 says a half-life CAN BE USED to
# calculate things; the arithmetic items therefore print their own decay record and compute
# from it rather than quoting any element's half-life from memory.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_6.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.6", "Nuclear Power", 6)

_T_DECAY = dict(
    headers=["Time since the sample was sealed (years)",
             "Radioactivity remaining (percent of the original)"],
    rows=[["0", "100"],
          ["30", "50"],
          ["60", "25"],
          ["90", "12.5"]])

_T_ISOTOPE = dict(
    headers=["Isotope in the stored waste",
             "Half-life (years)",
             "Share of the waste by mass (percent)"],
    rows=[["Isotope A", "7", "20"],
          ["Isotope B", "70", "30"],
          ["Isotope C", "700,000", "50"]])

_T_PLANT = dict(
    headers=["Plant compared",
             "Air pollutants released for each unit of electricity (kilograms)",
             "Waste heat discharged to the river for each unit of electricity (energy units)",
             "Hazardous solid waste produced for each unit of electricity (kilograms)"],
    rows=[["Coal plant", "9.0", "1.4", "0.30"],
          ["Nuclear plant", "0.0", "2.1", "0.45"]])

_T_SITE = dict(
    headers=["Site of a release",
             "Radiation in the soil one year after the release (units)",
             "Radiation in the soil twenty years after the release (units)"],
    rows=[["Site 1", "400", "110"],
          ["Site 2", "260", "70"],
          ["Site 3", "180", "40"]])

QUESTIONS = [

 dict(q="Through what process does the framework say nuclear power is generated?",
      choices=[
        "Fission, in which atoms are split into smaller parts",
        "Fusion, in which atoms are joined into larger ones",
        "Combustion, in which a fuel reacts with oxygen",
        "Fission, in which atoms are joined into larger ones",
        "Fusion, in which atoms are split into smaller parts"],
      ans=0,
      why="ENG-3.G.1 states that NUCLEAR POWER IS GENERATED THROUGH FISSION, WHERE ATOMS OF "
          "URANIUM-235 ARE SPLIT INTO SMALLER PARTS. The framework never mentions fusion, and the "
          "rejected options either rename the process or reverse the direction the atoms go."),

 dict(q="Which atoms does the framework name as the ones that are split?",
      choices=[
        "Atoms of Uranium-235",
        "Atoms of carbon in the fuel",
        "Atoms of hydrogen from water",
        "Atoms of helium formed in the reactor",
        "Atoms of any element present in the fuel rod"],
      ans=0,
      why="ENG-3.G.1 names ATOMS OF URANIUM-235 as what is split, and ENG-3.G.3 returns to "
          "Uranium-235 when it explains why nuclear waste is a problem. No other element is named "
          "as the fissile material anywhere in this topic."),

 dict(q="Where does the framework say those atoms are held inside the reactor?",
      choices=[
        "In fuel rods",
        "Dissolved in the cooling water",
        "In the turbine housing",
        "In the generator windings",
        "In the concrete of the containment building"],
      ans=0,
      why="ENG-3.G.1 states that the atoms of Uranium-235 ARE STORED IN FUEL RODS. The turbine and "
          "the generator come later in the framework's sequence and take no part in holding the "
          "fuel, and the statement mentions no other location."),

 dict(q="What does the framework say starts the splitting of one of those atoms?",
      choices=[
        "Being struck by a neutron",
        "Being heated by the steam",
        "Being struck by a beam of light",
        "Being compressed by the pressure inside the fuel rod",
        "Being dissolved by the cooling water"],
      ans=0,
      why="ENG-3.G.1 states that the atoms are split into smaller parts AFTER BEING STRUCK BY A "
          "NEUTRON. Heat, light, pressure and chemical attack appear nowhere in the framework's "
          "account of what triggers fission."),

 dict(q="What does the framework say nuclear fission releases, and what is done with it?",
      choices=[
        "A large amount of heat, which is used to generate steam",
        "A large amount of heat, which is turned straight into electricity",
        "A large amount of electricity, which is used to boil water",
        "A large amount of light, which is captured by cells",
        "A large amount of steam, which is heated by a separate furnace"],
      ans=0,
      why="ENG-3.G.1 states that NUCLEAR FISSION RELEASES A LARGE AMOUNT OF HEAT, WHICH IS USED TO "
          "GENERATE STEAM. The electricity comes at the end of the framework's sequence rather "
          "than at the start, and light captured by cells is photovoltaic solar energy."),

 dict(q="In that same account, what does the steam do?",
      choices=[
        "It powers a turbine, and that generates electricity",
        "It powers a generator, and that turns a turbine",
        "It is split by neutrons to release more heat",
        "It is stored until the fuel rods are replaced",
        "It cools the fuel rods so that fission can continue"],
      ans=0,
      why="ENG-3.G.1 states that the steam POWERS A TURBINE AND GENERATES ELECTRICITY. The "
          "turbine comes before the electricity in the framework's sequence, and steam is the "
          "working fluid rather than something that is split or stored."),

 dict(q="Which sequence matches the framework's account of a nuclear power plant?",
      choices=[
        "A neutron strikes a Uranium-235 atom in a fuel rod, the atom splits and releases heat, "
        "the heat generates steam, the steam powers a turbine, and electricity is generated",
        "A neutron strikes a Uranium-235 atom in a fuel rod, the atom joins with another, heat "
        "is released, and the heat is turned straight into electricity",
        "Steam is raised first, the steam splits the Uranium-235 atoms, and the heat released "
        "powers a turbine",
        "A turbine is spun first, the spinning generates the neutrons, and the neutrons split "
        "the Uranium-235 atoms",
        "Uranium-235 is burned with oxygen, the heat generates steam, and the steam powers a "
        "turbine"],
      ans=0,
      why="ENG-3.G.1 gives the whole sequence: a neutron strikes an atom of Uranium-235 stored in "
          "a fuel rod, the atom is split into smaller parts, the fission releases a large amount "
          "of heat, that heat generates steam, and the steam powers a turbine and generates "
          "electricity. Each rejected sequence joins the atoms instead of splitting them, "
          "exchanges two steps, or makes the reaction a combustion."),

 dict(q="How does the framework define radioactivity?",
      choices=[
        "The nucleus of a radioactive isotope losing energy by emitting radiation",
        "The nucleus of a radioactive isotope gaining energy by absorbing radiation",
        "The splitting of a nucleus after it is struck by a neutron",
        "The heating of water by a fuel rod inside a reactor",
        "The joining of two nuclei to form a heavier one"],
      ans=0,
      why="ENG-3.G.2 states that RADIOACTIVITY OCCURS WHEN THE NUCLEUS OF A RADIOACTIVE ISOTOPE "
          "LOSES ENERGY BY EMITTING RADIATION. Splitting after a neutron strike is fission, which "
          "the framework treats in a separate statement, and the energy goes out rather than in."),

 dict(q="What consequence does the framework draw from Uranium-235 remaining radioactive for a "
        "long time?",
      choices=[
        "The problems associated with the disposal of nuclear waste",
        "The impossibility of generating electricity from it",
        "The release of air pollutants from the plant",
        "The need to import it from other countries",
        "The high price of electricity from nuclear plants"],
      ans=0,
      why="ENG-3.G.3 states that Uranium-235 REMAINS RADIOACTIVE FOR A LONG TIME, WHICH LEADS TO "
          "THE PROBLEMS ASSOCIATED WITH THE DISPOSAL OF NUCLEAR WASTE. The statement draws no "
          "conclusion about generation, air pollutants, trade or price."),

 dict(q="How does the framework classify nuclear power generation as an energy source?",
      choices=[
        "As nonrenewable",
        "As a renewable source",
        "As renewable only where the fuel rods are reprocessed",
        "As neither renewable nor nonrenewable",
        "The framework does not classify it either way"],
      ans=0,
      why="ENG-3.G.4 opens by stating that NUCLEAR POWER GENERATION IS A NONRENEWABLE ENERGY "
          "SOURCE. It attaches no condition to that classification and it does classify the "
          "source, so the last two options are wrong on their face."),

 dict(q="The framework says nuclear power is considered a cleaner energy source. What reason does "
        "it give?",
      choices=[
        "Because it does not produce air pollutants",
        "Because it produces no waste of any kind",
        "Because it releases no heat to nearby water",
        "Because its fuel is replenished at the rate it is consumed",
        "Because it costs less than any other source"],
      ans=0,
      why="ENG-3.G.4 states that nuclear power IS CONSIDERED A CLEANER ENERGY SOURCE BECAUSE IT "
          "DOES NOT PRODUCE AIR POLLUTANTS. The same sentence goes on to say that it does release "
          "thermal pollution and hazardous solid waste, so the rejected reasons contradict it."),

 dict(q="What does the framework say nuclear power does release, despite that reputation?",
      choices=[
        "Thermal pollution and hazardous solid waste",
        "Air pollutants and hazardous solid waste",
        "Thermal pollution and volatile organic compounds",
        "Carbon dioxide and water",
        "Nothing at all is released"],
      ans=0,
      why="ENG-3.G.4 states that nuclear power DOES RELEASE THERMAL POLLUTION AND HAZARDOUS SOLID "
          "WASTE. Air pollutants are what the same sentence says it does not produce, volatile "
          "organic compounds belong to fracking in topic 6.5, and carbon dioxide and water are the "
          "products of combustion."),

 dict(q="How do the framework's two verdicts on nuclear power stand together?",
      choices=[
        "It is nonrenewable, and it is considered cleaner only in the sense that it produces no "
        "air pollutants",
        "It is renewable, and it is considered cleaner because it produces no waste at all",
        "It is nonrenewable, and it is considered cleaner because it produces no waste at all",
        "It is renewable, and it is considered cleaner only in the sense that it produces no "
        "air pollutants",
        "The framework gives only one verdict, that nuclear power is clean"],
      ans=0,
      why="ENG-3.G.4 makes both claims in one statement: nuclear power generation is a "
          "nonrenewable energy source, and it is considered cleaner because it does not produce "
          "air pollutants, though it does release thermal pollution and hazardous solid waste. "
          "Cleaner and renewable are separate properties and only one of them is granted here."),

 dict(q="Which three cases does the framework name where accidents or natural disasters led to a "
        "release of radiation?",
      choices=[
        "Three Mile Island, Chernobyl, and Fukushima",
        "Three Mile Island, Chernobyl, and Bhopal",
        "Chernobyl, Fukushima, and Love Canal",
        "Three Mile Island, Fukushima, and Minamata",
        "Chernobyl, Bhopal, and Minamata"],
      ans=0,
      why="ENG-3.H.1 names THREE MILE ISLAND, CHERNOBYL, AND FUKUSHIMA as its three cases. The "
          "other places in the rejected lists are associated with chemical or waste incidents "
          "rather than with a release of radiation, and the framework does not name them here."),

 dict(q="What does the framework say about the impacts of those releases on the environment?",
      choices=[
        "That they have had short-term and long-term impacts",
        "That they have had short-term impacts only",
        "That they have had long-term impacts only",
        "That they had no measurable impact on the environment",
        "That the framework does not describe the impacts"],
      ans=0,
      why="ENG-3.H.1 states that THESE RELEASES HAVE HAD SHORT- AND LONG-TERM IMPACTS ON THE "
          "ENVIRONMENT. Keeping only one of the two timescales drops half the statement, and the "
          "framework certainly does describe the impacts."),

 dict(q="What does the framework say a radioactive element's half-life can be used to calculate?",
      choices=[
        "A variety of things, including the rate of decay and the radioactivity level at "
        "specific points in time",
        "Only the rate of decay, and nothing else",
        "Only the total mass of waste a reactor will produce",
        "The price of the electricity a reactor generates",
        "The number of neutrons a reactor releases in a second"],
      ans=0,
      why="ENG-3.H.2 states that a half-life CAN BE USED TO CALCULATE A VARIETY OF THINGS, "
          "INCLUDING THE RATE OF DECAY AND THE RADIOACTIVITY LEVEL AT SPECIFIC POINTS IN TIME. "
          "The word including leaves the list open rather than closing it at one item, and price "
          "and neutron counts are not in the statement."),

 dict(q="A student writes that nuclear power is renewable because the fuel can be reprocessed and "
        "used again. What correction does the framework require?",
      choices=[
        "The framework calls nuclear power generation a nonrenewable energy source, without "
        "qualification",
        "The framework calls nuclear power renewable, so the student is correct",
        "The framework calls nuclear power renewable only where reprocessing is practised",
        "The framework declines to classify nuclear power at all",
        "The framework calls nuclear power renewable because it releases no air pollutants"],
      ans=0,
      why="ENG-3.G.4 states flatly that nuclear power generation is a nonrenewable energy source "
          "and makes no exception for reprocessing. The absence of air pollutants is the "
          "framework's ground for calling it cleaner, which is a different property from being "
          "renewable."),

 dict(q="A second student writes that a nuclear plant produces no pollution of any kind. What "
        "correction does the framework require?",
      choices=[
        "It produces no air pollutants, but it does release thermal pollution and hazardous "
        "solid waste",
        "It produces air pollutants but no thermal pollution and no solid waste",
        "It produces thermal pollution but no solid waste and no air pollutants",
        "It produces hazardous solid waste but no thermal pollution and no air pollutants",
        "No correction is needed, since the framework calls nuclear power entirely clean"],
      ans=0,
      why="ENG-3.G.4 grants the absence of air pollutants and then names two things nuclear power "
          "does release, thermal pollution and hazardous solid waste. Each rejected correction "
          "keeps one part of that sentence and drops another."),

 dict(q="A sealed sample of a radioactive element was measured at intervals. What is the "
        "half-life of the element in the record?",
      table=_T_DECAY,
      choices=[
        "30 years",
        "60 years",
        "90 years",
        "15 years",
        "50 years"],
      ans=0,
      why="The radioactivity falls from 100 to 50 percent of the original in the first 30 years, "
          "then from 50 to 25 in the next 30, then from 25 to 12.5 in the next. A half-life is the "
          "time for the radioactivity to fall by half, so it is 30 years. ENG-3.H.2 makes the "
          "half-life the quantity such a record yields."),

 dict(q="Using the same sealed sample, how many half-lives have passed by the sixtieth year?",
      table=_T_DECAY,
      choices=[
        "Two",
        "One",
        "Three",
        "Four",
        "Sixty"],
      ans=0,
      why="The radioactivity is 100 percent at the start, 50 percent after 30 years and 25 percent "
          "after 60, so the sample has halved twice by the sixtieth year. The rejected values "
          "count the wrong number of halvings or quote the elapsed years as though they were "
          "half-lives."),

 dict(q="Using the same sealed sample, what share of the original radioactivity would remain after "
        "120 years?",
      table=_T_DECAY,
      choices=[
        "6.25 percent",
        "12.5 percent",
        "3.125 percent",
        "50 percent",
        "None, because the sample would be inert by then"],
      ans=0,
      why="The record halves every 30 years, so the 12.5 percent standing at 90 years halves once "
          "more to 6.25 percent at 120 years. ENG-3.H.2 states that a half-life can be used to "
          "calculate the radioactivity level at specific points in time, which is exactly this "
          "step beyond the record. The rejected values stop one halving short, take one halving "
          "too many, halve only once from the start, or deny a level the record's own trend "
          "gives."),

 dict(q="Which of the framework's statements does that decay record most directly illustrate?",
      table=_T_DECAY,
      choices=[
        "That a half-life can be used to calculate the rate of decay and the radioactivity level "
        "at specific points in time",
        "That nuclear power generation is a nonrenewable energy source",
        "That nuclear power is generated through fission of Uranium-235",
        "That accidents and natural disasters have led to releases of radiation",
        "That nuclear power does not produce air pollutants"],
      ans=0,
      why="The record is a series of radioactivity levels at stated times, from which the "
          "half-life of 30 years and any later level can be worked out. That is precisely what "
          "ENG-3.H.2 says a half-life is used for, while the rejected statements concern "
          "classification, mechanism, accidents and emissions."),

 dict(q="Stored waste was broken down by isotope. Which isotope is the one that makes disposal a "
        "long-term problem, and why?",
      table=_T_ISOTOPE,
      choices=[
        "The third isotope, because its half-life is by far the longest of the three",
        "The first isotope, because its half-life is by far the longest of the three",
        "The third isotope, because it makes up the smallest share of the waste by mass",
        "The first isotope, because it makes up the largest share of the waste by mass",
        "None of them, because the framework attaches no disposal problem to long-lived waste"],
      ans=0,
      why="The half-lives are 7, 70 and 700,000 years, so the third isotope stays radioactive far "
          "longer than the others, and it is also half the waste by mass. ENG-3.G.3 ties the "
          "problems of disposal to a material remaining radioactive FOR A LONG TIME."),

 dict(q="Using the same stored waste, how many times as long is the longest half-life as the next "
        "longest?",
      table=_T_ISOTOPE,
      choices=[
        "Ten thousand times as long",
        "One hundred thousand times as long",
        "One thousand times as long",
        "Ten times as long",
        "The two are the same length"],
      ans=0,
      why="Dividing the two tabulated half-lives gives 700,000 divided by 70, which is 10,000. The "
          "rejected values shift the answer by a power of ten, quote the ratio between the two "
          "shorter isotopes, or deny that the half-lives differ."),

 dict(q="A coal plant and a nuclear plant were compared on what each releases for each unit of "
        "electricity. Which conclusion matches the framework's statement about nuclear power?",
      table=_T_PLANT,
      choices=[
        "The nuclear plant releases no air pollutants, but it does discharge more waste heat and "
        "more hazardous solid waste than the coal plant",
        "The nuclear plant releases no air pollutants and nothing else either",
        "The nuclear plant releases air pollutants but no waste heat and no hazardous solid "
        "waste",
        "The coal plant releases no air pollutants, but it does discharge more waste heat than "
        "the nuclear plant",
        "The two plants release the same amount of every substance in the record"],
      ans=0,
      why="The nuclear plant releases 0.0 kilograms of air pollutants against the coal plant's "
          "9.0, and 2.1 energy units of waste heat and 0.45 kilograms of hazardous solid waste "
          "against 1.4 and 0.30. ENG-3.G.4 says exactly this: cleaner because no air pollutants, "
          "but thermal pollution and hazardous solid waste all the same."),

 dict(q="Using the same two plants, how much more waste heat does the nuclear plant discharge for "
        "each unit of electricity?",
      table=_T_PLANT,
      choices=[
        "0.7 energy units",
        "2.1 energy units",
        "3.5 energy units",
        "1.4 energy units",
        "The nuclear plant discharges less waste heat than the coal plant"],
      ans=0,
      why="Subtracting the two tabulated values gives 2.1 minus 1.4, which is 0.7 energy units. "
          "The rejected values quote one plant alone, add the two, or invert the direction the "
          "record shows. ENG-3.G.4 names thermal pollution among what nuclear power does "
          "release."),

 dict(q="Using the same two plants, which claim about the nuclear plant does the record refute?",
      table=_T_PLANT,
      choices=[
        "That it produces no hazardous solid waste",
        "That it produces no air pollutants",
        "That it produces less hazardous solid waste than the coal plant",
        "That it discharges waste heat to the river",
        "That it generates electricity"],
      ans=0,
      why="The nuclear plant produces 0.45 kilograms of hazardous solid waste for each unit of "
          "electricity, more than the coal plant's 0.30, so the claim that it produces none is "
          "false. Its air pollutant figure is 0.0, so that claim stands, and ENG-3.G.4 names "
          "hazardous solid waste among what nuclear power does release."),

 dict(q="Soil at three sites of past radiation releases was measured twice. Which of the "
        "framework's claims do the values support?",
      table=_T_SITE,
      choices=[
        "That releases of radiation have had short-term and long-term impacts on the "
        "environment",
        "That releases of radiation have had short-term impacts that were gone within a year",
        "That releases of radiation have had no measurable impact on the environment",
        "That nuclear power generation is a nonrenewable energy source",
        "That nuclear power does not produce air pollutants"],
      ans=0,
      why="Radiation in the soil stands at 400, 260 and 180 units a year after the releases and "
          "still at 110, 70 and 40 units twenty years later, so the effect is present both soon "
          "after and long after. ENG-3.H.1 states that such releases have had short- and long-term "
          "impacts on the environment."),

 dict(q="Using the same three sites, by how much did the radiation in the soil fall at the site "
        "that started highest?",
      table=_T_SITE,
      choices=[
        "By 290 units",
        "By 400 units",
        "By 510 units",
        "By 190 units",
        "By 140 units"],
      ans=0,
      why="Subtracting the two tabulated values for that site gives 400 minus 110, which is 290 "
          "units. The rejected values quote the first reading alone, add the two, or take the fall "
          "at one of the other two sites."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Fission splits atoms of Uranium-235 held in fuel rods after a neutron strikes them, "
        "releasing heat that raises steam to power a turbine and generate electricity; "
        "radioactivity is a nucleus losing energy by emitting radiation; Uranium-235 stays "
        "radioactive a long time, which is why disposal is a problem; nuclear power is "
        "nonrenewable and cleaner only for want of air pollutants, since it still gives off "
        "thermal pollution and hazardous solid waste; Three Mile Island, Chernobyl and "
        "Fukushima released radiation with short-term and long-term effects; and a half-life "
        "can be used to calculate decay rates and levels at given times.",
        "Fusion joins atoms of Uranium-235 in fuel rods, and the heat released is turned "
        "straight into electricity without a turbine.",
        "Nuclear power is renewable and entirely clean, and the framework names no accidents "
        "and no waste problem.",
        "Radioactivity is a nucleus gaining energy, Uranium-235 decays within a few years, and "
        "disposal poses no long-term difficulty.",
        "Nuclear power produces air pollutants but no solid waste, and a half-life can be used "
        "only to find the rate of decay."],
      ans=0,
      why="The keyed summary carries ENG-3.G.1 through G.4 and ENG-3.H.1 and H.2 in the "
          "framework's own terms and adds nothing. Each rejected summary joins the atoms instead "
          "of splitting them, calls the source renewable or entirely clean, reverses the direction "
          "of the energy in radioactivity, or closes a list the framework leaves open."),
]
