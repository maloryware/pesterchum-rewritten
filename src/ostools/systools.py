# honoring the fabled ostools.py from the original project
import sys, ctypes

from ostools.dirtools import *


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
