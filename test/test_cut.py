from setup_test import TestSetup
from apps.cut import Cut


class TestCut(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cut()

    # test no flag
    def test_cut_1(self):
        self.run_test(
            ["file3.txt"],
            ["cut: you must specify a list of bytes, characters, or fields\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    # test -b flag
    def test_cut_2(self):
        self.run_test(
            ["-b 1,2,3 file3.txt"],
            ["And\nAru\nAss\nBih\nChh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_3(self):
        self.run_test(
            ["-b 1-3,5-7 file3.txt"],
            ["Andra\Aruach\nAssm\nBihr\nChhtti\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_4(self):
        self.run_test(
            ["-b 1- file3.txt"],
            ["Andhra Pradesh\nArunachal Pradesh\nAssam\nBihar\nChhattisgarh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_5(self):
        self.run_test(
            ["-b -3 file3.txt"],
            ["And\nAru\nAss\nBih\nChh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    # test -c flag
    def test_cut_6(self):
        self.run_test(
            ["-c 2,5,7 file3.txt"],
            ["nr\nrah\nsm\nir\nhti\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_7(self):
        self.run_test(
            ["-c 1-7 file3.txt"],
            ["Andhra\nArunach\nAssam\nBihar\nChhatti\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_8(self):
        self.run_test(
            ["-c 1- file3.txt"],
            ["Andhra Pradesh\nArunachal Pradesh\nAssam\nBihar\nChhattisgarh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_9(self):
        self.run_test(
            ["-c -5 file3.txt"],
            ["Andhr\nAruna\nAssam\nBihar\nChhat\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    # test -f flag
    def test_cut_10(self):
        self.run_test(
            ["-f 1 file3.txt"],
            ["Andhra Pradesh\nArunachal Pradesh\nAssam\nBihar\nChhattisgarh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )

    def test_cut_11(self):
        self.run_test(
            ["-d " " -f 1 file3.txt"],
            ["Andhra\nArunachal\nAssam\nBihar\nChhattisgarh\n"],
            "apps.cut.Cut.read_lines",
            TestSetup.mock_read_lines,
        )
