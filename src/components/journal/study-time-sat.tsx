/**
 * "Study Time, Focus, and Baseline Ability as Correlates of SAT Score
 * Improvement" — the body of the paper.
 *
 * Every figure here comes from the author's survey data. Where the source
 * material stated a causal relationship the wording has been changed to an
 * associational one, because the design is observational; where a rival
 * explanation exists it is named rather than left out.
 */

function H2({ children }: { children: React.ReactNode }) {
  return (
    <h2 className="mt-12 font-display text-xl font-semibold tracking-tight sm:text-2xl">
      {children}
    </h2>
  );
}

function H3({ children }: { children: React.ReactNode }) {
  return <h3 className="mt-8 text-[15px] font-semibold tracking-tight">{children}</h3>;
}

function P({ children }: { children: React.ReactNode }) {
  return <p className="mt-4 text-[15px] leading-[1.75] text-foreground/85">{children}</p>;
}

function Table({
  caption,
  headers,
  rows,
  align,
}: {
  caption: string;
  headers: string[];
  rows: (string | number)[][];
  align?: ("left" | "right")[];
}) {
  const at = (i: number) => (align?.[i] === "right" ? "text-right tabular-nums" : "text-left");
  return (
    <figure className="mt-6">
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full border-collapse text-[14px]">
          <thead>
            <tr className="bg-secondary/50">
              {headers.map((h, i) => (
                <th
                  key={i}
                  scope="col"
                  className={`border-b border-border px-3 py-2 font-semibold ${at(i)}`}
                >
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((r, i) => (
              <tr key={i} className="border-b border-border last:border-0">
                {r.map((c, j) => (
                  <td key={j} className={`px-3 py-2 text-foreground/85 ${at(j)}`}>
                    {c}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <figcaption className="mt-2 text-[13px] leading-relaxed text-muted-foreground">
        {caption}
      </figcaption>
    </figure>
  );
}

export function StudyTimeSatPaper() {
  return (
    <article className="max-w-none">
      <H2>Abstract</H2>
      <P>
        Preparation for the SAT varies widely in intensity, duration, and quality of attention,
        yet students receive little evidence about which of those dimensions matters most, or
        whether the answer depends on where they begin. This study surveyed more than twenty
        test-takers on five self-reported variables — baseline score, months of preparation,
        daily study hours, focus, and score improvement — and compared respondents whose
        baseline fell below a 1100 cut point with those whose baseline fell above it. In both
        groups, daily study intensity was more closely associated with improvement than total
        preparation duration: within pairs of respondents matched on months of preparation,
        the respondent reporting more hours per day reported the larger gain. The below-cut
        group improved more on average (320 points, against 220). Both findings are reported
        as associations rather than as effects. The design is observational, the sample is
        small, and regression to the mean is a rival explanation for the group difference that
        the present data cannot exclude.
      </P>

      <H2>1. Introduction</H2>
      <P>
        The SAT occupies a consequential position in undergraduate admissions, and students
        approach it with markedly different preparation strategies. Some study for a year at
        an hour a day; others compress preparation into a few intense months. The choice is
        not costless: time spent preparing is time withdrawn from coursework, employment,
        extracurricular commitments, and rest. Students making that trade-off would benefit
        from knowing which dimension of preparation is most closely associated with score
        gains, and whether the answer differs by starting ability.
      </P>
      <P>
        This study addresses three questions. First, is score improvement more closely
        associated with the <em>intensity</em> of preparation (hours per day) or its{" "}
        <em>duration</em> (months)? Second, is self-reported focus associated with improvement
        independently of the hours in which that focus is exercised? Third, do these
        relationships differ between students beginning below and above a fixed baseline cut
        point?
      </P>
      <P>
        The comparison by baseline is the study&apos;s organising choice. Students who begin
        lower have more headroom on the scale and more elementary content still to gain from,
        so the same preparation may yield different point returns at different starting
        levels. Any practical recommendation that ignores the starting point risks being
        useful to one group and misleading to the other.
      </P>

      <H2>2. Method</H2>

      <H3>2.1 Design and participants</H3>
      <P>
        The study used a cross-sectional self-report survey of secondary students who had
        prepared for and sat the SAT. More than twenty responses were analysed. Responses that
        were incomplete, internally inconsistent, or ambiguous were excluded before analysis.
        The exact analytic sample size following exclusions was not recorded, which is a
        limitation returned to in Section 5.
      </P>

      <H3>2.2 Measures</H3>
      <P>
        Respondents reported five quantities: baseline SAT score prior to preparation; total
        preparation duration in months; average daily study time in hours; focus, self-rated
        on an eleven-point scale anchored at 0 and 10; and score improvement in points between
        the baseline and the most recent sitting. Respondents were additionally asked what
        they had given up in order to prepare — an opportunity-cost item — which was collected
        but is not analysed quantitatively here, as the responses were free text and did not
        support a common scale.
      </P>

      <H3>2.3 Grouping</H3>
      <P>
        Respondents were divided at a baseline score of 1100. This cut point sits somewhat
        above the College Board&apos;s reported mean total score for recent cohorts, which has
        been near 1050. It should be read as a convenient dividing line within this sample
        rather than as a population median; the sample is not representative of test-takers
        generally, and no defensible worldwide median exists, since the SAT is not
        administered uniformly across populations.
      </P>

      <H3>2.4 Analytic approach</H3>
      <P>
        The analysis is descriptive. Group distributions are summarised by range, and by
        median or mean where the source data supported it. Beyond that, the study relies on{" "}
        <em>matched comparisons</em>: pairs of respondents who reported the same value on one
        preparation variable but different values on another, allowing the second variable to
        be examined with the first approximately held constant. With a sample of this size,
        matched pairs are more informative than a correlation coefficient computed across
        twenty-odd heterogeneous cases, but they remain illustrative rather than inferential.
        No significance tests were performed, and none should be inferred from the comparisons
        below.
      </P>

      <H2>3. Results</H2>

      <H3>3.1 Baseline composition</H3>
      <P>
        Forty per cent of respondents fell below the 1100 cut point and sixty per cent above
        it. The two groups were well separated at baseline, with no overlap between the
        highest below-cut score (1080) and the lowest above-cut score (1130).
      </P>
      <Table
        caption="Table 1. Baseline composition of the two groups. The 50-point gap between the groups' nearest scores means the division is clean; no respondent sits near the cut point."
        headers={["Group", "Share of sample", "Baseline score range"]}
        align={["left", "right", "right"]}
        rows={[
          ["Below cut (< 1100)", "40%", "790 – 1080"],
          ["Above cut (≥ 1100)", "60%", "1130 – 1390"],
        ]}
      />

      <H3>3.2 Preparation duration and intensity</H3>
      <P>
        Total preparation duration was similar across groups, spanning roughly a year in each.
        Daily intensity differed: the below-cut group contained respondents studying as much
        as nine hours a day, whereas the above-cut group was compressed into a one-to-three
        hour band. In both groups the typical respondent studied about two hours a day, so the
        difference lies in the upper tail rather than in the centre of the distribution.
      </P>
      <Table
        caption="Table 2. Preparation duration and daily intensity. The below-cut group's much wider intensity range is driven by a small number of respondents studying far above the group norm; two hours a day was typical in both groups."
        headers={["Group", "Duration (months)", "Hours per day", "Typical hours per day"]}
        align={["left", "right", "right", "right"]}
        rows={[
          ["Below cut", "2 – 12", "1.4 – 9", "≈ 2 (most common)"],
          ["Above cut", "1 – 13", "1 – 3", "2 (median)"],
        ]}
      />

      <H3>3.3 Self-reported focus</H3>
      <P>
        Self-rated focus was narrowly distributed and near-identical between groups at the
        median. The below-cut group rated itself slightly higher at both ends of the range.
        Given that both medians are 6 out of 10, focus does not distinguish the groups.
      </P>
      <Table
        caption="Table 3. Self-rated focus on an eleven-point scale. Identical medians and heavily overlapping ranges mean this variable does not separate the two groups."
        headers={["Group", "Focus range", "Median focus"]}
        align={["left", "right", "right"]}
        rows={[
          ["Below cut", "5 – 8", "6"],
          ["Above cut", "4 – 7", "6"],
        ]}
      />

      <H3>3.4 Score improvement</H3>
      <P>
        The below-cut group improved by 320 points on average, against 220 points for the
        above-cut group — a difference of 100 points. The below-cut group was also more
        variable, with a range spanning 340 points against 290.
      </P>
      <Table
        caption="Table 4. Score improvement by group. The below-cut group gained about 100 points more on average, and its lowest observed gain (180) exceeds the above-cut group's lowest (30) by a wide margin."
        headers={["Group", "Improvement range", "Mean improvement"]}
        align={["left", "right", "right"]}
        rows={[
          ["Below cut", "180 – 520", "320"],
          ["Above cut", "30 – 320", "220"],
        ]}
      />

      <H3>3.5 Matched comparisons within the below-cut group</H3>
      <P>
        Holding preparation duration constant, the respondent reporting more daily hours
        reported the larger gain in each available pair. In the first pair the difference is
        large in both the predictor and the outcome; in the second, a single additional hour a
        day accompanies an 80-point difference. The third pair holds focus constant instead,
        and shows duration also carrying some association.
      </P>
      <Table
        caption="Table 5. Matched comparisons, below-cut group. In pairs 1 and 2 duration is held constant and intensity varies; in pair 3 focus is held constant and duration varies. Pair 1 is confounded: the respondent studying nine hours a day also reported the higher focus rating, so the two cannot be separated."
        headers={["Pair", "Duration", "Hours/day", "Focus", "Improvement"]}
        align={["left", "right", "right", "right", "right"]}
        rows={[
          ["1a", "same", "9", "8", "+520"],
          ["1b", "same", "2", "6", "+180"],
          ["2a", "3 months", "3", "6", "+320"],
          ["2b", "3 months", "4", "—", "+400"],
          ["3a", "3 months", "—", "6", "+320"],
          ["3b", "2 months", "—", "6", "+230"],
        ]}
      />

      <H3>3.6 Matched comparisons within the above-cut group</H3>
      <P>
        The same pattern appears above the cut point, and in one comparison duration runs
        against improvement outright: a respondent preparing for thirteen months at one hour a
        day gained less than one preparing for five months at two hours a day. A respondent
        preparing for three months at three hours a day gained more than one preparing for six
        months at one hour a day, despite half the calendar time.
      </P>
      <Table
        caption="Table 6. Matched comparisons, above-cut group. Rows 1–2 and 3–4 each pair a longer, less intense preparation against a shorter, more intense one; in both pairs the more intense preparation is associated with the larger gain. Rows 5–6 hold focus at 4/10 and vary intensity."
        headers={["#", "Duration", "Hours/day", "Focus", "Improvement"]}
        align={["left", "right", "right", "right", "right"]}
        rows={[
          ["1", "13 months", "≈ 1", "—", "+270"],
          ["2", "5 months", "≈ 2", "—", "+320"],
          ["3", "6 months", "≈ 1", "—", "+220"],
          ["4", "3 months", "3", "4", "+270"],
          ["5", "4 months", "≈ 2", "4", "+210"],
          ["6", "—", "—", "7", "+320"],
        ]}
      />
      <P>
        Against these patterns, several respondents reporting similar baselines, similar daily
        hours, and similar durations nonetheless reported substantially different gains. The
        measured variables therefore leave a considerable share of the variation unexplained.
      </P>

      <H2>4. Discussion</H2>

      <H3>4.1 Intensity appears to matter more than duration</H3>
      <P>
        The most consistent pattern in the data is that daily hours track improvement more
        closely than months of preparation do. It holds in both groups, and in the above-cut
        group it holds even when duration runs in the opposite direction — thirteen months at
        one hour a day was associated with a smaller gain than five months at two. A plausible
        reading is that preparation spread very thinly across a long period loses to
        forgetting between sessions what it gains in total exposure, but this study cannot
        test that mechanism, and the pattern rests on a handful of matched pairs.
      </P>

      <H3>4.2 The larger gains below the cut point have a rival explanation</H3>
      <P>
        The below-cut group improved by about 100 points more on average. The intuitive
        reading — that lower-scoring students have more accessible content left to learn — is
        plausible and consistent with the structure of the test. It is not, however, the only
        explanation available, and the study design cannot distinguish between them.
      </P>
      <P>
        <strong>Regression to the mean</strong> predicts this result on its own. Baseline
        scores were measured once. A single measurement of any partly noisy quantity will
        place some students below their true level and others above it, and on a second
        measurement both tend to move back toward the centre. Because the groups were formed{" "}
        <em>by</em> the baseline measurement, the below-cut group is enriched with students who
        underperformed on that occasion, and the above-cut group with students who
        overperformed — so the first group would be expected to appear to improve more even if
        preparation had no effect at all. A <strong>ceiling effect</strong> works in the same
        direction: a respondent starting at 1390 has at most 210 points available, less than
        the below-cut group&apos;s mean gain.
      </P>
      <P>
        Separating these explanations requires a design this study does not have: repeated
        baseline measurement to estimate the noise, or a comparison group that prepared
        differently. Until then, the 100-point difference should be read as a real feature of
        the sample rather than as evidence that low-scoring students benefit more from
        preparation.
      </P>

      <H3>4.3 Focus could not be separated from intensity</H3>
      <P>
        The clearest focus contrast in the data — 8/10 associated with +520 against 6/10
        associated with +180 — is confounded, because the more focused respondent also studied
        nine hours a day against two. Where focus was held constant, intensity and duration
        still tracked the outcome. The honest conclusion is that this study cannot estimate an
        association for focus independent of the hours in which it is exercised. The measure
        itself is also weak: a single unvalidated self-rating, collected after the outcome was
        known, is open to the respondent&apos;s reconstruction of how hard they worked in light
        of how well they did.
      </P>

      <H2>5. Limitations</H2>
      <P>
        The findings above should be weighed against the following, which are substantial.
      </P>
      <ul className="mt-4 space-y-3 text-[15px] leading-[1.75] text-foreground/85">
        <li className="flex gap-3">
          <span aria-hidden className="mt-[0.6em] h-1 w-1 shrink-0 rounded-full bg-foreground/40" />
          <span>
            <strong>Observational design.</strong> Preparation was chosen by respondents, not
            assigned. Students who study nine hours a day differ from those who study two in
            ways beyond study time — motivation, resources, and available time among them —
            and any of those may drive the outcome. No causal claim is supported.
          </span>
        </li>
        <li className="flex gap-3">
          <span aria-hidden className="mt-[0.6em] h-1 w-1 shrink-0 rounded-full bg-foreground/40" />
          <span>
            <strong>Sample size and composition.</strong> More than twenty respondents is
            enough for description and too few for inference. The exact analytic sample after
            exclusions was not recorded, so the group percentages cannot be converted back to
            counts. Respondents were not randomly sampled.
          </span>
        </li>
        <li className="flex gap-3">
          <span aria-hidden className="mt-[0.6em] h-1 w-1 shrink-0 rounded-full bg-foreground/40" />
          <span>
            <strong>Self-report throughout.</strong> Predictors and outcome come from the same
            respondent at the same moment. Study hours are known to be over-reported, and a
            respondent pleased with their result may recall their preparation more favourably.
          </span>
        </li>
        <li className="flex gap-3">
          <span aria-hidden className="mt-[0.6em] h-1 w-1 shrink-0 rounded-full bg-foreground/40" />
          <span>
            <strong>Improvement is not attributable to preparation alone.</strong> Part of any
            second-sitting gain reflects familiarity with the format and the conditions, which
            this design does not separate from the effect of studying.
          </span>
        </li>
        <li className="flex gap-3">
          <span aria-hidden className="mt-[0.6em] h-1 w-1 shrink-0 rounded-full bg-foreground/40" />
          <span>
            <strong>Unanalysed data.</strong> The opportunity-cost item was collected as free
            text and could not be placed on a common scale, so the trade-off that motivated
            the study is described but not measured.
          </span>
        </li>
      </ul>

      <H2>6. Practical implications</H2>
      <P>
        The following are offered as tentative guidance consistent with this sample, not as
        established findings. They should be read alongside Section 5.
      </P>
      <Table
        caption="Table 7. Tentative guidance by starting point. The above-cut recommendation is conditional on available time: the same total preparation appears to be better concentrated than spread out."
        headers={["Starting point", "Time available", "Suggested daily study", "Focus"]}
        align={["left", "left", "right", "right"]}
        rows={[
          ["Below 1100", "Any", "4 – 5 hours", "≥ 6/10"],
          ["1100 and above", "About 3 months", "3 hours", "As high as sustainable"],
          ["1100 and above", "5 – 6 months", "2 hours", "As high as sustainable"],
        ]}
      />
      <P>
        The observed effective range for the below-cut group was wider than the recommendation
        — from three to nine hours a day — but the upper end reflects a single respondent, and
        a recommendation to study nine hours a day is not one this data can support or that
        most students could sustain. The narrower four-to-five-hour recommendation sits within
        the observed range while remaining plausible as a daily routine.
      </P>

      <H2>7. Conclusion</H2>
      <P>
        Across both groups in this sample, how much a student studied on a given day tracked
        score improvement more closely than how long they had been preparing. Students
        beginning below 1100 improved more on average than those beginning above it, though
        regression to the mean and a ceiling effect predict that result independently of any
        benefit from preparation, and this design cannot separate the explanations. Self-rated
        focus did not distinguish the groups and could not be disentangled from study
        intensity.
      </P>
      <P>
        The clearest direction for further work is measurement rather than scale. A larger
        sample would narrow the estimates, but it would not fix the design: a study that took
        two baseline measurements before preparation began could estimate how much of the
        below-cut group&apos;s advantage is regression to the mean, and one that recorded study
        time prospectively — logged as it happened rather than recalled afterwards — would
        remove the most serious reporting bias. Both are within reach of a study run through a
        preparation platform, where practice sessions are already timestamped.
      </P>

      <H2>Notes on sources</H2>
      <P>
        The comparison figure for recent mean total scores is drawn from the College
        Board&apos;s annual SAT Suite of Assessments Program Results. The account of regression
        to the mean in Section 4.2 follows the standard treatment in A. G. Barnett, J. C. van
        der Pols and A. J. Dobson, &ldquo;Regression to the mean: what it is and how to deal
        with it&rdquo;, <em>International Journal of Epidemiology</em> 34 (2005), 215–220. All
        data reported in this paper come from the author&apos;s own survey.
      </P>
    </article>
  );
}
