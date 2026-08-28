import { redirect } from "next/navigation";

/** The classroom moved to /classes — old links and emails land here. */
export default function LegacyClassPage() {
  redirect("/classes");
}
