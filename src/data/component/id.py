from typing import Any

from PySide6.QtGui import QColor

from data.component.mood import Mood, Moods


# directory: {data}/profile/{handle}
class PesterchumID:
    """
    Constitutes a Pesterchum ID.

    Pesterchum IDs make up the identity of any one user within the platform.
    IDs are only present in the following contexts:
    - User list
    - Friends list
    - Chat Window
    - Memo Window

    stub
    """

    handle: str
    color: QColor
    mood: Mood

    def __init__(
            self,
            handle: str,
            color: Any = QColor(0x000000),
            mood: Mood = Moods.OFFLINE,
            notes: str | None = None,
            group: str | None = None,
    ):
        self.handle = handle
        self.color = color
        self.mood = mood
        self.notes = notes
        self.group = group
