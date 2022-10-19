from unittest.mock import patch
from setup_test import TestSetup
from apps.ls import Ls


class TestLs(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Ls()

    # HAPPY PATHS

    def test_ls(self):
        return_value = ["test.txt", "dir2", "dir1"]
        expected_output = ["test.txt\n", "dir2\n", "dir1\n"]
        self.run_test_patch_return(
            [], expected_output, "apps.ls.listdir", return_value, unordered=True)

    def test_ls_with_hidden(self):
        return_value = ["test.txt", "dir2", "dir1", ".hidden"]
        expected_output = ["test.txt\n", "dir2\n", "dir1\n"]
        self.run_test_patch_return(
            [], expected_output, "apps.ls.listdir", return_value, unordered=True)

    def test_ls_directory(self):
        return_value = ["longfile.txt", "file1.txt", "file2.txt", "subdir"]
        expected_output = ["longfile.txt\n",
                           "file2.txt\n", "file1.txt\n", "subdir\n"]
        self.run_test_patch_return(
            ["dir1"], expected_output, "apps.ls.listdir",  return_value, unordered=True)

    def test_ls_directory_with_hidden(self):
        return_value = ["longfile.txt", "file1.txt",
                        "file2.txt", "subdir", ".hidden"]
        expected_output = ["longfile.txt\n",
                           "file2.txt\n", "file1.txt\n", "subdir\n"]
        self.run_test_patch_return(
            ["dir1"], expected_output, "apps.ls.listdir", return_value, unordered=True)

    def test_ls_subdirectory(self):
        self.run_test_patch_return(
            ["dir1/subdir"], ["text.txt\n"], "apps.ls.listdir", ["text.txt"], unordered=True)

    def test_ls_subdirectory_with_hidden(self):
        self.run_test_patch_return(["dir1/subdir"], ["text.txt\n"],
                                   "apps.ls.listdir", ["text.txt", ".hidden"], unordered=True)
