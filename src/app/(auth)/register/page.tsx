import { redirect } from "next/navigation";

/**
 * Sign-up now happens at the end of the onboarding wizard, so the product has a
 * single funnel. This route stays as a redirect for bookmarks and any links
 * still pointing at it.
 */
export default function RegisterPage() {
  redirect("/onboarding");
}
