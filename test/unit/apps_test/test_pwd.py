from setup_test import TestSetup


class TestPwd(TestSetup):
    def test_matches_current_directory(self):
        self.run_test("pwd", '/test')
