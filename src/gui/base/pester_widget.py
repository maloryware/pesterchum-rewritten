from typing import Self

from PySide6.QtWidgets import QMessageBox


class PesterchumMsgBox:


    def __init__(self):
        self.box = QMessageBox()

    def title(self, title: str) -> PesterchumMsgBox:
        self.box.setWindowTitle(title)
        return self

    def body(self, text: str) -> PesterchumMsgBox:
        self.box.setInformativeText(text)
        return self

    def icon(self, icon: QMessageBox.Icon) -> PesterchumMsgBox:
        self.box.icon()
        return self
