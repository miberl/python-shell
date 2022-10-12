from application import Application
import os


class Cd(Application):
    def run(self, args, out) -> None:
        if len(args) == 0 or len(args) > 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(args[0])
