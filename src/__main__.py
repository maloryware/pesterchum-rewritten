import sys

from gui.home import PesterHome
from pesterchum import PesterchumApp
from util.common import LOGGER

class Main:

    status: int

    def __init__(self):
        super().__init__()
        self.app = PesterchumApp(sys.argv)
        self.home = PesterHome()

    def run(self) -> int:
        self.status = self.app.exec()
        return self.status


if __name__ == "__main__":
    pesterchum = Main()
    LOGGER.warning("constructed")
    try:
        status = pesterchum.run()
    except Exception as e:
        LOGGER.exception(f"Exception running Pesterchum: {e}")
