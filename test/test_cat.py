from unittest.mock import patch
from setup_test import TestSetup
from apps.cat import Cat


class TestCat(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cat()

    # HAPPY PATHS
    def test_cat(self):
        self.run_test(["test.txt"], ["Test\n"],
                      "apps.cat.Cat.read_file", TestSetup.mock_read_file)

    def test_cat_two_args(self):
        args = ["dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["AAA\nBBB\nAAA\n", "CCC\n"]
        self.run_test(args, expected_output,
                      "apps.cat.Cat.read_file", TestSetup.mock_read_file)

    def test_cat_three_args(self):
        args = ["test.txt", "dir1/file1.txt", "dir1/file2.txt"]
        expected_output = ["Test\n", "AAA\nBBB\nAAA\n", "CCC\n"]
        self.run_test(args, expected_output,
                      "apps.cat.Cat.read_file", TestSetup.mock_read_file)

    def test_hidden(self):
        self.run_test(["dir1/subdir/.hidden"], ["secret\n"],
                      "apps.cat.Cat.read_file", TestSetup.mock_read_file)

    def test_hidden_2(self):
        args = ["dir1/subdir/.hidden", "dir1/file1.txt"]
        expected_output = ["secret\n", "AAA\nBBB\nAAA\n"]
        self.run_test(args, expected_output,
                      "apps.cat.Cat.read_file", TestSetup.mock_read_file)
