# honoring the fabled ostools.py from the original project
import sys, ctypes
from enum import Enum

import os

# dirs: (always @ .pesterchum_data)

## windows: C:/Users/%user%/AppData/Local/.pesterchum_data
## linux: ~/%user%/AppData/Local/.pesterchum_data
## macos: (?)

# TODO: expand...?
# see https://stackoverflow.com/questions/446209/possible-values-from-sys-platform
class OSLabel(Enum):
    LINUX = "Linux",
    WINDOWS = "Windows",
    MACOS = "MacOS",
    INVALID = "???"


def get_os() -> OSLabel:
    return \
        OSLabel.LINUX if is_linux() else \
        OSLabel.WINDOWS if is_win() else \
        OSLabel.MACOS if is_osx() or is_osx_bundle() else \
        OSLabel.INVALID

def is_osx() -> bool:
    return sys.platform == "darwin"

def is_win() -> bool:
    return sys.platform == "win32"

def is_linux() -> bool:
    return sys.platform.startswith("linux")

def is_osx_bundle() -> bool:
    return sys.platform == "darwin" and (os.path.abspath(".").find(".app") != -1)

def is_64bit() -> bool:
    return sys.maxsize > 2**32

def is_root() -> bool:
    """Return True if running as root on Linux/Mac/Misc"""
    if hasattr(os, "getuid"):
        return not os.getuid()  # 0 if root
    return False

def is_admin() -> bool:
    """Return True if running as Admin on Windows."""
    try:
        if is_win():
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except OSError as win_issue:
        print(win_issue)
    return False
