from typing import Any
from uuid import UUID
from PySide6.QtGui import QColor
from data.component.mood import Mood, Moods
from data.pc_database import PesterchumDB


# directory: {data}/{id}/
class PesterchumProfile:
    """
    Constitutes a Pesterchum Profile (not to be mistaken for in-app "profiles", aka UserProfile)

    Pesterchum Profiles make up the identity of any one user within the platform.
    stub
    """

    handle: str
    color: QColor
    mood: None

    def __init__(
            self,
            db: PesterchumDB,
            handle: str,
            color: Any, # TODO: update type hint
            mood: Mood = Mood(Moods.CHUMMY),
            notes: str = "",
            group = None,
                 ):

        # load component from settings -> default component
        self.handle = "pesterClient"
        self.color = QColor(0x000000)
