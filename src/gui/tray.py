from PySide6.QtWidgets import QSystemTrayIcon
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QIcon
from util.common import LOGGER

class PesterTray(QSystemTrayIcon):

    def __init__(self, icon: QIcon, parent: QObject) -> None:
        super().__init__(icon, parent)

    @Slot(bool)
    def change_tray_icon(self, new_message: bool) -> None:
        if new_message:
            LOGGER.debug("Changing tray icon (blinking)")
        else:
            LOGGER.debug("Changing tray icon (default)")

    @Slot
    def close_main_window(self) -> None:
        self.hide()
