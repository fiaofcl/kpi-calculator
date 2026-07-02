"""
Maps each industry to the KPIs that are most relevant for it,
along with a short note explaining why each KPI matters in that context.
"""

INDUSTRIES = {
    "1": {
        "name": "E-commerce",
        "description": "Online retail, direct-to-consumer stores\n",
        "kpis": [
            "conversion_rate",
            "average_order_value",
            "customer_acquisition_cost",
            "customer_lifetime_value",
            "clv_to_cac_ratio",
            "churn_rate",
            "revenue_growth",
            "gross_profit_margin",
        ],
        "tips": [
            "AOV × Conversion Rate drives most e-commerce revenue growth.",
            "CLV:CAC should be ≥ 3:1 — below that, ads are eating your margin.",
            "Churn > 5%/month means your retention strategy needs work.",
        ],
    },
    "2": {
        "name": "SaaS / Software",
        "description": "Subscription software products\n",
        "kpis": [
            "churn_rate",
            "customer_lifetime_value",
            "customer_acquisition_cost",
            "clv_to_cac_ratio",
            "revenue_growth",
            "net_profit_margin",
            "mrr",
        ],
        "tips": [
            "Churn is the #1 SaaS killer — even 2%/month = ~22% annual loss.",
            "CLV:CAC should be ≥ 3:1. Payback period ideally under 12 months.",
            "MRR growth rate matters more than absolute revenue at early stage.",
        ],
    },
    "3": {
        "name": "Retail (Brick & Mortar)",
        "description": "Physical stores, shops, supermarkets\n",
        "kpis": [
            "revenue_growth",
            "average_order_value",
            "gross_profit_margin",
            "net_profit_margin",
            "conversion_rate",
            "customer_acquisition_cost",
        ],
        "tips": [
            "Gross margin is everything in retail — watch COGS closely.",
            "Conversion rate here = (transactions / foot traffic) × 100.",
            "Net margin in retail is often thin (2–5%) — volume is key.",
        ],
    },
    "4": {
        "name": "Agency / Consulting",
        "description": "Marketing, design, legal, consulting firms\n",
        "kpis": [
            "revenue_growth",
            "net_profit_margin",
            "customer_acquisition_cost",
            "customer_lifetime_value",
            "clv_to_cac_ratio",
            "churn_rate",
        ],
        "tips": [
            "Client retention (inverse of churn) is critical — acquiring clients is expensive.",
            "Net margin for agencies should be 15–30%.",
            "CLV is high if clients stay long — focus on retainer relationships.",
        ],
    },
    "5": {
        "name": "Restaurant / Food & Beverage",
        "description": "Restaurants, cafes, food delivery, catering\n",
        "kpis": [
            "revenue_growth",
            "average_order_value",
            "gross_profit_margin",
            "net_profit_margin",
            "churn_rate",
            "conversion_rate",
        ],
        "tips": [
            "Food cost (COGS) should be 28–35% of revenue for healthy margins.",
            "Net margin in restaurants is typically 3–9% — very tight.",
            "Repeat customer rate (inverse of churn) is a strong loyalty signal.",
        ],
    },
    "6": {
        "name": "Healthcare / Clinic",
        "description": "Private clinics, dental, therapy, wellness\n",
        "kpis": [
            "revenue_growth",
            "customer_acquisition_cost",
            "customer_lifetime_value",
            "clv_to_cac_ratio",
            "churn_rate",
            "net_profit_margin",
        ],
        "tips": [
            "Patient retention (low churn) is the primary growth lever.",
            "CLV is high in healthcare — patients return for years.",
            "CAC via referrals is far lower than paid ads — track the difference.",
        ],
    },
    "7": {
        "name": "Real Estate",
        "description": "Property sales, rentals, property management\n",
        "kpis": [
            "revenue_growth",
            "customer_acquisition_cost",
            "conversion_rate",
            "net_profit_margin",
            "gross_profit_margin",
        ],
        "tips": [
            "Conversion rate = leads that closed as deals.",
            "CAC in real estate is high — track cost per closed deal.",
            "Net margin varies widely: 10–30% for sales, thinner for rentals.",
        ],
    },
    "8": {
        "name": "Manufacturing",
        "description": "Factories, production lines, industrial goods\n",
        "kpis": [
            "revenue_growth",
            "gross_profit_margin",
            "net_profit_margin",
            "overall_equipment_effectiveness",
            "production_yield",
            "inventory_turnover",
            "customer_acquisition_cost",
        ],
        "tips": [
            "OEE below 65% signals major inefficiency — world class is 85%+.",
            "Production yield losses directly eat gross margin — track scrap rate.",
            "Inventory turnover should be high; slow-moving stock ties up cash.",
            "Gross margin in manufacturing typically ranges 25–40%.",
        ],
    },
    "9": {
        "name": "Pharma / Life Sciences",
        "description": "Pharmaceutical companies, biotech, medical devices\n",
        "kpis": [
            "revenue_growth",
            "gross_profit_margin",
            "net_profit_margin",
            "research_and_development_ratio",
            "production_yield",
            "customer_acquisition_cost",
            "customer_lifetime_value",
            "clv_to_cac_ratio",
        ],
        "tips": [
            "R&D ratio (R&D spend / revenue) is a core health metric — typically 15–25% in pharma.",
            "Gross margins in pharma are very high (60–90%) but R&D and compliance costs are heavy.",
            "Production yield is critical — batch failures are extremely expensive.",
            "CLV is very high for pharma — hospitals and clinics are long-term repeat buyers.",
        ],
    },
}

# KPI display labels (used in the filtered menu)
KPI_LABELS = {
    "revenue_growth":           "Revenue Growth",
    "customer_acquisition_cost": "Customer Acquisition Cost (CAC)",
    "churn_rate":                "Churn Rate",
    "conversion_rate":           "Conversion Rate",
    "average_order_value":       "Average Order Value (AOV)",
    "customer_lifetime_value":   "Customer Lifetime Value (CLV)",
    "gross_profit_margin":       "Gross Profit Margin",
    "net_profit_margin":         "Net Profit Margin",
    "clv_to_cac_ratio":          "CLV : CAC Ratio",
    "mrr":                            "Monthly Recurring Revenue (MRR)",
    "overall_equipment_effectiveness": "Overall Equipment Effectiveness (OEE)",
    "production_yield":                "Production Yield",
    "inventory_turnover":              "Inventory Turnover",
    "research_and_development_ratio":  "R&D Ratio",
}

