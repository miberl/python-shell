from application import Application
from os.path import exists


class Cut(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args
        raise NotImplementedError("Implement me, Filipp!")

    def read_lines(self, filename):
        with open(filename) as f:
            return f.readlines()

    # always returns true due to mock thing... ask Filipp about this
    def file_exists(self, filename):
        # return exists(filename)
        return True
