# Test Tail

from unittest.mock import patch
from setup_test import TestSetup
from apps.tail import Tail


class TestTail(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Tail()

    # HAPPY PATHS

    def test_tail(self):
        self.run_test(["test.txt"], ["Test\n"],
                      "apps.tail.Tail.read_lines", TestSetup.mock_read_lines)

    def test_tail_2(self):
        self.run_test(["dir1/file1.txt"],  ["AAA\n", "BBB\n", "AAA\n"],
                      "apps.tail.Tail.read_lines", TestSetup.mock_read_lines)

    # Expects last 10 lines of file as return
    def test_tail_longfile(self):
        expected_output = [f"{str(i)}\n" for i in range(11, 21)]
        self.run_test(["dir1/longfile.txt"], expected_output,
                      "apps.tail.Tail.read_lines", TestSetup.mock_read_lines)

    def test_tail_specific_line_limit(self):
        expected_output = [f"{str(i)}\n" for i in range(16, 21)]
        self.run_test(["-n", "5", "dir1/longfile.txt"], expected_output,
                      "apps.tail.Tail.read_lines", TestSetup.mock_read_lines)

    def test_tail_specific_line_limit_2(self):
        expected_output = [f"{str(i)}\n" for i in range(1, 21)]
        self.run_test(["-n", "100", "dir1/longfile.txt"], expected_output,
                      "apps.tail.Tail.read_lines", TestSetup.mock_read_lines)
