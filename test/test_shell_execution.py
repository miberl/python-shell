import sys

import shell
from setup_test import TestSetup
from shell import Shell


class TestShell(TestSetup):
    TestSetup.stdout_mock = None

    def code_under_test(self, args):
        Shell().main([''] + args)
        self.out = TestSetup.stdout_mock

    def test_can_execute_from_args(self):
        self.run_test(['-c', 'echo foo'], ['foo\n'],
                      'shell.Shell._display', TestSetup.mock_display)

    def test_too_few_args(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['a'], [])

        assert str(err.exception) == 'wrong number of command line arguments'

    def test_many_arguments(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['a', 'b', 'c'], [])

        assert str(err.exception) == 'wrong number of command line arguments'

    def test_first_argument_not_c(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['c', 'hello'], [])

        assert str(err.exception) == 'unexpected command line argument c'


class TestShellMainMethod(TestSetup):
    def code_under_test(self, args):
        shell.main()
        self.out = TestSetup.stdout_mock

    def run_test(self, args, expected, **kwargs):
        super().run_test(args, expected,
                         'shell.Shell._display', TestSetup.mock_display)

    def test_use_main_method(self):
        old_args = sys.argv
        sys.argv = ['shell', '-c', 'echo hello']

        self.run_test(None, ['hello\n'])

        sys.argv = old_args

    def test_run_empty_ok(self):
        old_args = sys.argv
        sys.argv = ['shell', '-c', '']

        self.run_test(None, [])

        sys.argv = old_args
