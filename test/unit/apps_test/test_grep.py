from setup_test import TestSetup


class TestGrep(TestSetup):
    # HAPPY PATHS

    def test_grep_file(self):
        self.run_test("grep AAA dir1/file1.txt", ["AAA", "AAA"])

    def test_grep_subdir(self):
        self.run_test("grep aaa dir2/subdir/file.txt", ["aaa"])

    def test_grep_multiple_files(self):
        self.run_test("grep AAA dir1/file1.txt dir1/file2.txt",
                      ["dir1/file1.txt:AAA", "dir1/file1.txt:AAA"])

    def test_grep_subdir_multiple_files(self):
        self.run_test("grep AAA dir1/file1.txt dir2/subdir/file.txt",
                      ["dir1/file1.txt:AAA", "dir1/file1.txt:AAA", "dir2/subdir/file.txt:AAA", "dir2/subdir/file.txt:AAA"])

    def test_grep_longfile(self):
        self.run_test("grep 10 dir1/longfile.txt", ["10"])

    def test_grep_no_matches(self):
        self.run_test("grep DDD dir1/file1.txt", [""])

    def test_grep_no_matches_multiple_files(self):
        self.run_test("grep DDD dir1/file1.txt dir1/file2.txt", [""])
