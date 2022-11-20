from application import Application
from exceptions.invalid_syntax_error import InvalidSyntaxError
from os import listdir, getcwd


class Ls(Application):
    def __init__(self):
        super().__init__() 

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        if len(command_args) > 1:
            raise InvalidSyntaxError("multiple arguments provided, expected 0 or 1")

        ls_dir = self.get_ls_dir(command_args)

        self.get_list_from_dir(ls_dir, out)


    def get_list_from_dir(self, ls_dir, out):
        for f in listdir(ls_dir):
            if not self.is_hidden(f):
                out.append(f + "\n")

    @staticmethod
    def is_hidden(f):
        return f.startswith(".")

    def get_ls_dir(self, command_args):
        return getcwd() if len(command_args) == 0 else command_args[0]
