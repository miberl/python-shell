from application import Application


class Head(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        self.error_if_has_bad_num_args()

        file, num_lines = self.get_file_and_num_lines_to_read()

        self.open_file_and_read_lines(file, num_lines, out)

    def open_file_and_read_lines(self, file, num_lines, out):
        with open(file) as f:
            lines = f.readlines()
            self.write_out_lines(lines, num_lines, out)

    def write_out_lines(self, lines, num_lines, out):
        for i in self.line_num_range(lines, num_lines):
            self.write_out_line(i, lines, out)

    @staticmethod
    def line_num_range(lines, num_lines):
        return range(0, min(len(lines), num_lines))

    @staticmethod
    def write_out_line(i, lines, out):
        out.append(lines[i])

    def get_file_and_num_lines_to_read(self):
        file = ''
        num_lines = 0

        if len(self.args) == 1:
            file, num_lines = self.read_10_with_one_arg()
        if len(self.args) == 3:
            file, num_lines = self.read_n_with_three_args()

        return file, num_lines

    def read_n_with_three_args(self):
        self.error_if_not_flag_n()

        file, num_lines = self.read_in_args()
        return file, num_lines

    def read_in_args(self):
        num_lines = int(self.args[1])
        file = self.args[2]
        return file, num_lines

    def error_if_not_flag_n(self):
        if not self.is_first_flag_n():
            raise ValueError("wrong flags")

    def is_first_flag_n(self):
        return self.args[0] == "-n"

    def read_10_with_one_arg(self):
        num_lines = 10
        file = self.args[0]
        return file, num_lines

    def error_if_has_bad_num_args(self):
        if not self.one_or_three_args():
            raise ValueError("wrong number of command line arguments")

    def one_or_three_args(self):
        return len(self.args) == 1 or len(self.args) == 3
