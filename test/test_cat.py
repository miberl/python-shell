from unittest.mock import patch
from setup_test import TestSetup
from apps.cat import Cat


class TestCat(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.cat = Cat()

    # HAPPY PATHS
    def test_cat(self):
        with patch("apps.cat.Cat.read_file", side_effect=TestSetup.mock_read_file):
            self.cat.run(["test.txt"], self.out)
            self.assertEqual(self.out, ["Test\n"])

    def test_cat_two_args(self):
        with patch("apps.cat.Cat.read_file", side_effect=TestSetup.mock_read_file):
            self.cat.run(["dir1/file1.txt", "dir1/file2.txt"], self.out)
            self.assertEqual(self.out, ["AAA\nBBB\nAAA\n", "CCC\n"])

    def test_cat_three_args(self):
        with patch("apps.cat.Cat.read_file", side_effect=TestSetup.mock_read_file):
            self.cat.run(["test.txt", "dir1/file1.txt",
                         "dir1/file2.txt"], self.out)
            self.assertEqual(self.out, ["Test\n", "AAA\nBBB\nAAA\n", "CCC\n"])

    def test_hidden(self):
        with patch("apps.cat.Cat.read_file", side_effect=TestSetup.mock_read_file):
            self.cat.run(["dir1/subdir/.hidden"], self.out)
            self.assertEqual(self.out, ["secret\n"])

    def test_hidden_2(self):
        with patch("apps.cat.Cat.read_file", side_effect=TestSetup.mock_read_file):
            self.cat.run(["dir1/subdir/.hidden", "dir1/file1.txt"], self.out)
            self.assertEqual(self.out, ["secret\n", "AAA\nBBB\nAAA\n"])
