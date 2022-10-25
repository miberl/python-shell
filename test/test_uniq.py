from setup_test import TestSetup
from apps.uniq import Uniq


class TestUniq(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Uniq()

    def test_uniq(self):
        self.run_test(
            ["test.txt"],
            ["Test\n"],
            "apps.uniq.Uniq.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_uniq_2(self):
        self.run_test(
            ["dir1/file1.txt"],
            ["AAA\n", "BBB\n", "AAA\n"],
            "apps.uniq.Uniq.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_uniq_3(self):
        self.run_test(
            ["repeatedFile.txt"],
            ["AAA\n", "BBB\n", "AAA\n", "\n", "BBB\n"],
            "apps.uniq.Uniq.read_lines",
            TestSetup.mock_read_lines,
        )
