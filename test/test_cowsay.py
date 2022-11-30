import sys
from io import StringIO
from setup_test import TestSetup
from apps.cowsay import Cowsay

COW = [
    "        \\   ^__^\n",
    "         \\  (oo)\\_______\n",
    "            (__)\\       )\\/\\\n",
    "                ||----w |\n",
    "                ||     ||\n",
]


class TestCowsay(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cowsay()

    def test_cowsay(self):
        bubble = [" -------\n", "< hello >\n", " -------\n"]
        self.run_test(["hello"], bubble + COW)

    def test_cowsay_single_word_wrapping(self):
        MAX_LINE_LEN = 39
        very_long_string = "a" * MAX_LINE_LEN * 3
        bubble = [
            f" {'-'*41}\n",
            f"/ {'a'*39} \\\n",
            f"| {'a'*39} |\n",
            f"\\ {'a'*39} /\n",
            f" {'-'*41}\n",
        ]
        self.run_test([very_long_string], bubble + COW)

    def test_cowsay_multiple_word_wrapping(self):
        first_word = "a" * 20
        second_word = "b" * 30
        bubble = [
            f" {'-'*32}\n",
            f"/ {'a'*20}{' '*10} \\\n",
            f"\\ {'b'*30} /\n",
            f" {'-'*32}\n",
        ]
        self.run_test([first_word, second_word], bubble + COW)

    def test_cowsay_stdin(self):
        original_stdin = sys.stdin
        sys.stdin = StringIO("hello")
        bubble = [" -------\n", "< hello >\n", " -------\n"]
        self.run_test([], bubble + COW)
        sys.stdin = original_stdin
