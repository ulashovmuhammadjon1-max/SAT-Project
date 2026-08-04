"use client";

import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Legend,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

/** Distinct enough to stay readable when a slice is small. */
const PALETTE = [
  "hsl(226 84% 56%)",
  "hsl(266 84% 60%)",
  "hsl(152 60% 40%)",
  "hsl(38 92% 50%)",
  "hsl(190 84% 45%)",
  "hsl(340 75% 55%)",
  "hsl(20 85% 55%)",
  "hsl(280 60% 50%)",
  "hsl(200 70% 45%)",
  "hsl(95 55% 42%)",
];

const TOOLTIP_STYLE = {
  contentStyle: {
    borderRadius: "0.5rem",
    border: "1px solid hsl(var(--border))",
    background: "hsl(var(--card))",
    fontSize: 12,
  },
} as const;

export function CountryPieChart({ data }: { data: { name: string; value: number }[] }) {
  return (
    <div className="h-[300px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            cx="50%"
            cy="50%"
            innerRadius={55}
            outerRadius={95}
            paddingAngle={2}
          >
            {data.map((_, i) => (
              <Cell key={i} fill={PALETTE[i % PALETTE.length]} />
            ))}
          </Pie>
          <Tooltip {...TOOLTIP_STYLE} formatter={(v: number) => [`${v} students`, "Users"]} />
          <Legend
            layout="vertical"
            align="right"
            verticalAlign="middle"
            wrapperStyle={{ fontSize: 12, lineHeight: "20px" }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export function AudienceBarChart({
  data,
  color = "hsl(226 84% 56%)",
  unit,
  horizontal = false,
}: {
  data: { name: string; value: number }[];
  color?: string;
  unit?: string;
  horizontal?: boolean;
}) {
  return (
    <div className="h-[300px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          layout={horizontal ? "vertical" : "horizontal"}
          margin={{ top: 8, right: 16, bottom: 8, left: horizontal ? 8 : 0 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" vertical={!horizontal} />
          {horizontal ? (
            <>
              <XAxis type="number" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
              <YAxis
                type="category"
                dataKey="name"
                width={150}
                tick={{ fontSize: 11 }}
                axisLine={false}
                tickLine={false}
              />
            </>
          ) : (
            <>
              <XAxis dataKey="name" tick={{ fontSize: 11 }} axisLine={false} tickLine={false} />
              <YAxis tick={{ fontSize: 11 }} axisLine={false} tickLine={false} allowDecimals={false} />
            </>
          )}
          <Tooltip
            {...TOOLTIP_STYLE}
            cursor={{ fill: "hsl(var(--secondary))" }}
            formatter={(v: number) => [`${v}${unit ? ` ${unit}` : ""}`, ""]}
          />
          <Bar dataKey="value" fill={color} radius={horizontal ? [0, 4, 4, 0] : [4, 4, 0, 0]} maxBarSize={44} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
