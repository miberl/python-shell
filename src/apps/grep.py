
from application import Application
from exceptions.invalid_syntax_error import InvalidSyntaxError
from re import match


class Grep(Application):
    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)

        if len(command_args) == 0:
            raise InvalidSyntaxError("no pattern provided")
        pattern = command_args[0]

        if len(command_args) >= 2:  # files as arguments
            files = args[1:]
            for file in files:
                lines = self.read_lines(file)
                out.extend(self.filter_matching_lines(lines, pattern, file,
                                                      len(files) > 1))
        else:
            lines = []
            for line in inpt:
                lines.append(line)
            out.extend(self.filter_matching_lines(lines, pattern))

    # filter lines that match pattern
    @staticmethod
    def filter_matching_lines(lines, pattern, file_name="",
                              multiple_files=False):
        res = []
        for line in lines:
            if match(pattern, line):
                if multiple_files:
                    res.append(f"{file_name}:{line}")
                else:
                    res.append(line)
        return res
