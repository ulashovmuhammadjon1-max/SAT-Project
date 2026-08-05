"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Save, Sparkles, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import { Separator } from "@/components/ui/separator";
import { cn } from "@/lib/utils";
import {
  deleteQuestion,
  generateExplanationDraft,
  saveExplanation,
  updatePassage,
  updateQuestion,
} from "@/server/actions/admin/questions";
import { ImageUploadField } from "@/components/admin/image-upload-field";
import { RichTextField } from "@/components/admin/rich-text-field";

interface Choice {
  id?: string;
  label: string;
  content: string;
  isCorrect: boolean;
  order: number;
}

interface Domain {
  id: string;
  name: string;
  skills: { id: string; name: string }[];
}

interface QuestionData {
  id: string;
  stem: string;
  imageUrl: string | null;
  domainId: string;
  skillId: string;
  difficulty: "EASY" | "MEDIUM" | "HARD";
  isPublished: boolean;
  choices: Choice[];
  passage: { id: string; content: string; title: string | null } | null;
  explanation: {
    content: string;
    whyCorrect: string | null;
    whyWrongJson: unknown;
    commonMistakes: string | null;
    tips: string | null;
    relatedConcepts: string | null;
  } | null;
}

export function QuestionEditor({ question, domains }: { question: QuestionData; domains: Domain[] }) {
  const router = useRouter();
  const [stem, setStem] = useState(question.stem);
  const [imageUrl, setImageUrl] = useState(question.imageUrl);
  const [passageContent, setPassageContent] = useState(question.passage?.content ?? "");
  const [domainId, setDomainId] = useState(question.domainId);
  const [skillId, setSkillId] = useState(question.skillId);
  const [difficulty, setDifficulty] = useState(question.difficulty);
  const [isPublished, setIsPublished] = useState(question.isPublished);
  const [choices, setChoices] = useState<Choice[]>(question.choices);

  const [explContent, setExplContent] = useState(question.explanation?.content ?? "");
  const [explWhyCorrect, setExplWhyCorrect] = useState(question.explanation?.whyCorrect ?? "");
  const [explMistakes, setExplMistakes] = useState(question.explanation?.commonMistakes ?? "");
  const [explTips, setExplTips] = useState(question.explanation?.tips ?? "");
  const [explRelated, setExplRelated] = useState(question.explanation?.relatedConcepts ?? "");

  const [isSaving, startSave] = useTransition();
  const [isGenerating, startGenerate] = useTransition();
  const [isDeleting, startDelete] = useTransition();

  const activeDomain = domains.find((d) => d.id === domainId) ?? domains[0];

  function updateChoice(index: number, patch: Partial<Choice>) {
    setChoices((prev) => prev.map((c, i) => (i === index ? { ...c, ...patch } : c)));
  }

  function setCorrect(label: string) {
    setChoices((prev) => prev.map((c) => ({ ...c, isCorrect: c.label === label })));
  }

  function addChoice() {
    setChoices((prev) => [
      ...prev,
      { label: "ABCD"[prev.length], content: "", isCorrect: false, order: prev.length },
    ]);
  }

  function removeChoice(index: number) {
    setChoices((prev) =>
      prev.filter((_, i) => i !== index).map((c, i) => ({ ...c, label: "ABCD"[i], order: i }))
    );
  }

  function save() {
    startSave(async () => {
      await updateQuestion(question.id, { stem, imageUrl, domainId, skillId, difficulty, isPublished, choices });
      if (question.passage) {
        await updatePassage(question.passage.id, passageContent);
      }
      await saveExplanation(question.id, {
        content: explContent,
        whyCorrect: explWhyCorrect,
        whyWrongJson: {},
        commonMistakes: explMistakes,
        tips: explTips,
        relatedConcepts: explRelated,
      });
      toast.success("Question saved.");
      router.refresh();
    });
  }

  function generate() {
    startGenerate(async () => {
      const draft = await generateExplanationDraft(question.id);
      setExplContent(draft.content);
      setExplWhyCorrect(draft.whyCorrect);
      setExplMistakes(draft.commonMistakes);
      setExplTips(draft.tips);
      setExplRelated(draft.relatedConcepts);
      toast.success("Explanation draft generated.");
    });
  }

  function remove() {
    if (!confirm("Delete this question permanently?")) return;
    startDelete(async () => {
      const result = await deleteQuestion(question.id);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      toast.success("Question deleted.");
      router.push("/admin/questions");
    });
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Question Editor</h1>
          <p className="text-sm text-muted-foreground">Edit content, taxonomy, and explanation. Preview updates live.</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="outline" className="text-destructive" onClick={remove} disabled={isDeleting}>
            {isDeleting ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4" />} Delete
          </Button>
          <Button onClick={save} disabled={isSaving}>
            {isSaving ? <Loader2 className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />} Save changes
          </Button>
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        {/* Editor */}
        <div className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="text-base">Content</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {question.passage && (
                <div className="space-y-1.5">
                  <Label>Passage {question.passage.title ? `— ${question.passage.title}` : ""}</Label>
                  <RichTextField value={passageContent} onChange={setPassageContent} rows={6} />
                </div>
              )}

              <div className="space-y-1.5">
                <Label>Question stem</Label>
                <RichTextField value={stem} onChange={setStem} rows={4} />
              </div>

              <div className="space-y-1.5">
                <Label>Figure (graph, diagram, table)</Label>
                <ImageUploadField imageUrl={imageUrl} onChange={setImageUrl} />
              </div>

              <div className="space-y-2">
                <Label>Answer choices</Label>
                {choices.map((choice, i) => (
                  <div key={choice.label} className="flex items-center gap-2">
                    <input
                      type="radio"
                      name="correct-choice"
                      checked={choice.isCorrect}
                      onChange={() => setCorrect(choice.label)}
                    />
                    <span className="w-5 shrink-0 font-semibold">{choice.label}</span>
                    <Textarea
                      value={choice.content}
                      onChange={(e) => updateChoice(i, { content: e.target.value })}
                      rows={1}
                      className="min-h-9 py-2"
                    />
                    <Button variant="ghost" size="icon" onClick={() => removeChoice(i)}>
                      <Trash2 className="h-3.5 w-3.5 text-muted-foreground" />
                    </Button>
                  </div>
                ))}
                {choices.length < 4 && (
                  <Button variant="outline" size="sm" onClick={addChoice}>
                    Add choice {"ABCD"[choices.length]}
                  </Button>
                )}
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>Domain</Label>
                  <Select
                    value={domainId}
                    onValueChange={(v) => {
                      setDomainId(v);
                      const d = domains.find((x) => x.id === v);
                      if (d?.skills[0]) setSkillId(d.skills[0].id);
                    }}
                  >
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      {domains.map((d) => (
                        <SelectItem key={d.id} value={d.id}>
                          {d.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
                <div className="space-y-1.5">
                  <Label>Skill</Label>
                  <Select value={skillId} onValueChange={setSkillId}>
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      {activeDomain?.skills.map((s) => (
                        <SelectItem key={s.id} value={s.id}>
                          {s.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>Difficulty</Label>
                  <Select value={difficulty} onValueChange={(v) => setDifficulty(v as typeof difficulty)}>
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="EASY">Easy</SelectItem>
                      <SelectItem value="MEDIUM">Medium</SelectItem>
                      <SelectItem value="HARD">Hard</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="flex items-end justify-between rounded-lg border border-border px-3 py-2">
                  <Label className="text-sm">Published</Label>
                  <Switch checked={isPublished} onCheckedChange={setIsPublished} />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <CardTitle className="text-base">Explanation</CardTitle>
              <Button variant="outline" size="sm" onClick={generate} disabled={isGenerating}>
                {isGenerating ? <Loader2 className="h-4 w-4 animate-spin" /> : <Sparkles className="h-4 w-4" />}
                Generate with AI
              </Button>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="space-y-1.5">
                <Label className="text-xs text-muted-foreground">Overview</Label>
                <Textarea value={explContent} onChange={(e) => setExplContent(e.target.value)} rows={3} />
              </div>
              <div className="space-y-1.5">
                <Label className="text-xs text-muted-foreground">Why the correct answer is right</Label>
                <Textarea value={explWhyCorrect} onChange={(e) => setExplWhyCorrect(e.target.value)} rows={2} />
              </div>
              <div className="space-y-1.5">
                <Label className="text-xs text-muted-foreground">Common mistakes</Label>
                <Textarea value={explMistakes} onChange={(e) => setExplMistakes(e.target.value)} rows={2} />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label className="text-xs text-muted-foreground">Tips</Label>
                  <Textarea value={explTips} onChange={(e) => setExplTips(e.target.value)} rows={2} />
                </div>
                <div className="space-y-1.5">
                  <Label className="text-xs text-muted-foreground">Related concepts</Label>
                  <Textarea value={explRelated} onChange={(e) => setExplRelated(e.target.value)} rows={2} />
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Live preview */}
        <div className="lg:sticky lg:top-6 lg:self-start">
          <Card className="overflow-hidden">
            <CardHeader className="bg-navy-950 text-white">
              <CardTitle className="text-sm font-medium text-navy-200">Student preview</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 p-6">
              {question.passage && (
                <div
                  className="rounded-lg bg-secondary p-4 text-sm leading-relaxed"
                  dangerouslySetInnerHTML={{ __html: passageContent }}
                />
              )}
              <div
                className="font-medium leading-relaxed"
                dangerouslySetInnerHTML={{ __html: stem || "Question stem preview…" }}
              />
              {imageUrl && (
                // eslint-disable-next-line @next/next/no-img-element -- proxy URL, not statically optimizable
                <img src={imageUrl} alt="" className="max-h-64 rounded-lg border border-border" />
              )}
              <div className="space-y-2">
                {choices.map((choice) => (
                  <div
                    key={choice.label}
                    className={cn(
                      "flex items-start gap-3 rounded-lg border border-border p-3 text-sm",
                      choice.isCorrect && "border-success bg-success/5"
                    )}
                  >
                    <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full border border-current text-xs font-semibold">
                      {choice.label}
                    </span>
                    <span dangerouslySetInnerHTML={{ __html: choice.content || `Choice ${choice.label}` }} />
                  </div>
                ))}
              </div>
              <Separator />
              <div className="flex flex-wrap gap-2">
                <Badge variant="outline">{activeDomain?.name}</Badge>
                <Badge variant="outline">{difficulty}</Badge>
                {isPublished ? <Badge variant="success">Published</Badge> : <Badge variant="warning">Draft</Badge>}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
