export type SupportedState = {
  code: string;
  name: string;
  planned: string[];
};

export const platformState: SupportedState = {
  code: "TN",
  name: "Tamil Nadu",
  planned: ["Karnataka", "Kerala"]
};

export const categories = [
  "Property and Housing",
  "Business and Entrepreneurship",
  "Marriage and Family",
  "Death and Inheritance",
  "Vehicles",
  "Construction and Industry",
  "Entertainment Businesses",
  "Digital Economy"
];

export const examples = [
  "Build House",
  "Open Bakery",
  "Marriage Hall",
  "Vehicle Transfer"
];
