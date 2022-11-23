from setup_test import TestSetup
from apps.cd import Cd
from exceptions.invalid_syntax_error import InvalidSyntaxError


class TestCd(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.app = Cd()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(
            args,
            expected_output,
            "apps.cd.os.chdir",
            TestSetup.fetch_directory_from_fs,
            False,
        )

    def test_cd(self):
        self.run_test(["dir1"], None)

    def test_cd_multiple_args(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test(["dir1", "dir2"], None)

    def test_cd_no_args(self):
        with self.assertRaises(InvalidSyntaxError):
            self.run_test([], None)
