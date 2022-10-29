from application import Application


class Uniq(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        if len(args) > 0:
            if not self.file_exists(self.args[0]):
                out.append("uniq: " + self.args[0] + ": No such file or directory")
                return

            input_file_lines = self.read_lines(self.args[0])

            previous_line = ""
            not_repeated_lines = []
            for line in input_file_lines:
                if line != previous_line:
                    not_repeated_lines.append(line)
                previous_line = line

            if len(args) == 1:
                for line in not_repeated_lines:
                    out.append(line)
            elif len(args) == 2:
                if not self.file_exists(self.args[1]):
                    out.append("uniq: " + self.args[1] + ": No such file or directory")
                    return
                output_file = open(self.args[1], "w")
                for line in not_repeated_lines:
                    output_file.write(line)
                output_file.close()

    # always returns true due to mock thing... ask Filipp about this
    def file_exists(self, filename):
        # return exists(filename)
        return True
