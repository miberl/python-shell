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
        # split flag arguments into different ranges and then cut each line
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
            # just a single value
            if len(r) == 1:
                if not int(r[0]) > len(line):
                    output += line[int(r[0]) - 1]
            else:
                lower_bound, upper_bound = self.get_bounds(line, r)

                if lower_bound > upper_bound:
                    raise ValueError("invalid range")

                # skip line if the lower bound is out of range
                if lower_bound > len(line):
                    continue

                if upper_bound > len(line):
                    upper_bound = len(line)

                output += line[lower_bound:upper_bound]

        if len(output) > 0 and output[-1] != "\n":
            output += "\n"
        return output

    def get_bounds(self, line, range):
        # :*
        if range[0] == "":
            lower_bound = 0
        # 5:*
        else:
            lower_bound = int(range[0]) - 1

        # *:
        if range[1] == "":
            upper_bound = len(line)
        # *:5
        else:
            upper_bound = int(range[1])

        return lower_bound, upper_bound
