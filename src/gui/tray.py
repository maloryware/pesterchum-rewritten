from PyQt6.QtWidgets import QSystemTrayIcon
from PyQt6.QtCore import QObject, pyqtSlot as Slot
from PyQt6.QtGui import QIcon
from util.common import LOGGER

class PesterTray(QSystemTrayIcon):

    def __init__(self, icon: QIcon, mainwindow: QIcon, parent: QObject) -> None:
        super().__init__(icon, parent)

    @Slot(bool)
    def change_tray_icon(self, new_message: bool) -> None:
        if new_message:
            LOGGER.warning("Changing tray icon (blinking)")
        else:
            LOGGER.warning("Changing tray icon (default)")

    @Slot
    def close_main_window(self) -> None:
        self.hide()
