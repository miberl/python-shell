from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from apps import cat, echo, ls, cd, pwd, head, grep, tail, uniq, sort


class Shell:
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
            "sort": sort.Sort(),
        }

    def run_instructions(self, instruction: str, out):
        commands = self.get_commands(instruction)

        for (app, args) in commands:
            self.run_app(app, args, out)

    def run_app(self, app, args, out) -> None:
        if app in self.appList:
            self.appList[app].run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")

    def get_commands(self, instruction) -> [(str, [str])]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(instruction, visitor)
        commands = visitor.get_commands()
        return commands
