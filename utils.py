"""
Terminal presentation helpers.

Uses the `rich` library for colored panels/tables when available, and
falls back to clean plain-text output if `rich` isn't installed, so the
CLI always runs (pure terminal, no browser/GUI/frontend involved).
"""
from __future__ import annotations

from typing import Iterable, List, Optional, Sequence

from data import KPI

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
    console = Console()
except ImportError:  # pragma: no cover - exercised only without rich installed
    RICH_AVAILABLE = False
    console = None


# ---------------------------------------------------------------------------
# Generic output helpers
# ---------------------------------------------------------------------------

def clear_screen() -> None:
    print("\n" * 2)


def print_header(title: str = "BUSINESS KPI RECOMMENDATION TOOL", subtitle: str = "") -> None:
    if RICH_AVAILABLE:
        text = Text(title, style="bold white on blue", justify="center")
        console.print(Panel(text, subtitle=subtitle or None, box=box.DOUBLE))
    else:
        print("\n" + "=" * 60)
        print(title.center(60))
        if subtitle:
            print(subtitle.center(60))
        print("=" * 60)


def print_section(title: str) -> None:
    if RICH_AVAILABLE:
        console.print(f"\n[bold cyan]{title}[/bold cyan]")
        console.print("[cyan]" + "-" * len(title) + "[/cyan]")
    else:
        print(f"\n{title}")
        print("-" * len(title))


def print_success(message: str) -> None:
    if RICH_AVAILABLE:
        console.print(f"[bold green]✓ {message}[/bold green]")
    else:
        print(f"✓ {message}")


def print_error(message: str) -> None:
    if RICH_AVAILABLE:
        console.print(f"[bold red]✗ {message}[/bold red]")
    else:
        print(f"✗ {message}")


def print_info(message: str) -> None:
    if RICH_AVAILABLE:
        console.print(f"[dim]{message}[/dim]")
    else:
        print(message)


def pause(message: str = "Press Enter to continue...") -> None:
    input(f"\n{message}")


def confirm(prompt: str, default: bool = False) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    answer = input(f"{prompt} {suffix}: ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


# ---------------------------------------------------------------------------
# Numbered menus
# ---------------------------------------------------------------------------

def print_menu(title: str, options: Sequence[str], back_label: str = "Back", exit_label: Optional[str] = None) -> None:
    print_section(title)
    for i, opt in enumerate(options, start=1):
        line = f"  {i:>2}. {opt}"
        if RICH_AVAILABLE:
            console.print(line)
        else:
            print(line)
    if exit_label:
        line = f"   0. {exit_label}"
    else:
        line = f"   0. {back_label}"
    if RICH_AVAILABLE:
        console.print(f"[dim]{line}[/dim]")
    else:
        print(line)


def _truncate(text: str, max_len: int = 100) -> str:
    text = text.strip()
    return text if len(text) <= max_len else text[: max_len - 1].rstrip() + "…"


def print_menu_with_descriptions(
    title: str,
    options: Sequence[str],
    descriptions: Sequence[str],
    back_label: str = "Back",
    exit_label: Optional[str] = None,
) -> None:
    """Same as print_menu, but prints a short italic description under each option."""
    print_section(title)
    for i, (opt, desc) in enumerate(zip(options, descriptions), start=1):
        line = f"  {i:>2}. {opt}"
        if RICH_AVAILABLE:
            console.print(line)
            if desc:
                console.print(f"      [dim italic]{_truncate(desc)}[/dim italic]")
        else:
            print(line)
            if desc:
                print(f"      {_truncate(desc)}")
    if exit_label:
        line = f"   0. {exit_label}"
    else:
        line = f"   0. {back_label}"
    if RICH_AVAILABLE:
        console.print(f"[dim]{line}[/dim]")
    else:
        print(line)


def get_menu_choice(num_options: int, prompt: str = "Enter your choice") -> int:
    """Returns 0..num_options. Loops until valid input is given."""
    while True:
        raw = input(f"\n{prompt}: ").strip()
        if raw.isdigit():
            choice = int(raw)
            if 0 <= choice <= num_options:
                return choice
        print_error(f"Please enter a number between 0 and {num_options}.")


def get_multi_choice(num_options: int, prompt: str = "Enter numbers separated by commas") -> List[int]:
    """Returns a list of valid 1-based indices chosen, or [] for 'all'."""
    raw = input(f"\n{prompt} (or press Enter for ALL): ").strip()
    if not raw:
        return list(range(1, num_options + 1))
    chosen: List[int] = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit() and 1 <= int(part) <= num_options:
            chosen.append(int(part))
        else:
            print_error(f"'{part}' is not valid — skipped.")
    return chosen


def get_text(prompt: str, allow_empty: bool = False) -> str:
    while True:
        value = input(f"{prompt}: ").strip()
        if value or allow_empty:
            return value
        print_error("This field cannot be empty.")


def get_float(prompt: str, allow_negative: bool = False) -> float:
    while True:
        try:
            val = float(input(f"  {prompt}: ").strip())
            if not allow_negative and val < 0:
                print_error("Value cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print_error("Please enter a valid number.")


def get_int(prompt: str, allow_zero: bool = True) -> int:
    while True:
        try:
            val = int(input(f"  {prompt}: ").strip())
            if val < 0 or (val == 0 and not allow_zero):
                print_error("Please enter a positive whole number.")
                continue
            return val
        except ValueError:
            print_error("Please enter a valid whole number.")


# ---------------------------------------------------------------------------
# KPI-specific rendering
# ---------------------------------------------------------------------------

def print_kpi_list(kpis: Sequence[KPI], title: str = "KPIs") -> None:
    if not kpis:
        print_info("No KPIs found.")
        return

    if RICH_AVAILABLE:
        table = Table(title=title, box=box.SIMPLE_HEAVY, header_style="bold magenta")
        table.add_column("#", justify="right", style="dim")
        table.add_column("KPI Name", style="bold")
        table.add_column("Process", style="cyan")
        table.add_column("Unit")
        table.add_column("Better")
        for i, k in enumerate(kpis, start=1):
            table.add_row(str(i), k.name, k.process, k.unit, k.better)
        console.print(table)
    else:
        print_section(title)
        for i, k in enumerate(kpis, start=1):
            print(f"  {i:>2}. {k.name:<40} [{k.process}]  ({k.unit}, {k.better} is better)")


def print_kpi_detail(kpi: KPI) -> None:
    tips = "\n".join(f"  • {t}" for t in kpi.improvement_tips) or "  • N/A"
    industries = ", ".join(kpi.industries) if kpi.industries else "General"

    body = (
        f"Meaning:\n  {kpi.meaning}\n\n"
        f"Why it Matters:\n  {kpi.why_it_matters}\n\n"
        f"Formula:\n  {kpi.formula}\n\n"
        f"Example:\n  {kpi.example}\n\n"
        f"Unit:            {kpi.unit}\n"
        f"Better:          {kpi.better}\n"
        f"Business Process: {kpi.process}\n"
        f"Industries:      {industries}\n\n"
        f"Improvement Tips:\n{tips}"
    )

    if RICH_AVAILABLE:
        console.print(Panel(body, title=f"[bold]{kpi.name}[/bold]", box=box.ROUNDED, expand=False))
    else:
        print("\n" + "=" * 60)
        print(kpi.name)
        print("=" * 60)
        print(body)
        print("=" * 60)


def print_kpi_comparison(kpi_a: KPI, kpi_b: KPI) -> None:
    if RICH_AVAILABLE:
        table = Table(title=f"{kpi_a.name}  vs  {kpi_b.name}", box=box.SIMPLE_HEAVY, header_style="bold magenta")
        table.add_column("Attribute", style="bold cyan")
        table.add_column(kpi_a.name)
        table.add_column(kpi_b.name)
        rows = [
            ("Meaning", kpi_a.meaning, kpi_b.meaning),
            ("Formula", kpi_a.formula, kpi_b.formula),
            ("Unit", kpi_a.unit, kpi_b.unit),
            ("Better", kpi_a.better, kpi_b.better),
            ("Process", kpi_a.process, kpi_b.process),
            ("Industries", ", ".join(kpi_a.industries), ", ".join(kpi_b.industries)),
        ]
        for label, va, vb in rows:
            table.add_row(label, va, vb)
        console.print(table)
    else:
        print("\n" + "=" * 60)
        print(f"{kpi_a.name}  vs  {kpi_b.name}")
        print("=" * 60)
        for label, va, vb in [
            ("Meaning", kpi_a.meaning, kpi_b.meaning),
            ("Formula", kpi_a.formula, kpi_b.formula),
            ("Unit", kpi_a.unit, kpi_b.unit),
            ("Better", kpi_a.better, kpi_b.better),
            ("Process", kpi_a.process, kpi_b.process),
        ]:
            print(f"\n{label}:")
            print(f"  A) {va}")
            print(f"  B) {vb}")
        print("=" * 60)