"""
Haryana Partition Manager (HPM)

Settings service.
"""

from __future__ import annotations

import json

from hpm.configuration.settings import Settings


class SettingsService:
    """
    Manages application settings.

    Responsible for loading, saving and maintaining the
    application's configuration and directory structure.
    """

    SETTINGS_FILE = "settings.json"

    def __init__(
        self,
    ) -> None:
        """
        Initialize the settings service.
        """

        self._settings = Settings()

        self._settings_file = (
            self._settings.data_directory
            / self.SETTINGS_FILE
        )

        self._ensure_directories()

        self.load()

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def settings(
        self,
    ) -> Settings:
        """
        Return the current application settings.
        """

        return self._settings

    # ------------------------------------------------------------------
    # Directory Management
    # ------------------------------------------------------------------

    def _ensure_directories(
        self,
    ) -> None:
        """
        Ensure the required application directories exist.
        """

        directories = (
            self._settings.data_directory,
            self._settings.database_directory,
            self._settings.backup_directory,
            self._settings.export_directory,
            self._settings.report_directory,
            self._settings.log_directory,
        )

        for directory in directories:

            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

    # ------------------------------------------------------------------
    # Settings Management
    # ------------------------------------------------------------------

    def load(
        self,
    ) -> None:
        """
        Load settings from disk.

        If the settings file is missing or invalid,
        default settings are restored automatically.
        """

        if not self._settings_file.exists():

            self.save()

            return

        try:

            data = json.loads(
                self._settings_file.read_text(
                    encoding="utf-8",
                )
            )

            self._settings = Settings.from_dict(
                data,
            )

        except (
            OSError,
            json.JSONDecodeError,
            TypeError,
            ValueError,
            KeyError,
        ):

            self.reset()

    def save(
        self,
    ) -> None:
        """
        Save settings to disk.
        """

        self._ensure_directories()

        self._settings_file.write_text(
            json.dumps(
                self._settings.to_dict(),
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def reload(
        self,
    ) -> None:
        """
        Reload settings from disk.
        """

        self.load()

    def reset(
        self,
    ) -> None:
        """
        Restore default application settings.
        """

        self._settings = Settings()

        self._ensure_directories()

        self.save()