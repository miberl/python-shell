from setup_test import TestSetup


class CdPwd(TestSetup):
    def test_cd_pwd_home(self):
        self.run_test("cd .; pwd", [self.TEST_DIR])

    def test_cd_pwd_home_2(self):
        self.run_test("cd dir1/..; pwd", [self.TEST_DIR])

    def test_cd_pwd_home_3(self):
        self.run_test(f"cd {self.TEST_DIR}; pwd", [self.TEST_DIR])

    def test_cd_pwd_dir_change(self):
        self.run_test("cd dir1; pwd", [self.TEST_DIR + "/dir1"])

    def test_cd_pwd_dir_change_2(self):
        self.run_test("cd dir1/../dir1; pwd", [self.TEST_DIR + "/dir1"])

    def test_cd_pwd_subdirectory_change(self):
        self.run_test("cd dir2/subdir; pwd", [self.TEST_DIR + "/dir2/subdir"])

    def test_cd_pwd_root(self):
        self.run_test("cd /; pwd", ["/"])

    def test_cd_pwd_root_up_one_level(self):
        self.run_test("cd /..; pwd", ["/"])
