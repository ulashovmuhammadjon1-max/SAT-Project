import { LegalLayout, Section } from "@/components/marketing/legal-layout";
import { getSettings } from "@/lib/settings";

export const metadata = {
  title: "Terms of Use",
  description: "The rules for using SATForge — short, and in plain English.",
};
export const dynamic = "force-dynamic";

/**
 * Terms of use.
 *
 * Deliberately plain. The audience is teenagers, and a wall of legalese nobody
 * reads protects nobody. Every clause here describes something the product
 * actually does — the coin rules match lib/settings.ts and lib/coins.ts, and
 * the community-check clause matches what the booking form says.
 */
export default async function TermsPage() {
  const settings = await getSettings();
  const contact = settings.contactEmail;

  return (
    <LegalLayout title="Terms of Use" updated="9 August 2026">
      <Section title="The short version">
        <p>
          SATForge is free. Use it to study, don&apos;t abuse it, don&apos;t redistribute what is on
          it, and be decent to the people running it. That&apos;s essentially all of it — the rest is
          detail.
        </p>
      </Section>

      <Section title="Using SATForge">
        <p>
          You need an account, and you must give a real email address so we can reach you about your
          sessions. One account per person. You are responsible for what happens under your account,
          so keep your password to yourself.
        </p>
        <p>
          You must be at least 13. If you are under the age at which your country lets you agree to
          terms on your own, a parent or guardian needs to agree on your behalf.
        </p>
      </Section>

      <Section title="What we don&apos;t promise">
        <p>
          We do <strong className="text-foreground">not</strong> promise a particular SAT score. No
          preparation platform honestly can — your score depends on your work. Estimates shown in
          the app are estimates, not predictions, and are labelled as such.
        </p>
        <p>
          SATForge is not affiliated with, endorsed by, or connected to the College Board, which
          administers the SAT. &ldquo;SAT&rdquo; is their trademark; we use it only to describe what
          this platform prepares you for.
        </p>
      </Section>

      <Section title="Using the material">
        <p>
          Everything on SATForge is here for you to study with, personally, as much as you like.
          Please do not republish it, sell it, feed it into another product, or scrape the site in
          bulk — that is the fastest way to make a free platform stop being free.
        </p>
      </Section>

      <Section title="SATForge Coins">
        <p>
          Coins are points inside SATForge for booking sessions. They are{" "}
          <strong className="text-foreground">not money</strong>. They cannot be bought, sold,
          exchanged, transferred between accounts, or cashed out, and they have no value outside
          this site.
        </p>
        <p>
          You get {settings.signupBonusCoins} when you sign up and {settings.referralRewardCoins}{" "}
          when a friend joins through your link and confirms their email address. A friend counts
          once — referring yourself, or making extra accounts, does not work and will cost you the
          coins you gained that way.
        </p>
        <p>
          We may adjust balances to correct a mistake or reverse abuse. Every adjustment is recorded
          in your wallet history, so you can always see what happened and why.
        </p>
      </Section>

      <Section title="Sessions">
        <p>
          Sessions are free and run by volunteers. Booking one costs coins, which exist to keep the
          limited spots reaching as many students as possible rather than the same few people.
        </p>
        <p>
          Before each session, volunteers check that you are subscribed to our Instagram and
          Telegram. If you are not, the session is cancelled and your coins are returned.
        </p>
        <p>
          Cancel at least {settings.bookingRefundHours ?? 24} hours before and your coins come back.
          Repeatedly booking and not showing up may cost you access to sessions — someone else
          wanted that slot.
        </p>
        <p>
          We may need to move or cancel a session. If we do, your coins are returned in full.
        </p>
      </Section>

      <Section title="Things you must not do">
        <ul className="list-disc space-y-1.5 pl-5">
          <li>Create multiple accounts, including to farm referral coins.</li>
          <li>Scrape, bulk-download, or republish material from the site.</li>
          <li>Try to break, overload, or find your way around the site&apos;s security.</li>
          <li>Harass or abuse mentors, volunteers or other students, in sessions or anywhere else.</li>
          <li>Share your account with someone else.</li>
        </ul>
        <p>
          If you do these things we may suspend or delete your account. For anything serious we will
          do it without warning.
        </p>
      </Section>

      <Section title="Ending it">
        <p>
          You can stop using SATForge whenever you like and ask us to delete your account. We may
          close an account that breaks these terms. If we ever shut the service down, we will give
          notice so you can take your data with you.
        </p>
      </Section>

      <Section title="Liability">
        <p>
          SATForge is provided as-is, free of charge. We are not liable for exam results, missed
          deadlines, or decisions you make based on the site. We are, of course, still responsible
          for things the law does not let us disclaim.
        </p>
      </Section>

      <Section title="Questions">
        <p>
          {contact ? (
            <>
              Email{" "}
              <a href={`mailto:${contact}`} className="text-primary underline-offset-4 hover:underline">
                {contact}
              </a>{" "}
              or message us on Telegram at @{settings.telegramHandle}.
            </>
          ) : (
            <>Message us on Telegram at @{settings.telegramHandle}.</>
          )}
        </p>
      </Section>
    </LegalLayout>
  );
}
