SUPPORTED_STATES = {
    "TN": {
        "name": "Tamil Nadu",
        "planned": ["Karnataka", "Kerala"]
    }
}

SERVICES = {
    "patta": {
        "id": "patta",
        "name": "Patta Verification",
        "department": "Revenue Department",
        "approximate_cost": "Varies by portal fee",
        "processing_time": "7-15 days",
        "official_url": "https://eservices.tn.gov.in",
        "source_document": "TN e-Services public guidance",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "ec": {
        "id": "ec",
        "name": "Encumbrance Certificate",
        "department": "Registration Department",
        "approximate_cost": "Varies by search period",
        "processing_time": "3-7 days",
        "official_url": "https://tnreginet.gov.in",
        "source_document": "TNREGINET service listing",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "survey": {
        "id": "survey",
        "name": "Survey Sketch",
        "department": "Survey and Settlement Department",
        "approximate_cost": "As notified",
        "processing_time": "10-20 days",
        "official_url": "https://eservices.tn.gov.in",
        "source_document": "Revenue service catalogue",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "building_approval": {
        "id": "building-approval",
        "name": "Building Approval",
        "department": "Local Planning Authority",
        "approximate_cost": "Based on building area",
        "processing_time": "30-45 days",
        "official_url": "https://onlineppa.tn.gov.in",
        "source_document": "Online Planning Permission portal",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "water": {
        "id": "water",
        "name": "Water",
        "department": "Local Body / Water Board",
        "approximate_cost": "Connection charges apply",
        "processing_time": "7-21 days",
        "official_url": "https://tnurbanepay.tn.gov.in",
        "source_document": "Urban local body services",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "electricity": {
        "id": "electricity",
        "name": "Electricity",
        "department": "TANGEDCO",
        "approximate_cost": "Connection charges apply",
        "processing_time": "7-30 days",
        "official_url": "https://nsc.tnebltd.gov.in",
        "source_document": "TANGEDCO new service connection",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "trade_license": {
        "id": "trade-license",
        "name": "Trade Licence",
        "department": "Local Body",
        "approximate_cost": "As notified",
        "processing_time": "7-15 days",
        "official_url": "https://tnurbanepay.tn.gov.in",
        "source_document": "Urban local body trade licence guidance",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "fssai": {
        "id": "fssai",
        "name": "FSSAI Registration",
        "department": "Food Safety and Standards Authority",
        "approximate_cost": "Based on licence type",
        "processing_time": "7-30 days",
        "official_url": "https://foscos.fssai.gov.in",
        "source_document": "FoSCoS public service guidance",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "gst": {
        "id": "gst",
        "name": "GST Registration",
        "department": "Goods and Services Tax Network",
        "approximate_cost": "No government fee",
        "processing_time": "3-7 days",
        "official_url": "https://www.gst.gov.in",
        "source_document": "GST registration portal",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "rc_transfer": {
        "id": "rc-transfer",
        "name": "Vehicle Ownership Transfer",
        "department": "Transport Department",
        "approximate_cost": "Based on vehicle class",
        "processing_time": "7-15 days",
        "official_url": "https://parivahan.gov.in",
        "source_document": "Parivahan transfer of ownership service",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "sale_deed_registration": {
        "id": "sale-deed-registration",
        "name": "Sale Deed Registration",
        "department": "Registration Department",
        "approximate_cost": "Stamp duty and registration fee apply",
        "processing_time": "1-7 days",
        "official_url": "https://tnreginet.gov.in",
        "source_document": "TNREGINET document registration guidance",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    },
    "patta_transfer": {
        "id": "patta-transfer",
        "name": "Patta Transfer",
        "department": "Revenue Department",
        "approximate_cost": "As notified",
        "processing_time": "15-30 days",
        "official_url": "https://eservices.tn.gov.in",
        "source_document": "TN e-Services patta transfer guidance",
        "last_verified": "2026-06-01",
        "version": "2026.06",
        "applicable_state": "TN"
    }
}

GOALS = {
    "build_house": {
        "patterns": [r"\bbuild\b.*\b(house|home)\b", r"\bconstruct\b.*\bhouse\b"],
        "goal": "Build House",
        "category": "Property and Housing",
        "timeline": "6-12 weeks",
        "services": ["patta", "ec", "survey", "building_approval", "water", "electricity"],
        "dependencies": [
            ("patta", "building_approval"),
            ("ec", "building_approval"),
            ("survey", "building_approval"),
            ("building_approval", "water"),
            ("building_approval", "electricity")
        ]
    },
    "open_bakery": {
        "patterns": [r"\b(open|start)\b.*\bbakery\b", r"\bbakery\b"],
        "goal": "Open Bakery",
        "category": "Business and Entrepreneurship",
        "timeline": "3-8 weeks",
        "services": ["trade_license", "fssai", "gst"],
        "dependencies": [("trade_license", "fssai")]
    },
    "vehicle_transfer": {
        "patterns": [r"\bvehicle\b.*\btransfer\b", r"\brc\b.*\btransfer\b"],
        "goal": "Vehicle Transfer",
        "category": "Vehicles",
        "timeline": "1-3 weeks",
        "services": ["rc_transfer"],
        "dependencies": []
    },
    "sale_land": {
        "patterns": [
            r"\bsale\b.*\bland\b",
            r"\bsell\b.*\bland\b",
            r"\bland\b.*\bsale\b",
            r"\bsell\b.*\bproperty\b"
        ],
        "goal": "Sale Land",
        "category": "Property and Housing",
        "timeline": "2-6 weeks",
        "services": ["patta", "ec", "sale_deed_registration", "patta_transfer"],
        "dependencies": [
            ("patta", "sale_deed_registration"),
            ("ec", "sale_deed_registration"),
            ("sale_deed_registration", "patta_transfer")
        ]
    }
}
