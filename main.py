#!/usr/bin/env python3
"""
main.py — entry point. Run with:  python main.py

Pure terminal app. Files needed (all in the same folder):
  main.py, cli.py, data.py, calculators.py, utils.py
"""
import sys
from cli import KPICli


def main() -> None:
    try:
        KPICli().run()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()