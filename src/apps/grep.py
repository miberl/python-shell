
from application import Application
from re import match


class Grep(Application):
    def run(self, args, out) -> None:
        if len(args) < 2:
            raise ValueError("wrong number of command line arguments")
        pattern = args[0]
        files = args[1:]
        for file in files:
            lines = self.read_lines(file)
            out.extend(self.filter_matching_lines(
                lines, pattern, file, len(files) > 1))


    # filter lines that match pattern
    def filter_matching_lines(self, lines, pattern, file_name, multiple_files):
        res = []
        for line in lines:
            if match(pattern, line):
                if multiple_files:
                    res.append(f"{file_name}:{line}")
                else:
                    res.append(line)
        return res
