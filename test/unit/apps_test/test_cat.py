import unittest

from setup_test import TestSetup


class TestCat(TestSetup):
    # HAPPY PATHS

    def test_cat(self):
        self.run_test("cat dir1/file1.txt",
                      ["AAA", "BBB", "AAA"])

    def test_cat_2(self):
        self.run_test("cat dir1/file2.txt", ["CCC"])

    def test_cat_multiple_args(self):
        self.run_test("cat dir1/file1.txt dir1/file2.txt",
                      ["AAA", "BBB", "AAA", "CCC"])

    def test_cat_subdir(self):
        self.run_test("cat dir2/subdir/file.txt",
                      ["AAA", "aaa", "AAA"])

    def test_cat_longfile(self):
        res = [str(x) for x in range(1, 21)]
        self.run_test("cat dir1/longfile.txt", res)

    def test_cat_hidden(self):
        self.run_test("cat dir1/subdir/.hidden", ["secret"])

    def test_cat_hidden_2(self):
        self.run_test("cat dir1/subdir/.hidden dir1/file1.txt",
                      ["secret", "AAA", "BBB", "AAA"])


if __name__ == "__main__":
    unittest.main()
