from setup_test import TestSetup
from collections import deque
from apps.history import History


class TestHistory(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.out = []
        self.app = History()

    def test_history_no_command(self):
        self.run_test_patch_return([], [],
                                   "application.Application.read_lines", [""])
    

    def test_history_one_command(self):
        self.run_test_patch_return([], ["1 ls"],
                                   "application.Application.read_lines", ["1 ls", "2 history"])

    def test_history_multiple_commands(self):
        self.run_test_patch_return([], ["1 ls", "2 history", "3 ls", "4 pwd"],
                                   "application.Application.read_lines", ["1 ls", "2 history", "3 ls", "4 pwd", "5 history"])