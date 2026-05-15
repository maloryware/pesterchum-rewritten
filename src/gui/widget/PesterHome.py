from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit
from util.common import LOGGER


class PesterHome(QWidget):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.setWindowTitle("Pesterchum")

        self.handle_field = QLineEdit('cogitantCaitiff', self)
        self.button = QPushButton("submit handle")
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)
        self.button.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.button)
        self.layout.addWidget()

        self.show()

    def button_clicked(self) -> None:
        LOGGER.warning("Button was clicked")
