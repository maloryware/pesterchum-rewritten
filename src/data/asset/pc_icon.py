from typing import Tuple

from PySide6.QtGui import QIcon, QPixmap

from data.component.theme import PesterchumTheme
from util.assets import Assets
from util.common import LOGGER


class PesterchumIcon(QIcon):

    def __init__(self, dat: Tuple):
        _icon = dat[0]
        super().__init__(*dat)

        if isinstance(_icon, str):
            self.icon_pixmap = QPixmap(_icon)

    @staticmethod
    def of(name: str, theme: PesterchumTheme) -> PesterchumIcon:
        try:
            _path = theme["main/chums/moods"][name]["icon"]
        except KeyError as e:
            LOGGER.warning(f"ERROR: Failed to load icon for {name}.")
            _path = Assets.MISSING
        return PesterchumIcon(_path)

    def get_real_size(self):
        if self.icon_pixmap is not None:
            return self.icon_pixmap.size()
        if len(self.availableSizes()) > 0:
            return self.availableSizes()[0]
        return None