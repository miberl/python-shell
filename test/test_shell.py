import unittest

from shell import Shell
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        shell = Shell()
        out = shell.eval("echo foo")
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)
