from setup_test import TestSetup

class TestSort(TestSetup):
    
    def test_sort(self):
        self.run_test("sort test.txt", ["Test"])
    
    def test_sort_2(self):
        self.run_test("sort dir1/file2.txt", ["CCC"])

    def test_sort_3(self):
        self.run_test("sort dir1/file1.txt", ["AAA", "AAA", "BBB"])

    def test_sort_multiple_args(self):
        self.run_test("sort dir1/file1.txt dir1/file2.txt", ["AAA", "AAA", "BBB", "CCC"])

    def test_sort_reverse(self):
        self.run_test("sort -r test.txt", ["Test"])

    def test_sort_2_reverse(self):
        self.run_test("sort -r dir1/file2.txt", ["CCC"])

    def test_sort_3_reverse(self):
        self.run_test("sort -r dir1/file1.txt", ["BBB", "AAA", "AAA"])

    def test_sort_multiple_args_reverse(self):
        self.run_test("sort -r dir1/file1.txt dir1/file2.txt", ["CCC", "BBB", "AAA", "AAA"])

    def test_sort_int_list(self):
        expected_output = [str(i) for i in range(1, 21)]
        expected_output = sorted(expected_output)
        self.run_test("sort dir1/longfile.txt", expected_output)

    def test_sort_hidden(self):
        self.run_test("sort dir1/subdir/.hidden", ["secret"])