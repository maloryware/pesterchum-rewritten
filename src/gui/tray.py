from PySide6.QtWidgets import QSystemTrayIcon
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QIcon

from data.asset.pc_icon import PesterchumIcon
from util.common import LOGGER

class PesterTray(QObject):

    # TODO: missing requirements
    #  - loaded theme
    icon: QSystemTrayIcon

    def __init__(self, icon: QIcon, parent: QObject) -> None:
        super().__init__()

    # @Slot(bool)
    # def change_tray_icon(self, new_message: bool) -> None:
    #     if new_message:
    #         LOGGER.debug("Changing tray icon (blinking)")
    #     else:
    #         LOGGER.debug("Changing tray icon (default)")

    # @Slot
    # def close_main_window(self) -> None:
    #     self.hide()
