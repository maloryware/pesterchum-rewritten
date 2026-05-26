import json
import os
from string import Template
from typing import Any

from data.structure.pesterchum_data import PesterchumData
from ostools.dirtools import get_theme_dir, get_data_dir
from util.common import LOGGER


class PesterchumTheme(dict, PesterchumData):
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

    inherited: PesterchumTheme

    # yes, "call to __init__ of super class is missed"
    # i'm not sure how necessary it is, but original
    # seems to work well so i'm not touching it for now
    # ~maloryware

    # noinspection PyMissingConstructor
    def __init__(self, name: str = "pesterchum"):

        self._path = PesterchumTheme._get_path(name)
        self.update(self.load())

        if "inherits" in self:
            self.inherited = PesterchumTheme(self["inherits"])

    # noinspection PyTypeChecker
    @staticmethod
    def get_available_themes(include_repo_themes=True):
        themes: set[str] = set()

        # this uses set comprehension to gather all the themes and store them to one set
        # the 'break' instruction is there to stop os.walk() from recursively searching dirs,
        # as we only care for what's at the root directory
        # ~maloryware

        for dirpath, dir_names, z in os.walk(get_theme_dir()):
            themes.update({theme for theme in dir_names if include_repo_themes})
            break

        for dirpath, dir_names, _ in os.walk("../assets/themes"):
            themes.update({theme for theme in dir_names})
            break

        output = list(themes)
        output.sort(key=str.casefold)
        return output

    # ~ PesterchumData::load ~
    def load(self) -> PesterchumTheme:
        try:
            with open(self._path + "style.json") as fp:
                return json.load(fp, object_hook=self._hook_theme_file)
        except OSError:
            return json.loads("{}")

    # ~ PesterchumData::save ~
    def save(self) -> None:
        raise IOError("Pesterchum themes cannot be updated from the client")

    @staticmethod
    def _get_path(name: str) -> str:
        _path = None

        for p in [
            get_data_dir() + f"themes/{name}",  # downloaded themes
            f"themes/{name}"  # local themes
        ]:
            if os.path.exists(p):
                return p

        LOGGER.info(f"Could not find {name} - loading default theme...")
        if name == "pesterchum":
            LOGGER.critical("could not locate default theme!!")
            raise FileNotFoundError
        return PesterchumTheme._get_path("pesterchum")

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

    # ~ PesterchumData::get_dir ~
    def get_dir(self) -> str:
        return PesterchumTheme._get_path(self._path)
