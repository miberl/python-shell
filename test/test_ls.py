import unittest
from unittest.mock import patch
from setup_test import TestSetup
from apps.ls import Ls
from setup_test import TestSetup


class TestLs(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.ls = Ls()

    def test_ls(self):
        with patch("apps.ls.listdir", return_value=["test.txt", "dir2", "dir1"]):
            self.ls.run([], self.out)
            self.assertEqual(set(self.out), set(["test.txt\n", "dir2\n", "dir1\n"]))
            self.assertEqual(len(self.out), 3)
