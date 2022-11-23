import sys
from io import StringIO

from exceptions.invalid_syntax_error import InvalidSyntaxError
from setup_test import TestSetup
from apps.uniq import Uniq


class TestUniq(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Uniq()

    def run_test(self, args, expected_output):
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    def test_uniq(self):
        self.run_test(
            ["test.txt"],
            ["''\n"]
        )

    def test_uniq_2(self):
        self.run_test(
            ["dir1/file1.txt"],
            ["AAA\n", "BBB\n", "AAA\n"]
        )

    def test_uniq_3(self):
        self.run_test(
            ["dir1/file2.txt"],
            ["CCC\n"]
        )
    

    def test_uniq_repeated(self):
        self.run_test(
            ["dir1/file3.txt"],
            ["AAA\n", "BBB\n", "CCC\n"]
        )

    def test_uniq_repeated_2(self):
        self.run_test(
            ["dir1/file4.txt"],
            ["AAA\n"]
        )

    def test_uniq_ignore_case(self):
        self.run_test(
            ["-i", "dir2/subdir/file.txt"],
            ["AAA\n"]
        )

    def test_too_many_args(self):
        with self.assertRaises(InvalidSyntaxError) as err:
            self.run_test(['hello', 'there', 'sir'], [])

        assert 'multiple arguments provided, expected 1' in str(err.exception)

    def test_no_args_fine(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("AAA\nBBB\nAAA\n")

        self.run_test([], ['AAA\n', 'BBB\n', 'AAA\n'])

        sys.stdin = original_stdin
