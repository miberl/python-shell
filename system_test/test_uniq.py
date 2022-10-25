from setup_test import TestSetup


class TestUniq(TestSetup):
    # check file with one line
    def test_simple_file(self):
        self.run_test("uniq dir1/file2.txt", ["CCC"])

    # check file with multiple lines but no duplicates
    def test_files_with_multiple_lines_no_repreated(self):
        self.run_test("uniq dir1/file1.txt", ["AAA", "BBB", "AAA"])

    # check file with one repeated line
    def test_files_with_repeated_line(self):
        self.run_test("uniq dir1/file4.txt", ["AAA"])

    # check file with many repeated lines
    def test_files_with_many_repeated_lines(self):
        self.run_test("uniq dir1/file3.txt", ["AAA", "BBB", "CCC"])

    # more will be added later once mock issue and options are sorted out
