import unittest

from setup_test import TestSetup
from collections import deque
from apps.echo import Echo


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.echo = Echo()

    def test_echo_empty_args(self):
        self.echo.run([""], self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_no_args(self):
        self.echo.run([], self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_newline(self):
        self.echo.run(["\n"], self.out)
        self.assertEqual(self.out.popleft(), "\n\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_args(self):
        self.echo.run(["foo"], self.out)
        self.assertEqual(self.out.popleft(), "foo\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_newline_args(self):
        self.echo.run(["foo\n"], self.out)
        self.assertEqual(self.out.popleft(), "foo\n\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_single_space_separated_args(self):
        self.echo.run(["foo bar"], self.out)
        self.assertEqual(self.out.popleft(), "foo bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_single_doublespace_separated_args(self):
        self.echo.run(["foo  bar"], self.out)
        self.assertEqual(self.out.popleft(), "foo  bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_args(self):
        self.echo.run(["foo", "bar"], self.out)
        self.assertEqual(self.out.popleft(), "foo bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_space_separated_args(self):
        self.echo.run(["foo bar", "bar foo"], self.out)
        self.assertEqual(self.out.popleft(), "foo bar bar foo\n")
        self.assertEqual(len(self.out), 0)


if __name__ == "__main__":
    unittest.main()
