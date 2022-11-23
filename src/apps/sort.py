from application import Application


class Sort(Application):
    def __init__(self):
        super().__init__()
        self.options = {
            "-r": 0
        }

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        is_reversed = options.get("-r") is not None

        lines = []
        if len(command_args) > 0:
            for filename in command_args:
                lines.extend(self.read_lines(filename))
        else:
            for line in inpt:
                lines.append(line)

        lines.sort(reverse=is_reversed)
        out.extend(lines)
