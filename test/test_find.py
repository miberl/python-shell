from setup_test import TestSetup
from apps.find import Find


class TestFind(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Find()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(
            args,
            expected_output,
            "apps.find.os.walk",
            TestSetup.mock_os_walk,
            unordered=True,
        )

    # HAPPY PATHS

    def test_find_with_name_base_directory(self):
        self.run_test([".", "-name", "file1.txt"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern_base_directory(self):
        self.run_test([".", "-name", "*1*"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern_multiple_returns_base_directory(self):
        expected_return = [
            "./dir1/file1.txt\n",
            "./dir1/file2.txt\n",
            "./dir1/file3.txt\n",
            "./dir1/file4.txt\n",
            "./dir2/subdir/file.txt\n",
        ]
        self.run_test([".", "-name", "file*.txt"], expected_return)

    def test_find_with_name_no_directory(self):
        self.run_test(["-name", "file1.txt"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern_no_directory(self):
        self.run_test(["-name", "*1*"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern_and_subdirectory(self):
        self.run_test(["./dir1", "-name", "file1.txt"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern_and_relative_subdirectory(self):
        self.run_test(["dir1", "-name", "file1.txt"], ["dir1/file1.txt\n"])
