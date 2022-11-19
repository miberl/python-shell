from application import Application

class Cat(Application):
    def __init__(self) -> None:
        super().__init__()

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        if len(command_args) > 0:
            for arg in command_args:
                out.append(self.read_file(arg))
            return None 
        for line in inpt:
            out.append(line)
