import { Suspense } from "react";
import { Header } from "@/components/header";
import { WorkflowClient } from "@/components/workflow-client";

export default function WorkflowPage() {
  return (
    <>
      <Header />
      <Suspense fallback={<WorkflowFallback />}>
        <WorkflowClient />
      </Suspense>
    </>
  );
}

function WorkflowFallback() {
  return (
    <main className="shell py-8">
      <section className="rounded-md border border-[var(--line)] bg-white p-8 text-center">
        <h1 className="text-2xl font-semibold">Loading workflow</h1>
      </section>
    </main>
  );
}
