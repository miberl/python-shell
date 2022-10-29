from setup_test import TestSetup
from apps.head import Head
from unittest.mock import patch


class TestHead(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Head()

    def run_test(self, args, expected_output):
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    def test_head(self):
        self.run_test(["test.txt"], ["Test\n"])

    def test_head_2(self):
        self.run_test(["dir1/file1.txt"], ["AAA\n", "BBB\n", "AAA\n"])

    # Expects first 10 lines of file as return
    def test_head_longfile(self):
        expected_output = [f"{str(i)}\n" for i in range(1, 11)]
        self.run_test(["dir1/longfile.txt"], expected_output)

    def test_head_specific_line_limit(self):
        args = ["-n", "5", "dir1/longfile.txt"]
        expected_output = [f"{str(i)}\n" for i in range(1, 6)]
        self.run_test(args, expected_output)

    def test_head_specific_line_limit_2(self):
        args = ["-n", "100", "dir1/longfile.txt"]
        expected_output = [f"{str(i)}\n" for i in range(1, 21)]
        self.run_test(args, expected_output)
