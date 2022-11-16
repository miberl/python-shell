from abc import ABC, abstractmethod


class Application(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def run(self, args, inpt, out):
        pass

    @classmethod
    def read_lines(cls, filename):
        with open(filename) as f:
            return f.readlines()

    @classmethod
    def read_file(cls, filename):
        with open(filename) as f:
            return f.read()