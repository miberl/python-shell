import unittest
from syntax_highlighting.eval_apps import SyntaxHighlighter
from syntax_highlighting.eval_apps import ShellColours


class TestSyntaxhighlighting(unittest.TestCase):
    @staticmethod
    def run_test(command, expected_command):
        sh = SyntaxHighlighter()
        actual_command = sh._highlight_code(command)
        assert actual_command == expected_command

    def test_no_highlighting(self):
        self.run_test("test", "test")

    def test_app_highlighting(self):
        self.run_test("ls", ShellColours.APP + "ls" + ShellColours.ENDC)

    def test_directory_highlighting(self):
        self.run_test(
            "./",
            ShellColours.UNDERLINE + ShellColours.DIR + "./" + ShellColours.ENDC,
        )

    def test_flag_highlighting(self):
        self.run_test(
            "-l ",
            ShellColours.FLAG + "-l" + ShellColours.ENDC + " ",
        )

    def test_pipe_highlighting(self):
        self.run_test(
            "|",
            ShellColours.PIPE + "|" + ShellColours.ENDC,
        )

    def test_redir_in_highlighting(self):
        self.run_test(
            "<",
            ShellColours.REDIR_IN + "<" + ShellColours.ENDC,
        )

    def test_redir_out_highlighting(self):
        self.run_test(
            ">",
            ShellColours.REDIR_OUT + ">" + ShellColours.ENDC,
        )

    def test_multiple_highlighting(self):
        self.run_test(
            "ls -l | grep test",
            ShellColours.APP
            + "ls"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test",
        )

    def test_multiple_highlighting_with_directory(self):
        self.run_test(
            "./ -l | grep test",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test",
        )

    def test_multiple_highlighting_with_redir(self):
        self.run_test(
            "./ -l | grep test > test.txt",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test"
            + " "
            + ShellColours.REDIR_OUT
            + ">"
            + ShellColours.ENDC
            + " "
            + "test.txt",
        )

    def test_multiple_highlighting_with_redir_and_dir(self):
        self.run_test(
            "./ -l | grep test > ./test.txt",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test"
            + " "
            + ShellColours.REDIR_OUT
            + ">"
            + ShellColours.ENDC
            + " "
            + "./test.txt",
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test"
            + " "
            + ShellColours.REDIR_OUT
            + ">"
            + ShellColours.ENDC
            + " "
            + "./test.txt"
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC,
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag_and_app(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l ls",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test"
            + " "
            + ShellColours.REDIR_OUT
            + ">"
            + ShellColours.ENDC
            + " "
            + "./test.txt"
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "ls"
            + ShellColours.ENDC,
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag_and_app_and_pipe(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l ls | grep test",
            ShellColours.UNDERLINE
            + ShellColours.DIR
            + "./"
            + ShellColours.ENDC
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test"
            + " "
            + ShellColours.REDIR_OUT
            + ">"
            + ShellColours.ENDC
            + " "
            + "./test.txt"
            + " "
            + ShellColours.FLAG
            + "-l"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "ls"
            + ShellColours.ENDC
            + " "
            + ShellColours.PIPE
            + "|"
            + ShellColours.ENDC
            + " "
            + ShellColours.APP
            + "grep"
            + ShellColours.ENDC
            + " "
            + "test",
        )
