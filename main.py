import calculators
from utils import (
    print_header,
    display_menu,
    print_result,
    print_error,
    about,
    pause,
    get_float,
    get_int,
)


def calc_revenue_growth():
    print("\n  Revenue Growth")
    print("  How much did revenue grow vs the previous period?")
    print("-" * 45)
    current  = get_float("Current period revenue")
    previous = get_float("Previous period revenue")
    try:
        print_result(calculators.revenue_growth(current, previous))
    except ValueError as e:
        print_error(str(e))


def calc_cac():
    print("\n  Customer Acquisition Cost (CAC)")
    print("  How much does it cost to acquire one new customer?")
    print("-" * 45)
    marketing = get_float("Total marketing spend")
    sales     = get_float("Total sales team spend")
    customers = get_int("Number of new customers acquired")
    try:
        print_result(calculators.customer_acquisition_cost(marketing, sales, customers))
    except ValueError as e:
        print_error(str(e))


def calc_churn():
    print("\n  Churn Rate")
    print("  What percentage of customers did you lose?")
    print("-" * 45)
    lost     = get_int("Customers lost in the period")
    at_start = get_int("Customers at the start of the period")
    try:
        print_result(calculators.churn_rate(lost, at_start))
    except ValueError as e:
        print_error(str(e))


def calc_conversion():
    print("\n  Conversion Rate")
    print("  What % of visitors became customers?")
    print("-" * 45)
    conversions = get_int("Number of conversions (purchases / sign-ups)")
    visitors    = get_int("Total visitors or leads")
    try:
        print_result(calculators.conversion_rate(conversions, visitors))
    except ValueError as e:
        print_error(str(e))


def calc_aov():
    print("\n  Average Order Value (AOV)")
    print("  How much does each order earn on average?")
    print("-" * 45)
    revenue = get_float("Total revenue in the period")
    orders  = get_int("Total number of orders")
    try:
        print_result(calculators.average_order_value(revenue, orders))
    except ValueError as e:
        print_error(str(e))


def calc_clv():
    print("\n  Customer Lifetime Value (CLV)")
    print("  How much is one customer worth over their lifetime?")
    print("-" * 45)
    aov       = get_float("Average order value (AOV)")
    frequency = get_float("Average purchases per year per customer")
    lifespan  = get_float("Average customer lifespan (years)")
    try:
        print_result(calculators.customer_lifetime_value(aov, frequency, lifespan))
    except ValueError as e:
        print_error(str(e))


def calc_gross_margin():
    print("\n  Gross Profit Margin")
    print("  How much is left after cost of goods?")
    print("-" * 45)
    revenue = get_float("Total revenue")
    cogs    = get_float("Cost of goods sold (COGS)")
    try:
        print_result(calculators.gross_profit_margin(revenue, cogs))
    except ValueError as e:
        print_error(str(e))


def calc_net_margin():
    print("\n  Net Profit Margin")
    print("  How much is left after ALL expenses?")
    print("-" * 45)
    net_profit = get_float("Net profit (can be negative)", allow_negative=True)
    revenue    = get_float("Total revenue")
    try:
        print_result(calculators.net_profit_margin(net_profit, revenue))
    except ValueError as e:
        print_error(str(e))


def calc_clv_cac():
    print("\n  CLV : CAC Ratio")
    print("  Is acquiring customers actually worth it?")
    print("-" * 45)
    clv = get_float("Customer Lifetime Value (CLV)")
    cac = get_float("Customer Acquisition Cost (CAC)")
    try:
        print_result(calculators.clv_to_cac_ratio(clv, cac))
    except ValueError as e:
        print_error(str(e))


MENU = {
    "1":  calc_revenue_growth,
    "2":  calc_cac,
    "3":  calc_churn,
    "4":  calc_conversion,
    "5":  calc_aov,
    "6":  calc_clv,
    "7":  calc_gross_margin,
    "8":  calc_net_margin,
    "9":  calc_clv_cac,
    "10": about,
    "11": None,  # Exit
}


def main():
    while True:
        print_header()
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "11":
            print("\nGoodbye!")
            break

        action = MENU.get(choice)
        if action is None:
            print_error("Invalid choice. Please select 1–11.")
        else:
            action()

        pause()


if __name__ == "__main__":
    main()