# -*- coding: utf-8 -*-
"""Classifies every Test 1 question (all 6 modules) into a College Board
domain + skill, using stem/passage phrasing patterns. Best-effort, same
spirit as the AI extraction pipeline's domainGuess/skillGuess -- the admin
can correct any of these later via the existing question editor.
"""
import json
import re

RW_DOMAINS_SKILLS = {
    "Craft and Structure": ["Words in Context", "Text Structure and Purpose", "Cross-Text Connections"],
    "Information and Ideas": ["Central Ideas and Details", "Command of Evidence", "Inferences"],
    "Standard English Conventions": ["Boundaries", "Form, Structure, and Sense"],
    "Expression of Ideas": ["Rhetorical Synthesis", "Transitions"],
}
MATH_DOMAINS_SKILLS = {
    "Algebra": ["Linear Equations and Systems", "Linear Functions", "Linear Inequalities"],
    "Advanced Math": ["Nonlinear Functions", "Equivalent Expressions", "Nonlinear Equations and Systems"],
    "Problem-Solving and Data Analysis": ["Ratios, Rates, and Proportions", "Data Interpretation", "Statistics and Probability"],
    "Geometry and Trigonometry": ["Area and Volume", "Lines, Angles, and Triangles", "Trigonometry"],
}


def classify_rw(passage, stem):
    s = stem.strip()
    blob = (passage + " " + stem).lower()

    if re.search(r"completes the text with the most logical and precise word or phrase", s, re.I):
        return "Craft and Structure", "Words in Context"
    if re.search(r"as used in (the|this) text.{0,40}most nearly mean", s, re.I):
        return "Craft and Structure", "Words in Context"
    if re.search(r"function of the (underlined|selected|highlighted)|main purpose of (the|this) text|text as a whole", s, re.I):
        return "Craft and Structure", "Text Structure and Purpose"
    if re.search(r"\btext 1\b.*\btext 2\b|both texts|text 2.{0,20}respond to text 1", blob, re.I):
        return "Craft and Structure", "Cross-Text Connections"

    if re.search(r"which quotation", s, re.I):
        return "Information and Ideas", "Command of Evidence"
    if re.search(r"data from the (graph|table)", s, re.I):
        return "Information and Ideas", "Command of Evidence"
    if re.search(r"(finding|result|data).{0,40}(support|weaken|undermine)", s, re.I):
        return "Information and Ideas", "Command of Evidence"
    if re.search(r"main (idea|point|claim)|central (idea|claim)|according to the text", s, re.I):
        return "Information and Ideas", "Central Ideas and Details"
    if re.search(r"most logically completes the text\??$|most reasonably be concluded|best supports", s, re.I):
        return "Information and Ideas", "Inferences"

    if re.search(r"student.{0,15}(wants|notes)|relevant information from the notes|information from the given sentences|given sentences", blob, re.I):
        return "Expression of Ideas", "Rhetorical Synthesis"
    if re.search(r"most logical transition", s, re.I):
        return "Expression of Ideas", "Transitions"

    if re.search(r"conventions of standard english", s, re.I):
        if re.search(r"\bcomma\b|\bsemicolon\b|\bcolon\b|\bapostrophe\b|independent clause|sentence boundary", blob, re.I):
            return "Standard English Conventions", "Boundaries"
        return "Standard English Conventions", "Form, Structure, and Sense"

    # Fallback: unmatched patterns default to the most common R&W skill.
    return "Information and Ideas", "Central Ideas and Details"


def classify_math(problem):
    p = problem.lower()

    if re.search(r"triangle|angle|circle|radius|diameter|circumference|degree|parallel|perpendicular|hypotenuse|\bsin\b|\bcos\b|\btan\b|trig", p):
        if re.search(r"\bsin\b|\bcos\b|\btan\b|trig", p):
            return "Geometry and Trigonometry", "Trigonometry"
        if re.search(r"area|volume|surface area|cubic|square (centimeters|units|meters|feet|inches)", p):
            return "Geometry and Trigonometry", "Area and Volume"
        return "Geometry and Trigonometry", "Lines, Angles, and Triangles"

    if re.search(r"percent|percentage|ratio\b|proportion|rate of|per hour|per mile|per minute|per gallon", p):
        return "Problem-Solving and Data Analysis", "Ratios, Rates, and Proportions"

    if re.search(r"scatterplot|mean|median|mode|standard deviation|probability|survey|margin of error", p):
        if re.search(r"probability|standard deviation|\bmean\b|\bmedian\b|\bmode\b|margin of error|sample|survey", p):
            return "Problem-Solving and Data Analysis", "Statistics and Probability"
        return "Problem-Solving and Data Analysis", "Data Interpretation"

    if re.search(r"increase(d|s)? by (approximately )?\d+%|decrease(d|s)? by (approximately )?\d+%|compounded|each year|each month|previous year", p):
        return "Advanced Math", "Nonlinear Equations and Systems"

    if re.search(r"\^|squared|cubed|quadratic|parabola|exponential|exponent|nonlinear|sqrt|radical|factor|expand|equivalent to", p):
        if re.search(r"equivalent to|factor|expand|simplif", p):
            return "Advanced Math", "Equivalent Expressions"
        if re.search(r"maximum|minimum|vertex|zero(s)? (of|at)|end behavior|graph of", p):
            return "Advanced Math", "Nonlinear Functions"
        return "Advanced Math", "Nonlinear Equations and Systems"

    if re.search(r"\bthe graph shows\b|\baccording to the graph\b", p) and not re.search(r"=\s*-?\d", p):
        return "Problem-Solving and Data Analysis", "Data Interpretation"

    if re.search(r"system of equations|two equations", p):
        return "Algebra", "Linear Equations and Systems"
    if re.search(r"f\(x\)|g\(x\)|function f|function g|slope|y-intercept|linear function", p):
        return "Algebra", "Linear Functions"
    if re.search(r"inequality|inequalities|at least|at most|no more than|no less than", p):
        return "Algebra", "Linear Inequalities"

    return "Algebra", "Linear Equations and Systems"


DIAGRAM_BRACKET = re.compile(r"\s*\[(?:DIAGRAM|TABLE|Diagram|Scatterplot)[^\]]*\]\s*")


def strip_diagram_note(text):
    """Once a real diagram image is attached, the bracketed text
    description of it (written during transcription, before any image
    existed) is redundant clutter sitting right next to the real image --
    remove it and collapse the resulting double space."""
    if not text:
        return text
    cleaned = DIAGRAM_BRACKET.sub(" ", text)
    return re.sub(r"\s+", " ", cleaned).strip()


def main():
    alloc = json.load(open("/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad/batch2/pool/final_allocation_2tests.json"))
    out = {}
    for key in ["0|RW_M1", "0|RW_M2_EASY", "0|RW_M2_HARD", "0|MATH_M1", "0|MATH_M2_EASY", "0|MATH_M2_HARD"]:
        items = alloc[key]
        classified = []
        for q in items:
            qc = dict(q)
            qc["problem"] = strip_diagram_note(qc.get("problem", ""))
            qc["stem"] = strip_diagram_note(qc.get("stem", ""))
            qc["passage"] = strip_diagram_note(qc.get("passage", ""))
            if "RW" in key:
                domain, skill = classify_rw(qc["passage"], qc["stem"])
            else:
                domain, skill = classify_math(qc["problem"])
            qc["domain"] = domain
            qc["skill"] = skill
            classified.append(qc)
        out[key] = classified

    json.dump(out, open("/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad/batch2/pool/test1_classified.json", "w"), indent=2)

    # Print a distribution summary for a sanity check.
    for key, items in out.items():
        counts = {}
        for q in items:
            k = f"{q['domain']} / {q['skill']}"
            counts[k] = counts.get(k, 0) + 1
        print(f"\n=== {key} ({len(items)}) ===")
        for k, c in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {c:3d}  {k}")


if __name__ == "__main__":
    main()
