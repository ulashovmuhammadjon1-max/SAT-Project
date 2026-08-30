"""Key audit for AP PSYCHOLOGY 2.4 Encoding Memories.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on. For
the six statistics items the claim carries the ARITHMETIC as well, recomputed
here rather than restated from the module -- that is the closest this subject
gets to a sympy check and it is the only part of a psychology bank that can be
verified by calculation, so it is worth doing explicitly:

    item 22  mean    4+6+7+9+10+12 = 48; 48/6 = 8
    item 23  median  2,5,6,8,9,20 -> middle pair 6 and 8 -> (6+8)/2 = 7
                     (the mean of that set is 50/6 = 8.33, ABOVE the median,
                     because 20 is an outlier -- the distractor "10" is the
                     round number a careless reader supplies, and 8.33 is
                     offered as "8" is not, so mean-for-median is catchable)
    item 24  mode    5,5,6,8,8,8,11 -> 8 occurs three times, 5 twice
                     (7.3 is the mean of that set, offered as the standard
                     confusion; 51/7 = 7.29)
    item 25  range   15 - 3 = 12

Items 22-25 deliberately use FOUR DIFFERENT data sets. An earlier draft reused
one set across mean, median and range and produced the answer 8 three times,
which would have been answerable by pattern rather than by computation.

The CED assigns skill 3.B to this topic specifically, which is why statistics
items sit here rather than being spread thinly across Unit 2. No item refers to
a figure; every data set is stated in the stem as prose.

Content distinctions tested against each other on purpose: massed vs
distributed practice; primacy (beginning of a list) vs recency (end); chunking
(regrouping the material itself) vs method of loci (attaching material to an
external framework of places); encoding (this topic) vs storage, retrieval, and
forgetting (Topics 2.5, 2.6, 2.7, which supply the distractors in item 1).

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_4

CLAIMS = [
 ("processes and strategies that get information into memory",
  "EK 2.4.A.1, near verbatim. The three distractors are storage, retrieval, and forgetting -- the subjects of Topics 2.5, 2.6 and 2.7 -- so the item fixes the boundary of this topic rather than testing against invented terms."),
 ("determines how effectively the information is later stored and retrieved",
  "EK 2.4.A.1 states that how information is encoded can determine how effectively it is stored and retrieved. That claim is the reason encoding has a topic of its own, and it is what the whole of 2.4.A.2 through 2.4.A.5 elaborates."),
 ("aids in encoding information into working and long-term memory",
  "EK 2.4.A.2, near verbatim: mnemonic devices are processes that aid in encoding information into working and long-term memory. The distractors are long-term potentiation (EK 2.3.A.2), interference (Topic 2.7), and a heuristic (EK 2.2.A.4)."),
 ("location along a familiar route",
  "EK 2.4.A.2 gives method of loci as its worked example of a mnemonic device; it operates by attaching items to remembered places. The distractors are chunking (2.4.A.3), the spacing effect (2.4.A.4), and the primacy effect (2.4.A.5) -- every one a real member of this topic."),
 ("grouping information into meaningful units",
  "EK 2.4.A.3, near verbatim: encoding can be improved by grouping information together into meaningful chunks, categories, or hierarchies."),
 ("chunking",
  "EK 2.4.A.3. Recoding 1492 and 1776 as two dates converts eight units into two meaningful ones, which is the definition applied. The stem gives the digits in a form that makes the regrouping available without naming it."),
 ("hierarchies",
  "EK 2.4.A.3 names categories and hierarchies alongside chunks. Nesting examples inside subcategories inside categories is the hierarchy case specifically, not the chunk case."),
 ("studied all at once or distributed over time",
  "EK 2.4.A.4 defines the spacing effect by the massed/distributed contrast. The second distractor is the serial position effect (2.4.A.5) and the third is levels of processing (2.3.A.5) -- both real, both about something other than schedule."),
 ("massed practice",
  "EK 2.4.A.4 names massed practice for information encoded all at once."),
 ("distributed practice",
  "EK 2.4.A.4 names distributed practice for information distributed over time. Items 9 and 10 are adjacent so the pair must be known in both directions."),
 ("several shorter sessions spread across the two weeks",
  "EK 2.4.A.4 makes the spacing effect a difference in encoding and consolidation between massed and distributed practice, and distributed practice is the favoured condition. This is the item that requires the effect's DIRECTION, not just its definition."),
 ("order in which the information was presented",
  "EK 2.4.A.5: encoding processes can be affected by the order of how the information is presented, called the serial position effect."),
 ("primacy effect",
  "EK 2.4.A.5 attaches the primacy effect to information presented at the beginning of a list."),
 ("recency effect",
  "EK 2.4.A.5 attaches the recency effect to the end of a list. Adjacent to item 13 so neither can be answered from a single remembered half."),
 ("middle of the list",
  "EK 2.4.A.5 predicts that beginning and end will BOTH be more memorable than the middle, so the middle is what the effect disadvantages. The item is keyed to a LEAST stem, which is why both end positions appear as distractors."),
 ("serial position effect",
  "EK 2.4.A.5. Recall of the first two and last two names with the middle lost is the two-ended pattern the effect predicts; naming primacy or recency alone would describe only half of it, which is why the general term is the key."),
 ("recency effect",
  "EK 2.4.A.5. The stem specifies the LAST three items, which is the recency half specifically. Item 16 asks for the whole pattern and this one asks for one end, so the two are not duplicates."),
 ("regroups the material itself into meaningful units; the method of loci attaches the material to an external framework of places",
  "EK 2.4.A.3 versus EK 2.4.A.2: chunking reorganises the information, a mnemonic supplies an outside scaffold. The first distractor is that contrast reversed; the third asserts a restriction to numbers and words that neither EK makes."),
 ("massed in one session or distributed across four",
  "Science practice 2.B: the independent variable is the manipulated, randomly assigned condition. Total study time (60 minutes) and the one-week delay were held constant for both groups, which is why those options are neither the independent nor the dependent variable."),
 ("amount of study, rather than its spacing, could explain any difference",
  "A confounding variable changes along with the manipulation and offers a rival account. If the distributed group also studied longer, amount of practice rather than schedule could produce the result, so equating total time is what isolates the spacing effect."),
 ("number of words from the studied list correctly written down in five minutes",
  "An operational definition states the countable procedure. A word count in a fixed interval is measurable; 'seems to have learned', 'strength of memory', and 'felt confident' restate the construct or measure something else entirely."),
 ("8",
  "Computed: 4+6+7+9+10+12 = 48, and 48/6 = 8. The mean is the sum divided by the count."),
 ("7",
  "Computed: the set 2,5,6,8,9,20 has six scores, so the median is the mean of the middle pair, (6+8)/2 = 7. The mean of the same set is 50/6 = 8.33, pulled above the median by the outlier of 20 -- which is why '8' is an offered distractor and why this item uses a different data set from item 22."),
 ("8",
  "Computed: in 5,5,6,8,8,8,11 the value 8 occurs three times and 5 twice, so the mode is 8. The distractor 7.3 is the MEAN of this set (51/7 = 7.29), the standard mode-for-mean confusion."),
 ("12",
  "Computed: the range is the maximum minus the minimum, 15 - 3 = 12. The distractors are the maximum itself, the minimum itself, and a middle value."),
 ("more spread out around the mean",
  "Standard deviation is a measure of VARIATION, not of central tendency, and the stem states that the two means are equal. A larger standard deviation therefore means greater dispersion, not a higher average and not a larger sample."),
 ("scored higher than about 80 percent of her classmates",
  "Percentile rank is a position within a distribution: the percentage of scores falling below a given score. It is not a percentage of items answered correctly, which is the misreading the second distractor supplies, and the last distractor is the same statistic read backwards."),
 ("randomly assigned to spaced study recall more a week later",
  "Only a manipulated, randomly assigned schedule can support a causal claim about the schedule. The second and third options are correlational, and the fourth describes the serial position effect (EK 2.4.A.5), which is a different phenomenon entirely."),
 ("already conscientious may both use mnemonics and earn higher grades",
  "A survey manipulates nothing, so a third variable is a live rival explanation. EK 2.4.A.2 does say mnemonics aid encoding, which is what makes the causal reading tempting -- the flaw is in the design, not in the construct, and the second distractor gets that backwards."),
 ("spacing effect favors distributed practice, and grouping the terms into meaningful chunks",
  "The advice fails on two counts this topic supplies: EK 2.4.A.4 favours distributing study over massing it the night before, and EK 2.4.A.3 says grouping into meaningful chunks improves encoding, which rereading an unstructured list does not do. The other options are true statements of framework content that simply do not bear on the advice."),
]

psych_check.check(p2_4, CLAIMS, per_topic=30, n_choices=4)
