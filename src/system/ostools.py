# honoring the fabled ostools.py from the original project
import os, sys, ctypes

from system.directories import *


# dirs: (always @ .pesterchum_data)

## windows: C:/Users/%user%/AppData/Local/.pesterchum_data
## linux: ~/%user%/AppData/Local/.pesterchum_data
## macos: (?)

def is_osx() -> bool:
    return sys.platform == "darwin"

def is_win32() -> bool:
    return sys.platform == "win32"

def is_linux() -> bool:
    return sys.platform.startswith("linux")

def is_osx_bundle() -> bool:
    return is_osx() and (os.path.abspath(".").find(".app") != -1)

def is_root() -> bool:
    """Return True if running as root on Linux/Mac/Misc"""
    if hasattr(os, "getuid"):
        return not os.getuid()  # 0 if root
    return False


def is_admin() -> bool:
    """Return True if running as Admin on Windows."""
    try:
        if is_win32():
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except OSError as win_issue:
        print(win_issue)
    return False


def validate_data_dir() -> None:
    """Checks if data directory is present"""
    # Define paths
    data_dir = get_data_dir()
    profile = get_profile_dir()
    quirks = get_quirk_dir()
    pesterlogs = get_pesterlog_dir()
    logs = get_log_dir()
    backup = get_backup_dir()
    themes = get_theme_dir()
    # ~lisanne `datadir/themes` is for repository installed themes
    # Apparently everything checks this folder for themes already
    # So hopefully im not plugging into an existng system on accident

    config_file = os.path.join(data_dir, "pesterchum.json")
    manifest_file = os.path.join(data_dir, "manifest.json")

    dirs = [data_dir, profile, quirks, pesterlogs, themes, logs, backup]
    for d in dirs:
        if not os.path.isdir(d) or not os.path.exists(d):
            os.makedirs(d, exist_ok=True)

    # pesterchum.json
    for filepath in [config_file, manifest_file]:
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write("{}")
