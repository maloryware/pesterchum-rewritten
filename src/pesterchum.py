# flake8: noqa

import sys
from logging import Logger

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication

from gui.tray import PesterTray


# from data.component import Profile
# from data.config import Config

# TODO: find a good way to hold global data
#       for now, we're making PesterchumApp cascade down...
#       ...which genuinely seems like a terrible idea.

# TODO: important things to take note of
#   - validation of EVERYTHING directory-related should take place on startup
#   - data should be centralized and passed down to normalize access logic

class Pesterchum(QObject):

    # tray: PesterTray

    def __init__(self, /) -> None:
        super().__init__()

        self.app = QApplication()
        self.app.setApplicationName("Pesterchum")

        raise NotImplementedError