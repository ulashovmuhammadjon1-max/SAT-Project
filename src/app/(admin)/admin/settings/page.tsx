import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AdaptiveConfigForm } from "@/components/admin/adaptive-config-form";
import { FeatureFlagToggle } from "@/components/admin/feature-flag-toggle";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Adaptive Settings" };
export const dynamic = "force-dynamic";

export default async function AdminSettingsPage() {
  const [configs, flags] = await Promise.all([
    prisma.adaptiveConfig.findMany({ orderBy: { createdAt: "desc" } }),
    prisma.featureFlag.findMany({ orderBy: { key: "asc" } }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Adaptive Module Settings</h1>
        <p className="text-sm text-muted-foreground">
          Configure the Module 1 performance threshold that routes students to the easier or harder Module 2.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Create configuration</CardTitle>
        </CardHeader>
        <CardContent>
          <AdaptiveConfigForm />
        </CardContent>
      </Card>

      <div className="space-y-3">
        {configs.map((config) => (
          <Card key={config.id} className={config.isActive ? "border-primary" : undefined}>
            <CardContent className="flex flex-wrap items-center justify-between gap-3 p-5">
              <div>
                <p className="flex items-center gap-2 font-medium">
                  {config.name}
                  {config.isActive && (
                    <span className="rounded-full bg-primary/10 px-2 py-0.5 text-xs font-semibold text-primary">
                      Active
                    </span>
                  )}
                </p>
                <p className="text-sm text-muted-foreground">
                  Reading &amp; Writing threshold: {config.rwThresholdPct}% · Math threshold: {config.mathThresholdPct}%
                </p>
              </div>
              <AdaptiveConfigForm existing={config} />
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Feature flags</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          {flags.length === 0 && (
            <p className="text-sm text-muted-foreground">No feature flags configured yet — add them via seed data.</p>
          )}
          {flags.map((flag) => (
            <div key={flag.id} className="flex items-center justify-between rounded-lg border border-border p-3">
              <div>
                <p className="text-sm font-medium">{flag.label}</p>
                <p className="text-xs text-muted-foreground">{flag.description}</p>
              </div>
              <FeatureFlagToggle flagKey={flag.key} isEnabled={flag.isEnabled} />
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
}
