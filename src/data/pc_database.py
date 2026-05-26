import json
import os.path

from data.structure.pc_data import PesterchumData
from ostools.dirtools import get_data_dir


class PesterchumDB(dict, PesterchumData):


    # noinspection PyMissingConstructor
    def __init__(self):
        raise NotImplementedError

    # ~ PesterchumData::load ~
    def load(self) -> None:
        raise NotImplementedError


    # ~ PesterchumData::save ~
    def save(self) -> None:
        raise NotImplementedError


    # ~ PesterchumData::get_dir ~
    def get_dir(self) -> str:
        raise NotImplementedError
