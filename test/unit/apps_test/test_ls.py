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
        self.run_test("ls", ["test.txt", "dir2", "dir1"])

    # ls in specified dir
    def test_read_dir_1(self):
        self.run_test("ls dir1", ["longfile.txt", "file2.txt", "file1.txt", "subdir"])

    # check for secret files
    def test_read_dir_with_hidden_not_shown(self):
        self.run_test("ls dir1/subdir", ["normal"])
