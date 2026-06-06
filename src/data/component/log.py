from data.base.pc_data import PesterchumData


class PesterLog(PesterchumData):

    def __init__(self):
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError

    def save(self) -> None:
        raise NotImplementedError

    def get_dir(self) -> str:
        raise NotImplementedError