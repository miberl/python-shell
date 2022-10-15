import unittest
from unittest.mock import patch
from setup_test import TestSetup
from apps.pwd import Pwd
from setup_test import TestSetup


class TestPwd(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.pwd = Pwd()

    def test_pwd(self):
        with patch("apps.pwd.getcwd", return_value=self.TEST_DIR):
            self.pwd.run([], self.out)
            self.assertEqual(self.out[0], self.TEST_DIR)
            self.assertEqual(len(self.out), 1)
