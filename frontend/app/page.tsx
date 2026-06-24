import { Header } from "@/components/header";
import { SearchPanel } from "@/components/search-panel";
import { categories, platformState } from "@/lib/platform";

const howToJsonLd = {
  "@context": "https://schema.org",
  "@type": "HowTo",
  name: "Plan a civic workflow with ProcessIQ",
  step: [
    { "@type": "HowToStep", name: "Enter a goal" },
    { "@type": "HowToStep", name: "Review detected category and timeline" },
    { "@type": "HowToStep", name: "Verify each service on official portals" }
  ]
};

const faqJsonLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: [
    {
      "@type": "Question",
      name: "Does ProcessIQ submit applications?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "No. ProcessIQ provides informational workflow guidance only."
      }
    },
    {
      "@type": "Question",
      name: "Which state is supported?",
      acceptedAnswer: {
        "@type": "Answer",
        text: `ProcessIQ currently supports ${platformState.name} workflows.`
      }
    }
  ]
};

export default function Home() {
  return (
    <>
      <Header />
      <main>
        <section className="shell grid min-h-[calc(100vh-64px)] content-center gap-10 py-10">
          <div className="mx-auto max-w-4xl text-center">
            <p className="mb-3 text-sm font-semibold uppercase tracking-[0.18em] text-[var(--accent)]">
              ProcessIQ
            </p>
            <h1 className="text-4xl font-semibold tracking-tight sm:text-6xl">
              Plan {platformState.name} civic processes effortlessly
            </h1>
            <p className="mx-auto mt-5 max-w-2xl text-base leading-7 text-[var(--muted)]">
              Goal-oriented workflows with deterministic phases, official portals, and source freshness.
            </p>
          </div>
          <SearchPanel />
        </section>

        <section className="border-y border-[var(--line)] bg-white py-10">
          <div className="shell">
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
              {categories.map((category) => (
                <a
                  key={category}
                  href="/workflow"
                  className="rounded-md border border-[var(--line)] p-4 text-sm font-semibold transition hover:border-[var(--brand)]"
                >
                  {category}
                </a>
              ))}
            </div>
          </div>
        </section>

        <section id="faq" className="shell grid gap-4 py-10 md:grid-cols-2">
          <div className="rounded-md border border-[var(--line)] bg-white p-5">
            <h2 className="font-semibold">Informational only</h2>
            <p className="mt-2 text-sm leading-6 text-[var(--muted)]">
              ProcessIQ provides informational workflow guidance only.
            </p>
          </div>
          <div className="rounded-md border border-[var(--line)] bg-white p-5">
            <h2 className="font-semibold">Verify officially</h2>
            <p className="mt-2 text-sm leading-6 text-[var(--muted)]">
              Always verify details using official government portals.
            </p>
          </div>
        </section>
      </main>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(howToJsonLd) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }} />
    </>
  );
}
