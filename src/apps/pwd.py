from application import Application
from os import getcwd


class Pwd(Application):
    def __init__(self) -> None:
        super().__init__()

    def run(self, args, out) -> None:
        out.append(getcwd())
