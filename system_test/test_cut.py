from setup_test import TestSetup


class TestCut(TestSetup):

    # test -b flag
    def test_selected_characters(self):
        self.run_test(
            "cut -b 1,2,3 dir1/cutTest.txt", ["And", "Aru", "Ass", "Bih", "Chh"]
        )

    def test_multiple_ranges(self):
        self.run_test(
            "cut -b 1-3,5-7 dir1/cutTest.txt",
            ["Andra ", "Aruach", "Assm", "Bihr", "Chhtti"],
        )

    def test_range_to_end(self):
        self.run_test(
            "cut -b 1- dir1/cutTest.txt",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"],
        )

    def test_range_from_start(self):
        self.run_test("cut -b -3 dir1/cutTest.txt", ["And", "Aru", "Ass", "Bih", "Chh"])

    # test -c flag
    def test_selected_columns(self):
        self.run_test(
            "cut -c 2,5,7 dir1/cutTest.txt", ["nr ", "rah", "sm", "ir", "hti"]
        )

    def test_range_columns(self):
        self.run_test(
            "cut -c 1-7 dir1/cutTest.txt",
            ["Andhra ", "Arunach", "Assam", "Bihar", "Chhatti"],
        )

    def test_range_columns_to_end(self):
        self.run_test(
            "cut -c 1-  dir1/cutTest.txt",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"],
        )

    def test_range_columns_from_start(self):
        self.run_test(
            "cut -c -5 dir1/cutTest.txt", ["Andhr", "Aruna", "Assam", "Bihar", "Chhat"]
        )

    def test_cut_overlapping_range(self):
        self.run_test(
            "cut -b 2-,3- dir1/cutTest.txt",
            [
                "ndhra Pradesh",
                "runachal Pradesh",
                "ssam",
                "ihar",
                "hhattisgarh",
            ]
        )

    def test_cut_full_range_separate_cut(self):
        self.run_test(
            "cut -b -1,2- dir1/cutTest.txt",
            [
                "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chhattisgarh",
            ]
        )

    def test_cut_stdin(self):
        self.run_test("echo abc | cut -b 1",
                      ["a"])
