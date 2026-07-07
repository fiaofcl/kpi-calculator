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