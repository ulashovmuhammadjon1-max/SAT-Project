"use client";

import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

const TOOLTIP = {
  borderRadius: 12,
  border: "1px solid hsl(var(--border))",
  background: "hsl(var(--background))",
  fontSize: 13,
} as const;

/**
 * The three series, in fixed order. The colour follows the measure, not its
 * rank on the chart, so hiding a series never repaints the others.
 */
const SERIES = [
  { key: "total", label: "Total", color: "hsl(var(--chart-1))" },
  { key: "rw", label: "Reading & Writing", color: "hsl(var(--chart-2))" },
  { key: "math", label: "Math", color: "hsl(var(--chart-3))" },
] as const;

export interface ScorePoint {
  label: string;
  total: number;
  rw: number | null;
  math: number | null;
}

/**
 * One student's scores across the tests they have submitted, in the order they
 * sat them.
 *
 * All three series share one y-axis because they share one unit — SAT points.
 * The total is the sum of the two sections, so it rides above them on the same
 * scale; giving the sections their own axis would put 600 level with 1200 and
 * invent a crossover that isn't there.
 */
export function ScoreProgressChart({ data }: { data: ScorePoint[] }) {
  return (
    <div className="h-72 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data} margin={{ left: -14, right: 12, top: 8 }}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} className="stroke-border" />
          <XAxis dataKey="label" tick={{ fontSize: 11 }} interval="preserveStartEnd" minTickGap={16} />
          {/* Fixed to the real SAT range, so two students' charts are directly
              comparable and a flat run doesn't get magnified into a cliff. */}
          <YAxis tick={{ fontSize: 11 }} domain={[200, 1600]} ticks={[200, 600, 1000, 1400]} width={46} />
          <Tooltip contentStyle={TOOLTIP} />
          <Legend wrapperStyle={{ fontSize: 12, paddingTop: 8 }} />
          {SERIES.map((s) => (
            <Line
              key={s.key}
              type="monotone"
              dataKey={s.key}
              name={s.label}
              stroke={s.color}
              strokeWidth={2}
              // A gap where a section score is missing, rather than a straight
              // line pretending the student scored between two sittings.
              connectNulls={false}
              dot={{ r: 4, strokeWidth: 2 }}
              activeDot={{ r: 6 }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

/**
 * Questions answered per day over the trailing window.
 *
 * Bars rather than an area: study days are discrete events, and an area fill
 * across a fortnight of zeros reads as sustained low activity instead of none.
 */
export function StudyActivityChart({ data }: { data: { label: string; value: number }[] }) {
  return (
    <div className="h-48 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ left: -22, right: 8, top: 8 }}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} className="stroke-border" />
          <XAxis dataKey="label" tick={{ fontSize: 10 }} interval="preserveStartEnd" minTickGap={40} />
          <YAxis tick={{ fontSize: 11 }} allowDecimals={false} width={40} />
          <Tooltip contentStyle={TOOLTIP} formatter={(v: number) => [v, "questions"]} />
          <Bar dataKey="value" radius={[4, 4, 0, 0]} fill="hsl(var(--chart-1))" maxBarSize={14} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
