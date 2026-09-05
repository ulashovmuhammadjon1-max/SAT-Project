"""Assert every authored module's TOPIC title matches its subject's topic file.

    python3 check_topic_titles.py [SUBJECT ...]

Every brief says "copy the title VERBATIM out of the JSON, do not retype it",
and nothing enforced it. One module retyped `Earth's` with a straight
apostrophe where the CED has the curly U+2019, shipped 30 questions under a
title that differed from the course outline's, and it was found only by
diffing the committed topic file against production months later.

The titles matter beyond display: `gen_course_units.py` builds the outline a
student navigates from the JSON, while `export_units.py` writes `topicTitle`
from the MODULE. Nothing joins on the title -- the code is the key -- so a
mismatch is cosmetic rather than dangerous, which is exactly why it survives
unnoticed.

NEGATIVE CONTROL: `--selftest` corrupts a title in memory and asserts the
check fires.
"""
import importlib
import json
import os
import re
import sys

# Verified by importing each prefix's first module and reading its TOPIC, not
# assumed from the order words appear in a brief. A first attempt had `u` and
# `v` the wrong way round and reported 30 false problems -- `u` is Micro
# ("Demand") and `v` is US Government ("Ideals of Democracy").
#
# Only the subjects with a committed <SUBJECT>_topics.json can be checked at
# all; the rest predate that convention and are listed so the gap is visible
# rather than silent.
PREFIX = {"BIOLOGY": "b", "CHEMISTRY": "h", "ENV_SCI": "e", "WORLD_HISTORY": "w", "US_HISTORY": "a",
          "HUMAN_GEO": "g", "US_GOV": "v", "COMP_GOV": "k", "PSYCHOLOGY": "p",
          "MICRO": "u", "MACRO": "m", "STATISTICS": "s"}


def modules(pre):
    return sorted((f[:-3] for f in os.listdir(".") if re.match(rf"^{pre}\d+_\d+\.py$", f)),
                  key=lambda s: [int(x) for x in s[len(pre):].split("_")])


def check(subject, mutate=None):
    path = f"{subject}_topics.json"
    if not os.path.exists(path):
        return []
    topics = json.load(open(path, encoding="utf-8"))
    problems = []
    for name in modules(PREFIX[subject]):
        mod = importlib.import_module(name)
        code, title, unit = mod.TOPIC
        if mutate and name == mutate:
            title = title + " (corrupted)"
        if code not in topics:
            problems.append(f"{subject} {name}: code {code!r} is not in {path}")
        elif topics[code] != title:
            problems.append(
                f"{subject} {name}: module {title!r} != topic file {topics[code]!r}")
        if str(unit) != code.split(".")[0]:
            problems.append(f"{subject} {name}: unit {unit} does not match code {code}")
    return problems


def main():
    subjects = [a for a in sys.argv[1:] if not a.startswith("--")] or list(PREFIX)
    if "--selftest" in sys.argv:
        for subject in subjects:
            names = modules(PREFIX[subject])
            # A subject with no topic file cannot be checked at all, so a
            # control on it would pass by doing nothing -- the exact shape of
            # "a checker that cannot fail". Say so instead of skipping quietly.
            if not names or not os.path.exists(f"{subject}_topics.json"):
                print(f"  (skipped {subject}: "
                      f"{'no modules' if not names else 'no topic file, so nothing is checked'})")
                continue
            assert check(subject, mutate=names[0]), (
                f"CONTROL FAILED: a corrupted title in {names[0]} did not raise"
            )
            print(f"  control OK  {subject}: a corrupted title in {names[0]} is caught")
        print("negative controls all fired.")
    problems = []
    for subject in subjects:
        problems += check(subject)
    for p in problems:
        print(" ", p)
    n = sum(len(modules(PREFIX[s])) for s in subjects if os.path.exists(f"{s}_topics.json"))
    print(f"{n} module(s) checked; {len(problems)} title problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
