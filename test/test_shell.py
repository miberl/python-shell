import unittest

from shell import Shell
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        shell = Shell()
        out = deque()
        shell.eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
