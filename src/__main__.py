import sys

from PySide6.QtWidgets import QApplication

from data.component.theme import PesterchumTheme
from ostools.dirtools import validate_data_dir
from util.common import LOGGER

'''

    UP NEXT:
    - complete profile save/load
    - complete settings save/load
    - create profile selection widget PROPERLY

    REQUIRES TESTING:
    - theme data
'''

def main():

    app = QApplication(sys.argv)
    status = None
    try:
        status = app.exec()
    except Exception as e:
        LOGGER.exception(f"Exception running Pesterchum: {e}")
    finally:
        if status is None:
            LOGGER.critical("CRITICAL ERROR! Failed to execute QApplication!!!")
        LOGGER.info(f"Exiting with status code {status}")

# main()

def test():
    validate_data_dir()
    themes = PesterchumTheme.get_available_themes(include_repo_themes=True)
    print("Themes:")
    print(themes)
    # raise NotImplementedError

test()