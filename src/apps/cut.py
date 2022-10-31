from application import Application
from os.path import exists


class Cut(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        if len(self.args) != 3:
            raise ValueError("wrong number of command line arguments")

        flag_name = self.args[0]
        flag_arg = self.args[1]
        file_name = self.args[2]

        # in our context -b and -c are the same thing so why not support both
        if flag_name == "-b" or flag_name == "-c":
            self.cut_by_chars(flag_arg, self.read_lines(file_name), out)

    def read_lines(self, filename):
        with open(filename) as f:
            return f.readlines()

    def cut_by_chars(self, flag_arg, lines, out):
        ranges = self.get_ranges(flag_arg)
        for line in lines:
            out.append(self.cut_line_with_ranges(line, ranges))

    def get_ranges(self, input):
        ranges = []
        split_ranges = input.split(",")
        for r in split_ranges:
            nums = r.split("-")
            ranges.append(nums)
        return ranges

    def cut_line_with_ranges(self, line, ranges):
        output = ""
        for r in ranges:
            if len(r) == 1:
                if not int(r[0]) > len(line):
                    output += line[int(r[0]) - 1]
            else:
                if r[0] == "":
                    output += line[: int(r[1])]
                elif r[1] == "":
                    output += line[int(r[0]) - 1 :]
                else:
                    output += line[int(r[0]) - 1 : int(r[1])]
        if len(output) > 0 and output[-1] != "\n":
            output += "\n"
        return output
