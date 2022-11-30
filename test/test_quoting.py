import unittest

from shell_runner.shell_exec import ShellExec


class TestQuoting(unittest.TestCase):
    @staticmethod
    def run_test(cmdline, app, args):
        instrs = ShellExec()._get_instructions_object_from_string(cmdline)
        instr = instrs[0]
        cmd = instr.get_next_command()
        assert cmd.get_app() == app
        assert cmd.get_args() == args

    def test_single_quote_arg(self):
        self.run_test("echo 'hello'", "echo", ["hello"])

    def test_double_quote_arg(self):
        self.run_test('echo "hello"', "echo", ["hello"])

    def test_quote_app(self):
        self.run_test('"echo"', "echo", [])

    def test_quote_with_quote_inside(self):
        self.run_test("\"echo''\"", "echo''", [])

    def test_quote_with_before(self):
        self.run_test('ec"ho"', "echo", [])

    def test_quote_with_asterisk(self):
        self.run_test('"ec*ho"', "ec*ho", [])

    def test_quote_with_command_substitution(self):
        self.run_test('echo "echo `echo hello`"', "echo", ["echo hello"])
