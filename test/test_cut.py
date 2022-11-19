from setup_test import TestSetup
from apps.cut import Cut


class TestCut(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Cut()

    def run_test(self, args, expected_output):
        super().run_test(
     args, expected_output, "application.Application.read_lines", TestSetup.mock_read_lines
        )

    # test -b flag
    def test_cut_2(self):
        self.run_test(
            ["-b", "1,2,3", "dir1/cutTest.txt"],
            ["And\n", "Aru\n", "Ass\n", "Bih\n", "Chh\n"],
        )

    def test_cut_3(self):
        self.run_test(
            ["-b", "1-3,5-7", "dir1/cutTest.txt"],
            ["Andra \n", "Aruach\n", "Assm\n", "Bihr\n", "Chhtti\n"],
        )

    def test_cut_4(self):
        self.run_test(
            ["-b", "1-", "dir1/cutTest.txt"],
            [
                "Andhra Pradesh\n",
                "Arunachal Pradesh\n",
                "Assam\n",
                "Bihar\n",
                "Chhattisgarh\n",
            ],
        )

    def test_cut_5(self):
        self.run_test(
            ["-b", "-3", "dir1/cutTest.txt"],
            ["And\n", "Aru\n", "Ass\n", "Bih\n", "Chh\n"],
        )

    # test -c flag
    def test_cut_6(self):
        self.run_test(
            ["-c", "2,5,7", "dir1/cutTest.txt"],
            ["nr \n", "rah\n", "sm\n", "ir\n", "hti\n"],
        )

    def test_cut_7(self):
        self.run_test(
            ["-c", "1-7", "dir1/cutTest.txt"],
            ["Andhra \n", "Arunach\n", "Assam\n", "Bihar\n", "Chhatti\n"],
        )

    def test_cut_8(self):
        self.run_test(
            ["-c", "1-", "dir1/cutTest.txt"],
            [
                "Andhra Pradesh\n",
                "Arunachal Pradesh\n",
                "Assam\n",
                "Bihar\n",
                "Chhattisgarh\n",
            ],
        )

    def test_cut_9(self):
        self.run_test(
            ["-c", "-5", "dir1/cutTest.txt"],
            ["Andhr\n", "Aruna\n", "Assam\n", "Bihar\n", "Chhat\n"],
        )

    def test_cut_overlapping_range(self):
        self.run_test(
            ["-b", "2-,3-", "dir1/cutTest.txt"],
            [
                "ndhra Pradesh\n",
                "runachal Pradesh\n",
                "ssam\n",
                "ihar\n",
                "hhattisgarh\n",
            ]
        )

    def test_cut_full_range_separate_cut(self):
        self.run_test(
            ["-b", "-1,2-", "dir1/cutTest.txt"],
            [
                "Andhra Pradesh\n",
                "Arunachal Pradesh\n",
                "Assam\n",
                "Bihar\n",
                "Chhattisgarh\n",
            ]
        )
