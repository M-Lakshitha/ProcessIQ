import Link from "next/link";
import { CheckCircle2 } from "lucide-react";

export function Header() {
  return (
    <header className="border-b border-[var(--line)] bg-white/80 backdrop-blur">
      <div className="shell flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-semibold tracking-tight">
          <span className="grid size-8 place-items-center rounded-md bg-[var(--brand)] text-white">
            <CheckCircle2 size={18} />
          </span>
          ProcessIQ
        </Link>
        <nav className="hidden items-center gap-6 text-sm text-[var(--muted)] sm:flex">
          <Link href="/#examples" className="hover:text-[var(--foreground)]">Examples</Link>
          <Link href="/workflow" className="hover:text-[var(--foreground)]">Workflow</Link>
          <Link href="/#faq" className="hover:text-[var(--foreground)]">FAQ</Link>
        </nav>
      </div>
    </header>
  );
}
