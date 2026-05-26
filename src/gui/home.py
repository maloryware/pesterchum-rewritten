from PySide6 import QtCore
from PySide6.QtCore import QSize, Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from gui.dialog.profile_select import ProfileSelectWidget
from util.common import LOGGER


class PesterHome(QWidget):


    init: bool = False
    handle: str
    profile_select: ProfileSelectWidget
    # layout
    layout: QVBoxLayout
    welcome_label: QLabel
    # signals
    # ...

    @Slot()
    def on_profile_select(self):
        self.init = True
        self.handle = self.profile_select.handle_field.text()
        self.welcome_label.setText(f"Welcome, {self.handle}!")

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setWindowTitle("Pesterchum")
        self.setFixedSize(QSize(800, 600))

        self.build_layout()
        self.connect_all()

        self.show()


    def build_layout(self) -> None:
        self.layout = QVBoxLayout()
        self.welcome_label = QLabel("Loading...")

        self.layout.addWidget(self.welcome_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def connect_all(self):
        self.profile_select = ProfileSelectWidget(self)

