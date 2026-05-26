from abc import ABC, abstractmethod


class PesterchumWidget(ABC):

    @abstractmethod
    def build(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def assign_signals(self) -> None:
        raise NotImplementedError