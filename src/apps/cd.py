from application import Application
import os
from exceptions.invalid_syntax_error import InvalidSyntaxError


class Cd(Application):
    def run(self, args, inpt, out) -> None:
        if len(args) == 0 or len(args) > 1:
            raise InvalidSyntaxError("multiple arguments provided, expected 1")
        os.chdir(args[0])
