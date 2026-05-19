# flake8: noqa

import sys
from logging import Logger

from PySide6.QtWidgets import QApplication
# from data.profile import Profile
# from data.config import Config
from gui.home import PesterHome
from util.common import LOGGER

# TODO: find a good way to hold global data
#       for now, we're making PesterchumApp cascade down...
#       ...which genuinely seems like a terrible idea.

class PesterchumApp(QApplication):

    # profile: Profile
    # settings: Config
    logger: Logger

    def __init__(self, argv) -> None:
        super().__init__(argv)
        # self.profile = Profile(self)
        # self.settings = Config()


class Main:

    status: int

    def __init__(self):
        super().__init__()
        self.app = PesterchumApp(sys.argv)
        self.home = PesterHome()

    def run(self) -> int:
        status = self.app.exec()
        return status


if __name__ == "__main__":
    pesterchum = Main()
    LOGGER.warning("constructed")
    try:
        status = pesterchum.run()
    except Exception as e:
        LOGGER.exception(f"Exception running Pesterchum: {e}")
