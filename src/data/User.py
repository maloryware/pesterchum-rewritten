from PyQt6.QtGui import QColor


class User():

    def __init__(self, handle: str):
        self.handle = handle
        self.color = QColor.black