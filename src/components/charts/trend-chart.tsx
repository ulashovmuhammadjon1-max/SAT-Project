"use client";

import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
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

export interface TrendPoint {
  label: string;
  value: number;
}

/**
 * A dated series — signups per week, questions answered per day.
 *
 * `interval="preserveStartEnd"` rather than showing every tick: thirty daily
 * labels overlap into an unreadable smear at this width, and the first and last
 * dates are what orient the reader.
 */
export function TrendAreaChart({ data, unitLabel }: { data: TrendPoint[]; unitLabel: string }) {
  return (
    <div className="h-56 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ left: -22, right: 8, top: 8 }}>
          <defs>
            <linearGradient id="trendFill" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="hsl(var(--primary))" stopOpacity={0.35} />
              <stop offset="100%" stopColor="hsl(var(--primary))" stopOpacity={0.02} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" vertical={false} className="stroke-border" />
          <XAxis dataKey="label" tick={{ fontSize: 11 }} interval="preserveStartEnd" minTickGap={24} />
          <YAxis tick={{ fontSize: 11 }} allowDecimals={false} width={44} />
          <Tooltip contentStyle={TOOLTIP} formatter={(v: number) => [v, unitLabel]} />
          <Area
            type="monotone"
            dataKey="value"
            stroke="hsl(var(--primary))"
            strokeWidth={2}
            fill="url(#trendFill)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}

/** A histogram — score bands. Categorical, so bars rather than an area. */
export function DistributionChart({ data, unitLabel }: { data: TrendPoint[]; unitLabel: string }) {
  return (
    <div className="h-56 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ left: -22, right: 8, top: 8 }}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} className="stroke-border" />
          <XAxis dataKey="label" tick={{ fontSize: 10 }} interval={0} angle={-30} textAnchor="end" height={54} />
          <YAxis tick={{ fontSize: 11 }} allowDecimals={false} width={44} />
          <Tooltip contentStyle={TOOLTIP} formatter={(v: number) => [v, unitLabel]} />
          <Bar dataKey="value" radius={[6, 6, 0, 0]} fill="hsl(var(--primary))" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
