"use client";

import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";

const FORMULAS: { label: string; formula: string }[] = [
  { label: "Circle area", formula: "A = πr²" },
  { label: "Circle circumference", formula: "C = 2πr" },
  { label: "Rectangle area", formula: "A = lw" },
  { label: "Triangle area", formula: "A = ½bh" },
  { label: "Pythagorean theorem", formula: "a² + b² = c²" },
  { label: "Rectangular solid volume", formula: "V = lwh" },
  { label: "Cylinder volume", formula: "V = πr²h" },
  { label: "Sphere volume", formula: "V = (4/3)πr³" },
  { label: "Cone volume", formula: "V = ⅓πr²h" },
  { label: "Pyramid volume", formula: "V = ⅓lwh" },
  { label: "Sum of angles (triangle)", formula: "180°" },
  { label: "Sum of angles (quadrilateral)", formula: "360°" },
  { label: "Degrees in a circle", formula: "360° = 2π radians" },
];

export function ReferenceSheetDialog({ open, onOpenChange }: { open: boolean; onOpenChange: (v: boolean) => void }) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-xl">
        <DialogHeader>
          <DialogTitle>Reference sheet</DialogTitle>
        </DialogHeader>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
          {FORMULAS.map((f) => (
            <div key={f.label} className="rounded-lg border border-border p-3 text-center">
              <p className="font-display text-base font-semibold">{f.formula}</p>
              <p className="mt-1 text-xs text-muted-foreground">{f.label}</p>
            </div>
          ))}
        </div>
        <p className="text-xs text-muted-foreground">
          The number of degrees of arc in a circle is 360. The number of radians of arc in a circle is 2π. The sum of
          the measures in degrees of the angles of a triangle is 180.
        </p>
      </DialogContent>
    </Dialog>
  );
}
