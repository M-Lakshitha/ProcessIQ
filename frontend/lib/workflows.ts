import { platformState } from "./platform";

export type Service = {
  id: string;
  name: string;
  department: string;
  approximateCost: string;
  processingTime: string;
  officialUrl: string;
  sourceDocument: string;
  lastVerified: string;
  version: string;
  applicableState: string;
};

export type Phase = {
  id: string;
  title: string;
  services: Service[];
};

export type Workflow = {
  goal: string;
  category: string;
  timeline: string;
  phases: Phase[];
};

const common = {
  lastVerified: "2026-06-01",
  version: "2026.06",
  applicableState: platformState.code
};

export const workflows: Record<string, Workflow> = {
  "build house": {
    goal: "Build House",
    category: "Property and Housing",
    timeline: "6-12 weeks",
    phases: [
      {
        id: "land-readiness",
        title: "Phase 1",
        services: [
          {
            id: "patta",
            name: "Patta Verification",
            department: "Revenue Department",
            approximateCost: "Varies by portal fee",
            processingTime: "7-15 days",
            officialUrl: "https://eservices.tn.gov.in",
            sourceDocument: "TN e-Services public guidance",
            ...common
          },
          {
            id: "ec",
            name: "Encumbrance Certificate",
            department: "Registration Department",
            approximateCost: "Varies by search period",
            processingTime: "3-7 days",
            officialUrl: "https://tnreginet.gov.in",
            sourceDocument: "TNREGINET service listing",
            ...common
          },
          {
            id: "survey",
            name: "Survey Sketch",
            department: "Survey and Settlement Department",
            approximateCost: "As notified",
            processingTime: "10-20 days",
            officialUrl: "https://eservices.tn.gov.in",
            sourceDocument: "Revenue service catalogue",
            ...common
          }
        ]
      },
      {
        id: "approval",
        title: "Phase 2",
        services: [
          {
            id: "building-approval",
            name: "Building Approval",
            department: "Local Planning Authority",
            approximateCost: "Based on building area",
            processingTime: "30-45 days",
            officialUrl: "https://onlineppa.tn.gov.in",
            sourceDocument: "Online Planning Permission portal",
            ...common
          }
        ]
      },
      {
        id: "utilities",
        title: "Phase 3",
        services: [
          {
            id: "water",
            name: "Water",
            department: "Local Body / Water Board",
            approximateCost: "Connection charges apply",
            processingTime: "7-21 days",
            officialUrl: "https://tnurbanepay.tn.gov.in",
            sourceDocument: "Urban local body services",
            ...common
          },
          {
            id: "electricity",
            name: "Electricity",
            department: "TANGEDCO",
            approximateCost: "Connection charges apply",
            processingTime: "7-30 days",
            officialUrl: "https://nsc.tnebltd.gov.in",
            sourceDocument: "TANGEDCO new service connection",
            ...common
          }
        ]
      }
    ]
  },
  "open bakery": {
    goal: "Open Bakery",
    category: "Business and Entrepreneurship",
    timeline: "3-8 weeks",
    phases: [
      {
        id: "business-base",
        title: "Phase 1",
        services: [
          {
            id: "trade-license",
            name: "Trade Licence",
            department: "Local Body",
            approximateCost: "As notified",
            processingTime: "7-15 days",
            officialUrl: "https://tnurbanepay.tn.gov.in",
            sourceDocument: "Urban local body trade licence guidance",
            ...common
          },
          {
            id: "fssai",
            name: "FSSAI Registration",
            department: "Food Safety and Standards Authority",
            approximateCost: "Based on licence type",
            processingTime: "7-30 days",
            officialUrl: "https://foscos.fssai.gov.in",
            sourceDocument: "FoSCoS public service guidance",
            ...common
          }
        ]
      },
      {
        id: "operations",
        title: "Phase 2",
        services: [
          {
            id: "gst",
            name: "GST Registration",
            department: "Goods and Services Tax Network",
            approximateCost: "No government fee",
            processingTime: "3-7 days",
            officialUrl: "https://www.gst.gov.in",
            sourceDocument: "GST registration portal",
            ...common
          }
        ]
      }
    ]
  },
  "marriage hall": {
    goal: "Marriage Hall",
    category: "Entertainment Businesses",
    timeline: "8-16 weeks",
    phases: [
      {
        id: "site-and-building",
        title: "Phase 1",
        services: [
          {
            id: "building-approval",
            name: "Building Approval",
            department: "Local Planning Authority",
            approximateCost: "Based on building area",
            processingTime: "30-45 days",
            officialUrl: "https://onlineppa.tn.gov.in",
            sourceDocument: "Online Planning Permission portal",
            ...common
          }
        ]
      },
      {
        id: "business-clearances",
        title: "Phase 2",
        services: [
          {
            id: "fire-noc",
            name: "Fire NOC",
            department: "Fire and Rescue Services",
            approximateCost: "As notified",
            processingTime: "15-30 days",
            officialUrl: "https://www.tnfrs.tn.gov.in",
            sourceDocument: "TNFRS service information",
            ...common
          },
          {
            id: "trade-license",
            name: "Trade Licence",
            department: "Local Body",
            approximateCost: "As notified",
            processingTime: "7-15 days",
            officialUrl: "https://tnurbanepay.tn.gov.in",
            sourceDocument: "Urban local body trade licence guidance",
            ...common
          }
        ]
      }
    ]
  },
  "vehicle transfer": {
    goal: "Vehicle Transfer",
    category: "Vehicles",
    timeline: "1-3 weeks",
    phases: [
      {
        id: "transfer",
        title: "Phase 1",
        services: [
          {
            id: "rc-transfer",
            name: "Vehicle Ownership Transfer",
            department: "Transport Department",
            approximateCost: "Based on vehicle class",
            processingTime: "7-15 days",
            officialUrl: "https://parivahan.gov.in",
            sourceDocument: "Parivahan transfer of ownership service",
            ...common
          }
        ]
      }
    ]
  },
  "sale land": {
    goal: "Sale Land",
    category: "Property and Housing",
    timeline: "2-6 weeks",
    phases: [
      {
        id: "title-readiness",
        title: "Phase 1",
        services: [
          {
            id: "patta",
            name: "Patta Verification",
            department: "Revenue Department",
            approximateCost: "Varies by portal fee",
            processingTime: "7-15 days",
            officialUrl: "https://eservices.tn.gov.in",
            sourceDocument: "TN e-Services public guidance",
            ...common
          },
          {
            id: "ec",
            name: "Encumbrance Certificate",
            department: "Registration Department",
            approximateCost: "Varies by search period",
            processingTime: "3-7 days",
            officialUrl: "https://tnreginet.gov.in",
            sourceDocument: "TNREGINET service listing",
            ...common
          }
        ]
      },
      {
        id: "registration",
        title: "Phase 2",
        services: [
          {
            id: "sale-deed-registration",
            name: "Sale Deed Registration",
            department: "Registration Department",
            approximateCost: "Stamp duty and registration fee apply",
            processingTime: "1-7 days",
            officialUrl: "https://tnreginet.gov.in",
            sourceDocument: "TNREGINET document registration guidance",
            ...common
          }
        ]
      },
      {
        id: "mutation",
        title: "Phase 3",
        services: [
          {
            id: "patta-transfer",
            name: "Patta Transfer",
            department: "Revenue Department",
            approximateCost: "As notified",
            processingTime: "15-30 days",
            officialUrl: "https://eservices.tn.gov.in",
            sourceDocument: "TN e-Services patta transfer guidance",
            ...common
          }
        ]
      }
    ]
  }
};

export function resolveWorkflow(goal: string): Workflow | null {
  const normalized = goal.trim().toLowerCase();
  if (!normalized) {
    return null;
  }

  const direct = workflows[normalized];
  if (direct) {
    return direct;
  }

  if (normalized.includes("house") || normalized.includes("home")) {
    return workflows["build house"];
  }

  if (normalized.includes("bakery")) {
    return workflows["open bakery"];
  }

  if (normalized.includes("marriage") || normalized.includes("hall")) {
    return workflows["marriage hall"];
  }

  if (normalized.includes("vehicle") || normalized.includes("transfer")) {
    return workflows["vehicle transfer"];
  }

  if (
    normalized.includes("sale land") ||
    normalized.includes("sell land") ||
    normalized.includes("land sale") ||
    normalized.includes("sell property")
  ) {
    return workflows["sale land"];
  }

  return null;
}
