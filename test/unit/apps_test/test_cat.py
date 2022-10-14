import unittest

from setup_test import TestSetup
from collections import deque
from apps.cat import Cat


class TestCat(TestSetup):
    # def setUp(self):
    #     super().setUp()
    #     self.cat = Cat()
    #     self.out = deque()

    def test_cat(self):
        cmdline = "cat dir1/file1.txt dir1/file2.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["AAA", "BBB", "AAA", "CCC"])


if __name__ == "__main__":
    unittest.main()
