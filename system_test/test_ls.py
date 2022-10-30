from setup_test import TestSetup

class TestLs(TestSetup):
    # Error on three args
    def test_fail_on_three_args(self):
        self.run_test("ls dir1 bla", [""])

    # try invalid path
    def test_bad_path(self):
        self.run_test("ls bla", [""])

    # ls in current dir
    def test_read_current_dir(self):
        self.run_test_no_order("ls", ["test.txt",  "dir1", "dir2"])

    # ls in specified dir
    def test_read_dir_1(self):
        self.run_test_no_order(
            "ls dir1", [ "file1.txt", "file2.txt","file3.txt","file4.txt", "longfile.txt"]
        )

    # check for secret files
    def test_read_dir_with_hidden_not_shown(self):
        self.run_test_no_order("ls dir2/subdir", ["file.txt", "normal"])
