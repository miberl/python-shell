import sys

from application import Application
from exceptions.unknown_option_error import UnknownFlagError


class Cut(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, inpt, out) -> None:
        self.args = args

        if len(self.args) != 2 and len(self.args) != 3:
            raise ValueError("wrong number of command line arguments")
        elif len(self.args) == 2:
            data = []
            for line in inpt:
                data.append(line)
        else:
            data = self.read_lines(self.args[2])

        flag_name = self.args[0]
        flag_arg = self.args[1]

        # in our context -b and -c are the same thing so why not support both
        if flag_name == "-b" or flag_name == "-c":
            self.cut_by_chars(flag_arg, data, out)
        else:
            raise UnknownFlagError(flag_name)

    def cut_by_chars(self, flag_arg, lines, out):
        # split flag arguments into different ranges and then cut each line
        ranges = self.get_ranges(flag_arg)
        for line in lines:
            out.append(self.cut_line_with_ranges(line, ranges))

    def get_ranges(self, inp):
        ranges = []
        split_ranges = inp.split(",")
        for r in split_ranges:
            nums = r.split("-")
            ranges.append(nums)
        ranges = self.adjust_for_overlapping_ranges(ranges)
        return ranges

    @staticmethod
    def cut_line_with_ranges(line, ranges):
        output = ""
        for r in ranges:
            lower_bound, upper_bound = r

            if lower_bound > upper_bound:
                raise ValueError("invalid range")

            # skip line if the lower bound is out of range
            if lower_bound > len(line):
                continue

            if upper_bound > len(line):
                upper_bound = len(line)

            output += line[lower_bound - 1:upper_bound]

        if len(output) > 0 and output[-1] != "\n":
            output += "\n"
        return output

    def adjust_for_overlapping_ranges(self, ranges):
        new_ranges = set(self.to_int_ranges(ranges))
        change_made = True

        while change_made:
            nr_list = list(new_ranges)
            change_made = False
            change_made = self._for_all_r(change_made, new_ranges, nr_list)

        return sorted(list(new_ranges))

    def _for_all_r(self, made, new_ranges, new_ranges_list):
        for i, r_1 in enumerate(new_ranges_list):
            for r_2 in new_ranges_list[i + 1:]:
                made = self._update_new_ranges(made, new_ranges, r_1, r_2)
        return made

    def _update_new_ranges(self, change_made, new_ranges, r_1, r_2):
        if (r_1[0] <= r_2[1] and r_1[1] >= r_2[0]) or (
                r_1[1] <= r_2[0] and r_1[0] >= r_2[1]):
            change_made = True
            new_ranges.remove(r_1)
            new_ranges.remove(r_2)
            new_ranges.add((min(r_1[0], r_2[0]), min(r_1[1], r_2[1])))
        return change_made

    @staticmethod
    def to_int_ranges(ranges):
        new_ranges = []
        for r in ranges:
            if len(r) == 1:
                new_ranges.append((int(r[0]), int(r[0])))
                continue
            start, end = r[0], r[1]
            if start == '':
                new_start = 1
            else:
                new_start = int(start)
            if end == '':
                new_end = sys.maxsize
            else:
                new_end = int(end)

            new_ranges.append((new_start, new_end))

        return new_ranges
