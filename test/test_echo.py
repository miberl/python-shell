import sys
import unittest
from collections import deque
from apps.echo import Echo
from setup_test import TestSetup


class TestEcho(TestSetup):
    # HAPPY PATHS

    def setUp(self) -> None:
        super().setUp()
        self.out = deque()
        self.app = Echo()

    def test_echo_empty_args(self):
        self.app.run([""], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_no_args(self):
        self.app.run([], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_newline(self):
        self.app.run(["\n"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "\n\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_args(self):
        self.app.run(["foo"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_newline_args(self):
        self.app.run(["foo\n"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo\n\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_single_space_separated_args(self):
        self.app.run(["foo bar"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_single_doublespace_separated_args(self):
        self.app.run(["foo  bar"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo  bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_args(self):
        self.app.run(["foo", "bar"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo bar\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_space_separated_args(self):
        self.app.run(["foo bar", "bar foo"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo bar bar foo\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_doublespace_separated_args(self):
        self.app.run(["foo  bar", "bar  foo"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo  bar bar  foo\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_multiple_space_and_doublespace_separated_args(self):
        self.app.run(["foo bar", "bar  foo"], sys.stdin, self.out)
        self.assertEqual(self.out.popleft(), "foo bar bar  foo\n")
        self.assertEqual(len(self.out), 0)


if __name__ == "__main__":
    unittest.main()
