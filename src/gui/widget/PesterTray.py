from PyQt6.QtWidgets import QSystemTrayIcon
from PyQt6.QtCore import QObject, pyqtSlot as Slot
from PyQt6.QtGui import QIcon
from utils.consts import LOGGER


class PesterTray(QSystemTrayIcon):

    def __init__(self, icon: QObject, mainwindow: QIcon, parent: QObject):
        super().__init__(self, icon, mainwindow, parent)

    @Slot(bool)
    def changeTrayIcon(self, new_message: bool):
        if new_message:
            LOGGER.warning("Changing tray icon (blinking)")
        else:
            LOGGER.warning("Changing tray icon (default)")

    @Slot
    def closeMainWindow(self):
        self.hide()
