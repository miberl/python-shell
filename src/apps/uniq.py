from application import Application


class Uniq(Application):
    def __init__(self):
        super().__init__()
        self.args = None

    def run(self, args, out) -> None:
        self.args = args

        if len(args) > 0:
            input_file = open(self.args[0], "r")
            input_file_lines = input_file.readlines()
            input_file.close()

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
                output_file = open(self.args[1], "w")
                for line in not_repeated_lines:
                    output_file.write(line)
                output_file.close()
