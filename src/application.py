from abc import ABC, abstractmethod


class Application(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def run(self, args, out):
        pass

    
    def read_lines(self, filename):
        with open(filename) as f:
            return f.readlines()

    def read_file(self, filename):
        with open(filename) as f:
            return f.read()