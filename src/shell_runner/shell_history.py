from application import Application
class ShellHistory:
    def __init__(self) -> None:
        self.history_file = ".history.txt"

    def add_to_history(self, command):
        # history doesn't save consecutive duplicates
        last_command = self.get_last_command()
        if last_command and command.strip() == last_command.strip():
            return

        with open(self.history_file, "a") as f:
            command_num = self.get_line_count() + 1
            f.write(f"{command_num} {command}\n")

    def get_history(self):
        return Application.read_lines(self.history_file)
        
    def get_line_count(self):
        return len(self.get_history())

    def get_last_command(self):
        try:
            return Application.read_lines(self.history_file)[-1].split(" ")[1]
        except Exception:
            return None

