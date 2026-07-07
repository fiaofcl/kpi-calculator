from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from typing import List, Optional

import data
import calculators
import utils

EXPORT_DIR = Path(__file__).resolve().parent / "exports"
CALCULATOR_KPI_ALIASES = {
    "churn_rate": "customer_churn_rate",
    "research_and_development_ratio": "r_d_ratio",
    "overall_equipment_effectiveness": "overall_equipment_effectiveness_oee",
}
# reverse lookup: kpi_key -> calculator_key
_KPI_TO_CALCULATOR_KEY = {v: k for k, v in CALCULATOR_KPI_ALIASES.items()}


def _calculator_key_for(kpi_key: str) -> Optional[str]:
    """Return the calculators.CALCULATORS key for a given KPI key, if any."""
    if kpi_key in calculators.CALCULATORS:
        return kpi_key
    return _KPI_TO_CALCULATOR_KEY.get(kpi_key)


class KPICli:
    def __init__(self):
        self.bookmarks: List[str] = []       # KPI keys, in-memory for this session
        self.recently_viewed: List[str] = []  # KPI keys, most recent first


    def run(self) -> None:
        utils.print_header(
            "BUSINESS KPI RECOMMENDATION TOOL",
            "Find the right KPIs for your industry & business process",
        )
        print(
            "\nWelcome! Pick an industry, then a business process, and we'll\n"
            "show you the relevant KPIs with full details.\n"
        )

        options = [
            "Find KPIs by Industry (guided walkthrough)",
            "Search KPIs by keyword",
            "Search KPIs by business process",
            "Browse all KPIs",
            "My Bookmarked KPIs (this session)",
            "Recently Viewed KPIs",
            "Compare two KPIs",
            "Filter KPIs (Higher/Lower/%/Currency/Time)",
            "Random KPI (learning mode)",
            "Quick KPI Calculators",
            "KPI Glossary",
            "Help",
        ]

        while True:
            utils.print_menu("MAIN MENU", options, exit_label="Exit")
            choice = utils.get_menu_choice(len(options))

            if choice == 0:
                if utils.confirm("Are you sure you want to exit?", default=True):
                    break
                continue
            elif choice == 1:
                self.guided_walkthrough()
            elif choice == 2:
                self.search_keyword()
            elif choice == 3:
                self.search_process()
            elif choice == 4:
                self.browse_all()
            elif choice == 5:
                self.show_bookmarks()
            elif choice == 6:
                self.show_recent()
            elif choice == 7:
                self.compare_kpis()
            elif choice == 8:
                self.filter_kpis()
            elif choice == 9:
                self.random_kpi()
            elif choice == 10:
                self.quick_calculators()
            elif choice == 11:
                self.show_glossary()
            elif choice == 12:
                self.show_help()

        utils.print_success("Thanks for using the Business KPI Recommendation Tool. Goodbye!")

    # =========================================================================
    # 1. GUIDED WALKTHROUGH: Industry -> Process -> KPI -> Detail
    # =========================================================================

    def guided_walkthrough(self) -> None:
        industry = self._select_industry()
        if industry is None:
            return

        process = self._select_process(industry)
        if process is None:
            return

        kpis = data.get_kpis_for_process(process)
        if not kpis:
            utils.print_info(f"No KPIs are populated yet for '{process}'. "
                              f"Add them to data.py to enable this process.")
            utils.pause()
            return

        self._select_and_show_kpi(kpis, title=f"KPIs for {industry} -> {process}")

    def _select_industry(self) -> Optional[str]:
        industries = data.get_industries()
        descriptions = [data.get_industry_description(i) for i in industries]
        utils.print_menu_with_descriptions(
            "STEP 1 — Select Your Industry", industries, descriptions, exit_label="Back to Main Menu"
        )
        choice = utils.get_menu_choice(len(industries))
        if choice == 0:
            return None
        return industries[choice - 1]

    def _select_process(self, industry: str) -> Optional[str]:
        processes = data.get_processes_for_industry(industry)
        if not processes:
            utils.print_info(f"No business processes mapped yet for '{industry}'.")
            utils.pause()
            return None
        utils.print_menu(f"STEP 2 — Business Processes in {industry}", processes, exit_label="Back")
        choice = utils.get_menu_choice(len(processes))
        if choice == 0:
            return None
        return processes[choice - 1]
    def _select_and_show_kpi(self, kpis: List[data.KPI], title: str = "KPIs") -> None:
        while True:
            labels = [f"{k.name}  ({k.process})" for k in kpis]
            descriptions = [k.meaning for k in kpis]
            utils.print_menu_with_descriptions(title, labels, descriptions, exit_label="Back")
            choice = utils.get_menu_choice(len(kpis))
            if choice == 0:
                return
            kpi = kpis[choice - 1]
            self._show_kpi_detail_menu(kpi)

    def _show_kpi_detail_menu(self, kpi: data.KPI) -> None:
        self._record_view(kpi.key)
        while True:
            utils.print_kpi_detail(kpi)
            bookmarked = kpi.key in self.bookmarks
            calc_key = _calculator_key_for(kpi.key)
            generic = None if calc_key else calculators.parse_formula(kpi.formula)

            options = []
            if calc_key or generic:
                options.append("Calculate This KPI (enter your own numbers)")
            options.append("Remove Bookmark" if bookmarked else "Add Bookmark")
            options.append("Export This KPI")

            utils.print_menu("KPI OPTIONS", options, exit_label="Back")
            choice = utils.get_menu_choice(len(options))
            if choice == 0:
                return

            selected = options[choice - 1]
            if selected.startswith("Calculate"):
                if calc_key:
                    self._run_calculator(calc_key)
                else:
                    self._run_generic_calculator(kpi, generic)
            elif selected in ("Remove Bookmark", "Add Bookmark"):
                self._toggle_bookmark(kpi.key)
            elif selected == "Export This KPI":
                self._export_kpi(kpi)

    def _run_generic_calculator(self, kpi: data.KPI, parsed) -> None:
        expr_template, labels = parsed
        utils.print_section(f"Enter values for {kpi.name}")
        values = [utils.get_float(label) for label in labels]
        try:
            result = calculators.evaluate_formula(expr_template, values)
        except Exception as e:
            utils.print_error(f"Could not calculate that: {e}")
            utils.pause()
            return

        utils.print_section(kpi.name)
        unit = kpi.unit
        rounded = round(result, 2)
        if "%" in unit:
            print(f"  Result  : {rounded}%")
        elif "ratio" in unit.lower():
            print(f"  Result  : {rounded}:1")
        else:
            print(f"  Result  : {rounded}  ({unit})")
        print(f"  Formula : {kpi.formula}")
        print(f"  Better  : {kpi.better}")
        utils.pause()

    def _run_calculator(self, calculator_key: str) -> None:
        spec = calculators.CALCULATORS[calculator_key]
        utils.print_section(f"Enter values for {spec['label']}")
        args = []
        for prompt, kind in spec["params"]:
            args.append(utils.get_float(prompt) if kind == "float" else utils.get_int(prompt))
        try:
            result = spec["fn"](*args)
            self._print_calc_result(result)
        except ValueError as e:
            utils.print_error(str(e))
        utils.pause()

    def _record_view(self, key: str) -> None:
        if key in self.recently_viewed:
            self.recently_viewed.remove(key)
        self.recently_viewed.insert(0, key)
        self.recently_viewed = self.recently_viewed[:15]

    def _toggle_bookmark(self, key: str) -> None:
        if key in self.bookmarks:
            self.bookmarks.remove(key)
            utils.print_success("Bookmark removed.")
        else:
            self.bookmarks.append(key)
            utils.print_success("Bookmarked!")

    def _export_kpi(self, kpi: data.KPI) -> None:
        formats = ["TXT", "JSON", "CSV"]
        utils.print_menu("Export Format", formats, exit_label="Cancel")
        choice = utils.get_menu_choice(len(formats))
        if choice == 0:
            return
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = "".join(c if c.isalnum() else "_" for c in kpi.name).strip("_")
        fmt = formats[choice - 1].lower()
        path = EXPORT_DIR / f"{safe_name}.{fmt}"

        if fmt == "txt":
            lines = [
                kpi.name, "=" * len(kpi.name), "",
                f"Meaning: {kpi.meaning}", "",
                f"Why it Matters: {kpi.why_it_matters}", "",
                f"Formula: {kpi.formula}", "",
                f"Example: {kpi.example}", "",
                f"Unit: {kpi.unit}", f"Better: {kpi.better}",
                f"Business Process: {kpi.process}",
                f"Industries: {', '.join(kpi.industries)}", "",
                "Improvement Tips:",
            ] + [f"  - {t}" for t in kpi.improvement_tips]
            path.write_text("\n".join(lines), encoding="utf-8")
        elif fmt == "json":
            path.write_text(json.dumps(kpi.__dict__, indent=2, ensure_ascii=False), encoding="utf-8")
        else:  # csv
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Field", "Value"])
                for field_name in ["name", "meaning", "why_it_matters", "formula", "example",
                                   "unit", "better", "process"]:
                    writer.writerow([field_name, getattr(kpi, field_name)])
                writer.writerow(["industries", ", ".join(kpi.industries)])
                writer.writerow(["improvement_tips", " | ".join(kpi.improvement_tips)])

        utils.print_success(f"Exported to {path}")
        utils.pause()

    # =========================================================================
    # 2-3. SEARCH
    # =========================================================================

    def search_keyword(self) -> None:
        keyword = utils.get_text("Enter a keyword to search KPIs (name, meaning, process)")
        results = data.search_by_keyword(keyword)
        if not results:
            utils.print_info("No KPIs matched that keyword.")
            utils.pause()
            return
        self._select_and_show_kpi(results, title=f"Search results for '{keyword}'")

    def search_process(self) -> None:
        processes = data.get_all_processes()
        utils.print_menu("Select a Business Process", processes, exit_label="Back")
        choice = utils.get_menu_choice(len(processes))
        if choice == 0:
            return
        process = processes[choice - 1]
        kpis = data.get_kpis_for_process(process)
        self._select_and_show_kpi(kpis, title=f"KPIs for {process}")

    # =========================================================================
    # 4. BROWSE ALL
    # =========================================================================

    def browse_all(self) -> None:
        kpis = sorted(data.get_all_kpis(), key=lambda k: k.name)
        utils.print_kpi_list(kpis, title=f"All KPIs ({len(kpis)})")
        self._select_and_show_kpi(kpis, title="All KPIs")

    # =========================================================================
    # 5-6. BOOKMARKS / RECENTLY VIEWED
    # =========================================================================

    def show_bookmarks(self) -> None:
        kpis = [data.get_kpi_by_key(k) for k in self.bookmarks]
        kpis = [k for k in kpis if k is not None]
        if not kpis:
            utils.print_info("You haven't bookmarked any KPIs this session yet.")
            utils.pause()
            return
        self._select_and_show_kpi(kpis, title="Bookmarked KPIs")

    def show_recent(self) -> None:
        kpis = [data.get_kpi_by_key(k) for k in self.recently_viewed]
        kpis = [k for k in kpis if k is not None]
        if not kpis:
            utils.print_info("No recently viewed KPIs yet.")
            utils.pause()
            return
        self._select_and_show_kpi(kpis, title="Recently Viewed KPIs")

    # =========================================================================
    # 7. COMPARE
    # =========================================================================

    def compare_kpis(self) -> None:
        all_kpis = sorted(data.get_all_kpis(), key=lambda k: k.name)
        utils.print_kpi_list(all_kpis, title="Available KPIs")
        names = [k.name for k in all_kpis]
        descs = [k.meaning for k in all_kpis]
        utils.print_menu_with_descriptions("Select FIRST KPI (by number above)", names, descs, exit_label="Cancel")
        c1 = utils.get_menu_choice(len(all_kpis))
        if c1 == 0:
            return
        utils.print_menu_with_descriptions("Select SECOND KPI", names, descs, exit_label="Cancel")
        c2 = utils.get_menu_choice(len(all_kpis))
        if c2 == 0:
            return
        utils.print_kpi_comparison(all_kpis[c1 - 1], all_kpis[c2 - 1])
        utils.pause()

    # =========================================================================
    # 8. FILTER
    # =========================================================================

    def filter_kpis(self) -> None:
        options = ["Higher is Better", "Lower is Better", "Percentage (%)", "Currency", "Time (Days/Hours/Minutes)"]
        utils.print_menu("Filter KPIs By", options, exit_label="Cancel")
        choice = utils.get_menu_choice(len(options))
        if choice == 0:
            return

        if choice == 1:
            results = data.filter_kpis(better="Higher")
        elif choice == 2:
            results = data.filter_kpis(better="Lower")
        elif choice == 3:
            results = data.filter_kpis(unit_contains="%")
        elif choice == 4:
            results = data.filter_kpis(unit_contains="currency")
        else:
            results = [k for k in data.get_all_kpis()
                       if any(t in k.unit.lower() for t in ["day", "hour", "minute", "month"])]

        if not results:
            utils.print_info("No KPIs matched that filter.")
            utils.pause()
            return
        self._select_and_show_kpi(results, title=f"Filtered: {options[choice - 1]}")

    # =========================================================================
    # 9. RANDOM / LEARNING MODE
    # =========================================================================

    def random_kpi(self) -> None:
        kpi = random.choice(data.get_all_kpis())
        utils.print_info("Here's a random KPI to learn about:")
        self._show_kpi_detail_menu(kpi)

    # =========================================================================
    # 10. CALCULATORS
    # =========================================================================

    def quick_calculators(self) -> None:
        keys = list(calculators.CALCULATORS.keys())
        labels = [calculators.CALCULATORS[k]["label"] for k in keys]
        utils.print_menu("Quick KPI Calculators", labels, exit_label="Back")
        choice = utils.get_menu_choice(len(keys))
        if choice == 0:
            return

        key = keys[choice - 1]
        spec = calculators.CALCULATORS[key]
        utils.print_section(f"Enter values for {spec['label']}")

        args = []
        for prompt, kind in spec["params"]:
            args.append(utils.get_float(prompt) if kind == "float" else utils.get_int(prompt))

        try:
            result = spec["fn"](*args)
            self._print_calc_result(result)
        except ValueError as e:
            utils.print_error(str(e))
        utils.pause()

    def _print_calc_result(self, result: dict) -> None:
        unit = result.get("unit", "")
        value = result["result"]
        utils.print_section(result["kpi"])
        if unit == "%":
            print(f"  Result  : {value}%")
        elif unit == "ratio":
            print(f"  Result  : {value}:1")
        else:
            print(f"  Result  : {value} {unit}")
        if "health" in result:
            print(f"  Health  : {result['health']}")
        print(f"  Formula : {result['formula']}")
        print(f"  Meaning : {result['description']}")

    # =========================================================================
    # 11. GLOSSARY
    # =========================================================================

    def show_glossary(self) -> None:
        glossary = data.get_glossary()
        utils.print_section("KPI Glossary")
        for term, definition in sorted(glossary.items()):
            print(f"  {term:<8} — {definition}")
        utils.pause()

    # =========================================================================
    # 12. HELP
    # =========================================================================

    def show_help(self) -> None:
        utils.print_section("Help")
        print(
            "  • 'Find KPIs by Industry' walks you through Industry -> Process -> KPI.\n"
            "  • Use Search to jump straight to a KPI by keyword or process.\n"
            "  • Bookmark KPIs you want to revisit (kept for this session only).\n"
            "  • Export any KPI's full details to TXT, JSON, or CSV (see exports/).\n"
            "  • Compare puts two KPIs side-by-side.\n"
            "  • Quick KPI Calculators compute a live result from your own numbers.\n"
            "  • Adding new industries/processes/KPIs only requires editing data.py.\n"
        )
        utils.pause()



