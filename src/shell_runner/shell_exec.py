from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from apps import cat, echo, ls, cd, pwd, head, grep, tail, uniq, sort, cut, history
from shell_runner.shell_history import ShellHistory

class ShellExec:
    def __init__(self):
        self.appList = {
            "cat": cat.Cat(),
            "cd": cd.Cd(),
            "echo": echo.Echo(),
            "grep": grep.Grep(),
            "head": head.Head(),
            "ls": ls.Ls(),
            "pwd": pwd.Pwd(),
            "tail": tail.Tail(),
            "uniq": uniq.Uniq(),
            "cut": cut.Cut(),
            "sort": sort.Sort(),
            "history": history.History(),
        }
        self.history = ShellHistory()

    def run_instructions(self, instruction: str, out):
        self.history.add_to_history(instruction)
        commands = self.get_commands(instruction)
        for (app, args) in commands:
            self.run_app(app, args, out)

    def run_app(self, app, args, out) -> None:
        if app in self.appList:
            self.appList[app].run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")

    def get_commands(self, instruction) -> list[tuple[str, list[str]]]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(instruction, visitor)
        commands = visitor.get_commands()
        return commands
