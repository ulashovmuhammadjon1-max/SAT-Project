#!/usr/bin/env python3
"""
Compute the aggregate figures for the scholarly.space impact overview.

Reads the production database through Neon's HTTP SQL endpoint (the sandbox
blocks raw Postgres) using read-only SELECT statements, and writes
aggregates.json next to this file.

PRIVACY: only totals and a list of ISO country codes are written. No names,
emails, usernames, ids, or per-country counts are queried into the output.

Usage:
    PROD_URL='postgresql://...' python3 compute_aggregates.py

The connection string is read from the environment and never written to disk.
"""

import json
import os
import re
import ssl
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

# Accounts created by an administrator import on 2026-09-10 (1,371 accounts,
# no email, all inside this 14-minute window). They are excluded from
# "students registered" because they did not register through sign-up.
IMPORT_FILTER = (
    "(email IS NULL AND \"createdAt\" >= '2026-09-10T07:23:00Z' "
    "AND \"createdAt\" < '2026-09-10T07:37:00Z')"
)

QUERIES = {
    # --- figures used on the page ---
    "students_registered": (
        f'SELECT count(*)::int AS n FROM "User" WHERE role = \'STUDENT\' AND NOT {IMPORT_FILTER}'
    ),
    "country_codes": (
        'SELECT DISTINCT "countryCode" AS code FROM "User" '
        f"WHERE role = 'STUDENT' AND \"countryCode\" IS NOT NULL AND NOT {IMPORT_FILTER} "
        "ORDER BY 1"
    ),
    "mentorship_session_requests": 'SELECT count(*)::int AS n FROM "Booking"',
    "mentorship_sessions_held": (
        'SELECT count(DISTINCT b."slotId")::int AS n FROM "Booking" b '
        'JOIN "MentorSlot" s ON s.id = b."slotId" '
        "WHERE b.status = 'COMPLETED' AND s.\"startsAt\" < now()"
    ),
    # --- checked, reported, not used on the page ---
    "student_accounts_all": "SELECT count(*)::int AS n FROM \"User\" WHERE role = 'STUDENT'",
    "student_accounts_admin_import": (
        f"SELECT count(*)::int AS n FROM \"User\" WHERE role = 'STUDENT' AND {IMPORT_FILTER}"
    ),
    "country_codes_all_students": (
        'SELECT DISTINCT "countryCode" AS code FROM "User" '
        "WHERE role = 'STUDENT' AND \"countryCode\" IS NOT NULL ORDER BY 1"
    ),
    "mentors_approved": (
        "SELECT count(*)::int AS n FROM \"PeerMentorApplication\" WHERE status = 'APPROVED'"
    ),
    "mentor_slot_hosts": 'SELECT count(DISTINCT "hostId")::int AS n FROM "MentorSlot"',
    "financial_literacy_sessions_held": (
        'SELECT count(DISTINCT b."slotId")::int AS n FROM "Booking" b '
        'JOIN "MentorSlot" s ON s.id = b."slotId" '
        "WHERE b.status = 'COMPLETED' AND s.\"startsAt\" < now() "
        "AND s.\"sessionType\" = 'FINANCIAL_LITERACY'"
    ),
    "financial_literacy_slots_any": (
        "SELECT count(*)::int AS n FROM \"MentorSlot\" WHERE \"sessionType\" = 'FINANCIAL_LITERACY'"
    ),
    "research_proposals_accepted": (
        "SELECT count(*)::int AS n FROM \"ResearchProposal\" WHERE status = 'ACCEPTED'"
    ),
}


def neon_query(conn: str, query: str) -> list[dict]:
    if not re.match(r"^\s*SELECT\b", query, re.I):
        raise ValueError("read-only: only SELECT statements are allowed")
    host = urllib.parse.urlparse(conn).hostname
    endpoint = "https://" + re.sub(r"^[^.]+\.", "api.", host) + "/sql"
    req = urllib.request.Request(
        endpoint,
        data=json.dumps({"query": query, "params": []}).encode(),
        headers={"Content-Type": "application/json", "Neon-Connection-String": conn},
        method="POST",
    )
    cafile = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    ctx = ssl.create_default_context(cafile=cafile if Path(cafile).exists() else None)
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        return json.loads(resp.read())["rows"]


def journal_papers_published() -> int:
    """Entries in the published-papers registry (src/lib/journal/papers.ts)."""
    src = (REPO / "src/lib/journal/papers.ts").read_text()
    array = src[src.index("export const JOURNAL_PAPERS"): src.index("export function paperBySlug")]
    return len(re.findall(r'^\s+slug:\s*"', array, re.M))


def main() -> None:
    conn = os.environ.get("PROD_URL")
    if not conn:
        sys.exit("Set PROD_URL to the production connection string.")

    results = {name: neon_query(conn, sql) for name, sql in QUERIES.items()}
    count = lambda name: results[name][0]["n"]

    codes = [r["code"] for r in results["country_codes"]]
    codes_all = [r["code"] for r in results["country_codes_all_students"]]

    papers = journal_papers_published()
    now = datetime.now(timezone.utc)

    out = {
        "computed_at_utc": now.isoformat(timespec="seconds"),
        "computed_on": now.strftime("%-d %B %Y"),
        "source": "scholarly.space production database (read-only SELECT queries)",
        "figures": {
            "students_registered": {
                "value": count("students_registered"),
                "label": "Students registered",
                "query": QUERIES["students_registered"],
            },
            "countries_represented": {
                "value": len(codes),
                "label": "Countries represented",
                "query": QUERIES["country_codes"] + "  -- value = number of rows",
            },
            "mentorship_session_requests": {
                "value": count("mentorship_session_requests"),
                "label": "Mentorship session requests",
                "query": QUERIES["mentorship_session_requests"],
            },
            "mentorship_sessions_held": {
                "value": count("mentorship_sessions_held"),
                "label": "Mentorship sessions held",
                "query": QUERIES["mentorship_sessions_held"],
            },
            "papers_published": {
                "value": papers,
                "label": "Papers published",
                "query": "count of entries in JOURNAL_PAPERS, src/lib/journal/papers.ts",
            },
        },
        # Codes only. No per-country counts are queried or stored.
        "country_codes": codes,
        "checked_not_used": {
            "student_accounts_all": count("student_accounts_all"),
            "student_accounts_admin_import": count("student_accounts_admin_import"),
            "country_set_same_with_import_included": codes == codes_all,
            "mentors_approved": count("mentors_approved"),
            "mentor_slot_hosts": count("mentor_slot_hosts"),
            "matches_made": "no matching record type exists in the schema",
            "financial_literacy_sessions_held": count("financial_literacy_sessions_held"),
            "financial_literacy_slots_any": count("financial_literacy_slots_any"),
            "research_proposals_accepted": count("research_proposals_accepted"),
        },
        "queries": QUERIES,
    }

    (HERE / "aggregates.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v["value"] for k, v in out["figures"].items()}, indent=2))
    print("checked_not_used:", json.dumps(out["checked_not_used"]))


if __name__ == "__main__":
    main()
