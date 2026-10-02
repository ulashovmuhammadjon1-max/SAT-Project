#!/usr/bin/env python3
"""
Build scholarly_impact_overview.pdf (A4, one page) from aggregates.json.

- Every number on the page is read from aggregates.json; nothing is typed in.
- The map shades countries from the stored ISO codes. No per-country numbers
  exist in the input, so none can appear on the page.
- Map boundaries: Natural Earth 1:110m (public domain); countries too small to
  draw at that scale are marked with a circle placed from the 1:50m data.
- Rendered with Chromium via Playwright; fonts are embedded by Chromium.

Usage:  python3 build_overview.py
"""

import json
import math
import subprocess
from html import escape
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT_PDF = HERE / "scholarly_impact_overview.pdf"
OUT_PNG = HERE / "scholarly_impact_overview.png"
CHROMIUM = "/opt/pw-browsers/chromium"

ACCENT = "#1F4E79"      # the one accent colour; reads as dark grey in black and white
LAND = "#DCE0E5"
INK = "#111111"
MUTED = "#555555"

# Countries Natural Earth does not map as a separate shape. Name and region are
# the ISO 3166-1 name and UN region; the point is the island's location.
FALLBACK = {
    "MQ": {"name": "Martinique", "region": "Americas", "lonlat": (-61.02, 14.64)},
}

# Shorter display names where Natural Earth's long form is formal.
DISPLAY_NAME = {
    "KR": "South Korea",
    "RU": "Russia",
    "LA": "Laos",
    "CD": "Democratic Republic of the Congo",
}

REGION_ORDER = ["Africa", "Americas", "Asia", "Europe", "Oceania"]


# --------------------------------------------------------------------------
# Projection: Equal Earth (Šavrič, Patterson, Jenny 2018)
# --------------------------------------------------------------------------
A1, A2, A3, A4 = 1.340264, -0.081106, 0.000893, 0.003796
M = math.sqrt(3) / 2


def equal_earth(lon: float, lat: float) -> tuple[float, float]:
    lam, phi = math.radians(lon), math.radians(lat)
    theta = math.asin(M * math.sin(phi))
    t2, t6 = theta * theta, theta ** 6
    x = (2 * math.sqrt(3) * lam * math.cos(theta)) / (
        3 * (9 * A4 * t6 * t2 + 7 * A3 * t6 + 3 * A2 * t2 + A1)
    )
    y = theta * (A1 + A2 * t2 + t6 * (A3 + A4 * t2))
    return x, -y


def code_of(props: dict) -> str | None:
    for k in ("ISO_A2_EH", "ISO_A2"):
        c = props.get(k)
        if c and c != "-99":
            return c
    return None


def polygons(geom: dict):
    if geom["type"] == "Polygon":
        yield geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        yield from geom["coordinates"]


def load(path: Path) -> list[dict]:
    return json.loads(path.read_text())["features"]


# --------------------------------------------------------------------------
# Map
# --------------------------------------------------------------------------
def build_map(codes: set[str], f110: list[dict], f50: list[dict]) -> tuple[str, list[str]]:
    feats = [f for f in f110 if code_of(f["properties"]) != "AQ"]

    xs, ys = [], []
    for f in feats:
        for poly in polygons(f["geometry"]):
            for lon, lat in poly[0]:
                x, y = equal_earth(lon, lat)
                xs.append(x)
                ys.append(y)
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    W = 1000.0
    s = W / (maxx - minx)
    H = (maxy - miny) * s

    def P(lon, lat):
        x, y = equal_earth(lon, lat)
        return (x - minx) * s, (y - miny) * s

    shaded, base = [], []
    drawn = set()
    for f in feats:
        c = code_of(f["properties"])
        d = []
        for poly in polygons(f["geometry"]):
            for ring in poly:
                pts = [P(lon, lat) for lon, lat in ring]
                d.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
        path = f'<path d="{"".join(d)}"/>'
        if c in codes:
            shaded.append(path)
            drawn.add(c)
        else:
            base.append(path)

    # Countries in the list but too small (or absent) at 1:110m: a circle.
    by50 = {code_of(f["properties"]): f for f in f50}
    markers, marked = [], []
    for c in sorted(codes - drawn):
        if c in by50:
            ring = max((p[0] for p in polygons(by50[c]["geometry"])), key=len)
            lon = sum(p[0] for p in ring) / len(ring)
            lat = sum(p[1] for p in ring) / len(ring)
        elif c in FALLBACK:
            lon, lat = FALLBACK[c]["lonlat"]
        else:
            continue
        x, y = P(lon, lat)
        markers.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6"/>')
        marked.append(c)

    svg = (
        f'<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="World map of countries represented">'
        f'<g fill="{LAND}" stroke="#FFFFFF" stroke-width="0.6">{"".join(base)}</g>'
        f'<g fill="{ACCENT}" stroke="#FFFFFF" stroke-width="0.6">{"".join(shaded)}</g>'
        f'<g fill="{ACCENT}" stroke="#FFFFFF" stroke-width="1.6">{"".join(markers)}</g>'
        f"</svg>"
    )
    return svg, marked


# --------------------------------------------------------------------------
# Country names grouped by region (names only)
# --------------------------------------------------------------------------
def names_by_region(codes: list[str], f110: list[dict], f50: list[dict]) -> dict[str, list[str]]:
    props = {}
    for f in f50 + f110:  # 110m wins where both exist
        c = code_of(f["properties"])
        if c:
            props[c] = f["properties"]
    groups: dict[str, list[str]] = {r: [] for r in REGION_ORDER}
    for c in codes:
        if c in props:
            name = DISPLAY_NAME.get(c, props[c]["NAME_LONG"])
            region = props[c]["REGION_UN"]
        elif c in FALLBACK:
            name, region = FALLBACK[c]["name"], FALLBACK[c]["region"]
        else:
            raise SystemExit(f"No name/region for country code {c}")
        groups.setdefault(region, []).append(name)
    return {r: sorted(v) for r, v in groups.items() if v}


# --------------------------------------------------------------------------
# Page
# --------------------------------------------------------------------------
def build_html(agg: dict, svg: str, regions: dict[str, list[str]], has_markers: bool) -> str:
    fig = agg["figures"]
    order = [
        "students_registered",
        "countries_represented",
        "mentorship_session_requests",
        "mentorship_sessions_held",
        "papers_published",
    ]
    stats = "".join(
        f'<div class="stat"><div class="num">{fig[k]["value"]:,}</div>'
        f'<div class="lbl">{escape(fig[k]["label"])}</div></div>'
        for k in order
    )
    region_rows = "".join(
        f'<div class="region"><div class="rname">{escape(r)}</div>'
        f'<div class="rlist">{escape(", ".join(names))}</div></div>'
        for r, names in regions.items()
    )
    marker_note = (
        '<p class="note">Circles mark countries too small to shade at this map scale.</p>'
        if has_markers
        else ""
    )

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>scholarly.space — Impact Overview</title>
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ background: #FFFFFF; }}
  body {{
    width: 210mm; height: 297mm; padding: 18mm 17mm 14mm;
    font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif;
    color: {INK}; position: relative;
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
  }}
  h1 {{ font-size: 21pt; font-weight: 700; letter-spacing: -0.2pt; }}
  .meta {{ margin-top: 4mm; font-size: 10pt; color: {MUTED}; line-height: 1.5; }}
  .rule {{ height: 0; border-top: 1.2pt solid {ACCENT}; margin: 7mm 0 6mm; }}
  .stats {{ display: grid; grid-template-columns: repeat(5, 1fr); }}
  .stat {{ padding: 0 3mm; border-left: 0.6pt solid #C9CDD2; }}
  .stat:first-child {{ padding-left: 0; border-left: none; }}
  .num {{ font-size: 28pt; font-weight: 700; color: {ACCENT}; line-height: 1.05;
          font-variant-numeric: tabular-nums; }}
  .lbl {{ margin-top: 2mm; font-size: 8.5pt; color: {MUTED}; line-height: 1.3; }}
  h2 {{ font-size: 11.5pt; font-weight: 700; margin: 10mm 0 3.5mm; }}
  .map svg {{ width: 100%; height: auto; display: block; }}
  .note {{ margin-top: 2mm; font-size: 7.5pt; color: {MUTED}; }}
  .regions {{ margin-top: 5mm; }}
  .region {{ display: grid; grid-template-columns: 24mm 1fr; padding: 2.2mm 0;
             border-top: 0.6pt solid #E1E4E8; }}
  .region:last-child {{ border-bottom: 0.6pt solid #E1E4E8; }}
  .rname {{ font-size: 8.5pt; font-weight: 700; }}
  .rlist {{ font-size: 8.5pt; line-height: 1.45; color: {INK}; }}
  footer {{ position: absolute; left: 17mm; right: 17mm; bottom: 12mm;
            font-size: 7.5pt; color: {MUTED}; border-top: 0.6pt solid #E1E4E8; padding-top: 2.5mm; }}
</style></head>
<body>
  <h1>scholarly.space — Impact Overview</h1>
  <div class="meta">https://scholarly.space<br>Muhammadjon Ulashov</div>
  <div class="rule"></div>
  <div class="stats">{stats}</div>
  <h2>Countries represented</h2>
  <div class="map">{svg}</div>
  {marker_note}
  <div class="regions">{region_rows}</div>
  <footer>Figures computed from the scholarly.space platform database on {escape(agg["computed_on"])}. Map data: Natural Earth.</footer>
</body></html>"""


def main() -> None:
    agg = json.loads((HERE / "aggregates.json").read_text())
    codes = agg["country_codes"]
    f110 = load(HERE / "ne_110m_admin_0_countries.geojson")
    f50 = load(HERE / "ne_50m_admin_0_countries.geojson")

    svg, marked = build_map(set(codes), f110, f50)
    regions = names_by_region(codes, f110, f50)
    listed = sum(len(v) for v in regions.values())
    assert listed == len(codes) == agg["figures"]["countries_represented"]["value"], "country list mismatch"

    html = build_html(agg, svg, regions, bool(marked))
    (HERE / "scholarly_impact_overview.html").write_text(html)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROMIUM)
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.emulate_media(media="print")
        # Overflow guard: content must end above the footer, inside one A4 page.
        overflow = page.evaluate(
            """() => {
              const footer = document.querySelector('footer').getBoundingClientRect();
              const last = [...document.body.children].filter(e => e.tagName !== 'FOOTER')
                             .map(e => e.getBoundingClientRect().bottom);
              return { contentBottom: Math.max(...last), footerTop: footer.top,
                       pageHeight: document.body.getBoundingClientRect().height,
                       scrollHeight: document.documentElement.scrollHeight };
            }"""
        )
        if overflow["contentBottom"] > overflow["footerTop"] or overflow["scrollHeight"] > overflow["pageHeight"] + 1:
            raise SystemExit(f"Layout overflow: {overflow}")
        page.pdf(path=str(OUT_PDF), format="A4", print_background=True,
                 prefer_css_page_size=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        browser.close()

    subprocess.run(["pdftoppm", "-r", "110", "-png", "-singlefile", str(OUT_PDF),
                    str(OUT_PNG.with_suffix(""))], check=True)
    print(f"wrote {OUT_PDF.name} and {OUT_PNG.name}")
    print(f"layout: content ends {overflow['contentBottom']:.0f}px, footer starts {overflow['footerTop']:.0f}px")
    print(f"map: {len(codes) - len(marked)} shaded, {len(marked)} circled ({', '.join(marked)})")
    for r, names in regions.items():
        print(f"  {r} ({len(names)}): {', '.join(names)}")


if __name__ == "__main__":
    main()
