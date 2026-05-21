import os

from PySide6.QtCore import QStandardPaths

from system.ostools import is_osx, is_linux, is_win32, is_osx_bundle

_DATA_DIR: str

def get_data_dir() -> str:
    # Temporary fix for non-ascii usernames
    # If username has non-ascii characters, just store userdata
    # in the Pesterchum install directory (like before)

    if _DATA_DIR is not None:
        # ~Lisanne
        # On some systems (windows known 2b affected, OSX unknown, at least 1 linux distro unaffected)
        # the QStandardPaths.writableLocation changes its return path after the QApplication initialises
        # This means that anytime its called during runtime after init will just return a lie. it will just give you a different path
        # (Because the Application now has a Name which in turn makes it return an application-name-specific writableLocation, which pchum isnt expecting anywhere)
        # so
        # here im caching the result at init & returning that
        # seemed like the safest way to do this without breaking half of this program
        return _DATA_DIR

    try:
        if is_osx() or is_win32():
            return os.path.join(
                QStandardPaths.writableLocation(
                    QStandardPaths.StandardLocation.AppLocalDataLocation
                ),
                ".pesterchum_data/",
            )
        if is_linux() or is_osx_bundle():
            return os.path.join(
                QStandardPaths.writableLocation(
                    QStandardPaths.StandardLocation.HomeLocation
                ),
                ".pesterchum_data/",
            )
        raise Exception("OS not recognized")
    except UnicodeDecodeError as e:
        print(e)
    return ""

_DATA_DIR = get_data_dir()

def get_theme_dir():
    return get_data_dir() + "themes/"

def get_profile_dir():
    return get_data_dir() + "profiles/"

def get_pesterlog_dir():
    return get_data_dir() + "pesterlogs/"

def get_log_dir():
    return get_data_dir() + "logs/"

def get_quirk_dir():
    return get_data_dir() + "quirks/"

def get_backup_dir():
    return get_data_dir() + "backups/"

