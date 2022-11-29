import sys
from io import StringIO

from apps.wc import Wc
from exceptions.unknown_option_error import UnknownFlagError
from setup_test import TestSetup


class TestWc(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Wc()

    def run_test(self, args, expected_output, **kwargs):
        expected_output += ['\n']
        super().run_test(args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines)

    def test_reads_from_file(self):
        self.run_test(['dir1/file1.txt'],
                      ['    3    3    12 dir1/file1.txt\n'])

    def test_reads_multiple_files(self):
        self.run_test(['dir1/file1.txt', 'dir1/file2.txt'],
                      ['    3    3    12 dir1/file1.txt\n',
                       '    1    1     4 dir1/file2.txt\n',
                       '    4    4    16 total\n'])

    def test_reads_from_input(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("AAA\nBBB\nAAA\n")
        self.run_test([], ['    3    3    12\n'])
        sys.stdin = original_stdin

    def test_fails_with_bad_file(self):
        with self.assertRaises(KeyError):
            self.run_test(['nonsense'], [])

    def test_fails_with_bad_arg(self):
        with self.assertRaises(UnknownFlagError) as err:
            self.run_test(['-b'], [])
        assert 'Unknown option flag: -b' in str(err.exception)

    def test_l_option(self):
        self.run_test(['-l', 'dir1/file1.txt'],
                      ['    3 dir1/file1.txt\n'])

    def test_w_option(self):
        self.run_test(['-w', 'dir1/file1.txt'],
                      ['    3 dir1/file1.txt\n'])

    def test_c_option(self):
        self.run_test(['-c', 'dir1/file1.txt'],
                      ['    12 dir1/file1.txt\n'])

    def test_m_option(self):
        self.run_test(['-m', 'dir1/file1.txt'],
                      ['    12 dir1/file1.txt\n'])

    def test_tabs_as_word_delimiter(self):
        self.run_test(['-l', 'dir1/file1.txt'],
                      ['    3 dir1/file1.txt\n'])

    def test_newline_as_word_delimiter(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("hello\nthere")
        self.run_test(['-w'], ['    2\n'])
        sys.stdin = original_stdin

    def test_tab_as_word_delimiter(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("hello\tthere")
        self.run_test(['-w'], ['    2\n'])
        sys.stdin = original_stdin

    def test_empty_input(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("")
        self.run_test([], ['    0    0    0\n'])
        sys.stdin = original_stdin

    def test_only_line_ends_in_slash_n(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("hello\nthere\n:)")
        self.run_test([], ['    2    3    14\n'])
        sys.stdin = original_stdin

    def test_single_word(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("test")
        self.run_test([], ['    0    1    4\n'])
        sys.stdin = original_stdin
