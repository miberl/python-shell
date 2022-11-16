from unittest import TestCase

from inputparser.command import Command, Pipe
from inputparser.parse_command import ParseCommands
from inputparser.parser_visitor import ParseVisitor


class TestParserObjectConstruction(TestCase):
    @staticmethod
    def run_parser(cmd: str) -> list:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(cmd, visitor)
        return visitor.get_instructions()

    def run_single_command(self, cmd) -> Command:
        instrs = self.run_parser(cmd)
        self.assertEqual(len(instrs), 1)
        if type(instrs[0]) is Command:
            return instrs[0]
        else:
            self.assertFalse(True)

    def make_assertions(self, command, name='ls', args=None, redir=(None, None)):
        if args is None:
            args = []

        self.assertEqual(command.get_app(), name)
        self.assertEqual(command.get_flags_and_args(), args)
        self.assertEqual(command.get_redirs(), redir)

    def test_simple_command_name(self):
        command = self.run_single_command('ls')

        self.assertEqual(command.get_app(), 'ls')

    def test_simple_command_no_args(self):
        command = self.run_single_command('ls')

        self.assertEqual(command.get_flags_and_args(), [])

    def test_simple_command_no_redir(self):
        command = self.run_single_command('ls')

        self.assertEqual(command.get_redirs(), (None, None))

    def test_simple_command_with_extra_spaces(self):
        command = self.run_single_command(' ls ')

        self.make_assertions(command)

    def test_simple_command_one_arg(self):
        command = self.run_single_command('ls hello')

        self.make_assertions(command, args=[(None, ['hello'])])

    def test_simple_command_multi_arg(self):
        command = self.run_single_command('ls hello there mate')

        self.make_assertions(command, args=[(None, ['hello', 'there', 'mate'])])

    def test_command_one_flag(self):
        command = self.run_single_command('ls -a')

        self.make_assertions(command, args=[('a', [])])

    def test_command_many_flags(self):
        command = self.run_single_command('ls -a -b')

        self.make_assertions(command, args=[('a', []), ('b', [])])

    def test_command_flag_with_args(self):
        command = self.run_single_command('ls -a hello -b there you')

        self.make_assertions(command, args=[('a', ['hello']), ('b', ['there', 'you'])])

    def test_file_redir_in(self):
        command = self.run_single_command('ls < hello.txt')

        self.make_assertions(command, redir=('hello.txt', None))

    def test_file_redir_out(self):
        command = self.run_single_command('ls > bye.txt')

        self.make_assertions(command, redir=(None, 'bye.txt'))

    def test_file_redir_both(self):
        command = self.run_single_command('ls < hello.txt > bye.txt')

        self.make_assertions(command, redir=('hello.txt', 'bye.txt'))

    def test_flags_args_redir(self):
        command = self.run_single_command('ls -a hello -b there mate < input.txt > output.txt')

        self.make_assertions(command,
                             args=[('a', ['hello']), ('b', ['there', 'mate'])],
                             redir=('input.txt', 'output.txt'))

    def test_simple_pipe(self):
        instructions = self.run_parser('ls | ls')

        self.assertEqual(len(instructions), 1)
        instruction = instructions[0]

        pipe = self.get_pipe(instruction)

        left_command, right_command = pipe.get_piped_commands()

        self.make_assertions(left_command)

        self.make_assertions(right_command)

    def get_pipe(self, instruction):
        if type(instruction) is Pipe:
            pipe = instruction
            self.assertTrue(True)
        else:
            pipe = None
            self.assertTrue(False)
        return pipe


    def test_pipe(self):
        instructions = self.run_parser('ls -a hello -b there mate < input.txt | cat file.txt')

        self.assertEqual(len(instructions), 1)
        instruction = instructions[0]

        pipe = self.get_pipe(instruction)

        left_command, right_command = pipe.get_piped_commands()

        self.make_assertions(left_command,
                             args=[('a', ['hello']), ('b', ['there', 'mate'])],
                             redir=('input.txt', None))

        self.make_assertions(right_command,
                             name='cat',
                             args=[(None, ['file.txt'])])

    def test_concat_two_commands(self):
        instructions = self.run_parser('ls ; cat')

        self.assertEqual(len(instructions), 2)

        ls, cat = instructions[0], instructions[1]

        self.make_assertions(ls)
        self.make_assertions(cat, name='cat')
