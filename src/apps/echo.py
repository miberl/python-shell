from application import Application


class Echo(Application):
    def run(self, args, inpt, out) -> None:
        out.append(" ".join(args) + "\n")
