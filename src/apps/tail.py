from application import Application


class Tail(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        self.throw_if_not_one_or_three_args()
        file, num_lines = self.get_num_lines_and_file()

        self.print_tail_lines(file, num_lines, out)

    def read_lines(self, filename):
        with open(filename) as f:
            return f.readlines()

    def print_tail_lines(self, file, num_lines, out):
        lines = self.read_lines(file)
        display_length = self.get_display_length(lines, num_lines)
        self.print_in_display_range(display_length, lines, out)

    def print_in_display_range(self, display_length, lines, out):
        for i in range(0, display_length):
            out.append(self.get_ith_to_last_line(display_length, i, lines))

    @staticmethod
    def get_ith_to_last_line(display_length, i, lines):
        return lines[len(lines) - display_length + i]

    @staticmethod
    def get_display_length(lines, num_lines):
        return min(len(lines), num_lines)

    def get_num_lines_and_file(self):
        file = ''
        num_lines = 0

        if len(self.args) == 1:
            file, num_lines = self.set_for_one_arg()

        elif len(self.args) == 3:
            file, num_lines = self.set_for_three_arg()

        return file, num_lines

    def set_for_three_arg(self):
        self.throw_if_second_arg_not_n()

        num_lines = int(self.args[1])
        file = self.args[2]

        return file, num_lines

    def set_for_one_arg(self):
        num_lines = 10
        file = self.args[0]

        return file, num_lines

    def throw_if_second_arg_not_n(self):
        if self.args[0] != "-n":
            raise ValueError("wrong flags")

    def throw_if_not_one_or_three_args(self):
        if not self.has_one_or_three_args():
            raise ValueError("wrong number of command line arguments")

    def has_one_or_three_args(self):
        return len(self.args) == 1 or len(self.args) == 3
