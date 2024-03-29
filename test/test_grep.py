import sys
from io import StringIO
from setup_test import TestSetup
from apps.grep import Grep
from exceptions.invalid_syntax_error import InvalidSyntaxError


class TestGrep(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Grep()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(
            args,
            expected_output,
            "application.Application.read_lines",
            TestSetup.mock_read_lines,
        )

    # HAPPY PATHS

    def test_grep(self):
        self.run_test(["'", "test.txt"], ["''\n"])

    def test_grep_multiple_files(self):
        args = ["AAA", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["dir1/file1.txt:AAA\n", "dir1/file1.txt:AAA\n"]
        self.run_test(args, expected_output)

    def test_long_file(self):
        self.run_test(["10", "dir1/longfile.txt"], ["10\n"])

    def test_hidden_file(self):
        self.run_test(["secret", "dir2/subdir/.hidden"], ["secret\n"])

    def test_partial_match(self):
        self.run_test(["AA", "dir1/file1.txt"], ["AAA\n", "AAA\n"])

    def test_partial_match_multiple_files(self):
        args = ["AA", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["dir1/file1.txt:AAA\n", "dir1/file1.txt:AAA\n"]
        self.run_test(args, expected_output)

    def test_no_match(self):
        args = ["DDD", "dir1/file1.txt", "dir1/file2.txt"]
        self.run_test(args, [])

    def test_no_args(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test([], None)

    def test_stdin(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("AAA\nBBB\nAAA\n")

        self.run_test(["AAA"], ["AAA\n", "AAA\n"])
        sys.stdin = original_stdin
