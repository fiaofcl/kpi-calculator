"""
Business / Sales KPI calculation logic.
Each function returns a dict with result, formula, and plain-english description.
"""


def revenue_growth(current_revenue: float, previous_revenue: float) -> dict:
    if previous_revenue == 0:
        raise ValueError("Previous revenue cannot be zero.")
    growth = ((current_revenue - previous_revenue) / previous_revenue) * 100
    return {
        "kpi":         "Revenue Growth",
        "result":      round(growth, 2),
        "unit":        "%",
        "formula":     "((current - previous) / previous) × 100",
        "description": "How much revenue grew or shrank vs the previous period. Positive = growth.",
    }


def customer_acquisition_cost(marketing: float, sales: float, new_customers: int) -> dict:
    if new_customers <= 0:
        raise ValueError("New customers must be greater than zero.")
    cac = (marketing + sales) / new_customers
    return {
        "kpi":         "Customer Acquisition Cost (CAC)",
        "result":      round(cac, 2),
        "unit":        "currency",
        "formula":     "(marketing_spend + sales_spend) / new_customers",
        "description": "Average cost to acquire one new customer. Compare to CLV to check profitability.",
    }


def churn_rate(lost: int, at_start: int) -> dict:
    if at_start <= 0:
        raise ValueError("Customers at start must be greater than zero.")
    rate = (lost / at_start) * 100
    return {
        "kpi":         "Churn Rate",
        "result":      round(rate, 2),
        "unit":        "%",
        "formula":     "(customers_lost / customers_at_start) × 100",
        "description": "Percentage of customers lost in a period. Lower is better.",
    }


def conversion_rate(conversions: int, visitors: int) -> dict:
    if visitors <= 0:
        raise ValueError("Total visitors must be greater than zero.")
    rate = (conversions / visitors) * 100
    return {
        "kpi":         "Conversion Rate",
        "result":      round(rate, 2),
        "unit":        "%",
        "formula":     "(conversions / total_visitors) × 100",
        "description": "Percentage of visitors or leads that completed a purchase/sign-up.",
    }


def average_order_value(revenue: float, orders: int) -> dict:
    if orders <= 0:
        raise ValueError("Number of orders must be greater than zero.")
    aov = revenue / orders
    return {
        "kpi":         "Average Order Value (AOV)",
        "result":      round(aov, 2),
        "unit":        "currency",
        "formula":     "total_revenue / number_of_orders",
        "description": "Average amount a customer spends per transaction.",
    }


def customer_lifetime_value(aov: float, frequency: float, lifespan: float) -> dict:
    if any(v <= 0 for v in [aov, frequency, lifespan]):
        raise ValueError("All inputs must be greater than zero.")
    clv = aov * frequency * lifespan
    return {
        "kpi":         "Customer Lifetime Value (CLV)",
        "result":      round(clv, 2),
        "unit":        "currency",
        "formula":     "AOV × purchase_frequency × customer_lifespan_years",
        "description": "Total revenue expected from one customer over the entire relationship.",
    }


def gross_profit_margin(revenue: float, cogs: float) -> dict:
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")
    margin = ((revenue - cogs) / revenue) * 100
    return {
        "kpi":         "Gross Profit Margin",
        "result":      round(margin, 2),
        "unit":        "%",
        "formula":     "((revenue - COGS) / revenue) × 100",
        "description": "How much of each dollar of revenue remains after paying for goods.",
    }


def net_profit_margin(net_profit: float, revenue: float) -> dict:
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")
    margin = (net_profit / revenue) * 100
    return {
        "kpi":         "Net Profit Margin",
        "result":      round(margin, 2),
        "unit":        "%",
        "formula":     "(net_profit / revenue) × 100",
        "description": "Revenue remaining after ALL expenses — the true bottom line.",
    }


def overall_equipment_effectiveness(
    availability: float, performance: float, quality: float
) -> dict:
    """
    OEE = Availability × Performance × Quality
    Each input is a percentage (0–100).
    """
    for name, val in [("Availability", availability), ("Performance", performance), ("Quality", quality)]:
        if not (0 <= val <= 100):
            raise ValueError(f"{name} must be between 0 and 100.")
    oee = (availability / 100) * (performance / 100) * (quality / 100) * 100
    health = (
        "World Class (≥ 85%)"    if oee >= 85 else
        "Good (65–84%)"          if oee >= 65 else
        "Needs Improvement (< 65%)"
    )
    return {
        "kpi":         "Overall Equipment Effectiveness (OEE)",
        "result":      round(oee, 2),
        "unit":        "%",
        "formula":     "(availability% × performance% × quality%) / 100²",
        "health":      health,
        "description": (
            "Measures how effectively a production line is being used. "
            "World class = 85%+. Below 65% signals major inefficiency."
        ),
    }


def production_yield(good_units: int, total_units: int) -> dict:
    if total_units <= 0:
        raise ValueError("Total units produced must be greater than zero.")
    if good_units > total_units:
        raise ValueError("Good units cannot exceed total units produced.")
    yield_rate = (good_units / total_units) * 100
    return {
        "kpi":         "Production Yield",
        "result":      round(yield_rate, 2),
        "unit":        "%",
        "formula":     "(good_units / total_units_produced) × 100",
        "description": (
            "Percentage of units produced that meet quality standards. "
            "Scrap and rework directly reduce this — higher is better."
        ),
    }


def inventory_turnover(cogs: float, average_inventory: float) -> dict:
    if average_inventory <= 0:
        raise ValueError("Average inventory value must be greater than zero.")
    turnover = cogs / average_inventory
    health = (
        "High — inventory moving fast"      if turnover >= 8 else
        "Moderate — acceptable range"       if turnover >= 4 else
        "Low — stock may be slow-moving"
    )
    return {
        "kpi":         "Inventory Turnover",
        "result":      round(turnover, 2),
        "unit":        "times per period",
        "formula":     "COGS / average_inventory_value",
        "health":      health,
        "description": (
            "How many times inventory is sold and replaced in a period. "
            "Low turnover means cash is tied up in slow-moving stock."
        ),
    }


def research_and_development_ratio(rd_spend: float, revenue: float) -> dict:
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")
    ratio = (rd_spend / revenue) * 100
    return {
        "kpi":         "R&D Ratio",
        "result":      round(ratio, 2),
        "unit":        "%",
        "formula":     "(R&D_spend / revenue) × 100",
        "description": (
            "Percentage of revenue reinvested into research and development. "
            "Pharma benchmark is typically 15–25%. Too low risks future pipeline."
        ),
    }


def mrr(total_subscribers: int, average_revenue_per_user: float) -> dict:
    if total_subscribers <= 0:
        raise ValueError("Total subscribers must be greater than zero.")
    if average_revenue_per_user <= 0:
        raise ValueError("Average revenue per user must be greater than zero.")
    result = total_subscribers * average_revenue_per_user
    return {
        "kpi":         "Monthly Recurring Revenue (MRR)",
        "result":      round(result, 2),
        "unit":        "currency",
        "formula":     "total_subscribers × average_revenue_per_user",
        "description": "Predictable revenue your business earns every month from subscriptions.",
    }


def clv_to_cac_ratio(clv: float, cac: float) -> dict:
    if cac <= 0:
        raise ValueError("CAC must be greater than zero.")
    ratio = clv / cac
    health = (
        "Excellent (≥ 5:1)"   if ratio >= 5 else
        "Good (≥ 3:1)"        if ratio >= 3 else
        "Warning — may not be profitable (< 3:1)"
    )
    return {
        "kpi":         "CLV : CAC Ratio",
        "result":      round(ratio, 2),
        "unit":        "ratio",
        "formula":     "CLV / CAC",
        "health":      health,
        "description": "Is acquisition profitable? A ratio of 3:1 or higher is healthy.",
    }