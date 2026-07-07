# KPI Calculator

**A Python terminal app for exploring, comparing, and calculating Business KPIs across multiple industries.**

Instead of hunting through spreadsheets and blog posts to remember what a KPI means or how to calculate it, KPI Calculator puts an interactive reference and calculator library right in your terminal — meaning, formula, example, unit, whether higher or lower is better, and improvement tips, all in one place.

---

## ✨ Features

- 🖥️ Interactive command-line interface
- 🏭 Browse KPIs by **industry**
- ⚙️ Browse KPIs by **business process**
- 📚 View the complete KPI catalog
- 🔍 Search KPIs by keyword
- 📄 Detailed KPI views including:
  - Meaning & importance
  - Formula & worked example
  - Unit of measurement
  - Whether higher or lower is better
  - Applicable industries & business process
  - Improvement tips
- 🧮 Built-in calculators to compute KPI values from your own numbers
- ⚖️ Side-by-side comparison of two KPIs
- 🔖 Session bookmarks for quick access
- 🕘 Recently viewed KPI history
- 🎲 Random KPI exploration mode
- 🎨 Clean terminal UI via the `rich` library, with automatic fallback to plain text if it isn't installed

---

## Technologies Used

- Python 3
- [Rich](https://github.com/Textualize/rich) *(optional, for enhanced terminal output)*
- `dataclasses`
- Standard Python libraries only — no heavy dependencies

---

## Installation

```bash
git clone https://github.com/fiaofcl/kpi-calculator.git
cd kpi-calculator
```

For the enhanced terminal interface, install Rich:

```bash
pip install rich
```

## Usage

```bash
python main.py
```

This launches an interactive menu where you can browse by industry or process, search by keyword, calculate values, compare KPIs, and bookmark favorites for the session.

---

## Project Structure

```
kpi-calculator/
│
├── main.py          # Application entry point
├── cli.py           # Menu system & navigation logic
├── data.py          # KPI dataset & retrieval
├── calculators.py   # KPI formulas & calculation logic
├── utils.py         # Terminal display helpers
└── README.md
```

| File | Responsibility |
|---|---|
| `main.py` | Launches the CLI |
| `cli.py` | Menu system, user interaction, navigation |
| `data.py` | Stores and retrieves the KPI dataset |
| `calculators.py` | Math/formulas behind each KPI |
| `utils.py` | Formatting, rendering, and input handling helpers |

---

## Application Workflow

1. Launch the application
2. Choose how to explore KPIs (by industry, by process, full catalog, or search)
3. View detailed KPI information
4. Calculate a KPI value using the built-in calculator
5. Compare two KPIs side-by-side
6. Bookmark KPIs for quick access during the session
7. Keep exploring via the interactive menu

---

## What You Can Learn

This project touches both business analytics and software engineering:

- Business performance measurement & KPIs
- Financial and operational metrics
- Modular Python application design
- Terminal-based UI development
- Data organization & input validation
- Command-line application development

---

## Future Enhancements

- [ ] Persistent bookmark storage
- [ ] Exporting KPI reports
- [ ] Additional KPI calculators
- [ ] More industry-specific KPI libraries
- [ ] Interactive charts and graphs
- [ ] Historical KPI tracking
- [ ] Database integration
- [ ] GUI version (Streamlit or Tkinter)

---

## About

KPI Calculator was built to make business performance metrics easier to understand and apply. It pairs a structured KPI database with an interactive CLI and calculation utilities, giving students, business professionals, and analytics enthusiasts a practical hands-on reference tool.

The codebase follows a modular architecture — separating interface, business logic, calculations, and data into distinct components — for better readability, maintainability, and scalability.

## License

This project is intended for educational and learning purposes. It may be used, modified, and extended for academic, personal, and non-commercial use.