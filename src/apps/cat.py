from application import Application


class Cat(Application):
    def run(self, args, out) -> None:
        for a in args:
            with open(a) as f:
                out.append(f.read())
