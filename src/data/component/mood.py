from enum import Enum

from data.asset.pc_icon import PesterchumIcon
from data.component.theme import PesterchumTheme


class Mood:

    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    def name(self):
        return self._name

    def value(self):
        return self._value

    def icon(self, theme: PesterchumTheme):
        return PesterchumIcon.of(self.name(), theme)


class Moods(Enum):
    """
    Moods enumerator, to keep code clean, concise and readable.
    """
    # yes, moods are out of order
    # this is unlikely to be modified to keep
    # parity with pesterchum-alt-servers
    # ~maloryware

    # chums
    CHUMMY = Mood("CHUMMY", 0)
    RANCOROUS = Mood("RANCOROUS", 1)
    OFFLINE = Mood("OFFLINE", 2)
    PLEASANT = Mood("PLEASANT", 3)
    DISTRAUGHT = Mood("DISTRAUGHT", 4)
    PRANKY = Mood("PRANKY", 5)
    SMOOTH = Mood("SMOOTH", 6)
    MYSTIFIED = Mood("MYSTIFIED", 19)
    AMAZED = Mood("AMAZED", 20)
    INSOLENT = Mood("INSOLENT", 21)
    BEMUSED = Mood("BEMUSED", 22)
    # trolls
    ECSTATIC = Mood("ECSTATIC", 7)
    RELAXED = Mood("RELAXED", 8)
    DISCONTENT = Mood("DISCONTENT", 9)
    DEVIOUS = Mood("DEVIOUS", 10)
    SLEEK = Mood("SLEEK", 11)
    DETESTFUL = Mood("DETESTFUL", 12)
    MIRTHFUL = Mood("MIRTHFUL", 13)
    MANIPULATIVE = Mood("MANIPULATIVE", 14)
    VIGOROUS = Mood("VIGOROUS", 15)
    PERKY = Mood("PERKY", 16)
    ACCEPTANT = Mood("ACCEPTANT", 17)
    # other (doc scratch)
    PROTECTIVE = Mood("PROTECTIVE", 18)