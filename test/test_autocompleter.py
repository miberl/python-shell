import unittest
from unittest import mock
from interactive_input.autocompleter import completer


class TestAutocompleter(unittest.TestCase):
    @staticmethod
    def run_test(code, expected_options, file_system, isDir_side_effect):
        with mock.patch("os.listdir") as mocked_listdir:
            with mock.patch("os.path.isdir") as mocked_isdir:
                with mock.patch("readline.get_line_buffer") as mocked_get_line_buffer:
                    mocked_listdir.return_value = file_system
                    mocked_get_line_buffer.return_value = code
                    mocked_isdir.return_value = isDir_side_effect
                    options = []
                    for i in range(len(expected_options)):
                        options.append(completer(None, i))
                    assert sorted(options) == sorted(expected_options)

    def test_complete_options(self):
        self.run_test(
            "",
            [
                "cat",
                "cd",
                "echo",
                "grep",
                "head",
                "ls",
                "pwd",
                "tail",
                "uniq",
                "cut",
                "sort",
                "find",
                "wc",
                "file1.txt",
                "file2.txt",
                "file3.txt",
            ],
            ["file1.txt", "file2.txt", "file3.txt"],
            False,
        )

    def test_complete_options_7(self):
        self.run_test(
            "f",
            ["find", "file1.txt", "file2.txt", "file3.txt"],
            ["file1.txt", "file2.txt", "file3.txt"],
            False,
        )

    def test_complete_options_6(self):
        self.run_test(
            "cd ./",
            ["dir1/", "dir2/", "dir3/"],
            ["dir1", "dir2", "dir3"],
            True,
        )

    def test_complete_options_5(self):
        self.run_test(
            "cd ./file2", ["file2.txt"], ["file1.txt", "file2.txt", "file3.txt"], False
        )

    def test_complete_options_4(self):
        self.run_test(
            "cd ",
            [
                "cat",
                "cd",
                "echo",
                "grep",
                "head",
                "ls",
                "pwd",
                "tail",
                "uniq",
                "cut",
                "sort",
                "find",
            ],
            [],
            False,
        )

    def test_complete_options_3(self):
        self.run_test(
            "cd ./dir1/f",
            ["file1.txt", "file2.txt", "file3.txt", "find"],
            ["file1.txt", "file2.txt", "file3.txt"],
            False,
        )

    def test_complete_options_2(self):
        self.run_test(
            "cd ",
            [
                "dir1/",
                "cat",
                "cd",
                "echo",
                "grep",
                "head",
                "ls",
                "pwd",
                "tail",
                "uniq",
                "cut",
                "sort",
                "find",
                "wc",
            ],
            ["dir1"],
            True,
        )

    def test_complete_options_1(self):
        self.run_test(
            "cd dir",
            [
                "dir/",
            ],
            ["dir"],
            True,
        )
