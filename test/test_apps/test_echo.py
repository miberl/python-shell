import unittest

from shell import eval
from collections import deque


class TestCat(unittest.TestCase):
    def test_echo(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)

    def test_echo_no_args(self):
        out = deque()
        eval("echo", out)
        self.assertEqual(out.popleft(), "\n")
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()
