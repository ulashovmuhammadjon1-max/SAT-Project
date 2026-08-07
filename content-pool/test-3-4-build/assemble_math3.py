import json, random
from collections import defaultdict

random.seed(7)
pool = json.load(open("math_pool.json"))
MODULES = ["test3|M1", "test3|M2E", "test3|M2H", "test4|M1", "test4|M2E", "test4|M2H"]

by_skill = defaultdict(list)
for q in pool:
    by_skill[q["skill_code"]].append(q)
for s in by_skill:
    random.shuffle(by_skill[s])

SKILL_ORDER = {
    "GT": ["GT-AV", "GT-LA", "GT-TR"],
    "PSDA": ["PSDA-RP", "PSDA-ST", "PSDA-DI"],
    "ADV": ["ADV-NF", "ADV-NE", "ADV-EQ"],
    "ALG": ["ALG-LE", "ALG-LF", "ALG-LI"],
}
DOMAIN_QUOTA = {"GT": 4, "PSDA": 4, "ADV": 6, "ALG": 8}
ALL_SKILLS = [s for skills in SKILL_ORDER.values() for s in skills]

modules_out = {m: [] for m in MODULES}
fr_count = {m: 0 for m in MODULES}


def pop_strict(skill, module):
    """Pop from skill queue respecting FR cap (<=3/module). Returns None if none available under cap."""
    lst = by_skill[skill]
    allow_fr = fr_count[module] < 3
    for i, q in enumerate(lst):
        if q["type"] == "FREE_RESPONSE" and not allow_fr:
            continue
        return lst.pop(i)
    return None


def add(module, q):
    modules_out[module].append(q)
    if q["type"] == "FREE_RESPONSE":
        fr_count[module] += 1


shortfall = defaultdict(int)

for domain in ["GT", "PSDA", "ADV", "ALG"]:
    quota = DOMAIN_QUOTA[domain]
    skills = SKILL_ORDER[domain]
    for m in MODULES:
        got = 0
        si = 0
        guard = 0
        while got < quota and guard < 200:
            guard += 1
            skill = skills[si % len(skills)]
            si += 1
            q = pop_strict(skill, m)
            if q is None:
                # try other skills in same domain
                found = None
                for sk2 in skills:
                    q2 = pop_strict(sk2, m)
                    if q2:
                        found = q2
                        break
                if found is None:
                    continue  # truly nothing left under cap for this domain right now
                q = found
            add(m, q)
            got += 1
        if got < quota:
            shortfall[m] += quota - got

print("shortfall after strict pass:", dict(shortfall))

# top-up pass: fill any module short of 22 using MC-only from ANY skill with remaining supply
for m in MODULES:
    while len(modules_out[m]) < 22:
        placed = False
        for skill in ALL_SKILLS:
            lst = by_skill[skill]
            for i, q in enumerate(lst):
                if q["type"] == "MULTIPLE_CHOICE":
                    add(m, lst.pop(i))
                    placed = True
                    break
            if placed:
                break
        if not placed:
            print(f"CANNOT FILL {m}, stuck at {len(modules_out[m])}")
            break

for m in MODULES:
    arr = modules_out[m]
    dom = defaultdict(int)
    for q in arr:
        dom[q["domain_code"]] += 1
    fr = sum(1 for q in arr if q["type"] == "FREE_RESPONSE")
    print(m, "len=", len(arr), "domains=", dict(dom), "FR=", fr)

leftover = sum(len(v) for v in by_skill.values())
print("leftover unused pool:", leftover)

json.dump(modules_out, open("math_built_raw.json", "w"), indent=2, ensure_ascii=False)
