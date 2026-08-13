import { Landing } from "@/components/marketing/landing";
import { PartnersStrip } from "@/components/marketing/partners-strip";

export default function HomePage() {
  return <Landing partners={<PartnersStrip />} />;
}
