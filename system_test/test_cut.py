from setup_test import TestSetup


class TestCut(TestSetup):
    # test no flag
    def test_no_flags(self):
        self.run_test(
            "cut dir1/file5.txt",
            ["cut: you must specify a list of bytes, characters, or fields"],
        )

    # test -b flag
    def test_selected_characters(self):
        self.run_test(
            "cut -b 1,2,3 dir1/file5.txt", ["And", "Aru", "Ass", "Bih", "Chh"]
        )

    def test_multiple_ranges(self):
        self.run_test(
            "cut -b 1-3,5-7 dir1/file5.txt",
            ["Andra", "Aruach", "Assm", "Bihr", "Chhtti"],
        )

    def test_range_to_end(self):
        self.run_test(
            "cut -b 1- dir1/file5.txt",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"],
        )

    def test_range_from_start(self):
        self.run_test("cut -b -3 dir1/file5.txt", ["And", "Aru", "Ass", "Bih", "Chh"])

    # test -c flag
    def test_selected_columns(self):
        self.run_test("cut -c 2,5,7 dir1/file5.txt", ["nr", "rah", "sm", "ir", "hti"])

    def test_range_columns(self):
        self.run_test(
            "cut -c 1-7 dir1/file5.txt",
            ["Andhra ", "Arunach", "Assam", "Bihar", "Chhatti"],
        )

    def test_range_columns_to_end(self):
        self.run_test(
            "cut -c 1-  dir1/file5.txt",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"],
        )

    def test_range_columns_from_start(self):
        self.run_test(
            "cut -c -5 dir1/file5.txt", ["Andhr", "Aruna", "Assam", "Bihar", "Chhat"]
        )

    # test -f flag
    def test_fields_no_delimiter(self):
        self.run_test(
            "cut -f 1 dir1/file5.txt",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"],
        )

    def test_fields_with_delimiter(self):
        self.run_test(
            "-d " " -f 1 dir1/file5.txt",
            ["Andhra", "Arunachal", "Assam", "Bihar", "Chhattisgarh"],
        )
