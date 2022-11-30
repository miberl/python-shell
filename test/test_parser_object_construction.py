from unittest import TestCase

from inputparser.command import Command
from inputparser.parse_command import ParseCommands
from inputparser.parser_visitor import ParseVisitor


class TestParserObjectConstruction(TestCase):
    @staticmethod
    def run_parser(cmd: str) -> []:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(cmd, visitor)
        return visitor.get_instructions()

    def run_single_command(self, cmd) -> Command:
        instrs = self.run_parser(cmd)
        self.assert_test_valid(instrs)
        return instrs[0].get_next_command()

    @staticmethod
    def assert_test_valid(instrs):  # pragma: no cover
        assert len(instrs) == 1
        assert instrs[0].has_next()

    def make_assertions(self, command, name="ls", args=None, redir=([], [])):
        if args is None:
            args = []

        self.assertEqual(command.get_app(), name)
        self.assertEqual(command.get_args(), args)
        self.assertEqual(command.get_redirs(), redir)

    def test_simple_command_name(self):
        command = self.run_single_command("ls")

        self.assertEqual(command.get_app(), "ls")

    def test_simple_command_no_args(self):
        command = self.run_single_command("ls")

        self.assertEqual(command.get_args(), [])

    def test_simple_command_no_redir(self):
        command = self.run_single_command("ls")

        self.assertEqual(command.get_redirs(), ([], []))

    def test_simple_command_with_extra_spaces(self):
        command = self.run_single_command(" ls ")

        self.make_assertions(command)

    def test_simple_command_one_arg(self):
        command = self.run_single_command("ls hello")

        self.make_assertions(command, args=["hello"])

    def test_simple_command_multi_arg(self):
        command = self.run_single_command("ls hello there mate")

        self.make_assertions(command, args=["hello", "there", "mate"])

    def test_command_one_flag(self):
        command = self.run_single_command("ls -a")

        self.make_assertions(command, args=["-a"])

    def test_command_many_flags(self):
        command = self.run_single_command("ls -a -b")

        self.make_assertions(command, args=["-a", "-b"])

    def test_command_flag_with_args(self):
        command = self.run_single_command("ls -a hello -b there you")
        args = ["-a", "hello", "-b", "there", "you"]
        self.make_assertions(command, args=args)

    def test_file_redir_in(self):
        command = self.run_single_command("ls < hello.txt")

        self.make_assertions(command, redir=(["hello.txt"], []))

    def test_file_redir_out(self):
        command = self.run_single_command("ls > bye.txt")

        self.make_assertions(command, redir=([], ["bye.txt"]))

    def test_file_redir_both(self):
        command = self.run_single_command("ls < hello.txt > bye.txt")

        self.make_assertions(command, redir=(["hello.txt"], ["bye.txt"]))

    def test_flags_args_redir(self):
        command = self.run_single_command(
            "ls -a hello -b there mate < input.txt > output.txt"
        )

        self.make_assertions(
            command,
            args=["-a", "hello", "-b", "there", "mate"],
            redir=(["input.txt"], ["output.txt"]),
        )

    def test_simple_pipe(self):
        instructions = self.run_parser("ls | ls")

        self.assertEqual(len(instructions), 1)
        instruction = instructions[0]

        left_command = instruction.get_next_command()
        right_command = instruction.get_next_command()

        self.make_assertions(left_command)

        self.make_assertions(right_command)

    @staticmethod
    def get_piped_commands(instruction):
        piped_commands = []
        while instruction.has_next():
            piped_commands.append(instruction.get_next_command())
        return piped_commands

    def test_pipe(self):
        instructions = self.run_parser(
            "ls -a hello -b there mate < input.txt | cat file.txt"
        )

        self.assertEqual(len(instructions), 1)
        instruction = instructions[0]

        commands = self.get_piped_commands(instruction)

        left_command, right_command = commands[0], commands[1]

        assert len(commands) == 2
        self.make_assertions(
            left_command,
            args=["-a", "hello", "-b", "there", "mate"],
            redir=(["input.txt"], []),
        )

        self.make_assertions(right_command, name="cat", args=["file.txt"])

    def test_concat_two_commands(self):
        instructions = self.run_parser("ls ; cat")

        self.assertEqual(len(instructions), 2)
        ls = instructions[0].get_next_command()
        cat = instructions[1].get_next_command()

        self.make_assertions(ls)
        self.make_assertions(cat, name="cat")

    def test_quote_text_double_quote_arg(self):
        command = self.run_single_command('ls "hello"')

        self.make_assertions(command, args=["hello"])

    def test_quote_multiple_words(self):
        command = self.run_single_command('ls "hello there"')

        self.make_assertions(command, args=["hello there"])

    def test_quote_with_loads_of_whitespace(self):
        command = self.run_single_command("ls ' a '")

        self.make_assertions(command, args=[" a "])

    def test_quote_empty(self):
        command = self.run_single_command("ls ''")

        self.make_assertions(command, args=[""])

    def test_single_quote(self):
        command = self.run_single_command("ls 'a'")

        self.make_assertions(command, args=["a"])

    def test_command_substitution(self):
        command = self.run_single_command("echo `echo hello`")

        self.make_assertions(command, name="echo", args=["hello"])
