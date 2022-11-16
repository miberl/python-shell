import sys
import unittest
from unittest.mock import patch


class TestSetup(unittest.TestCase):
    SHELL_IMAGE = "comp0010-test"
    TEST_VOLUME = "comp0010-test-volume"
    TEST_IMAGE = "comp0010-test-image"
    TEST_DIR = "/test"

    # This is a mock of the filesystem
    mock_fs = {
        "test.txt": "''\n",
        "dir1": {
            "file1.txt": "AAA\nBBB\nAAA\n",
            "file2.txt": "CCC\n",
            "cutTest.txt": "Andhra Pradesh\nArunachal Pradesh\nAssam\nBihar\nChhattisgarh\n",
            "file3.txt": "AAA\nAAA\nBBB\nCCC\nCCC\nCCC\n",
            "file4.txt": "AAA\nAAA\n",
            "longfile.txt": "\n".join([str(i) for i in range(1, 21)]) + "\n",
        },
        "dir2": {
            "subdir": {
                "file.txt": "AAA\naaa\nAAA\n",
                "normal": "secret\n",
                ".hidden": "secret\n",
            },
        },
    }

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.out = None
        self.app = None

    @classmethod
    def mock_read_file(self, file_path):
        return TestSetup.fetch_file_from_fs(file_path)

    @classmethod
    def mock_read_lines(self, file_path):
        lines = TestSetup.fetch_file_from_fs(file_path).strip().split("\n")
        return [f"{line}\n" for line in lines]

    @classmethod
    def fetch_file_from_fs(self, file_path):
        curr_dir = TestSetup.mock_fs

        file_directories = file_path.split("/")
        file_name = file_directories.pop()
        for path in file_directories:
            curr_dir = curr_dir[path]

        return curr_dir[file_name]

    # Runs a test, patches function with mock function if supplied
    def run_test(
        self,
        args,
        expected_output,
        ref_to_patch=None,
        patched_func=None,
        unordered=False,
    ):
        if ref_to_patch and patched_func:
            with patch(ref_to_patch, side_effect=patched_func):
                self.app.run(args, sys.stdin, self.out)
        else:
            self.app.run(args, self.out)
        if unordered:
            self.assertEqual(set(self.out), set(expected_output))
        else:
            self.assertEqual(self.out, expected_output)

    # Runs a test, patches function with mock return value
    def run_test_patch_return(
        self, args, expected_output, ref_to_patch, patched_return, unordered=False
    ):
        with patch(ref_to_patch, return_value=patched_return):
            self.app.run(args, sys.stdin, self.out)
        if unordered:
            self.assertEqual(sorted(self.out), sorted(expected_output))
        else:
            self.assertEqual(self.out, expected_output)
