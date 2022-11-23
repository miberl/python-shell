from application import Application
from exceptions.invalid_syntax_error import InvalidSyntaxError


# head [file ...]

class Head(Application):
    def __init__(self):
        super().__init__()
        self.options = {
            "-n": 1
        }

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)

        lines = []
        if len(command_args) == 1:
            lines.extend(self.read_lines(command_args[0]))
        elif len(command_args) > 1:
            raise InvalidSyntaxError("multiple arguments provided, expected 1")
        else:
            for line in inpt:
                lines.append(line)

        limit_option = int(options.get("-n")[0]) if options.get("-n") else None
        line_limit = self.line_limit_num(lines, limit_option)
        out.extend(lines[:line_limit])

    @staticmethod
    def line_limit_num(lines, limit):
        default_line_limit = 10
        if limit is None:
            limit = default_line_limit
        limit = min(limit, len(lines))
        return limit
