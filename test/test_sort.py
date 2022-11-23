import sys
from io import StringIO

from setup_test import TestSetup
from apps.sort import Sort


class TestSort(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Sort()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(args, expected_output,
                         "application.Application.read_lines",
                         TestSetup.mock_read_lines)

    # HAPPY PATHS
    def test_sort(self):
        self.run_test(["test.txt"], ["''\n"])

    def test_sort_2(self):
        self.run_test(["dir1/file1.txt"], ["AAA\n", "AAA\n", "BBB\n"])

    def test_sort_multiple_args(self):
        self.run_test(["test.txt", "dir1/file1.txt"],
                      ["''\n", "AAA\n", "AAA\n", "BBB\n"])

    def test_sort_reverse(self):
        self.run_test(["-r", "test.txt"], ["''\n"])

    def test_sort_2_reverse(self):
        self.run_test(["-r", "dir1/file1.txt"], ["BBB\n", "AAA\n", "AAA\n"])

    def test_sort_no_args(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("AAA\nBBB\nAAA\n")

        self.run_test([], ["AAA\n", "AAA\n", "BBB\n"])

        sys.stdin = original_stdin
