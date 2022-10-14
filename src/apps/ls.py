from application import Application
from os import listdir, getcwd


class Ls(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        self.throw_if_too_many_args()

        ls_dir = self.get_ls_dir()

        self.get_list_from_dir(ls_dir, out)

    def get_list_from_dir(self, ls_dir, out):
        for f in listdir(ls_dir):
            self.print_if_not_hidden(f, out)

    def print_if_not_hidden(self, f, out):
        if not self.is_hidden(f):
            out.append(f + "\n")

    @staticmethod
    def is_hidden(f):
        return f.startswith(".")

    def throw_if_too_many_args(self):
        if len(self.args) > 1:
            raise ValueError("wrong number of command line arguments")

    def get_ls_dir(self):
        return getcwd() if len(self.args) == 0 else self.args[0]
