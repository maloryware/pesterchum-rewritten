# flake8: noqa

import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from gui.widget.PesterHome import PesterHome 
from util.common import LOGGER


class PesterchumApp(QApplication):

    def __init__(self, argv) -> None:
        super().__init__(argv)


class Main:

    def __init__(self):
        super().__init__()
        self.app: PesterchumApp = PesterchumApp(sys.argv)
        self.window = PesterHome()

    def run(self) -> None:
        self.window.show()
        self.app.exec()


if __name__ == "__main__":
    pesterchum = Main()
    LOGGER.warning("constructed")
    try:
        pesterchum.run()
    except Exception as e:
        LOGGER.exception(f"Exception running Pesterchum: {e}")
