from unittest.mock import patch
from setup_test import TestSetup
from apps.grep import Grep


def mock_read_lines(filename):
    return {
        "dir1/dirfile.txt": ["AAA\n", "BBB\n", "CCC\n"],
        "dir1/subdir/subdirfile.txt": "subdirfile",
        "file1.txt": "file1",
        "file2.txt": "file2",
        "file3.txt": "file3",
        ".hidden": "hidden",
    }.get(filename)


class TestGrep(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Grep()

    def run_test(self, args, expected_output):
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    # HAPPY PATHS

    def test_grep(self):
        self.run_test(["Test", "test.txt"], ["Test\n"])

    def test_grep_multiple_files(self):
        args = ["AAA", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["dir1/file1.txt:AAA\n", "dir1/file1.txt:AAA\n"]
        self.run_test(args, expected_output)

    def test_long_file(self):
        self.run_test(["10", "dir1/longfile.txt"], ["10\n"])

    def test_hidden_file(self):
        self.run_test(["secret", "dir1/subdir/.hidden"], ["secret\n"])

    def test_partial_match(self):
        self.run_test(["AA", "dir1/file1.txt"], ["AAA\n", "AAA\n"])

    def test_partial_match_multiple_files(self):
        args = ["AA", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["dir1/file1.txt:AAA\n", "dir1/file1.txt:AAA\n"]
        self.run_test(args, expected_output)

    def test_no_match(self):
        args = ["DDD", "dir1/file1.txt", "dir1/file2.txt"]
        self.run_test(args, [])
