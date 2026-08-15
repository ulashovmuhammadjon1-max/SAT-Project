# Figure-building brief

Each question in your slice depends on a graph or diagram that the SAT books
printed but text extraction could not carry. A transcriber already read the
page and measured the figure; that measurement is in the record's `note`.
Your job is to draw it.

## Why this exists

A question that says "the graph shows…" with no graph is unanswerable, and
this project's standing rule is that a prose description must never stand in
for the picture — a description both replaces the reading task and usually
leaks the answer. So the figure gets built, or the question does not ship.

## What to do, per question

1. Read `note` for the measured spec — plotted points, line endpoints, axis
   ranges, angle positions, bar heights, dot counts.
2. **Open the original page image** to check your reading before you draw.
   The path is `pages/<src>-<pdf_page as 3 digits>.png`; render it if missing:
   `pdftoppm -f N -l N -r 150 -png -singlefile '<upload dir>/<src>' '<out>'`
   The upload directory is
   `/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45`.
   If `note` and the page disagree, the page wins — say so in your output.
3. Draw it with matplotlib and save a PNG as a base64 data URI.
4. Append one line to your JSONL.

## Drawing rules

- Plain and legible, not decorative. Black on white, no seaborn styling, no
  background tint, no title unless the book prints one.
- `figsize` around (5,3.6) for plots, `dpi=110`. Keep the file under ~120 KB.
- Label both axes exactly as the book does, including units.
- Show the gridlines only if the original does.
- For scatterplots draw the points and, only if the book shows one, the line
  of best fit.
- For geometry: draw the figure to scale where the maths allows, mark right
  angles with a small square, and label vertices and given lengths exactly as
  the book does. **Do not label anything the book leaves unlabelled** — an
  added label can hand over the answer.
- If the book says "Note: figure not drawn to scale", include that line as a
  caption beneath the axes.

## Output

Append one JSON object per line to `fig/fg-NN.jsonl`, after EVERY figure:

    {"id":"…","imageUrl":"data:image/png;base64,…","alt":"…","note":""}

- `alt` — a short factual description for screen readers. Describe the axes
  and the type of chart, **never the values a student is meant to read off**.
- `note` — only if something is wrong: the spec and the page disagree, the
  figure is unreconstructable, or the question needs more than one figure.
  Leave empty otherwise.

If a question's figure genuinely cannot be rebuilt from what is recorded, say
so in `note` and move on. A missing figure is recoverable; a wrong one that
looks right is not.
