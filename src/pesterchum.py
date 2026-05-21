# flake8: noqa

import sys
from logging import Logger

from PySide6.QtWidgets import QApplication
# from data.profile import Profile
# from data.config import Config

# TODO: find a good way to hold global data
#       for now, we're making PesterchumApp cascade down...
#       ...which genuinely seems like a terrible idea.

class PesterchumApp(QApplication):

    # profile: Profile
    # settings: Config

    def __init__(self, argv) -> None:
        super().__init__(argv)
        # self.profile = Profile(self)
        # self.settings = Config()
