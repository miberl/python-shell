import unittest

from setup_test import TestSetup
from collections import deque
from apps.cat import Cat


class TestCat(TestSetup):
    def test_cat(self):
        self.run_test("cat dir1/file1.txt dir1/file2.txt",
                      ["AAA", "BBB", "AAA", "CCC"])


if __name__ == "__main__":
    unittest.main()
