from unittest.mock import patch
from setup_test import TestSetup
from apps.ls import Ls


class TestLs(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.ls = Ls()

    # HAPPY PATHS

    def test_ls(self):
        with patch("apps.ls.listdir", return_value=["test.txt", "dir2", "dir1"]):
            self.ls.run([], self.out)
            self.assertEqual(set(self.out), {"test.txt\n", "dir2\n", "dir1\n"})

    def test_ls_with_hidden(self):
        with patch(
            "apps.ls.listdir", return_value=["test.txt", "dir2", "dir1", ".hidden"]
        ):
            self.ls.run([], self.out)
            self.assertEqual(set(self.out), {"test.txt\n", "dir2\n", "dir1\n"})

    def test_ls_directory(self):
        with patch(
            "apps.ls.listdir",
            return_value=["longfile.txt", "file1.txt", "file2.txt", "subdir"],
        ):
            self.ls.run(["dir1"], self.out)
            self.assertEqual(
                set(self.out),
                {"longfile.txt\n", "file2.txt\n", "file1.txt\n", "subdir\n"},
            )

    def test_ls_directory_with_hidden(self):
        with patch(
            "apps.ls.listdir",
            return_value=[
                "longfile.txt",
                "file1.txt",
                "file2.txt",
                "subdir",
                ".hidden",
            ],
        ):
            self.ls.run(["dir1"], self.out)
            self.assertEqual(
                set(self.out),
                {"longfile.txt\n", "file2.txt\n", "file1.txt\n", "subdir\n"},
            )

    def test_ls_subdirectory(self):
        with patch("apps.ls.listdir", return_value=["text.txt"]):
            self.ls.run(["dir1/subdir"], self.out)
            self.assertEqual(set(self.out), {"text.txt\n"})

    def test_ls_subdirectory_with_hidden(self):
        with patch("apps.ls.listdir", return_value=["text.txt", ".hidden"]):
            self.ls.run(["dir1/subdir"], self.out)
            self.assertEqual(set(self.out), {"text.txt\n"})
