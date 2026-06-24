"use client";

import { create } from "zustand";
import { resolveWorkflow, type Workflow } from "@/lib/workflows";
import { platformState } from "@/lib/platform";

type WorkflowStore = {
  goal: string;
  selectedState: string;
  workflow: Workflow | null;
  unsupportedMessage: string | null;
  setGoal: (goal: string) => void;
  setState: (state: string) => void;
  generate: () => { ok: boolean; message: string | null };
};

export const useWorkflowStore = create<WorkflowStore>((set, get) => ({
  goal: "",
  selectedState: platformState.code,
  workflow: null,
  unsupportedMessage: null,
  setGoal: (goal) => set({ goal }),
  setState: (selectedState) => set({ selectedState }),
  generate: () => {
    const { goal, selectedState } = get();

    if (selectedState !== platformState.code) {
      set({
        workflow: null,
        unsupportedMessage: `ProcessIQ currently supports ${platformState.name} workflows. Support for ${platformState.planned.join(", ")} and other states is planned.`
      });
      return {
        ok: false,
        message: `ProcessIQ currently supports ${platformState.name} workflows. Support for ${platformState.planned.join(", ")} and other states is planned.`
      };
    }

    const workflow = resolveWorkflow(goal);
    const message = workflow ? null : "We need a little more detail to match this goal to a predefined workflow.";
    set({
      workflow,
      unsupportedMessage: message
    });

    return { ok: Boolean(workflow), message };
  }
}));
