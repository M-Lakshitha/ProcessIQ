"use client";

import { useRouter } from "next/navigation";
import toast from "react-hot-toast";
import { ArrowRight, Search } from "lucide-react";
import { motion } from "framer-motion";
import { examples, platformState } from "@/lib/platform";
import { useWorkflowStore } from "@/store/workflow-store";

type SearchPanelProps = {
  compact?: boolean;
};

export function SearchPanel({ compact = false }: SearchPanelProps) {
  const router = useRouter();
  const { goal, selectedState, setGoal, setState, generate, unsupportedMessage } = useWorkflowStore();

  function submit() {
    if (!goal.trim()) {
      toast.error("Enter a goal first.");
      return;
    }

    const result = generate();
    if (!result.ok) {
      toast(result.message ?? unsupportedMessage ?? "Clarification needed.");
      return;
    }
    router.push(`/workflow?goal=${encodeURIComponent(goal)}&state=${selectedState}`);
  }

  return (
    <motion.section
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35 }}
      className={compact ? "space-y-4" : "mx-auto max-w-3xl space-y-5"}
    >
      <div className="grid gap-3 rounded-md border border-[var(--line)] bg-white p-3 shadow-sm sm:grid-cols-[1fr_170px_auto]">
        <label className="flex min-h-12 items-center gap-3 rounded-md border border-transparent bg-[#f2f5f1] px-4">
          <Search size={19} className="shrink-0 text-[var(--brand)]" />
          <input
            className="focus-ring w-full bg-transparent text-base outline-none placeholder:text-[#7c8782]"
            value={goal}
            onChange={(event) => setGoal(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === "Enter") {
                submit();
              }
            }}
            placeholder="What would you like to accomplish?"
          />
        </label>
        <select
          aria-label="State"
          value={selectedState}
          onChange={(event) => setState(event.target.value)}
          className="focus-ring min-h-12 rounded-md border border-[var(--line)] bg-white px-3 text-sm"
        >
          <option value={platformState.code}>{platformState.name}</option>
          <option value="KA">Karnataka</option>
          <option value="KL">Kerala</option>
        </select>
        <button
          onClick={submit}
          className="focus-ring inline-flex min-h-12 items-center justify-center gap-2 rounded-md bg-[var(--brand)] px-5 font-semibold text-white transition hover:bg-[#0d4d50]"
        >
          Generate Workflow
          <ArrowRight size={18} />
        </button>
      </div>
      {!compact ? (
        <div id="examples" className="flex flex-wrap items-center justify-center gap-2">
          <span className="mr-1 text-sm text-[var(--muted)]">Popular examples</span>
          {examples.map((example) => (
            <button
              key={example}
              onClick={() => setGoal(example)}
              className="focus-ring rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm hover:border-[var(--brand)]"
            >
              {example}
            </button>
          ))}
        </div>
      ) : null}
    </motion.section>
  );
}
