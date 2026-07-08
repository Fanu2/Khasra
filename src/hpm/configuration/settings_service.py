"""
Haryana Partition Manager (HPM)

Settings service.
"""

from __future__ import annotations

import json
from pathlib import Path

from hpm.configuration.settings import Settings


class SettingsService:
    """
    Manages application settings.
    """

    def __init__(self) -> None:

        self._settings = Settings()

        self._settings_file = (
            Path(self._settings.data_directory)
            / "settings.json"
        )

        self._ensure_directories()

        self.load()

    @property
    def settings(
        self,
    ) -> Settings:
        """
        Return current settings.
        """

        return self._settings

    def _ensure_directories(
        self,
    ) -> None:
        """
        Create application directories.
        """

        directories = [
            self._settings.data_directory,
            self._settings.database_directory,
            self._settings.backup_directory,
            self._settings.export_directory,
            self._settings.report_directory,
            self._settings.log_directory,
        ]

        for directory in directories:
            Path(directory).mkdir(
                parents=True,
                exist_ok=True,
            )

    def load(
        self,
    ) -> None:
        """
        Load settings from disk.
        """

        if not self._settings_file.exists():

            self.save()

            return

        data = json.loads(
            self._settings_file.read_text(
                encoding="utf-8",
            )
        )

        self._settings = Settings(
            **data,
        )

    def save(
        self,
    ) -> None:
        """
        Save settings.
        """

        self._settings_file.write_text(
            json.dumps(
                self._settings.to_dict(),
                indent=4,
            ),
            encoding="utf-8",
        )