from apps.pwd import Pwd
from setup_test import TestSetup


class TestPwd(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = Pwd()

    def test_pwd(self):
        self.run_test_patch_return(
            [], [self.TEST_DIR], "apps.pwd.getcwd", self.TEST_DIR)
