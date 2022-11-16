from application import Application
from os import getcwd


class Pwd(Application):
    def __init__(self) -> None:
        super().__init__()

    def run(self, args, inpt, out) -> None:
        out.append(getcwd())
