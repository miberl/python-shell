from application import Application
from os import chdir


class Cd(Application):
    def run(self, args, inpt, out) -> None:
        if len(args) == 0 or len(args) > 1:
            raise ValueError("wrong number of command line arguments")
        chdir(args[0])
