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
                      "instruction(command(app(atom())))")

    def test_command_single_arg(self):
        self.run_test("cmd hi",
                      "instruction(command(app(atom())arg(atom())))")

    def test_command_many_args(self):
        self.run_test("cmd one two three",
                      "instruction(command(app(atom())arg(atom())arg(atom())arg(atom())))")

    def test_command_whitespace_before(self):
        self.run_test("   cmd one",
                      "instruction(command(app(atom())arg(atom())))")

    def test_command_whitespace_everywhere(self):
        self.run_test("    cmd      ",
                      "instruction(command(app(atom())))")

    def test_globbed_arg(self):
        self.run_test("cmd *",
                      "instruction(command(app(atom())arg(atom(glob()))))")

    def test_globbed_between_text(self):
        self.run_test("cmd abc*def",
                      "instruction(command(app(atom())arg(atom(glob()))))")

    def test_can_glob_app(self):
        self.run_test("qwer*",
                      "instruction(command(app(atom(glob()))))")

    def test_use_backslash_in_app(self):
        self.run_test("l\\s",
                      "instruction(command(app(atom())))")

    def test_use_quote_in_app(self):
        self.run_test("\"ls\"",
                      "instruction(command(app(atom())))")

    def test_app_with_single_quote(self):
        self.run_test("'ls'",
                      "instruction(command(app(atom())))")

    def test_cannot_use_unrecognised_punctuation(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("l?", "")

    def test_ignore_whitespace_in_quotes(self):
        self.run_test("'l  s'",
                      "instruction(command(app(atom())))")

    def test_ignore_leading_whitespace_in_quotes(self):
        self.run_test("'  l  s  '",
                      "instruction(command(app(atom())))")

    def test_substitute_in_arguments(self):
        self.run_test("ls abc`def`ghi",
                      "instruction(command(app(atom())arg(atom("
                      "substituted(instruction(command(app(atom()))))))))")

    def test_multi_glob_in_app(self):
        self.run_test("*.*",
                      "instruction(command(app(atom(glob()glob()))))")

    def test_only_substitute(self):
        self.run_test("`ls`",
                      "instruction(command(app(atom("
                      "substituted(instruction(command(app(atom()))))))))")

    def test_cannot_glob_in_quote(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("'ls *'", "")

    def test_redir_in(self):
        self.run_test("cmd < file",
                      "instruction(command(app(atom())file_in(atom())))")

    def test_redir_out(self):
        self.run_test("cmd > file",
                      "instruction(command(app(atom())file_out(atom())))")

    def test_both_redir(self):
        self.run_test("cmd < file1 > file2",
                      "instruction(command(app(atom())file_in(atom())file_out(atom())))")

    def test_fails_if_redir_in_bad_order(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("cmd > file1 < file2", "")

    def test_fails_if_redir_not_last(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("cmd <file1 arg", "")

    def test_fails_if_redir_not_last_out(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("cmd > file2 arg", "")

    def test_whitespace_after_redir(self):
        self.run_test("cmd > file       ",
                      "instruction(command(app(atom())file_out(atom())))")

    def test_pipe_command(self):
        self.run_test("cmd1 | cmd2",
                      "instruction(command(app(atom()))"
                      "command(app(atom())))")

    def test_pipe_with_no_space(self):
        self.run_test("cmd1|cmd2",
                      "instruction(command(app(atom()))"
                      "command(app(atom())))")

    def test_pipe_many_command(self):
        self.run_test("cmd1 | cmd2 | cmd3",
                      "instruction(command(app(atom()))"
                      "command(app(atom()))"
                      "command(app(atom())))")

    def test_cannot_use_pipe_in_quotes(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("'cmd1 | cmd2'", "")

    def test_pipe_with_args(self):
        self.run_test("cmd1 bla | cmd2 bla",
                      "instruction(command(app(atom())arg(atom()))"
                      "command(app(atom())arg(atom())))")

    def test_append_commands(self):
        self.run_test("cmd1 ; cmd2",
                      "instruction(command(app(atom())))"
                      "instruction(command(app(atom())))")

    def test_cannot_use_semicolon_in_quotes(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("'cm;d'", "")

    def test_combine_without_space(self):
        self.run_test("cmd1;cmd2",
                      "instruction(command(app(atom())))"
                      "instruction(command(app(atom())))")

    def test_empty_errors(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test("", "")

    def test_single_flag(self):
        self.run_test("cmd -a",
                      "instruction(command(app(atom())arg(atom())))")

    def test_flag_with_arg(self):
        self.run_test("cmd -a arg",
                      "instruction(command(app(atom())arg(atom())arg(atom())))")

    def test_one_flag_many_arg(self):
        self.run_test("cmd -a one two three",
                      "instruction(command(app(atom())arg(atom())arg(atom())arg(atom())arg(atom())))")

    def test_two_flag_no_arg(self):
        self.run_test("cmd -a -b",
                      "instruction(command(app(atom())arg(atom())arg(atom())))")

    def test_can_use_double_dash(self):
        self.run_test("cmd --hello-there", "instruction(command(app(atom())arg(atom())))")
