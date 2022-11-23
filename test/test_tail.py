# Test Tail

from apps.tail import Tail
from setup_test import TestSetup


class TestTail(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Tail()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    # HAPPY PATHS

    def test_tail(self):
        self.run_test(["test.txt"], ["''\n"])

    def test_tail_2(self):
        self.run_test(["dir1/file1.txt"], ["AAA\n", "BBB\n", "AAA\n"])

    # Expects last 10 lines of file as return
    def test_tail_longfile(self):
        expected_output = [f"{str(i)}\n" for i in range(11, 21)]
        self.run_test(["dir1/longfile.txt"], expected_output)

    def test_tail_specific_line_limit(self):
        expected_output = [f"{str(i)}\n" for i in range(16, 21)]
        self.run_test(["-n", "5", "dir1/longfile.txt"], expected_output)

    def test_tail_specific_line_limit_2(self):
        expected_output = [f"{str(i)}\n" for i in range(1, 21)]
        self.run_test(["-n", "100", "dir1/longfile.txt"], expected_output)
