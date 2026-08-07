import json, re
from mathify2 import mathify_stem, wrap_choice, basic_math_convert

raw = json.load(open("math_built_raw.json"))
out = {}

for module_key, arr in raw.items():
    built = []
    for q in arr:
        stem_html = "<p>" + mathify_stem(q["problem"]) + "</p>"
        item = {
            "type": q["type"],
            "stem": stem_html,
            "domain": q["domain_code"],
            "skill": q["skill_code"],
            "_source": q["source"], "_num": q["num"], "_verified": q.get("verified", ""),
        }
        if q["type"] == "MULTIPLE_CHOICE":
            choices = []
            correct_label = q["correct"]
            for c in q["choices"]:
                choices.append({"label": c["label"], "content": wrap_choice(c["content"])})
            item["choices"] = choices
            item["correct"] = correct_label
        else:
            item["correctAnswerFR"] = json.dumps([str(q["correct"])])
        built.append(item)
    out[module_key] = built

json.dump(out, open("math_final.json", "w"), indent=2, ensure_ascii=False)

# sanity scan for unconverted raw math syntax leaking through
issues = []
for mk, arr in out.items():
    for q in arr:
        blob = q["stem"] + json.dumps(q.get("choices", []))
        if re.search(r"sqrt\(", blob):
            issues.append((mk, q["_source"], q["_num"], "unconverted sqrt("))
        if re.search(r"(?<![A-Za-z])pi(?![A-Za-z])", blob.replace(r"\pi", "")):
            issues.append((mk, q["_source"], q["_num"], "unconverted pi"))
        if re.search(r"\^\d{2,}(?!\})", blob):
            issues.append((mk, q["_source"], q["_num"], "unbraced multi-digit exponent"))
for i in issues:
    print("ISSUE:", i)
print("total issues:", len(issues))
for mk, arr in out.items():
    print(mk, len(arr))
