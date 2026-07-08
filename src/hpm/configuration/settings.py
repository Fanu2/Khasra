"""
Haryana Partition Manager (HPM)

Application settings.
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    """
    Application configuration.
    """

    application_name: str = "Haryana Partition Manager"

    data_directory: str = str(
        Path.home() / ".hpm",
    )

    database_directory: str = str(
        Path.home() / ".hpm" / "database",
    )

    database_file: str = str(
        Path.home() / ".hpm" / "database" / "hpm.db",
    )

    backup_directory: str = str(
        Path.home() / ".hpm" / "backups",
    )

    export_directory: str = str(
        Path.home() / ".hpm" / "exports",
    )

    report_directory: str = str(
        Path.home() / ".hpm" / "reports",
    )

    log_directory: str = str(
        Path.home() / ".hpm" / "logs",
    )

    theme: str = "System"

    language: str = "English"

    def to_dict(self) -> dict:
        """
        Convert settings to dictionary.
        """

        return asdict(self)