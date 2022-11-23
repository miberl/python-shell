from setup_test import TestSetup


class TestFind(TestSetup):
    def test_find(self):
        self.run_test("find . -name file1.txt", ["./dir1/file1.txt"])

    def test_find_no_directory(self):
        self.run_test("find -name file1.txt", ["./dir1/file1.txt"])

    def test_find_with_pattern(self):
        self.run_test("find . -name '*1*'", ["./dir1/file1.txt"])

    def test_find_multiple_matches(self):
        self.run_test_no_order(
            "find . -name 'file*.txt'",
            [
                "./dir1/file1.txt",
                "./dir1/file2.txt",
                "./dir1/file3.txt",
                "./dir1/file4.txt",
                "./dir2/subdir/file.txt",
            ],
        )

    def test_find_with_subdirectory(self):
        self.run_test("find dir1 -name file1.txt", ["dir1/file1.txt"])
