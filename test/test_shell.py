import unittest

from setup_test import TestSetup
from shell import Shell


# This is fast approaching integration tests, but required to test some sections of code that are not run otherwise
class TestShell(TestSetup):
    def code_under_test(self, args):
        self.out = list(Shell()._eval(args))

    def test_shell(self):
        self.run_test('echo foo', ['foo\n'])

    def test_globbing(self):
        self.run_test('echo *', ['dir1 dir2 test.txt\n'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_dir_globbing(self):
        self.run_test('echo dir1/*', ['dir1/cutTest.txt dir1/file1.txt dir1/file2.txt dir1/file3.txt dir1/file4.txt '
                                      'dir1/longfile.txt\n'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_quoted_name(self):
        self.run_test('"echo"', ['\n'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)


if __name__ == "__main__":
    unittest.main()
