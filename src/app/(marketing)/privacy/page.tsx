import { LegalLayout, Section } from "@/components/marketing/legal-layout";
import { getSettings } from "@/lib/settings";

export const metadata = {
  title: "Privacy Policy",
  description: "What SATForge collects, why, and how to get it deleted.",
};
export const dynamic = "force-dynamic";

/**
 * Privacy policy.
 *
 * Written from the actual schema rather than a template: every category listed
 * below corresponds to a real column the product writes. A policy that claims
 * less than the database holds is worse than none, and one that claims more
 * frightens people for no reason.
 */
export default async function PrivacyPage() {
  const settings = await getSettings();
  const contact = settings.contactEmail;
  const telegram = settings.telegramHandle;

  return (
    <LegalLayout title="Privacy Policy" updated="9 August 2026">
      <Section title="The short version">
        <p>
          SATForge is free and we do not sell anything, so we have no reason to sell your data — and
          we don&apos;t. We collect what the product needs to build your study plan and nothing we
          have no use for. You can ask us to delete your account and everything attached to it at
          any time, and we will.
        </p>
      </Section>

      <Section title="Who we are">
        <p>
          SATForge ({settings.operatorName}) operates satforge.org. For anything in this policy,
          including data deletion requests, contact{" "}
          {contact ? (
            <a href={`mailto:${contact}`} className="text-primary underline-offset-4 hover:underline">
              {contact}
            </a>
          ) : (
            <span>us on Telegram at @{telegram}</span>
          )}
          .
        </p>
      </Section>

      <Section title="What we collect">
        <p>Only these, and only because each one is used:</p>
        <ul className="list-disc space-y-1.5 pl-5">
          <li>
            <strong className="text-foreground">Account</strong> — your name, email address and a
            hashed password. We never store your password itself, only a bcrypt hash of it, which
            cannot be reversed.
          </li>
          <li>
            <strong className="text-foreground">What you tell us at signup</strong> — your current
            and target SAT score, test date, school year, country, the universities you&apos;re
            aiming at, your weakest area and how much time you can study. This is what makes your
            plan yours; without it everyone gets the same generic advice.
          </li>
          <li>
            <strong className="text-foreground">Your activity</strong> — which questions you
            answered, whether you got them right, how long each took, your scores, bookmarks and
            streaks. This is what the plan adapts to.
          </li>
          <li>
            <strong className="text-foreground">Sessions</strong> — when you book, what you asked
            for, and your timezone.
          </li>
          <li>
            <strong className="text-foreground">Coins and referrals</strong> — your balance, every
            transaction, and who invited you.
          </li>
        </ul>
        <p>
          We do not use advertising trackers, we do not build a profile of you for anyone else, and
          we do not ask for your address, phone number or payment details — SATForge is free, so
          there is nothing to pay.
        </p>
      </Section>

      <Section title="Why we&apos;re allowed to hold it">
        <p>
          We hold your account and practice data to provide the service you signed up for. Where
          local law requires consent, creating an account and answering the onboarding questions is
          that consent — and you can withdraw it by deleting your account.
        </p>
      </Section>

      <Section title="If you are under 18">
        <p>
          Most SAT students are. SATForge is intended for students aged 13 and over. If you are
          under the age where your country lets you agree to this on your own — 13 in the US, 16 in
          much of Europe — please ask a parent or guardian to read this with you before signing up.
        </p>
        <p>
          A parent or guardian can email us to see what we hold about their child or have it
          deleted, and we will act on that without argument. We do not knowingly collect data from
          children under 13; if we discover we have, we delete it.
        </p>
      </Section>

      <Section title="Who else sees it">
        <p>
          A small number of services we depend on, each doing one job, none of whom are allowed to
          use your data for their own purposes:
        </p>
        <ul className="list-disc space-y-1.5 pl-5">
          <li>
            <strong className="text-foreground">Vercel</strong> — hosts the website.
          </li>
          <li>
            <strong className="text-foreground">Neon</strong> — hosts the database.
          </li>
          <li>
            <strong className="text-foreground">Google Meet</strong> — runs the video call if you
            book a session. Google&apos;s own terms apply while you are in the call.
          </li>
          <li>
            <strong className="text-foreground">Resend</strong> — delivers emails such as booking
            confirmations and password resets.
          </li>
        </ul>
        <p>
          When you book a session, the mentor running it sees your name, email and what you wrote in
          the booking form — that is how they prepare for your session.
        </p>
        <p>
          Because these services operate internationally, your data may be processed outside your
          country.
        </p>
      </Section>

      <Section title="How long we keep it">
        <p>
          For as long as you have an account. Delete your account and we remove your profile,
          practice history, bookings, coins and referral records. We may keep a minimal record that
          an account was deleted, so that a deleted account cannot be silently re-credited with
          referral rewards.
        </p>
      </Section>

      <Section title="Your rights">
        <p>
          You can ask us for a copy of everything we hold about you, ask us to correct it, or ask us
          to delete it. Email us and we will do it — we are not going to make you fill in a form.
          You can also edit most of your profile yourself from Settings.
        </p>
      </Section>

      <Section title="Security">
        <p>
          Passwords are hashed with bcrypt. Traffic is encrypted in transit. Coin balances and
          session bookings are only ever changed on our servers, never from your browser, so they
          cannot be tampered with from the client.
        </p>
        <p>
          No system is perfect. If you find a security problem in SATForge, please tell us rather
          than anyone else, and we will fix it and credit you if you want us to.
        </p>
      </Section>

      <Section title="Changes">
        <p>
          If we change this policy in a way that matters, we will say so on the site rather than
          quietly updating the date at the top.
        </p>
      </Section>
    </LegalLayout>
  );
}
