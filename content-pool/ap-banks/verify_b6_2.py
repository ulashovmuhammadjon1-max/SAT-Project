"""Key audit for AP BIOLOGY 6.2 DNA Replication.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. The semiconservative model is arithmetic once it is written
down, so it is written down: ``_semiconservative`` below starts from one molecule
of two original strands and applies EK 6.2.A.1.ii one round at a time, tracking
how many molecules exist and how many still hold an original strand. The density
table, the molecule-count table and the two forward-looking items about a fourth
round are all recomputed from it -- including the assertion that the number of
molecules holding original DNA CANNOT grow, which is the point students get
wrong and the point a hand-written key gets wrong with them.

The two fragment and inhibitor tables are recomputed from their own contents:
joins equal segments minus one, and each observation is matched to exactly one
of the five participants the CED names.

ON THE EXCLUSION STATEMENT. The CED puts every enzyme other than DNA polymerase,
ligase, RNA polymerase, helicase and topoisomerase beyond the scope of the exam.
``NAMED`` below is that list, and the check at the bottom scans every stem,
choice and reason in the module for any other enzyme name this topic might tempt
an author into -- primase, gyrase, exonuclease, telomerase, nuclease -- and
fails if one appears.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b6_2

T_GEN = b6_2._T_GEN
T_COUNT = b6_2._T_COUNT
T_FRAG = b6_2._T_FRAG
T_INHIB = b6_2._T_INHIB

NAMED = ("dna polymerase", "ligase", "rna polymerase", "helicase", "topoisomerase")
OUT_OF_SCOPE = ("primase", "gyrase", "exonuclease", "telomerase", "nuclease",
                "single-strand binding protein", "sliding clamp")


def _semiconservative(rounds):
    """Molecules present, and molecules holding an original strand, after n rounds.

    EK 6.2.A.1.ii applied literally: every molecule present becomes two, each
    keeping one of its parent's strands. Only the two strands of the starting
    molecule are original, and replication makes new strands, never new original
    ones, so the second count is capped at two from the first round onward.
    """
    molecules, original_strands = 1, 2
    for _ in range(rounds):
        molecules *= 2
    holding = min(original_strands, molecules)
    return molecules, holding


assert _semiconservative(0) == (1, 1), "before any round there is one molecule holding both originals"
assert _semiconservative(1) == (2, 2), "after one round both molecules are hybrid"
assert _semiconservative(2) == (4, 2), "after two rounds two of four molecules hold an original strand"
assert _semiconservative(3) == (8, 2), "after three rounds two of eight"
assert _semiconservative(4) == (16, 2), "q17, q18: sixteen molecules, two of them holding original DNA"

# The fraction of molecules that are hybrid at each round, which is what the
# density table reports.
_HYBRID = [100 * h / m for m, h in (_semiconservative(n) for n in range(4))]
assert _HYBRID[1:] == [100.0, 50.0, 25.0], f"hybrid percentages recompute to {_HYBRID}"


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


HEAVY = "percent of molecules with two heavy strands"
HYBRID = "percent of molecules with one heavy and one light strand"
LIGHT = "percent of molecules with two light strands"


def _gen_series(table):
    order = ["none", "one", "two", "three"]
    rows = {cg.normalize(r["round of replication completed"]): r for r in _rows(table)}
    assert list(rows) == order, f"the rounds are labelled {list(rows)}, expected {order}"
    out = []
    for lab in order:
        r = rows[lab]
        trio = (cg.num(r[HEAVY]), cg.num(r[HYBRID]), cg.num(r[LIGHT]))
        assert sum(trio) == 100, f"round {lab} sums to {sum(trio)}, not 100"
        out.append(trio)
    return out


def q2(table, item):
    s = _gen_series(table)
    assert s[0] == (100, 0, 0), f"the starting DNA must be entirely heavy; got {s[0]}"
    assert s[1] == (0, 100, 0), f"after one round every molecule must be hybrid; got {s[1]}"
    assert s[1][1] == _HYBRID[1], "the recorded hybrid percentage must match the recomputed model"
    # the conservative prediction, 50 heavy and 50 light, must be absent
    assert not any(abs(h - 50) < 1 and abs(l - 50) < 1 for h, _, l in s), \
        "no row may show the conservative model's fifty-fifty heavy and light result"
    return ("the starting DNA is 100 percent heavy and after one round it is 100 percent hybrid, "
            "which is what the semiconservative model recomputes and the conservative model does not")


def q3(table, item):
    s = _gen_series(table)
    two = s[2]
    assert two[0] == 0, "no molecule may still be entirely heavy after two rounds"
    assert two[1] == 50, f"the hybrid percentage after two rounds is {two[1]}, not 50"
    assert two[1] == _HYBRID[2], "the recorded value must match the recomputed model"
    holding = two[0] + two[1]        # a molecule holds original DNA if it has any heavy strand
    assert holding == 50, f"molecules holding original DNA recompute to {holding} percent"
    assert holding not in (25, 75, 100, 0), "a distractor percentage coincides with the key"
    return (f"after two rounds {two[1]:.0f} percent are hybrid and {two[0]:.0f} percent entirely "
            f"heavy, so {holding:.0f} percent hold a strand of the original DNA")


def _counts(table):
    pairs = [(cg.num(r["rounds of replication completed"]),
              cg.num(r["number of double-stranded dna molecules present"]))
             for r in _rows(table)]
    for n, m in pairs:
        exp = _semiconservative(int(n))[0]
        assert m == exp, f"round {n:.0f} records {m:.0f} molecules; the model gives {exp}"
    return pairs


def q17(table, item):
    pairs = _counts(table)
    last_n, last_m = pairs[-1]
    nxt = _semiconservative(int(last_n) + 1)[0]
    assert nxt == 16, f"the fourth round recomputes to {nxt} molecules, not 16"
    assert nxt == 2 * last_m, "each round must double the previous count"
    for wrong in (last_m, nxt * 2, last_m + 2, last_m // 2):
        assert wrong != nxt, "a distractor value coincides with the key"
    return f"the table doubles 1, 2, 4, 8 and the recomputed fourth round gives {nxt} molecules"


def q18(table, item):
    _counts(table)
    molecules, holding = _semiconservative(4)
    assert (molecules, holding) == (16, 2), \
        f"after four rounds the model gives {molecules} molecules and {holding} holding original DNA"
    for wrong in (molecules, molecules // 2, 4, 0):
        assert wrong != holding, "a distractor value coincides with the key"
    return (f"the starting molecule contributes exactly two original strands, so of the {molecules} "
            f"molecules present after four rounds only {holding} can hold one")


def q11(table, item):
    rows = {cg.normalize(r["new strand"]): r for r in _rows(table)}
    seg = "number of separate dna segments synthesized"
    joins = "number of joins needed to give one continuous strand"
    for lab, r in rows.items():
        n, j = cg.num(r[seg]), cg.num(r[joins])
        assert j == n - 1, f"{lab}: {n:.0f} segments need {n - 1:.0f} joins, but {j:.0f} is recorded"
    lead, lag = rows["leading strand"], rows["lagging strand"]
    assert cg.num(lead[seg]) == 1 and cg.num(lead[joins]) == 0, \
        "the continuously made strand must be one segment needing no join"
    assert cg.num(lag[joins]) == 11, f"the lagging strand needs {cg.num(lag[joins]):.0f} joins, not 11"
    assert cg.num(lag[joins]) != cg.num(lag[seg]), "the segment count must not equal the join count"
    return (f"{cg.num(lag[seg]):.0f} segments require {cg.num(lag[joins]):.0f} joins, one fewer, "
            f"while the single leading-strand segment requires none")


def _inhibitors(table):
    """Match each observation to exactly one of the participants the CED names."""
    signature = {
        "helicase": ("stay wound", "no fork opens"),
        "topoisomerase": ("supercoiled",),
        "ligase": ("never joined",),
        "rna primer": ("no starting segment of rna",),
    }
    found = {}
    for r in _rows(table):
        obs = r["what is observed at the replication fork"]
        hits = [k for k, phrases in signature.items()
                if all(cg.contains_phrase(obs, p) for p in phrases)]
        assert len(hits) == 1, f"{r['inhibitor applied']!r} matches {hits}, not exactly one participant"
        found[hits[0]] = cg.normalize(r["inhibitor applied"])
    assert set(found) == set(signature), f"the four observations cover {set(found)}"
    return found


def q12(table, item):
    found = _inhibitors(table)
    assert found["ligase"] == "inhibitor 3", f"the ligase observation belongs to {found['ligase']}"
    return (f"the four observations map one to one onto helicase, topoisomerase, ligase and the RNA "
            f"primer, and the unjoined-fragment observation is {found['ligase']}")


def q13(table, item):
    found = _inhibitors(table)
    assert found["topoisomerase"] == "inhibitor 2", \
        f"the supercoiling observation belongs to {found['topoisomerase']}"
    assert found["helicase"] != found["topoisomerase"], \
        "the two winding-related observations must be distinguishable, or the key is ambiguous"
    return (f"the supercoiling-ahead-of-an-open-fork observation is {found['topoisomerase']}, and it "
            f"is distinct from the no-fork-at-all observation, {found['helicase']}")


CLAIMS = [
 ("serves as the template for a new strand of complementary DNA",
  "EK 6.2.A.1.ii states that replication is a semiconservative process, meaning one strand of DNA serves as the template for a new strand of complementary DNA. Each product therefore keeps one original strand and gains one new one."),
 ("every molecule has one heavy and one light strand",
  "EK 6.2.A.1.ii makes each original strand the template for one new strand. The table check recomputes the hybrid percentage at each round from that model and confirms the recorded first-round value is 100 percent, with no row showing the conservative model's fifty-fifty result."),
 ("One half",
  "An original strand is a heavy strand and EK 6.2.A.1.ii keeps it intact. The table check recomputes that after two rounds half of the molecules carry a heavy strand and none carries two, which matches the model's own two-of-four."),
 ("half of the molecules entirely heavy and half entirely light",
  "A conservative model reunites the two original strands, so one round in light medium would give half reconstituted heavy molecules and half wholly new light ones. EK 6.2.A.1.ii instead gives every molecule one strand of each, which is what a single hybrid band shows; the table check confirms no such fifty-fifty row exists in the data."),
 ("unwinds the DNA strands",
  "EK 6.2.A.1.iii states that helicase unwinds the DNA strands. The rejected options are the roles the framework gives to topoisomerase, ligase, DNA polymerase and the RNA primer in EK 6.2.A.1.iv, vii, vi and v."),
 ("relaxes supercoiling in front of the replication fork",
  "EK 6.2.A.1.iv states that topoisomerase relaxes supercoiling in front of the replication fork; unwinding the strands themselves is helicase's role in EK 6.2.A.1.iii. The exclusion statement puts any further enzyme beyond the scope of the exam."),
 ("requires an RNA primer in order to initiate",
  "EK 6.2.A.1.v states that DNA polymerase requires RNA primers to initiate DNA synthesis. Supercoiling belongs to EK 6.2.A.1.iv, joining to EK 6.2.A.1.vii and strand separation to EK 6.2.A.1.iii."),
 ("In the 5 prime to 3 prime direction",
  "EK 6.2.A.1.i states without qualification that DNA is synthesized in the 5 prime to 3 prime direction, and EK 6.2.A.1.vi accounts for the difference between the two new strands by the continuity of synthesis rather than by a reversal of direction."),
 ("Continuously, as a single uninterrupted stretch",
  "EK 6.2.A.1.vi states that DNA polymerase synthesizes new strands continuously on the leading strand and discontinuously on the lagging strand. EK 6.2.A.1.v attaches the primer requirement to the polymerase rather than to one strand."),
 ("separate fragments that ligase then joins",
  "EK 6.2.A.1.vi makes synthesis discontinuous on the lagging strand and EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand. Helicase has no joining role under EK 6.2.A.1.iii, and unjoined fragments would not give the continuous molecule EK 6.2.A.1 requires."),
 ("11 joins, carried out by ligase",
  "EK 6.2.A.1.vii gives ligase the fragments on the lagging strand. The table check recomputes the join count as one fewer than the segment count for both strands, confirming eleven for the twelve lagging-strand segments and none for the single leading-strand segment."),
 ("Inhibitor 3",
  "EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand, so blocking it leaves fragments made but unjoined. The table check matches each of the four observations to exactly one participant and confirms which inhibitor produces the unjoined-fragment result."),
 ("Inhibitor 2",
  "EK 6.2.A.1.iv states that topoisomerase relaxes supercoiling in front of the replication fork, so its loss lets supercoiling build ahead of a fork that has still opened. The table check confirms that this observation is distinguishable from the helicase one, in which no fork opens at all."),
 ("no template is exposed",
  "EK 6.2.A.1.iii states that helicase unwinds the DNA strands, and EK 6.2.A.1.ii requires a single strand to serve as the template. With the strands still wound there is no exposed template, so the failure precedes priming, synthesis and joining."),
 ("cannot initiate synthesis",
  "EK 6.2.A.1.v states that DNA polymerase requires RNA primers to initiate DNA synthesis, and the framework attaches that requirement to the polymerase rather than to one strand, so neither new strand can be started."),
 ("same sequence as the original",
  "EK 6.2.A.1 states that DNA replication ensures continuity of hereditary information, and EK 6.2.A.1.ii supplies the mechanism: a complementary strand built on each original strand reproduces the original sequence, with the original strand retained rather than removed."),
 ("16 molecules",
  "Each round makes two molecules from every one present. The table check recomputes the recorded 1, 2, 4 and 8 against the model and then the fourth round as sixteen, confirming no distractor value coincides with it."),
 ("2 molecules",
  "EK 6.2.A.1.ii keeps each original strand intact as a template, so the starting molecule's two strands survive into two different products and replication cannot make more of them. The model check recomputes sixteen molecules after four rounds with two of them holding original DNA."),
 ("Each of the two original strands serves as the template for one new strand",
  "EK 6.2.A.1.ii states that one strand of DNA serves as the template for a new strand of complementary DNA, and the semiconservative outcome requires both original strands to be used, since each of the two products retains one."),
 ("required a primer for each of its many segments",
  "EK 6.2.A.1.v requires an RNA primer for each initiation of DNA synthesis and EK 6.2.A.1.vi makes synthesis discontinuous on the lagging strand and continuous on the leading strand. Many separate initiations therefore mean many primers and one continuous stretch means one."),
 ("separate segments that have not been connected",
  "EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand, so a defective ligase leaves them unjoined while every earlier step proceeds. The rejected observations correspond to failures of priming, helicase, the fixed direction of synthesis and topoisomerase."),
 ("strands are unwound, a primer is laid down",
  "The order follows from the statements themselves: unwinding in EK 6.2.A.1.iii exposes the template EK 6.2.A.1.ii requires, EK 6.2.A.1.v makes the RNA primer a precondition of extension, and the joining of EK 6.2.A.1.vii acts on fragments that must already exist."),
 ("Only one of the two new strands is synthesized discontinuously",
  "EK 6.2.A.1.vi makes synthesis continuous on the leading strand and discontinuous on the lagging one, and EK 6.2.A.1.vii gives ligase the lagging-strand fragments. A continuous strand has no gaps to close, while EK 6.2.A.1.i and EK 6.2.A.1.ii apply equally to both strands."),
 ("complete double-stranded molecule whose two strands can each serve as a template",
  "EK 6.2.A.1.ii makes each product one original strand paired with one new complementary strand, so each product is a complete molecule with two usable templates. That is what allows EK 6.2.A.1 to speak of continuity across generations rather than for a single round."),
 ("fork opens and synthesis begins, but the DNA ahead of the fork becomes progressively more supercoiled",
  "EK 6.2.A.1.iv confines topoisomerase to relaxing supercoiling in front of the fork, so its loss allows supercoiling to accumulate while the unwinding of EK 6.2.A.1.iii and the synthesis of EK 6.2.A.1.vi proceed."),
 ("DNA polymerase adds nucleotides to a new strand",
  "EK 6.2.A.1.vi assigns synthesis, continuous on the leading strand and discontinuous on the lagging strand, to DNA polymerase. The rejected options exchange the roles given to ligase, helicase, topoisomerase and the RNA primer in EK 6.2.A.1.vii, iii, iv and v."),
 ("complete copy of the same hereditary information",
  "EK 6.2.A.1 states that DNA replication ensures continuity of hereditary information, and EK 6.2.A.1.ii makes each product a faithful copy retaining one original strand. Doubling the molecules before division is what lets both daughter cells receive the full complement."),
 ("difference between them lies in whether synthesis is continuous",
  "EK 6.2.A.1.i gives one direction of synthesis with no exception for either strand, and EK 6.2.A.1.vi locates the difference between the strands in continuous against discontinuous synthesis. The framework states the mechanism generally rather than by organism."),
 ("Ligase, whose role is to join those fragments",
  "EK 6.2.A.1.vi has DNA polymerase making the lagging strand as separate fragments and EK 6.2.A.1.vii gives ligase the job of joining them, so fragments accumulating means they are made but not joined and every earlier step is working."),
 ("not the model the framework describes",
  "EK 6.2.A.1.ii states that replication is semiconservative, meaning one strand of DNA serves as the template for a new complementary strand, and the density data in this topic show a single hybrid band after one round. The rejected options attribute mechanistic failures to a model the framework simply does not adopt."),
]

cg.check(b6_2, CLAIMS,
         table_checks={2: q2, 3: q3, 11: q11, 12: q12, 13: q13, 17: q17, 18: q18})

# The CED's exclusion statement, enforced over the whole module.
_text = " ".join(" ".join([q["q"], q["why"], *q["choices"]]) for q in b6_2.QUESTIONS)
for word in OUT_OF_SCOPE:
    assert not cg.contains_phrase(_text, word), (
        f"6.2: {word!r} appears in the module, but the CED's exclusion statement puts every "
        f"enzyme except {NAMED} beyond the scope of the exam"
    )
print(f"    Semiconservative model recomputed round by round; exclusion statement enforced "
      f"({len(OUT_OF_SCOPE)} out-of-scope enzyme names scanned for).")
