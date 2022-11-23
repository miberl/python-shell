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
    def fetch_directory_from_fs(self, dir_path):
        curr_dir = TestSetup.mock_fs

        file_directories = filter(lambda x: x not in ["", "."], dir_path.split("/"))
        for path in file_directories:
            curr_dir = curr_dir[path]
        return curr_dir

    @classmethod
    def fetch_file_from_fs(self, file_path):
        file_directories = file_path.split("/")
        file_name = file_directories.pop()
        file_directory_path = "/".join(file_directories)

        file_dir = self.fetch_directory_from_fs(file_directory_path)
        return file_dir[file_name]

    @classmethod
    def mock_os_walk(cls, top):
        exploreQueue = [cls.explore_dir(top)]

        while exploreQueue:
            path, dirs, files = exploreQueue.pop(0)
            yield (path, dirs, files)
            for dir in dirs:
                exploreQueue.append(cls.explore_dir(path + "/" + dir))

    @classmethod
    def explore_dir(cls, dir_path):
        directory = cls.fetch_directory_from_fs(dir_path)

        files, dirs = [], []
        for entry in directory.keys():
            if type(directory[entry]) is str:
                files.append(entry)
            else:
                dirs.append(entry)
        return dir_path, dirs, files

    def code_under_test(self, args):
        self.app.run(args, sys.stdin, self.out)

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
                self.code_under_test(args)
        else:
            self.code_under_test(args)

        self.assert_output(expected_output, unordered)

    # Runs a test, patches function with mock return value
    def run_test_patch_return(
        self, args, expected_output, ref_to_patch, patched_return, unordered=False
    ):
        with patch(ref_to_patch, return_value=patched_return):
            self.code_under_test(args)
        self.assert_output(expected_output, unordered)

    def assert_output(self, expected_output, unordered=False):
        if unordered:
            self.assertEqual(sorted(self.out), sorted(expected_output))
        else:
            self.assertEqual(self.out, expected_output)
