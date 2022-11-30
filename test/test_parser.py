import unittest

from exceptions.invalid_syntax_error import InvalidSyntaxError
from inputparser.parse_command import ParseCommands
from CustomParserListener import CustomParserListener


class TestParser(unittest.TestCase):
    def run_test(self, cmd, expected_structure):
        listener = CustomParserListener()
        ParseCommands().parse_listen(cmd, listener)
        actual = ''.join(listener.out)
        self.assertEqual(expected_structure, actual)

    def test_single_command(self):
        self.run_test("cmd",
                      "instruction(command(arg(atom())))")

    def test_command_single_arg(self):
        self.run_test("cmd hi",
                      "instruction(command(arg(atom())arg(atom())))")

    def test_command_many_args(self):
        self.run_test("cmd one two three",
                      "instruction(command(arg(atom())arg(atom())"
                      "arg(atom())arg(atom())))")

    def test_command_whitespace_before(self):
        self.run_test("   cmd one",
                      "instruction(command(arg(atom())arg(atom())))")

    def test_command_whitespace_everywhere(self):
        self.run_test("    cmd      ",
                      "instruction(command(arg(atom())))")

    def test_globbed_arg(self):
        self.run_test("cmd *",
                      "instruction(command(arg(atom())arg(atom(glob()))))")

    def test_globbed_between_text(self):
        self.run_test("cmd abc*def",
                      "instruction(command(arg(atom())arg(atom(glob()))))")

    def test_can_glob_app(self):
        self.run_test("qwer*",
                      "instruction(command(arg(atom(glob()))))")

    def test_use_backslash_in_app(self):
        self.run_test("l\\s",
                      "instruction(command(arg(atom())))")

    def test_use_quote_in_app(self):
        self.run_test("\"ls\"",
                      "instruction(command(arg(atom())))")

    def test_app_with_single_quote(self):
        self.run_test("'ls'",
                      "instruction(command(arg(atom())))")

    def test_cannot_use_unrecognised_punctuation(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("l?", "")

    def test_ignore_whitespace_in_quotes(self):
        self.run_test("'l  s'",
                      "instruction(command(arg(atom())))")

    def test_ignore_leading_whitespace_in_quotes(self):
        self.run_test("'  l  s  '",
                      "instruction(command(arg(atom())))")

    def test_substitute_in_arguments(self):
        self.run_test("ls abc`def`ghi",
                      "instruction(command(arg(atom())arg(atom("
                      "substituted(instruction(command(arg(atom()))))))))")

    def test_multi_glob_in_app(self):
        self.run_test("*.*",
                      "instruction(command(arg(atom(glob()glob()))))")

    def test_only_substitute(self):
        self.run_test("`ls`",
                      "instruction(command(arg(atom("
                      "substituted(instruction(command(arg(atom()))))))))")

    def test_can_use_asterisk_in_quotes(self):
        self.run_test("'ls *'", "instruction(command(arg(atom())))")

    def test_redir_in(self):
        self.run_test("cmd < file",
                      "instruction(command(arg(atom())file_in(atom())))")

    def test_redir_out(self):
        self.run_test("cmd > file",
                      "instruction(command(arg(atom())file_out(atom())))")

    def test_both_redir(self):
        self.run_test("cmd < file1 > file2",
                      "instruction(command(arg(atom())file_in(atom())"
                      "file_out(atom())))")

    def test_whitespace_after_redir(self):
        self.run_test("cmd > file       ",
                      "instruction(command(arg(atom())file_out(atom())))")

    def test_pipe_command(self):
        self.run_test("cmd1 | cmd2",
                      "instruction(command(arg(atom()))"
                      "command(arg(atom())))")

    def test_pipe_with_no_space(self):
        self.run_test("cmd1|cmd2",
                      "instruction(command(arg(atom()))"
                      "command(arg(atom())))")

    def test_pipe_many_command(self):
        self.run_test("cmd1 | cmd2 | cmd3",
                      "instruction(command(arg(atom()))"
                      "command(arg(atom()))"
                      "command(arg(atom())))")

    def test_can_use_pipe_in_quotes(self):
        self.run_test("'cmd1 | cmd2'", "instruction(command(arg(atom())))")

    def test_pipe_with_args(self):
        self.run_test("cmd1 bla | cmd2 bla",
                      "instruction(command(arg(atom())arg(atom()))"
                      "command(arg(atom())arg(atom())))")

    def test_append_commands(self):
        self.run_test("cmd1 ; cmd2",
                      "instruction(command(arg(atom())))"
                      "instruction(command(arg(atom())))")

    def test_can_use_punctuation_in_quotes(self):
        self.run_test("'cm;d'", "instruction(command(arg(atom())))")

    def test_combine_without_space(self):
        self.run_test("cmd1;cmd2",
                      "instruction(command(arg(atom())))"
                      "instruction(command(arg(atom())))")

    def test_empty_ok(self):
        self.run_test("", "")

    def test_empty_with_space_ok(self):
        self.run_test("  ", "")

    def test_empty_with_newline_ok(self):
        self.run_test("\n", "")

    def test_single_flag(self):
        self.run_test("cmd -a",
                      "instruction(command(arg(atom())arg(atom())))")

    def test_flag_with_arg(self):
        self.run_test("cmd -a arg",
                      "instruction(command(arg(atom())arg(atom())arg(atom())))")

    def test_one_flag_many_arg(self):
        self.run_test(
                      "cmd -a one two three",
                      "instruction(command(arg(atom())arg(atom())arg(atom())arg"
                      "(atom())arg(atom())))")

    def test_two_flag_no_arg(self):
        self.run_test("cmd -a -b",
                      "instruction(command(arg(atom())arg(atom())arg(atom())))")

    def test_can_use_double_dash(self):
        self.run_test("cmd --hello-there", "instruction(command(arg(atom())arg"
                                           "(atom())))")

    def test_redir_at_front(self):
        self.run_test("< file.txt cmd", "instruction(command(file_in(atom())arg"
                                        "(atom())))")

    def test_many_redir(self):
        self.run_test("cmd < file1 < file2", "instruction(command(arg(atom())"
                                             "file_in(atom())file_in(atom())))")

    def test_redir_between_args(self):
        self.run_test("cmd < file1 arg < file2 arg",
                      "instruction(command(arg(atom())file_in(atom())"
                      "arg(atom())file_in(atom())arg(atom())))")
