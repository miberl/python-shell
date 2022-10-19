import unittest


class TestSetup(unittest.TestCase):
    SHELL_IMAGE = "comp0010-test"
    TEST_VOLUME = "comp0010-test-volume"
    TEST_IMAGE = "comp0010-test-image"
    TEST_DIR = "/test"

    # This is a mock of the filesystem
    mock_fs = {
        "test.txt": "Test\n",
        "dir1": {
            "subdir": {
                ".hidden": "secret\n",
                "normal": "secret\n",
            },
            "file1.txt": "AAA\nBBB\nAAA\n",
            "file2.txt": "CCC\n",
            "longfile.txt": "\n".join([str(i) for i in range(1, 21)]) + "\n",
        },
        "dir2": {
            "subdir": {
                "file.txt": "AAA\naaa\nAAA\n",
            },
        },
    }

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
