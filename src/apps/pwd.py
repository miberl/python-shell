from application import Application


class Pwd(Application):
    def run(self, args, out) -> None:
        out.append(os.getcwd())
