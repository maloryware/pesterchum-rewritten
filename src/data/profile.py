from uuid import UUID
from PyQt6.QtGui import QColor
from data.model.chum import Chum
from data.model.quirk import Quirk
from pesterchum import PesterchumApp


# directory: {data}/{id}/
class Profile:
    handle: str
    id: UUID
    color: QColor
    quirks: list[Quirk] # dump separately
    chums: list[Chum] # dump separately
    theme: None
    mood: None

    mentions: list[str] # dump separately
    autojoins: list[str] # dump separately
    randoms: bool
    blocklist: list[str] # dump separately

    app: PesterchumApp

    def __init__(self, app: PesterchumApp):
        # load profile from settings -> default profile
        self.handle = "pesterClient"
        self.color = QColor(0x000000)
        self.app = app
