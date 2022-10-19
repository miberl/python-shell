from setup_test import TestSetup


class TestHead(TestSetup):
    # zero args errors
    def test_fails_if_zero_arguments_passed(self):
        self.run_test("head", [""])

    # two args errors
    def test_fails_if_two_arguments_passed(self):
        self.run_test("head 5 dir1/longfile.txt", [""])

    # 4 args errors
    def test_fails_if_four_arguments_passed(self):
        self.run_test("head -n 5 dir1/longfile.txt dir1/file1.txt", [""])

    # 1 and three args does not error (assume correct format)
    def test_not_raise_if_three_arguments(self):
        self.run_test("head -n 5 dir1/longfile.txt", [str(i) for i in range(1, 6)])

    # One arg tests
    def test_single_arg_works(self):
        self.run_test("head dir1/longfile.txt", [str(i) for i in range(1, 11)])

    # read 10 lines in file in current directory
    def test_default_n_equiv_to_set_n_ten(self):
        self.run_test("head dir1/longfile.txt", [str(i) for i in range(1, 11)])
        self.run_test("head -n 10 dir1/longfile.txt", [str(i) for i in range(1, 11)])

    # read lines of shorter file, stop at 10
    def test_reading_short_file(self):
        self.run_test("head dir1/file1.txt", ["AAA", "BBB", "AAA"])

    # Nonsense argument errors (bad file)
    def test_bad_filename_one_arg(self):
        self.run_test("head blablabla", [""])

    # Three arg tests
    # bad file name
    def test_bad_filename_three_arg(self):
        self.run_test("head -n 3 blablabla", [""])

    # exact file length
    def test_read_whole_file(self):
        self.run_test("head -n 20 dir1/longfile.txt", [str(i) for i in range(1, 21)])

    # n==0, n == -1 etc.
    def test_errors_on_zero_n(self):
        self.run_test("head -n 0 dir1/longfile.txt", [""])

    def test_errors_on_negative_n(self):
        self.run_test("head -n -5 dir1/longfile.txt", [""])

    # bad flag
    def test_with_bad_flag(self):
        self.run_test("head -r 5 dir1/longfile.txt", [""])

    # non int n
    def test_with_non_int_n(self):
        self.run_test("head -n hello dir1/longfile.txt", [""])
