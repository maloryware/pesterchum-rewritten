from abc import abstractmethod, ABC


class PesterchumData(ABC):
    """
    Defines a Class which contains a file within the data folder.
    """
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def get_dir(self) -> str:
        pass
