"use client";

import { useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { AlertTriangle } from "lucide-react";
import { SearchPanel } from "@/components/search-panel";
import { WorkflowBoard } from "@/components/workflow-board";
import { platformState } from "@/lib/platform";
import { useWorkflowStore } from "@/store/workflow-store";

export function WorkflowClient() {
  const params = useSearchParams();
  const { setGoal, setState, generate, workflow, unsupportedMessage } = useWorkflowStore();

  useEffect(() => {
    const goal = params.get("goal");
    const state = params.get("state");
    if (goal) {
      setGoal(goal);
    }
    if (state) {
      setState(state);
    }
    if (goal) {
      queueMicrotask(() => generate());
    }
  }, [generate, params, setGoal, setState]);

  return (
    <main className="shell space-y-8 py-8">
      <SearchPanel compact />

      {unsupportedMessage && !workflow ? (
        <div className="flex gap-3 rounded-md border border-[#f0d7b9] bg-[#fff9ef] p-4 text-sm">
          <AlertTriangle className="mt-0.5 shrink-0 text-[var(--accent)]" size={18} />
          <p>{unsupportedMessage}</p>
        </div>
      ) : null}

      {workflow ? (
        <>
          <WorkflowBoard workflow={workflow} />
          <section className="rounded-md border border-[var(--line)] bg-white p-5 text-sm leading-6 text-[var(--muted)]">
            This workflow is generated from manually verified sources and predefined rules. ProcessIQ does not
            guarantee approval or legal compliance.
          </section>
        </>
      ) : (
        <section className="rounded-md border border-[var(--line)] bg-white p-8 text-center">
          <h1 className="text-2xl font-semibold">Generate a workflow</h1>
          <p className="mx-auto mt-3 max-w-xl text-sm leading-6 text-[var(--muted)]">
            Current coverage is scoped to {platformState.name}. More states and services can be added through the same
            schema.
          </p>
        </section>
      )}
    </main>
  );
}
