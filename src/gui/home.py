from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from gui.dialog.profile_select import ProfileSelectWidget
from util.common import LOGGER


class PesterHome(QWidget):

    handle: str
    init: bool = False
    profile_select: ProfileSelectWidget
    layout: QVBoxLayout

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # default/constructor/static factory method params
        self.setWindowTitle("Pesterchum")
        self.setFixedSize(QSize(800, 600))
        # default param
        self.layout = QVBoxLayout()
        # delegate to generic class init
        self.setLayout(self.layout)
        self.show()

        self.profile_select = ProfileSelectWidget(self)


    @QtCore.pyqtSlot()
    def on_profile_select(self):
        self.init = True
        self.handle = self.profile_select.handle_field.text()
        self.layout.addWidget(QLabel(f"Welcome, {self.handle}!"), alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

