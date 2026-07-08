"""
Haryana Partition Manager (HPM)

Launcher.
"""

from hpm.application.application import Application


def main() -> int:
    """
    Application entry point.
    """

    application = Application()

    return application.run()


if __name__ == "__main__":
    raise SystemExit(main())