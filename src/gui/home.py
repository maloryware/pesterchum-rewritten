from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from gui.dialog.profile_select import ProfileSelectWidget
from util.common import LOGGER


class PesterHome(QWidget):

    handle: str
    init: bool = False
    profile_select: ProfileSelectWidget
    layout: QVBoxLayout

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # define parent widget format
        self.setWindowTitle("Pesterchum")
        self.setFixedSize(QSize(800, 600))
        # layout bullshit
        self.layout = QVBoxLayout()
        # ...
        self.setLayout(self.layout)
        self.show()

        # associate that one child layout to this
        self.profile_select = ProfileSelectWidget(self)


    # define this method as something for buttons to connect to (Qt library, signal/slot logic)
    @QtCore.pyqtSlot()
    def on_profile_select(self):
        self.init = True
        self.handle = self.profile_select.handle_field.text()
        self.layout.addWidget(QLabel(f"Welcome, {self.handle}!"), alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

