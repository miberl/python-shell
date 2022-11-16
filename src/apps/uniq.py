from application import Application

# `-i` ignores case when doing comparison (case insensitive)

class Uniq(Application):
    def __init__(self):
        super().__init__()

    def run(self, args, inpt, out) -> None:
        filename, ignore_case = self.get_filename(args), self.is_ignore_case(args)

        file_lines = self.read_lines(filename)
        previous_line = None
        for line in file_lines:
            if not previous_line or not self.compare_lines(line, previous_line, ignore_case):
                out.append(line)
                previous_line = line

    @classmethod
    def compare_lines(cls, line1, line2, ignore_case=False) -> bool:
        if ignore_case:
            return line1.lower() == line2.lower()
        return line1 == line2


    def is_ignore_case(self, args) -> bool:
        if "-i" in args:
            return True
        return False

    def get_filename(self, args) -> str:
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return args[1]
        else:
            raise ValueError("wrong number of command line arguments")