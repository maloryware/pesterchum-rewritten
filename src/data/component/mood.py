from enum import Enum

from data.asset.pc_icon import PesterchumIcon
from data.component.pc_theme import PesterchumTheme
from data.structure.pc_data import PesterchumData
from util.assets import Assets
from util.common import LOGGER


class Moods(Enum):
    """
    Moods enumerator, to keep code clean, concise and readable.
    """
    # yes, moods are out of order
    # this is unlikely to be modified to keep
    # parity with pesterchum-alt-servers
    # ~maloryware

    # chums
    CHUMMY = 0
    RANCOROUS = 1
    OFFLINE = 2
    PLEASANT = 3
    DISTRAUGHT = 4
    PRANKY = 5
    SMOOTH = 6
    MYSTIFIED = 19
    AMAZED = 20
    INSOLENT = 21
    BEMUSED = 22
    # trolls
    ECSTATIC = 7
    RELAXED = 8
    DISCONTENT = 9
    DEVIOUS = 10
    SLEEK = 11
    DETESTFUL = 12
    MIRTHFUL = 13
    MANIPULATIVE = 14
    VIGOROUS = 15
    PERKY = 16
    ACCEPTANT = 17
    # other (doc scratch)
    PROTECTIVE = 18

    @staticmethod
    def get(mood: int) -> Moods:
        """Returns the Moods enumerator for a given number."""
        return Moods(mood)

class Mood:

    def __init__(self, mood: Moods | int):
        if isinstance(mood, Moods):
            self.mood = mood
        if isinstance(mood, int):
            self.mood = Moods.get(mood)
        raise NotImplementedError

    def name(self):
        return Moods.get(self.mood.__str__())

    def icon(self, theme: PesterchumTheme):
        return PesterchumIcon.of(self.name(), theme)