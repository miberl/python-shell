from application import Application


class Cat(Application):
    def run(self, args, out) -> None:
        for a in args:
            out.append(self.read_file(a))

    def read_file(self, filename):
        with open(filename) as f:
            return f.read()
