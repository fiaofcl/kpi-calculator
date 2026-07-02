````markdown
# Business KPI Calculator (CLI)

A terminal-based Key Performance Indicator (KPI) calculator designed for businesses across multiple industries.

Select your industry, discover the most relevant KPIs, calculate metrics instantly, and receive:

- Formula explanations
- Plain-English descriptions
- Industry benchmarks
- Health ratings and insights

Perfect for business students, entrepreneurs, analysts, and anyone learning business metrics.

---

## Features

- Supports 9 business industries
- Calculates 14+ essential KPIs
- Industry-specific recommendations and benchmarks
- Beginner-friendly terminal interface
- No external dependencies
- Modular and easy to extend

---

## Getting Started

### Requirements

- Python 3.10 or later

### Installation

```bash
git clone https://github.com/yourusername/kpi-cli.git
cd kpi-cli
```

### Run the Application

```bash
python3 main.py
```

No additional packages or setup are required.

---

## Project Structure

```text
kpi-cli/
├── main.py          # CLI entry point and menu navigation
├── calculators.py   # Pure KPI calculation functions
├── industries.py    # Industry definitions and benchmarks
├── utils.py         # Input handlers and formatting utilities
└── README.md
```

---

## Application Flow

### Step 1 – Select an Industry

Choose the business type that best matches your organization.

```text
=============================================
  Step 1 — Select your Industry
=============================================
  1. E-commerce
  2. SaaS / Software
  3. Retail (Brick & Mortar)
  4. Agency / Consulting
  5. Restaurant / Food & Beverage
  6. Healthcare / Clinic
  7. Real Estate
  8. Manufacturing
  9. Pharma / Life Sciences
  0. Exit
```

---

### Step 2 – Learn Industry Benchmarks

Each industry includes:

- Business overview
- Recommended KPIs
- Performance benchmarks
- Practical tips and insights

Example:

```text
=============================================
  Industry : SaaS / Software
  About    : Subscription software products
=============================================

• Churn is the #1 SaaS killer.
• CLV:CAC should be ≥ 3:1.
• Payback period ideally under 12 months.
```

---

### Step 3 – Calculate KPIs

Select one or more KPIs and provide the required inputs.

Example:

```text
=============================================
  Step 2 — Suggested KPIs for your Industry
=============================================

1. Churn Rate
2. Customer Lifetime Value (CLV)
3. Customer Acquisition Cost (CAC)
4. CLV : CAC Ratio
5. Revenue Growth
6. Net Profit Margin
7. Monthly Recurring Revenue (MRR)
```

The application then displays:

- Calculated value
- Formula used
- Interpretation
- Benchmark comparison

---

## Supported Industries

| Industry | Description |
|----------|-------------|
| E-commerce | Online retail and direct-to-consumer businesses |
| SaaS / Software | Subscription-based software products |
| Retail (Brick & Mortar) | Physical stores and supermarkets |
| Agency / Consulting | Marketing, legal, design and consulting firms |
| Restaurant / Food & Beverage | Restaurants, cafes and catering businesses |
| Healthcare / Clinic | Medical, dental and wellness practices |
| Real Estate | Property sales and management |
| Manufacturing | Factories and industrial production |
| Pharma / Life Sciences | Pharmaceutical and biotechnology companies |

---

## Supported KPIs

| KPI | Formula |
|-----|----------|
| Revenue Growth | ((Current − Previous) / Previous) × 100 |
| Customer Acquisition Cost (CAC) | (Marketing + Sales Spend) / New Customers |
| Churn Rate | (Lost Customers / Starting Customers) × 100 |
| Conversion Rate | (Conversions / Visitors) × 100 |
| Average Order Value (AOV) | Revenue / Orders |
| Customer Lifetime Value (CLV) | AOV × Purchase Frequency × Lifespan |
| Gross Profit Margin | ((Revenue − COGS) / Revenue) × 100 |
| Net Profit Margin | (Net Profit / Revenue) × 100 |
| CLV:CAC Ratio | CLV / CAC |
| Monthly Recurring Revenue (MRR) | Subscribers × Average Revenue Per User |
| Overall Equipment Effectiveness (OEE) | (Availability × Performance × Quality) / 100² |
| Production Yield | (Good Units / Total Units) × 100 |
| Inventory Turnover | COGS / Average Inventory |
| R&D Ratio | (R&D Spend / Revenue) × 100 |

---

## Example Output

```text
=============================================
 KPI: Customer Acquisition Cost (CAC)
=============================================

Formula:
CAC = Total Marketing & Sales Spend ÷ New Customers

Result:
₹1,250.00 per customer

Health Rating:
Excellent

Interpretation:
You spend ₹1,250 to acquire each new customer.
```

---

## Extending the Project

1. Add a new industry to `industries.py`.
2. Register KPI labels in `KPI_LABELS`.
3. Add the calculation function in `calculators.py`.
4. Register the input handler in `main.py`.

---

## Educational Value

This project helps users understand:

- Business analytics
- Financial metrics
- Industry benchmarking
- Data-driven decision making
- Python CLI development and modular project design

---

## Built With

- Python 3.10+
- Standard Library Only

No third-party dependencies are required.

---

## License

This project is open-source and available under the MIT License.

This project is intended for learning and educational purposes.

---

## Future Improvements

- Export results to CSV or PDF
- Save calculation history
- Interactive charts
- Multi-currency support
- Flask web version
- Dashboard with KPI trends and visualizations
````
