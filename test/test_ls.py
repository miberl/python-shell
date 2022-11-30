from apps.ls import Ls
from exceptions.invalid_syntax_error import InvalidSyntaxError
from setup_test import TestSetup


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
            [], expected_output, "apps.ls.listdir", return_value, True
        )

    def test_ls_with_hidden(self):
        return_value = ["test.txt", "dir2", "dir1", ".hidden"]
        expected_output = ["test.txt\n", "dir2\n", "dir1\n"]
        self.run_test_patch_return(
            [], expected_output, "apps.ls.listdir", return_value, True
        )

    def test_ls_directory(self):
        return_value = ["longfile.txt", "file1.txt", "file2.txt", "subdir"]
        expected_output = ["longfile.txt\n", "file2.txt\n", "file1.txt\n", "subdir\n"]
        self.run_test_patch_return(
            ["dir1"], expected_output, "apps.ls.listdir", return_value, True
        )

    def test_ls_directory_with_hidden(self):
        return_value = ["longfile.txt", "file1.txt", "file2.txt", "subdir", ".hidden"]
        expected_output = ["longfile.txt\n", "file2.txt\n", "file1.txt\n", "subdir\n"]
        self.run_test_patch_return(
            ["dir1"], expected_output, "apps.ls.listdir", return_value, True
        )

    def test_ls_subdirectory(self):
        self.run_test_patch_return(
            ["dir1/subdir"],
            ["text.txt\n"],
            "apps.ls.listdir",
            ["text.txt"],
            unordered=True,
        )

    def test_ls_subdirectory_with_hidden(self):
        self.run_test_patch_return(
            ["dir1/subdir"],
            ["text.txt\n"],
            "apps.ls.listdir",
            ["text.txt", ".hidden"],
            unordered=True,
        )

    def test_ls_too_many_dirs(self):
        with self.assertRaises(InvalidSyntaxError) as err:
            self.run_test_patch_return(
                ["dir1", "hello"],
                ["text.txt\n"],
                "apps.ls.listdir",
                ["text.txt"],
                unordered=True,
            )
        error_message = "multiple arguments provided, expected 0 or 1"
        assert error_message in str(err.exception)
