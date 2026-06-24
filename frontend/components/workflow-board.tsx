"use client";

import { motion } from "framer-motion";
import { CalendarDays, ExternalLink, FileText, GitBranch, Landmark, ShieldCheck } from "lucide-react";
import type { ReactNode } from "react";
import type { Workflow } from "@/lib/workflows";

type WorkflowBoardProps = {
  workflow: Workflow;
};

export function WorkflowBoard({ workflow }: WorkflowBoardProps) {
  return (
    <section className="space-y-6">
      <div className="grid gap-3 md:grid-cols-3">
        <Metric icon={<ShieldCheck size={18} />} label="Goal detected" value={workflow.goal} />
        <Metric icon={<GitBranch size={18} />} label="Category" value={workflow.category} />
        <Metric icon={<CalendarDays size={18} />} label="Timeline" value={workflow.timeline} />
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="grid min-w-[760px] gap-4 md:grid-cols-3">
          {workflow.phases.map((phase, index) => (
            <motion.div
              key={phase.id}
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.08 }}
              className="rounded-md border border-[var(--line)] bg-white p-4"
            >
              <p className="text-sm font-semibold text-[var(--accent)]">{phase.title}</p>
              <div className="mt-4 space-y-3">
                {phase.services.map((service) => (
                  <article key={service.id} className="rounded-md border border-[#e6ebe6] bg-[#fafbf8] p-4">
                    <h3 className="font-semibold">{service.name}</h3>
                    <dl className="mt-4 grid gap-3 text-sm">
                      <Info label="Department" value={service.department} icon={<Landmark size={15} />} />
                      <Info label="Approximate cost" value={service.approximateCost} />
                      <Info label="Processing time" value={service.processingTime} />
                      <Info
                        label="Official URL"
                        value={
                          <a className="inline-flex items-center gap-1 text-[var(--brand)]" href={service.officialUrl}>
                            Portal <ExternalLink size={13} />
                          </a>
                        }
                      />
                      <Info label="Source document" value={service.sourceDocument} icon={<FileText size={15} />} />
                      <Info label="Last verified" value={service.lastVerified} />
                      <Info label="Version" value={service.version} />
                      <Info label="Applicable State" value={service.applicableState} />
                    </dl>
                  </article>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Metric({ icon, label, value }: { icon: ReactNode; label: string; value: string }) {
  return (
    <div className="rounded-md border border-[var(--line)] bg-white p-4">
      <div className="flex items-center gap-2 text-sm text-[var(--muted)]">
        {icon}
        {label}
      </div>
      <p className="mt-2 text-lg font-semibold">{value}</p>
    </div>
  );
}

function Info({
  icon,
  label,
  value
}: {
  icon?: ReactNode;
  label: string;
  value: ReactNode;
}) {
  return (
    <div className="grid grid-cols-[118px_1fr] gap-3">
      <dt className="flex items-center gap-1 text-[var(--muted)]">{icon}{label}</dt>
      <dd className="min-w-0 font-medium">{value}</dd>
    </div>
  );
}
