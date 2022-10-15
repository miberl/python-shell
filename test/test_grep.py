from unittest.mock import patch
from setup_test import TestSetup
from apps.grep import Grep


def mock_read_file(filename):
    return {
        "dir1/dirfile.txt": "dirfile",
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
        self.cat = Grep()

    # # HAPPY PATHS
    # def test_grep(self):
    #     with patch("apps.cat.Grep.read_file", side_effect=mock_read_file):
    #         self.cat.run(["file1.txt"], self.out)
    #         self.assertEqual(self.out, ["file1"])
