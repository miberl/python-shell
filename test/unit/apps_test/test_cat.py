import unittest

from setup_test import TestSetup


class TestCat(TestSetup):
    # HAPPY PATHS

    def test_cat(self):
        self.run_test("cat dir1/file1.txt",
                      ["AAA", "BBB", "AAA"], split_on_newline=True)

    def test_cat_2(self):
        self.run_test("cat dir1/file2.txt", ["CCC"], split_on_newline=True)

    def test_cat_multiple_args(self):
        self.run_test("cat dir1/file1.txt dir1/file2.txt",
                      ["AAA", "BBB", "AAA", "CCC"], split_on_newline=True)

    def test_cat_subdir(self):
        self.run_test("cat dir2/subdir/file.txt",
                      ["AAA", "aaa", "AAA"], split_on_newline=True)

    def test_cat_longfile(self):
        res = [str(x) for x in range(1, 21)]
        self.run_test("cat dir1/longfile.txt", res, split_on_newline=True)


if __name__ == "__main__":
    unittest.main()
