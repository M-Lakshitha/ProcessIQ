import type { Metadata } from "next";
import type { ReactNode } from "react";
import Script from "next/script";
import { Toaster } from "react-hot-toast";
import "./globals.css";

const siteUrl = "https://processiq.in";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "ProcessIQ | Civic Workflow Planning",
    template: "%s | ProcessIQ"
  },
  description: "Plan Tamil Nadu civic processes with deterministic, source-backed workflow guidance.",
  alternates: {
    canonical: "/"
  },
  openGraph: {
    title: "ProcessIQ",
    description: "Goal-oriented civic workflow planning for Tamil Nadu.",
    url: siteUrl,
    siteName: "ProcessIQ",
    type: "website"
  },
  robots: {
    index: true,
    follow: true
  },
  keywords: [
    "inherit property tamil nadu",
    "build warehouse tamil nadu",
    "open bakery tamil nadu",
    "vehicle transfer tamil nadu"
  ]
};

export default function RootLayout({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <html lang="en">
      <body>
        {children}
        <Toaster position="top-right" />
        {process.env.NEXT_PUBLIC_PLAUSIBLE_DOMAIN ? (
          <Script
            defer
            data-domain={process.env.NEXT_PUBLIC_PLAUSIBLE_DOMAIN}
            src="https://plausible.io/js/script.js"
          />
        ) : null}
      </body>
    </html>
  );
}
