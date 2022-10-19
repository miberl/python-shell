# Test Tail

from unittest.mock import patch
from setup_test import TestSetup
from apps.tail import Tail


class TestTail(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.tail = Tail()

    # HAPPY PATHS

    def test_tail(self):
        with patch("apps.tail.Tail.read_lines", side_effect=TestSetup.mock_read_lines):
            self.tail.run(["test.txt"], self.out)
            self.assertEqual(self.out, ["Test\n"])

    def test_tail_2(self):
        with patch("apps.tail.Tail.read_lines", side_effect=TestSetup.mock_read_lines):
            self.tail.run(["dir1/file1.txt"], self.out)
            self.assertEqual(self.out, ["AAA\n", "BBB\n", "AAA\n"])

    # Expects last 10 lines of file as return
    def test_tail_longfile(self):
        with patch("apps.tail.Tail.read_lines", side_effect=TestSetup.mock_read_lines):
            self.tail.run(["dir1/longfile.txt"], self.out)
            self.assertEqual(
                self.out, ([f"{str(i)}\n" for i in range(11, 21)]))

    def test_tail_specific_line_limit(self):
        with patch("apps.tail.Tail.read_lines", side_effect=TestSetup.mock_read_lines):
            self.tail.run(["-n", "5", "dir1/longfile.txt"], self.out)
            self.assertEqual(
                self.out, ([f"{str(i)}\n" for i in range(16, 21)]))

    def test_tail_specific_line_limit_2(self):
        with patch("apps.tail.Tail.read_lines", side_effect=TestSetup.mock_read_lines):
            self.tail.run(["-n", "100", "dir1/longfile.txt"], self.out)
            self.assertEqual(self.out, ([f"{str(i)}\n" for i in range(1, 21)]))
