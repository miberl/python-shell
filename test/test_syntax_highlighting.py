import unittest
from syntax_highlighting.syntaxhighlighter import SyntaxHighlighter
from syntax_highlighting.syntaxhighlighter import shell_colours


class TestSyntaxhighlighting(unittest.TestCase):
    def run_test(self, command, expected_command):
        sh = SyntaxHighlighter()
        actual_command = sh.highlight_code(command)
        assert actual_command == expected_command

    def test_no_highlighting(self):
        self.run_test("test", "test")

    def test_app_highlighting(self):
        self.run_test("ls", shell_colours.APP + "ls" + shell_colours.ENDC)

    def test_directory_highlighting(self):
        self.run_test(
            "./",
            shell_colours.UNDERLINE + shell_colours.DIR + "./" + shell_colours.ENDC,
        )

    def test_flag_highlighting(self):
        self.run_test(
            "-l ",
            shell_colours.FLAG + "-l" + shell_colours.ENDC + " ",
        )

    def test_pipe_highlighting(self):
        self.run_test(
            "|",
            shell_colours.PIPE + "|" + shell_colours.ENDC,
        )

    def test_redir_in_highlighting(self):
        self.run_test(
            "<",
            shell_colours.REDIR_IN + "<" + shell_colours.ENDC,
        )

    def test_redir_out_highlighting(self):
        self.run_test(
            ">",
            shell_colours.REDIR_OUT + ">" + shell_colours.ENDC,
        )

    def test_multiple_highlighting(self):
        self.run_test(
            "ls -l | grep test",
            shell_colours.APP
            + "ls"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test",
        )

    def test_multiple_highlighting_with_directory(self):
        self.run_test(
            "./ -l | grep test",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test",
        )

    def test_multiple_highlighting_with_redir(self):
        self.run_test(
            "./ -l | grep test > test.txt",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test"
            + " "
            + shell_colours.REDIR_OUT
            + ">"
            + shell_colours.ENDC
            + " "
            + "test.txt",
        )

    def test_multiple_highlighting_with_redir_and_dir(self):
        self.run_test(
            "./ -l | grep test > ./test.txt",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test"
            + " "
            + shell_colours.REDIR_OUT
            + ">"
            + shell_colours.ENDC
            + " "
            + "./test.txt",
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test"
            + " "
            + shell_colours.REDIR_OUT
            + ">"
            + shell_colours.ENDC
            + " "
            + "./test.txt"
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC,
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag_and_app(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l ls",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test"
            + " "
            + shell_colours.REDIR_OUT
            + ">"
            + shell_colours.ENDC
            + " "
            + "./test.txt"
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "ls"
            + shell_colours.ENDC,
        )

    def test_multiple_highlighting_with_redir_and_dir_and_flag_and_app_and_pipe(self):
        self.run_test(
            "./ -l | grep test > ./test.txt -l ls | grep test",
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + "./"
            + shell_colours.ENDC
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test"
            + " "
            + shell_colours.REDIR_OUT
            + ">"
            + shell_colours.ENDC
            + " "
            + "./test.txt"
            + " "
            + shell_colours.FLAG
            + "-l"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "ls"
            + shell_colours.ENDC
            + " "
            + shell_colours.PIPE
            + "|"
            + shell_colours.ENDC
            + " "
            + shell_colours.APP
            + "grep"
            + shell_colours.ENDC
            + " "
            + "test",
        )
