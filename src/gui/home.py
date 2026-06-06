from PySide6 import QtCore
from PySide6.QtCore import QSize, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from data.base.pc_widget import PesterchumWidget
from gui.dialog.profile_select import ProfileSelectWidget


class PesterHome(QWidget, PesterchumWidget):


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

        self.build()
        self.assign_signals()

        self.show()


    def build(self) -> None:
        self.layout = QVBoxLayout()
        self.welcome_label = QLabel("Loading...")

        self.layout.addWidget(self.welcome_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def assign_signals(self):
        self.profile_select = ProfileSelectWidget(self)

