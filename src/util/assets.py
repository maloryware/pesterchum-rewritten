from enum import Enum

def _asset(path: str) -> str:
    return "./assets/" + path

def _img(path: str) -> str:
    return _asset("img/" + path)

def _theme(path: str) -> str:
    return _asset("themes/" + path)

def _smily(path: str) -> str:
    return _asset("smilies/" + path)


class Assets(Enum):

    MISSING = _asset("missing.png")

    class Icons(Enum):
        # chums
        CHUMMY = _smily("pc_chummy.png")
        RANCOROUS = _smily("pc_rancorous.png")
        PLEASANT = _smily("pc_pleasant.png")
        DISTRAUGHT = _smily("pc_distraught.png")
        PRANKY = _smily("pc_pranky.png")
        SMOOTH = _smily("pccool.png")
        MYSTIFIED = _smily("pc_mystified.png")
        AMAZED = _smily("pc_amazed.png")
        INSOLENT = _smily("pc_insolent.png")
        BEMUSED = _smily("pc_bemused.png")
        # trolls
        ECSTATIC = _smily("ecstatic.png")
        RELAXED = _smily("relaxed.png")
        DISCONTENT = _smily(".png")
        DEVIOUS = _smily("devious.png")
        SLEEK = _smily("sleek.png")
        DETESTFUL = _smily("detestful.png")
        MIRTHFUL = _smily("mirthful.png")
        MANIPULATIVE = _smily("manipulative.png")
        VIGOROUS = _smily("vigorous.png")
        PERKY = _smily("perky.png")
        ACCEPTANT = _smily("acceptant.png")
