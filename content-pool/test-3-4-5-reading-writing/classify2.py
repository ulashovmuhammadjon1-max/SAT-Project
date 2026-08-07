import re

# Fine-grained SAT R&W domain classifier.
# READING_ORDER must end in INFERENCE; nothing reading-domain may sort after it.
READING_ORDER = ["WORDS_BLANK", "WORDS_UNDER", "STRUCT", "CROSS",
                  "CENTRAL", "EVID_QUOTE", "EVID_GRAPH", "EVID_SUPPORT", "INFERENCE"]
WRITING_ORDER = ["SEC", "TRANSITIONS", "RHET_SYNTH"]
ORDER = READING_ORDER + WRITING_ORDER

def classify(q):
    stem = (q.get("stem") or "").strip()
    passage = (q.get("passage") or "").strip()
    stem_l = stem.lower()
    passage_l = passage.lower()

    if "bulleted notes" in passage_l or ("student" in stem_l and ("notes" in stem_l or "wants to" in stem_l)):
        return "RHET_SYNTH"
    if "given sentences" in stem_l or "given notes" in stem_l:
        return "RHET_SYNTH"

    if "logical transition" in stem_l:
        return "TRANSITIONS"

    if "conforms to the conventions of standard english" in stem_l:
        return "SEC"

    if ("text 1" in stem_l and "text 2" in stem_l) or ("text 1" in passage_l and "text 2" in passage_l):
        return "CROSS"

    if "most logical and precise word or phrase" in stem_l:
        return "WORDS_BLANK"
    if "most nearly mean" in stem_l:
        return "WORDS_UNDER"

    if ("main purpose" in stem_l or "primary purpose" in stem_l or "main function" in stem_l
            or re.search(r"function of.*underlined", stem_l) or "overall structure of the text" in stem_l):
        return "STRUCT"

    if "most logically" in stem_l and ("completes" in stem_l or "competes" in stem_l):
        return "INFERENCE"
    if "most reasonably be concluded" in stem_l or "most reasonably be inferred" in stem_l:
        return "INFERENCE"

    if re.search(r"which (finding|response)[^.?]*if true[^.?]*would most (directly|strongly)", stem_l):
        return "EVID_SUPPORT"
    if "best supports" in stem_l or "best supported by the text" in stem_l:
        return "EVID_SUPPORT"
    if "quotation" in stem_l or ("example" in stem_l and "illustrate" in stem_l):
        return "EVID_QUOTE"

    if "graph" in stem_l or "table" in stem_l or "data" in stem_l:
        return "EVID_GRAPH"

    if re.search(r"main ide", stem_l) or "central idea" in stem_l or "central claim" in stem_l:
        return "CENTRAL"
    if ("according to the text" in stem_l or "the text makes which point" in stem_l
            or "based on the text" in stem_l or "base on the text" in stem_l
            or "the author makes which point" in stem_l):
        return "CENTRAL"

    return "UNKNOWN"

if __name__ == "__main__":
    import json
    alloc = json.load(open("final_allocation.json"))
    pool_by_test = {0: [], 1: [], 2: []}
    for k, items in alloc.items():
        if "RW" not in k:
            continue
        t = int(k.split("|")[0])
        pool_by_test[t].extend(items)
    total_counts = {}
    for t, pool in pool_by_test.items():
        counts = {}
        for q in pool:
            c = classify(q)
            counts[c] = counts.get(c, 0) + 1
            total_counts[c] = total_counts.get(c, 0) + 1
        print(f"test {t} (n={len(pool)}):", counts)
    print("GLOBAL:", total_counts)
