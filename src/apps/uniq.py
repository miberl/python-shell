from application import Application
from exceptions.invalid_syntax_error import InvalidSyntaxError


class Uniq(Application):
    def __init__(self):
        super().__init__()
        self.options = {
            "-i": 0  # ignores case when doing comparison (case insensitive)
        }

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        ignore_case = options.get("-i") is not None

        lines = []
        if len(command_args) == 1:
            lines.extend(self.read_lines(command_args[0]))
        elif len(command_args) > 1:
            raise InvalidSyntaxError("multiple arguments provided, expected 1")
        else:
            for line in inpt:
                lines.append(line)

        out.extend(self.unique_lines(lines, ignore_case))

    @classmethod
    def compare_lines(cls, line1, line2, ignore_case=False) -> bool:
        if ignore_case:
            return line1.lower() == line2.lower()
        return line1 == line2

    @classmethod
    def unique_lines(cls, lines, ignore_case=False) -> list:
        previous_line = None
        unique_lines = []
        for line in lines:
            if not previous_line or not cls.compare_lines(line, previous_line,
                                                          ignore_case):
                unique_lines.append(line)
                previous_line = line
        return unique_lines
