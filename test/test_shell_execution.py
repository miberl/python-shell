import sys
from io import StringIO

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
