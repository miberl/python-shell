from setup_test import TestSetup


class TestUniq(TestSetup):
    # check file with one line
    def test_uniq(self):
        self.run_test("uniq dir1/file2.txt", ["CCC"])

    def test_uniq_2(self):
        self.run_test("uniq dir2/subdir/file.txt", ["AAA", "aaa", "AAA"])

    # check file with multiple lines but no duplicates
    def test_uniq_multiple_lines_no_repeated(self):
        self.run_test("uniq dir1/file1.txt", ["AAA", "BBB", "AAA"])

    # check file with one repeated line
    def test_uniq_repeated_line(self):
        self.run_test("uniq dir1/file4.txt", ["AAA"])

    # check file with many repeated lines
    def test_uniq_multiple_repeated_lines(self):
        self.run_test("uniq dir1/file3.txt", ["AAA", "BBB", "CCC"])

    def test_uniq_ignore_case(self):
        self.run_test("uniq -i dir2/subdir/file.txt", ["AAA"])

    def test_uniq_ignore_case_2(self):
        self.run_test("uniq -i dir1/file1.txt", ["AAA", "BBB", "AAA"])
