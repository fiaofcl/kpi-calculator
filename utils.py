def print_header():
    print("\n" + "=" * 45)
    print("        BUSINESS KPI CALCULATOR")
    print("=" * 45)


def display_menu():
    print("\n 1. Revenue Growth")
    print(" 2. Customer Acquisition Cost (CAC)")
    print(" 3. Churn Rate")
    print(" 4. Conversion Rate")
    print(" 5. Average Order Value (AOV)")
    print(" 6. Customer Lifetime Value (CLV)")
    print(" 7. Gross Profit Margin")
    print(" 8. Net Profit Margin")
    print(" 9. CLV : CAC Ratio")
    print("10. About / What are KPIs?")
    print("11. Exit")


def print_result(result: dict):
    print()
    print("=" * 45)
    print(f"  {result['kpi']}")
    print("=" * 45)

    unit = result.get("unit", "")
    value = result["result"]

    if unit == "%":
        print(f"  Result  : {value}%")
    elif unit == "ratio":
        print(f"  Result  : {value}:1")
        if "health" in result:
            print(f"  Health  : {result['health']}")
    else:
        print(f"  Result  : {value}")

    print(f"  Formula : {result['formula']}")
    print(f"  What it means:")
    print(f"    {result['description']}")
    print("=" * 45)


def about():
    print()
    print("=" * 45)
    print("  About — What are KPIs?")
    print("=" * 45)
    print("""
KPIs (Key Performance Indicators) are measurable
values that show how effectively a business is
achieving its goals.

This tool calculates 9 core Business & Sales KPIs:

  1. Revenue Growth      — Are you making more money?
  2. CAC                 — What does a customer cost you?
  3. Churn Rate          — Are you losing customers?
  4. Conversion Rate     — Are visitors becoming buyers?
  5. AOV                 — How much does each order earn?
  6. CLV                 — How valuable is one customer?
  7. Gross Profit Margin — After goods cost, what's left?
  8. Net Profit Margin   — After ALL costs, what's left?
  9. CLV:CAC Ratio       — Is acquiring customers worth it?

Tip: A healthy business typically has:
  • Revenue growth  > 0%
  • Churn rate      < 5% per month
  • Conversion rate > 2–5%
  • CLV:CAC ratio   ≥ 3:1
""")
    print("=" * 45)


def get_float(prompt: str, allow_negative: bool = False) -> float:
    while True:
        try:
            val = float(input(f"  {prompt}: ").strip())
            if not allow_negative and val < 0:
                print("  ✗ Value cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("  ✗ Please enter a valid number.")


def get_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(f"  {prompt}: ").strip())
            if val < 0:
                print("  ✗ Value cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("  ✗ Please enter a whole number.")


def pause():
    input("\nPress Enter to continue...")


def print_error(msg: str):
    print(f"\n  ✗ Error: {msg}")