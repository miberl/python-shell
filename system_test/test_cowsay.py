from setup_test import TestSetup

COW = [
    "        \   ^__^",
    "         \  (oo)\_______",
    "            (__)\       )\/\\",
    "                ||----w |",
    "                ||     ||",
]


class TestCowsay(TestSetup):
    # HAPPY PATHS

    def test_cowsay(self):
        bubble = [" -------", "< hello >", " -------"]
        self.run_test("cowsay hello", bubble + COW)

    def test_cowsay_single_word_wrapping(self):
        MAX_LINE_LENGTH = 39
        very_long_string = "a" * MAX_LINE_LENGTH * 3
        bubble = [
            f" {'-'*41}",
            f"/ {'a'*39} \\",
            f"| {'a'*39} |",
            f"\\ {'a'*39} /",
            f" {'-'*41}",
        ]
        self.run_test(f"cowsay {very_long_string}", bubble + COW)

    def test_cowsay_multiple_word_wrapping(self):
        first_word = "a" * 20
        second_word = "b" * 30
        bubble = [
            f" {'-'*32}",
            f"/ {'a'*20}{' '*10} \\",
            f"\ {'b'*30} /",
            f" {'-'*32}",
        ]
        self.run_test(f"cowsay {first_word} {second_word}", bubble + COW)
