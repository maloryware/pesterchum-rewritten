import json
import os
from string import Template
from typing import Any

from system.directories import get_theme_dir
from system.ostools import get_data_dir
from util.common import LOGGER


class Theme(dict):
    """
    Constitutes a Pesterchum Theme.

    Args:
        name (str): The theme's folder name.

    Themes are dictionaries stored in .json files, which are located:
        - In the program directory (local themes, usually default ones)
        - In the data directory (downloaded themes)

    Themes mostly inherit the default Pesterchum theme to avoid redefining
    things that needn't be manually redefined.

    To create a theme, create a copy of the Pesterchum theme folder and
    either edit its `style.json' on your text editor of chocie, or load up
    the project in Mocha's Pesterchum Theme Editor.

    The theme editor can be found at:
    https://mocchapi.itch.io/pesterchum-theme-editor-2000
    """

    inherited: Theme

    # yes, "call to __init__ of super class is missed"
    # i'm not sure how necessary it is, but original
    # seems to work well so i'm not touching it for now
    # ~maloryware

    # noinspection PyMissingConstructor
    def __init__(self, name: str = "pesterchum"):

        self._path = Theme._get_path(name)
        self.update(self._load_theme())

        if "inherits" in self:
            self.inherited = Theme(self["inherits"])

    # TODO: check responses on discord to see
    #   if this check is in the right place
    @staticmethod
    def get_available_themes(include_repo_themes = False):
        repo_themes: set[str] = set()
        local_themes: set[str] = set()
        themes: list[str] = []

        for _, dir_names, _ in os.walk(get_theme_dir()):
            # noinspection PyTypeChecker
            repo_themes = {_dir for _dir in dir_names}

        # ???
        if get_data_dir() is not None:
            for _, dir_names, _ in os.walk("themes"):
                local_themes = {_dir for _dir in dir_names}

        themes.extend(local_themes)
        themes.extend(repo_themes)
        themes.sort(key=str.casefold)

        return themes

    def _load_theme(self) -> Theme:
        try:
            with open(self._path + "style.json") as fp:
                return json.load(fp, object_hook=self._hook_theme_file)
        except OSError:
            return json.loads("{}")

    @staticmethod
    def _get_path(name: str) -> str:
        _path = None

        for p in [
            get_data_dir() + f"themes/{name}/", # downloaded themes
            f"themes/{name}/" # local themes
        ]:
            if os.path.exists(p):
                return p

        if name is "pesterchum":
            LOGGER.critical("could not locate default theme!!")
            raise FileNotFoundError
        return Theme._get_path("pesterchum")

    # TODO: worth revisiting to make a little DRYer
    # [original: lisanne]
    def _hook_theme_file(self, theme: Any) -> Any:
        # This converts strings containing $path into the proper paths
        # Honestly ive never even seen this Template stuff before. very funky!
        for key, value in theme.items():
            if isinstance(value, str):
                templ = Template(value)
                theme[key] = templ.safe_substitute(path=self._path)
            elif isinstance(value, list):
                # ~lisanne : for dealing with 'main/fonts' which is an array which contains filepaths with $
                # probably good to have for future additions
                for idx, item in enumerate(value):
                    item = value[idx]
                    if isinstance(item, str):
                        # not very DRY of me >:3c
                        templ = Template(item)
                        value[idx] = templ.safe_substitute(path=self._path)
        return theme
