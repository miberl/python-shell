from setup_test import TestSetup
from apps.find import Find


class TestFind(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Find()

    def run_test(self, args, expected_output):
        super().run_test(
            args,
            expected_output,
            "apps.find.os.walk",
            TestSetup.mock_os_walk,
        )

    # HAPPY PATHS

    def test_find_with_name(self):
        self.run_test(["-name", "file1.txt"], ["./dir1/file1.txt\n"])

    def test_find_with_name_and_pattern(self):
        self.run_test(["-name", "*1*"], ["./dir1/file1.txt\n"])
