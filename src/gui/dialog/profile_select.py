from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QCompleter


# Test format --- this needs to be a Builder/Factory system.
# if not, it's just wrapping back around to what mocha said

# and if this proves to be impossible, we're moving to java

class ProfileSelectWidget(QDialog):

    layout = QVBoxLayout()
    ###
    select_reason: QLabel
    ###
    handle = QHBoxLayout() # [LABEL: [FIELD]]
    handle_label: QLabel
    handle_field: QLineEdit
    ###
    buttons = QHBoxLayout() # [CANCEL | OK]
    button_cancel: QPushButton
    button_ok: QPushButton

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.select_reason = QLabel("Enter a chumhandle.")
        self.layout.addWidget(self.select_reason)

        # this ALL needs to become a factory.
        self.handle_label = QLabel("CHUMHANDLE: ")
        self.handle_field = QLineEdit(self)
        self.handle_field.setCompleter(QCompleter(["cogitantCaitiff", "Mal", "telecastTadpole"]))
        self.handle.addWidget(self.handle_label)
        self.handle.addWidget(self.handle_field)
        self.layout.addLayout(self.handle)

        self.button_ok = QPushButton("OK", self)
        self.button_ok.setDefault(True)
        self.button_ok.clicked.connect(self.accept)
        self.button_cancel = QPushButton("CANCEL", self)
        self.button_cancel.clicked.connect(self.reject)
        self.buttons.addWidget(self.button_cancel)
        self.buttons.addWidget(self.button_ok)
        self.layout.addLayout(self.buttons)

        # either passed on factory methods, or outside lambda ref
        self.accepted.connect(self.parent().on_profile_select)
        self.setLayout(self.layout)
        self.show()

