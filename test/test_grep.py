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
        self.grep = Grep()

    # HAPPY PATHS

    def test_grep(self):
        with patch("apps.grep.Grep.read_lines", side_effect=TestSetup.mock_read_lines):
            self.grep.run(["Test", "test.txt"], self.out)
            self.assertEqual(self.out, ["Test\n"])

    def test_grep_multiple_files(self):
        with patch("apps.grep.Grep.read_lines", side_effect=TestSetup.mock_read_lines):
            self.grep.run(["AAA", "dir1/file1.txt",
                          "dir1/file2.txt"], self.out)
            self.assertEqual(
                self.out, ["dir1/file1.txt:AAA\n", "dir1/file1.txt:AAA\n"])

    def test_no_match(self):
        with patch("apps.grep.Grep.read_lines", side_effect=TestSetup.mock_read_lines):
            self.grep.run(["DDD", "dir1/file1.txt",
                          "dir1/file2.txt"], self.out)
            self.assertEqual(
                self.out, [])

    def test_long_file(self):
        with patch("apps.grep.Grep.read_lines", side_effect=TestSetup.mock_read_lines):
            self.grep.run(["10", "dir1/longfile.txt"], self.out)
            self.assertEqual(
                self.out, ["10\n"])
