from abc import ABC, abstractmethod


class Application(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def run(self, args, out):
        pass
