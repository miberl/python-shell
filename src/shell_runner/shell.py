from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from apps import cat, echo, ls, cd, pwd, head, grep, tail, uniq, sort, cut


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
            "cut": cut.Cut(),
            "sort": sort.Sort(),
        }

    def run_instructions(self, instruction: str, out):
        commands = self.get_instructions(instruction)

        for (app, args) in commands:
            self.run_app(app, args, out)

    def run_app(self, app, args, out) -> None:
        if app in self.appList:
            self.appList[app].run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")

    def get_instructions(self, instruction) -> [(str, [str])]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(instruction, visitor)
        instructions = visitor.get_instructions()
        return instructions
