from setup_test import TestSetup
from apps.head import Head
from unittest.mock import patch


class TestHead(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.head = Head()

    def test_head(self):
        with patch("apps.head.Head.read_lines", side_effect=TestSetup.mock_read_lines):
            self.head.run(["test.txt"], self.out)
            self.assertEqual(self.out, ["Test\n"])

    def test_head_2(self):
        with patch("apps.head.Head.read_lines", side_effect=TestSetup.mock_read_lines):
            self.head.run(["dir1/file1.txt"], self.out)
            self.assertEqual(self.out, ["AAA\n", "BBB\n", "AAA\n"])

    # Expects first 10 lines of file as return
    def test_head_longfile(self):
        with patch("apps.head.Head.read_lines", side_effect=TestSetup.mock_read_lines):
            self.head.run(["dir1/longfile.txt"], self.out)
            self.assertEqual(self.out, ([f"{str(i)}\n" for i in range(1, 11)]))

    def test_head_specific_line_limit(self):
        with patch("apps.head.Head.read_lines", side_effect=TestSetup.mock_read_lines):
            self.head.run(["-n", "5", "dir1/longfile.txt"], self.out)
            self.assertEqual(self.out, ([f"{str(i)}\n" for i in range(1, 6)]))

    def test_head_specific_line_limit_2(self):
        with patch("apps.head.Head.read_lines", side_effect=TestSetup.mock_read_lines):
            self.head.run(["-n", "100", "dir1/longfile.txt"], self.out)
            self.assertEqual(self.out, ([f"{str(i)}\n" for i in range(1, 21)]))
