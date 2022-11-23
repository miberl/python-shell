import sys
from io import StringIO

from exceptions.unknown_option_error import UnknownFlagError
from setup_test import TestSetup
from apps.cut import Cut


class TestCut(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cut()

    def run_test(self, args, expected_output, **kwargs):
        super().run_test(
            args, expected_output, "application.Application.read_lines",
            TestSetup.mock_read_lines
        )

    # test -b flag
    def test_cut_2(self):
        self.run_test(["-b", "1,2,3", "dir1/cutTest.txt"],
                      ["And\n", "Aru\n", "Ass\n", "Bih\n", "Chh\n"])

    def test_cut_3(self):
        self.run_test(["-b", "1-3,5-7", "dir1/cutTest.txt"],
                      ["Andra \n", "Aruach\n", "Assm\n", "Bihr\n", "Chhtti\n"])

    def test_cut_4(self):
        self.run_test(["-b", "1-", "dir1/cutTest.txt"], [
            "Andhra Pradesh\n",
            "Arunachal Pradesh\n",
            "Assam\n",
            "Bihar\n",
            "Chhattisgarh\n",
        ])

    def test_cut_5(self):
        self.run_test(["-b", "-3", "dir1/cutTest.txt"],
                      ["And\n", "Aru\n", "Ass\n", "Bih\n", "Chh\n"])

    # test -c flag
    def test_cut_6(self):
        self.run_test(["-c", "2,5,7", "dir1/cutTest.txt"],
                      ["nr \n", "rah\n", "sm\n", "ir\n", "hti\n"])

    def test_cut_7(self):
        self.run_test(["-c", "1-7", "dir1/cutTest.txt"],
                      ["Andhra \n", "Arunach\n", "Assam\n", "Bihar\n",
                       "Chhatti\n"])

    def test_cut_8(self):
        self.run_test(["-c", "1-", "dir1/cutTest.txt"], [
            "Andhra Pradesh\n",
            "Arunachal Pradesh\n",
            "Assam\n",
            "Bihar\n",
            "Chhattisgarh\n",
        ])

    def test_cut_9(self):
        self.run_test(["-c", "-5", "dir1/cutTest.txt"],
                      ["Andhr\n", "Aruna\n", "Assam\n", "Bihar\n", "Chhat\n"])

    def test_cut_overlapping_range(self):
        self.run_test(["-b", "2-,3-", "dir1/cutTest.txt"], [
            "ndhra Pradesh\n",
            "runachal Pradesh\n",
            "ssam\n",
            "ihar\n",
            "hhattisgarh\n",
        ])

    def test_cut_full_range_separate_cut(self):
        self.run_test(["-b", "-1,2-", "dir1/cutTest.txt"], [
            "Andhra Pradesh\n",
            "Arunachal Pradesh\n",
            "Assam\n",
            "Bihar\n",
            "Chhattisgarh\n",
        ])

    def test_cut_too_few_args_no_args(self):
        with self.assertRaises(ValueError) as err:
            self.run_test([], [])
        assert 'wrong number of command line arguments' in str(err.exception)

    def test_cut_too_few_args_one_arg(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['hello'], [])
        assert 'wrong number of command line arguments' in str(err.exception)

    def test_cut_too_many_args(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['hello', 'there', 'many', 'args'], [])
        assert 'wrong number of command line arguments' in str(err.exception)

    def test_cut_bad_flag(self):
        with self.assertRaises(UnknownFlagError) as err:
            self.run_test(['-g', 'hello', 'dir1/cutTest.txt'], [])
        assert 'Unknown option flag' in str(err.exception)

    def test_cut_invalid_range(self):
        with self.assertRaises(ValueError) as err:
            self.run_test(['-b', '4-3', 'dir1/cutTest.txt'], [])
        assert 'invalid range' in str(err.exception)

    def test_cut_stdin_ok(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("AAA\nBBB\nAAA\n")

        self.run_test(['-b', '1'], ['A\n', 'B\n', 'A\n'])

        sys.stdin = original_stdin
