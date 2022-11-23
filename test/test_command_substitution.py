import unittest

from shell_runner.shell_exec import ShellExec


class TestCommandSubstitution(unittest.TestCase):
    def run_test(self, cmdline, app, args):
        instrs = ShellExec()._get_instructions_object_from_string(cmdline)
        instr = instrs[0]
        cmd = instr.get_next_command()
        assert cmd.get_app() == app
        assert cmd.get_args() == args

    def test_substituted_arg(self):
        self.run_test('echo `echo hello`', 'echo', ['hello'])

    def test_substituted_command(self):
        self.run_test('`echo echo`', 'echo', [])

    def test_substitution_with_many_outputs(self):
        self.run_test('`echo echo 123`', 'echo 123', [])

    def test_substitution_with_preceding(self):
        self.run_test('ec`echo ho`', 'echo', [])

    def test_substitution_with_before_and_after(self):
        self.run_test('e`echo ch`o', 'echo', [])

    def test_bad_substitution(self):
        with self.assertRaises(ValueError) as err:
            self.run_test('`nonsense`', 'echo', [])

        assert 'unsupported application nonsense' in str(err.exception)

