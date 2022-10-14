from application import Application


class Echo(Application):
    def run(self, args, out) -> None:
        out.append(" ".join(args) + "\n")
