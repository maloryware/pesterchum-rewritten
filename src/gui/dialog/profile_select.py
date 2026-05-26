from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QCompleter
from PySide6.QtGui import QAction

# Test format --- this needs to be a Builder/Factory ostools.
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

        # create a label object
        self.select_reason = QLabel("Enter a chumhandle.")
        # add label object to the primary layout
        self.layout.addWidget(self.select_reason)

        self.handle_label = QLabel("CHUMHANDLE: ")
        # create editable text field
        self.handle_field = QLineEdit(self)
        # add autocomplete behaviour
        self.handle_field.setCompleter(QCompleter(["cogitantCaitiff", "Mal", "telecastTadpole"]))
        # add widget to horizontal layout 1
        self.handle.addWidget(self.handle_label)
        # add widget to horizontal layout 1
        self.handle.addWidget(self.handle_field)
        # add horizontal layout to primary vertical layout
        self.layout.addLayout(self.handle)

        # create button...
        self.button_ok = QPushButton("OK", self)
        # ...
        self.button_ok.setDefault(True)
        # connect button clicked behaviour to internal "accept" method
        self.button_ok.clicked.connect(self.accept)
        self.button_cancel = QPushButton("CANCEL", self)
        # connect button clicked behaviour to internal "reject" method
        self.button_cancel.clicked.connect(self.reject)
        self.buttons.addWidget(self.button_cancel)
        self.buttons.addWidget(self.button_ok)
        self.layout.addLayout(self.buttons)

        # connect internal "accept" method to a method of the parent widget
        self.accepted.connect(self.parent().on_profile_select)
        # define the widget's core layout to the [self.layout] object
        self.setLayout(self.layout)
        # display ts
        self.show()

