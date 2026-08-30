"""Key verification for AP PSYCH 4.4 (Psychodynamic and Humanistic Theories).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.4, p. 101.

SCOPE CHECK, run by eye against the module and recorded here because it is the
easiest thing on this topic to get wrong:
  * EK 4.4.A.1 excludes the stage theory of psychosexual development. No item
    names a psychosexual stage or turns on fixation.
  * EK 4.4.B.1 excludes Maslow's hierarchy of needs. No item names it; the
    humanistic items rest on unconditional regard and the self-actualizing
    tendency, which are what the CED actually requires.

The eight defense mechanisms EK 4.4.A.2 names are denial, displacement,
projection, rationalization, reaction formation, regression, repression, and
sublimation. All eight are keyed at least once below, and the three pairs
students most often merge are given explicit discriminator items.

Run: python3 verify_p4_4.py
"""
import p4_4
from psych_check import check

CLAIMS = [
 ("outside of conscious awareness",
  "EK 4.4.A.1, verbatim in substance: according to the psychodynamic theory of "
  "personality, unconscious processes drive personality. The three distractors "
  "state the behavioral, trait, and humanistic positions instead."),

 ("protect the ego from threat, and they operate unconsciously",
  "EK 4.4.A.2: ego defense mechanisms serve to protect the ego UNCONSCIOUSLY from "
  "threats. Operating outside awareness is part of the definition, which is "
  "precisely why a consciously chosen coping plan is not a defense mechanism."),

 ("denial",
  "EK 4.4.A.2. Denial refuses to acknowledge a threatening reality. The patient "
  "does not redirect the feeling onto a substitute (displacement), channel it into "
  "valued activity (sublimation), or retreat to earlier behavior (regression)."),

 ("displacement",
  "EK 4.4.A.2. Displacement redirects an impulse from a threatening target onto a "
  "safer substitute. The anger is unchanged; only its object moves. The employee "
  "does not attribute anger to anyone else, which would be projection."),

 ("projection",
  "EK 4.4.A.2. Projection attributes one's own unacceptable impulse to other "
  "people. The rule-bending is disowned and relocated in the colleagues rather "
  "than acted out on a substitute target."),

 ("rationalization",
  "EK 4.4.A.2. Rationalization supplies a plausible-sounding justification that "
  "conceals the real, less acceptable reason -- here, not having studied."),

 ("reaction formation",
  "EK 4.4.A.2. Reaction formation expresses the OPPOSITE of the unacceptable "
  "impulse, characteristically in exaggerated form. The conspicuous effusiveness "
  "is the diagnostic detail; simple denial would produce no positive display."),

 ("regression",
  "EK 4.4.A.2. Regression is a retreat to behavior characteristic of an earlier, "
  "less demanding period of development. Note the CED lists regression as a "
  "defense mechanism, which is in scope, while the psychosexual STAGE theory is "
  "excluded -- this item tests the mechanism, not a stage."),

 ("repression",
  "EK 4.4.A.2. Repression excludes anxiety-arousing material from consciousness. "
  "The item rules out an organic cause explicitly. Denial is excluded because "
  "denial concerns refusing a PRESENT reality, not a past memory becoming "
  "inaccessible -- the distinction these two are most often merged on."),

 ("sublimation",
  "EK 4.4.A.2. Sublimation redirects an unacceptable impulse into a socially "
  "valued activity. The socially constructive outlet is exactly what separates it "
  "from displacement, which needs only a safer target."),

 ("redirects the impulse onto a safer target, while projection attributes",
  "Discriminator item. EK 4.4.A.2 lists both. In displacement the person still "
  "OWNS the impulse and acts on it toward a substitute; in projection the person "
  "DISOWNS it and sees it in someone else. The reversed statement is the trap. "
  "Both are unconscious, so the consciousness contrast is false."),

 ("actively expresses the opposite of the impulse, while denial simply refuses",
  "Discriminator item. EK 4.4.A.2 lists both. Denial fails to register the threat "
  "at all and produces no substitute behavior; reaction formation registers the "
  "impulse and converts it into a visible, usually exaggerated opposite."),

 ("channels the impulse into a socially valued activity, while displacement merely",
  "Discriminator item. EK 4.4.A.2 lists both as separate mechanisms. Both "
  "redirect; only sublimation redirects toward something the culture values. "
  "Both are unconscious, so the consciousness contrast is false here too."),

 ("denial",
  "EK 4.4.A.2. Each report is refused rather than redirected, attributed to "
  "another person, or channeled into a valued outlet -- the threatening reality "
  "is simply not accepted."),

 ("projection",
  "EK 4.4.A.2. The envy is disowned and relocated in the friend, and the accusation "
  "names the very feeling the person holds. Displacement is excluded because the "
  "feeling is not being acted out on a substitute target."),

 ("rationalization",
  "EK 4.4.A.2. A comfortable justification replaces the real motive. Repression "
  "and denial are both excluded by the stem, which states the manager fully "
  "remembers and acknowledges the decision she made."),

 ("regression",
  "EK 4.4.A.2. Under stress the child returns to behavior belonging to an earlier "
  "developmental period. This tests the defense mechanism, which is required "
  "content, and not the excluded psychosexual stage theory."),

 ("sublimation",
  "EK 4.4.A.2. Painful feeling is converted into socially valued, productive "
  "activity. Denial is excluded because the loss is fully acknowledged -- the "
  "person is organizing services precisely about it -- and volunteering is not "
  "the opposite of grief, so it is not reaction formation."),

 ("ambiguous stimulus will reveal preconscious and unconscious material",
  "EK 4.4.A.3: psychodynamic personality psychologists assess personality using "
  "projective tests designed to probe the preconscious and unconscious mind. "
  "Ambiguity is what makes the response projective rather than a report."),

 ("scoring depends heavily on the individual interpreter",
  "Research-methods item. Open-ended responses to ambiguous stimuli must be "
  "interpreted, and interpreter-dependent scoring yields low interrater "
  "reliability -- the standard criticism. The 'measure conscious attitudes' "
  "option inverts the tests' stated purpose in EK 4.4.A.3."),

 ("inherent tendency toward growth and the realization of one's potential",
  "EK 4.4.B.1 names the self-actualizing tendency as a primary motivating factor "
  "of humanistic personality theory. Note this item deliberately does NOT route "
  "through Maslow's hierarchy, which the same EK statement excludes from scope."),

 ("as they are, without making that acceptance depend on their meeting standards",
  "EK 4.4.B.1 names unconditional regard as the other primary motivating factor. "
  "The precision that matters: it is acceptance of the PERSON that is not "
  "contingent, which is not the same as withholding all evaluation of behavior -- "
  "the overreach option."),

 ("value themselves only insofar as they meet others' standards",
  "The predicted consequence of CONDITIONAL regard, which is what EK 4.4.B.1's "
  "unconditional regard is defined against: worth becomes contingent on "
  "performance. The remaining options overstate what the theory predicts, and "
  "the attachment claim is not a humanistic prediction at all."),

 ("self-actualizing tendency",
  "EK 4.4.B.1. The humanistic premise is that people are inherently oriented "
  "toward growth and the practitioner's task is to supply the conditions for it, "
  "rather than to resolve conflict, measure traits, or arrange reinforcement."),

 ("hidden conflict or by an inherent tendency toward growth",
  "The substantive disagreement: EK 4.4.A.1 puts unconscious processes at the "
  "center of the psychodynamic account, EK 4.4.B.1 puts an inherent growth "
  "tendency at the center of the humanistic one. The measurement option is a "
  "methodological difference, not the theoretical one the question asks for."),

 ("psychodynamic theory with projective tests",
  "EK 4.4.A.3 explicitly pairs psychodynamic personality assessment with "
  "projective tests. Humanistic assessment centers on the person's own reported "
  "experience, so both humanistic pairings offered are wrong."),

 ("small number of unrepresentative individuals may not generalize",
  "Research-methods item (Science Practice 2.C). A case study yields rich detail "
  "with no basis for generalization. It is non-experimental, so random assignment "
  "does not apply, and nothing about the method requires deception."),

 ("can be made to fit any outcome",
  "Research-methods item. A claim that accommodates an outcome and equally its "
  "opposite makes no risky prediction, so no observation can count against it. "
  "That is the falsifiability criticism, and it is the reverse of the "
  "'confirmed in every study' option."),

 ("humanistic view of personality",
  "Both elements EK 4.4.B.1 names are present in the therapist's statement: "
  "acceptance that is not made conditional, and an inherent capacity to grow that "
  "the therapist need only make room for."),

 ("rationalization, because a face-saving justification replaces the real",
  "EK 4.4.A.2. A comfortable reason is supplied after the fact to protect the ego "
  "from the real one. No socially valued outlet appears (not sublimation), no "
  "return to earlier behavior (not regression), and no impulse is relocated into "
  "another person (not projection)."),
]

check(p4_4, CLAIMS)
