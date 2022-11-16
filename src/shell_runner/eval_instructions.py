import sys
from collections import deque

from application import Application
from apps import cat, cd, echo, grep, head, ls, pwd, tail, uniq, cut, sort
from inputparser.command import Instruction


class EvalInstructions:
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

    def eval(self, instructions: [Instruction]) -> deque:
        if not instructions:
            return deque()

        inp = sys.stdin

        for instruction in instructions:
            inp = self.run_one_instruction(inp, instruction)

        return self.get_return_val(inp)

    def run_one_instruction(self, inp, instruction):
        inp = sys.stdin
        outp = ''
        while instruction.has_next():
            inp = self.run_command(inp, instruction)
        return inp

    def run_command(self, inp, instruction):
        command = instruction.get_next_command()
        r_in, r_out = command.get_redirs()
        if r_in:
            if inp == sys.stdin:
                inp = Application.read_file(r_in)
            else:
                inp

        outp = self.eval_cmd(command, inp)
        inp = outp
        return inp

    def get_return_val(self, inp):
        if inp == sys.stdin:
            return deque()
        return inp

    def eval_cmd(self, command, inp):
        app = command.get_app()
        args = command.get_args()

        outp = deque()

        if app in self.appList:
            self.appList[app].run(args, outp)
        else:
            raise ValueError(f"unsupported application {app}")
