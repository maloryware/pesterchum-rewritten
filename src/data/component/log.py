from data.base.pc_data import PesterchumData


class PesterLog(PesterchumData):

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