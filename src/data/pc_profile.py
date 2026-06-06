import os.path

from data.component.id import PesterchumID
from data.base.pc_data import PesterchumData
from ostools.dirtools import get_profile_dir


class PesterchumProfile(PesterchumData):

    profile: PesterchumID
    chums: list[PesterchumID]
    mentions: list[str]
    blocklist: list[str]
    autojoins: list[str]
    randoms: bool
    _dir: str

    chums_path: str
    profile_path: str
    quirks_path: str


    def __init__(self, profile: PesterchumID | None):
        if profile is None:
            raise NotImplementedError("No handling for invalid profiles atm ;(")
        self.profile = profile

        if self.exists():
            self.load()
            return

        raise NotImplementedError


    def exists(self) -> bool:
        return os.path.exists(self.get_dir())


    def _is_temp_profile(self) -> bool:
        return "pesterClient" in self.profile.handle


    # ~ PesterchumData::save ~
    def save(self) -> None:
        if self._is_temp_profile():
            return
        raise NotImplementedError


    # ~ PesterchumData::load ~
    def load(self) -> None:
        if self._is_temp_profile():
            return
        raise NotImplementedError


    # ~ PesterchumData::get_dir ~
    def get_dir(self) -> str:
        return get_profile_dir() + "/" + self.profile.handle