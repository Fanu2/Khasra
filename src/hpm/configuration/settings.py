"""
Haryana Partition Manager (HPM)

Application settings.
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


#
# Application Home
#

HPM_HOME = Path.home() / ".hpm"


@dataclass(slots=True)
class Settings:
    """
    Application configuration.

    This class represents the complete application configuration.
    It is the single source of truth for application metadata,
    filesystem locations and user preferences.
    """

    # ------------------------------------------------------------------
    # Application Metadata
    # ------------------------------------------------------------------

    application_name: str = "Haryana Partition Manager"
    application_version: str = "0.1.0"
    organization_name: str = "HPM Project"

    # ------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------

    data_directory: Path = HPM_HOME

    database_directory: Path = HPM_HOME / "database"

    backup_directory: Path = HPM_HOME / "backups"

    export_directory: Path = HPM_HOME / "exports"

    report_directory: Path = HPM_HOME / "reports"

    log_directory: Path = HPM_HOME / "logs"

    # ------------------------------------------------------------------
    # Files
    # ------------------------------------------------------------------

    database_file: Path = (
        HPM_HOME
        / "database"
        / "hpm.db"
    )

    # ------------------------------------------------------------------
    # User Preferences
    # ------------------------------------------------------------------

    theme: str = "System"

    language: str = "English"

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:
        """
        Convert settings to a JSON-serializable dictionary.
        """

        data = asdict(
            self,
        )

        for key, value in data.items():

            if isinstance(
                value,
                Path,
            ):
                data[key] = str(
                    value,
                )

        return data

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "Settings":
        """
        Create Settings from a dictionary.
        """

        path_fields = {
            "data_directory",
            "database_directory",
            "backup_directory",
            "export_directory",
            "report_directory",
            "log_directory",
            "database_file",
        }

        converted = data.copy()

        for field in path_fields:

            if field in converted:

                converted[field] = Path(
                    converted[field],
                )

        return cls(
            **converted,
        )