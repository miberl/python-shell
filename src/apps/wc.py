from collections import deque

from application import Application


class WordObject:
    def __init__(self, inpt):
        self.line_count = self._get_lc(inpt)
        self.word_count = self._get_wc(inpt)
        self.byte_count = self._get_bc(inpt)
        self.char_count = self._get_cc(inpt)

    @staticmethod
    def _get_lc(inpt: str) -> int:
        return inpt.count('\n')

    @staticmethod
    def _get_wc(inpt: str) -> int:
        tot = sum(str.isspace(c) for c in inpt)
        if len(inpt) > 0 and not str.isspace(inpt[-1]):
            tot += 1
        return tot

    @staticmethod
    def _get_bc(inpt: str) -> int:
        return len(inpt.encode('utf-8'))

    @staticmethod
    def _get_cc(inpt: str) -> int:
        return len(inpt)


class Wc(Application):
    def __init__(self):
        super().__init__()
        self.options = {
            '-w': 0,
            '-l': 0,
            '-m': 0,
            '-c': 0
        }
        self.files = []

    def run(self, args, inpt, out):
        command_args, options = self.parse_args(args)

        self.read_input(command_args, inpt)

        out.extend(self._output(options))

    def read_input(self, command_args, inpt):
        for file_name in command_args:
            lines = Application.read_lines(file_name)
            self._process_file(lines, file_name)
        if len(command_args) == 0:
            self._process_file(inpt)

    def _process_file(self, inpt, file_name=None):
        concated_input = ''
        for line in inpt:
            concated_input += line
        file = WordObject(concated_input)
        self.files.append((file, file_name))

    def _output(self, options):
        total = self._get_total()
        output = []

        for file, file_name in self.files:
            output.append(self._produce_output_for(file, file_name, total, options))

        if len(self.files) > 1:
            output.append(self._produce_output_for(total, 'total', total, options))

        output.append('\n')
        return output

    def _produce_output_for(self, file: WordObject, file_name, total, options):
        output = ''
        if len(options) == 0 or options.get('-l') is not None:
            output += f'    {self._space_offset(file.line_count, total.line_count)}{file.line_count}'
        if len(options) == 0 or options.get('-w') is not None:
            output += f'    {self._space_offset(file.word_count, total.word_count)}{file.word_count}'
        if len(options) == 0 or options.get('-m') is not None:
            output += f'    {self._space_offset(file.byte_count, total.byte_count)}{file.byte_count}'
        if options.get('-c') is not None:
            output += f'    {self._space_offset(file.char_count, total.char_count)}{file.char_count}'
        if file_name is not None:
            output += f' {file_name}'
        return output + '\n'

    def _space_offset(self, file: int, total: int):
        return " " * (len(str(total)) - len(str(file)))

    def _get_total(self):
        total = WordObject('')
        for file, _ in self.files:
            self.update_total(file, total)
        return total

    def update_total(self, file, total):
        total.line_count += file.line_count
        total.word_count += file.word_count
        total.byte_count += file.byte_count
        total.char_count += file.char_count
