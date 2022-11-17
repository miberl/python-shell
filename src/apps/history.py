from application import Application
from shell_runner.shell_history import ShellHistory

class History(Application):

    def __init__(self):
        super().__init__()
        self.shellHistory = ShellHistory()

    def run(self, args, inpt, out) -> None:
        try:
            history = self.shellHistory.get_history()[:-1]
            out.extend(history)
        except Exception:
            pass

        
