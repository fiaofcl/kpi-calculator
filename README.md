# Business KPI Recommendation Tool

The Business KPI Recommendation Tool is a Python-based terminal application designed to help users explore, understand, and calculate Key Performance Indicators (KPIs) used across various industries and business processes. The project provides an interactive command-line interface that enables users to browse KPIs, learn their significance, understand their formulas, and calculate business metrics using real-world values.

The primary objective of this project is to simplify the process of learning and applying business KPIs while demonstrating modular software development in Python. Instead of searching through multiple resources for KPI definitions and formulas, users can access everything from a single terminal application.

---

## Features

* Interactive command-line interface
* Browse KPIs by industry
* Browse KPIs by business process
* View a complete KPI catalog
* Search KPIs by keyword
* View detailed KPI information including:

  * Meaning
  * Importance
  * Formula
  * Example
  * Unit of measurement
  * Performance indicator (Higher/Lower is better)
  * Applicable industries
  * Business process
  * Improvement tips
* Calculate KPI values using built-in calculators
* Compare two KPIs side-by-side
* Bookmark KPIs during the current session
* View recently accessed KPIs
* Random KPI exploration mode
* Clean terminal interface with optional Rich library support
* Automatic fallback to standard terminal output if Rich is not installed

---

## Technologies Used

* Python 3
* Rich (Optional)
* Dataclasses
* Standard Python Libraries

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Business-KPI-Recommendation-Tool.git
```

Navigate to the project directory:

```bash
cd Business-KPI-Recommendation-Tool
```

If you want the enhanced terminal interface, install Rich:

```bash
pip install rich
```

---

## Running the Application

Start the application by running:

```bash
python main.py
```

The program launches directly in the terminal and presents an interactive menu where users can navigate through industries, business processes, KPI categories, and calculators.

---

## Project Structure

```text
Business-KPI-Recommendation-Tool/
│
├── main.py
├── cli.py
├── data.py
├── calculators.py
├── utils.py
└── README.md
```

### File Description

**main.py**

Application entry point responsible for launching the command-line interface.

**cli.py**

Contains the application's menu system, user interaction logic, and navigation between different sections.

**data.py**

Stores the KPI dataset and manages retrieval of KPI information based on user selections.

**calculators.py**

Contains the mathematical formulas and calculation logic used to compute different business KPIs.

**utils.py**

Provides helper functions for terminal presentation, menu rendering, user input handling, KPI formatting, and display utilities.

---

## Application Workflow

1. Launch the application.
2. Choose how you want to explore KPIs.
3. Browse KPIs by industry or business process.
4. Search for specific KPIs using keywords.
5. View detailed KPI information.
6. Calculate KPI values using the built-in calculators.
7. Compare two KPIs to understand their differences.
8. Bookmark important KPIs for quick access during the session.
9. Continue exploring additional KPIs through the interactive menu system.

---

## What You Can Learn

This project demonstrates concepts from both business analytics and software development, including:

* Business Performance Measurement
* Key Performance Indicators (KPIs)
* Financial Metrics
* Operational Metrics
* Python Programming
* Modular Application Design
* Terminal-Based User Interfaces
* Data Organization
* User Input Validation
* Command-Line Application Development

---

## Future Enhancements

Potential improvements for future versions include:

* Persistent bookmark storage
* Exporting KPI reports
* Additional KPI calculators
* More industry-specific KPI libraries
* Interactive charts and graphs
* Historical KPI tracking
* Database integration
* Graphical user interface using Streamlit or Tkinter

---

## About

The Business KPI Recommendation Tool was developed as an educational Python project to make business performance metrics easier to understand and apply. By combining a structured KPI database with an interactive command-line interface and built-in calculation utilities, the application provides a practical learning environment for students, business professionals, and anyone interested in business analytics.

The project follows a modular architecture, separating the application's interface, business logic, calculations, and data into individual components. This design improves readability, maintainability, and scalability while demonstrating good software engineering practices.

---

## License

This project is intended for educational and learning purposes. It may be used, modified, and extended for academic, personal, and non-commercial use.
