from unittest.mock import patch
from setup_test import TestSetup
from apps.cat import Cat


def mock_read_file(filename):
    return {
        "dir1/dirfile.txt": "dirfile",
        "dir1/subdir/subdirfile.txt": "subdirfile",
        "file1.txt": "file1",
        "file2.txt": "file2",
        "file3.txt": "file3",
        ".hidden": "hidden",
    }.get(filename)


class TestCat(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.cat = Cat()

    # HAPPY PATHS
    def test_cat(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run(["file1.txt"], self.out)
            self.assertEqual(self.out, ["file1"])

    def test_cat_two_args(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run(["file1.txt", "file2.txt"], self.out)
            self.assertEqual(self.out, ["file1", "file2"])

    def test_cat_three_args(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run(["file1.txt", "file2.txt", "file3.txt"], self.out)
            self.assertEqual(self.out, ["file1", "file2", "file3"])

    def test_cat_directory(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run(["dir1/dirfile.txt"], self.out)
            self.assertEqual(self.out, ["dirfile"])

    def test_cat_subdir(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run(["dir1/subdir/subdirfile.txt"], self.out)
            self.assertEqual(self.out, ["subdirfile"])

    def test_cat_hidden(self):
        with patch("apps.cat.Cat.read_file", side_effect=mock_read_file):
            self.cat.run([".hidden"], self.out)
            self.assertEqual(self.out, ["hidden"])
