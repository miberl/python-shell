from setup_test import TestSetup


class TestHistory(TestSetup):
    def test_history_first_command(self):
        self.run_test("history",[''])

    def test_history_after_ls(self):
        self.eval("ls")
        self.run_test("history",["1 ls"])

    def test_history_after_multiple_ls(self):
        self.eval("ls")
        self.eval("ls")
        self.run_test("history",["1 ls"])
    
    def test_multiple_history(self):
        self.eval("ls")
        self.eval("ls")
        self.eval("history")
        self.run_test("history",["1 ls"])

    def test_history_with_commands_in_between(self):
        self.eval("ls")
        self.eval("ls")
        self.eval("history")
        self.eval("ls")
        self.eval("ls")
        self.run_test("history",["1 ls", "2 history", "3 ls"])
    
    def test_history_with_multiple_apps(self):
        self.eval("ls")
        self.eval("pwd")
        self.eval("history")
        self.eval("ls")
        self.eval("cat dir1/file1.txt")
        self.run_test("history",["1 ls", "2 pwd", "3 history", "4 ls", "5 cat dir1/file1.txt"])
