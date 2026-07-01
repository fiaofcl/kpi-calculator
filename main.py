import calculators
from industries import INDUSTRIES, KPI_LABELS
from utils import (
    print_header,
    print_result,
    print_error,
    pause,
    get_float,
    get_int,
)


# ── KPI input handlers ────────────────────────────────────────────────────────

def run_kpi(kpi_key: str):
    handlers = {
        "revenue_growth":            _calc_revenue_growth,
        "customer_acquisition_cost": _calc_cac,
        "churn_rate":                _calc_churn,
        "conversion_rate":           _calc_conversion,
        "average_order_value":       _calc_aov,
        "customer_lifetime_value":   _calc_clv,
        "gross_profit_margin":       _calc_gross_margin,
        "net_profit_margin":         _calc_net_margin,
        "clv_to_cac_ratio":          _calc_clv_cac,
        "mrr":                            _calc_mrr,
        "overall_equipment_effectiveness": _calc_oee,
        "production_yield":                _calc_production_yield,
        "inventory_turnover":              _calc_inventory_turnover,
        "research_and_development_ratio":  _calc_rd_ratio,
    }
    fn = handlers.get(kpi_key)
    if fn:
        fn()


def _calc_revenue_growth():
    print("\n  Enter values for Revenue Growth")
    print("-" * 45)
    current  = get_float("Current period revenue")
    previous = get_float("Previous period revenue")
    try:
        print_result(calculators.revenue_growth(current, previous))
    except ValueError as e:
        print_error(str(e))


def _calc_cac():
    print("\n  Enter values for Customer Acquisition Cost")
    print("-" * 45)
    marketing = get_float("Total marketing spend")
    sales     = get_float("Total sales team spend")
    customers = get_int("Number of new customers acquired")
    try:
        print_result(calculators.customer_acquisition_cost(marketing, sales, customers))
    except ValueError as e:
        print_error(str(e))


def _calc_churn():
    print("\n  Enter values for Churn Rate")
    print("-" * 45)
    lost     = get_int("Customers lost in the period")
    at_start = get_int("Customers at the start of the period")
    try:
        print_result(calculators.churn_rate(lost, at_start))
    except ValueError as e:
        print_error(str(e))


def _calc_conversion():
    print("\n  Enter values for Conversion Rate")
    print("-" * 45)
    conversions = get_int("Number of conversions (purchases / sign-ups)")
    visitors    = get_int("Total visitors or leads")
    try:
        print_result(calculators.conversion_rate(conversions, visitors))
    except ValueError as e:
        print_error(str(e))


def _calc_aov():
    print("\n  Enter values for Average Order Value")
    print("-" * 45)
    revenue = get_float("Total revenue in the period")
    orders  = get_int("Total number of orders")
    try:
        print_result(calculators.average_order_value(revenue, orders))
    except ValueError as e:
        print_error(str(e))


def _calc_clv():
    print("\n  Enter values for Customer Lifetime Value")
    print("-" * 45)
    aov       = get_float("Average order value (AOV)")
    frequency = get_float("Average purchases per year per customer")
    lifespan  = get_float("Average customer lifespan (years)")
    try:
        print_result(calculators.customer_lifetime_value(aov, frequency, lifespan))
    except ValueError as e:
        print_error(str(e))


def _calc_gross_margin():
    print("\n  Enter values for Gross Profit Margin")
    print("-" * 45)
    revenue = get_float("Total revenue")
    cogs    = get_float("Cost of goods sold (COGS)")
    try:
        print_result(calculators.gross_profit_margin(revenue, cogs))
    except ValueError as e:
        print_error(str(e))


def _calc_net_margin():
    print("\n  Enter values for Net Profit Margin")
    print("-" * 45)
    net_profit = get_float("Net profit (can be negative)", allow_negative=True)
    revenue    = get_float("Total revenue")
    try:
        print_result(calculators.net_profit_margin(net_profit, revenue))
    except ValueError as e:
        print_error(str(e))


def _calc_clv_cac():
    print("\n  Enter values for CLV : CAC Ratio")
    print("-" * 45)
    clv = get_float("Customer Lifetime Value (CLV)")
    cac = get_float("Customer Acquisition Cost (CAC)")
    try:
        print_result(calculators.clv_to_cac_ratio(clv, cac))
    except ValueError as e:
        print_error(str(e))


def _calc_oee():
    print("\n  Enter values for Overall Equipment Effectiveness (OEE)")
    print("  Each value is a percentage (0–100).")
    print("-" * 45)
    availability = get_float("Availability %  (planned time the machine was actually running)")
    performance  = get_float("Performance %   (actual speed vs ideal speed)")
    quality      = get_float("Quality %       (good units vs total units produced)")
    try:
        print_result(calculators.overall_equipment_effectiveness(availability, performance, quality))
    except ValueError as e:
        print_error(str(e))


def _calc_production_yield():
    print("\n  Enter values for Production Yield")
    print("-" * 45)
    good_units  = get_int("Good units produced (passed quality check)")
    total_units = get_int("Total units produced")
    try:
        print_result(calculators.production_yield(good_units, total_units))
    except ValueError as e:
        print_error(str(e))


def _calc_inventory_turnover():
    print("\n  Enter values for Inventory Turnover")
    print("-" * 45)
    cogs      = get_float("Cost of goods sold (COGS) for the period")
    avg_inv   = get_float("Average inventory value for the period")
    try:
        print_result(calculators.inventory_turnover(cogs, avg_inv))
    except ValueError as e:
        print_error(str(e))


def _calc_rd_ratio():
    print("\n  Enter values for R&D Ratio")
    print("-" * 45)
    rd_spend = get_float("Total R&D spend for the period")
    revenue  = get_float("Total revenue for the period")
    try:
        print_result(calculators.research_and_development_ratio(rd_spend, revenue))
    except ValueError as e:
        print_error(str(e))


def _calc_mrr():
    print("\n  Enter values for Monthly Recurring Revenue")
    print("-" * 45)
    subscribers = get_int("Total active subscribers")
    arpu        = get_float("Average revenue per user per month (ARPU)")
    try:
        print_result(calculators.mrr(subscribers, arpu))
    except ValueError as e:
        print_error(str(e))


# ── Industry selection ────────────────────────────────────────────────────────

def select_industry() -> dict | None:
    print("\n" + "=" * 45)
    print("  Step 1 — Select your Industry")
    print("=" * 45)

    for key, ind in INDUSTRIES.items():
        print(f"  {key}. {ind['name']}")
        print(f"     {ind['description']}")

    print("  0. Exit")
    print()

    choice = input("Enter number: ").strip()

    if choice == "0":
        return None

    industry = INDUSTRIES.get(choice)
    if not industry:
        print_error("Invalid choice.")
        return select_industry()

    return industry


def show_industry_info(industry: dict):
    print()
    print("=" * 45)
    print(f"  Industry : {industry['name']}")
    print(f"  About    : {industry['description']}")
    print("=" * 45)
    print()
    print("  Industry Benchmarks & Tips:")
    for tip in industry["tips"]:
        print(f"    • {tip}")


# ── KPI selection ─────────────────────────────────────────────────────────────

def select_kpis(industry: dict) -> list:
    kpi_keys = industry["kpis"]

    print()
    print("=" * 45)
    print("  Step 2 — Suggested KPIs for your Industry")
    print("=" * 45)
    print()
    print("  The following KPIs are most relevant for")
    print(f"  {industry['name']} businesses:\n")

    for i, key in enumerate(kpi_keys, start=1):
        label = KPI_LABELS.get(key, key)
        print(f"  {i:>2}. {label}")

    print()
    print("  Enter the numbers you want to calculate,")
    print("  separated by commas  (e.g. 1,3,5)")
    print("  or press Enter to calculate ALL of them.")
    print()

    raw = input("  Your choice: ").strip()

    if not raw:
        return kpi_keys  # all of them

    selected = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            idx = int(part) - 1
            if 0 <= idx < len(kpi_keys):
                selected.append(kpi_keys[idx])
            else:
                print_error(f"  '{part}' is out of range — skipped.")
        else:
            print_error(f"  '{part}' is not a valid number — skipped.")

    if not selected:
        print_error("No valid KPIs selected. Please try again.")
        return select_kpis(industry)

    return selected


# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    while True:
        print_header()
        print("  Welcome! Let's start by identifying")
        print("  your industry so we can suggest the")
        print("  most relevant KPIs for your business.")

        industry = select_industry()

        if industry is None:
            print("\nGoodbye!")
            break

        show_industry_info(industry)
        pause()

        chosen_kpis = select_kpis(industry)

        print()
        print("=" * 45)
        print(f"  Calculating {len(chosen_kpis)} KPI(s)...")
        print("=" * 45)

        for kpi_key in chosen_kpis:
            run_kpi(kpi_key)
            print()

        print("=" * 45)
        print("  All done! Want to calculate more KPIs?")
        print("=" * 45)

        again = input("\n  Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()