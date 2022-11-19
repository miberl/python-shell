from setup_test import TestSetup
from apps.cat import Cat


class TestCat(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cat()

    def run_test(self, args, expected_output):
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    # HAPPY PATHS
    def test_cat(self):
        self.run_test(["test.txt"], ["''\n"])

    def test_cat_two_args(self):
        args = ["dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["AAA\n", "BBB\n", "AAA\n", "CCC\n"]
        self.run_test(args, expected_output)

    def test_cat_three_args(self):
        args = ["test.txt", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["''\n", "AAA\n", "BBB\n", "AAA\n", "CCC\n"]
        self.run_test(args, expected_output)

    def test_hidden(self):
        self.run_test(["dir2/subdir/.hidden"], ["secret\n"])

    def test_hidden_2(self):
        args = ["dir2/subdir/.hidden", "dir1/file1.txt"]
        expected_output = ["secret\n", "AAA\n","BBB\n","AAA\n"]
        self.run_test(args, expected_output)
