import sys
from collections import deque

from application import Application
from apps import cat, cd, echo, grep, head, ls, pwd, tail, uniq, cut, sort, find

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
            "find": find.Find(),
        }

    def eval(self, instructions: [Instruction]) -> deque:
        if not instructions:
            return deque()

        outp = deque()
        for instruction in instructions:
            outp += self.run_one_instruction(instruction)

        return self.get_return_val(outp)

    def run_one_instruction(self, instruction):
        inp = sys.stdin
        while instruction.has_next():
            inp = self.run_command(inp, instruction)
        return inp

    def run_command(self, inp, instruction):
        command = instruction.get_next_command()
        r_in, r_out = command.get_redirs()
        inp = self.handle_input_redirection(inp, r_in)
        outp = self.eval_cmd(command, inp)
        outp = self.handle_output_redirection(outp, r_out)
        return outp

    @staticmethod
    def handle_input_redirection(inp, r_in):
        for r in r_in:
            if inp == sys.stdin:
                inp = Application.read_lines(r)
            else:
                inp += Application.read_lines(r)
        return inp

    @staticmethod
    def handle_output_redirection(outp, r_out):
        for r in r_out:
            Application.write_lines(r, list(outp))
            outp = deque()
        return outp

    @staticmethod
    def get_return_val(outp):
        if outp == sys.stdin:
            return deque()
        return outp

    def eval_cmd(self, command, inp):
        app = command.get_app()
        args = command.get_args()
        outp = deque()

        if app[0] == "_" and app[1:] in self.appList:
            self.appList[app[1:]].run_unsafe(args, inp, outp)
            return outp
        elif app in self.appList:
            self.appList[app].run(args, inp, outp)
            return outp
        else:
            raise ValueError(f"unsupported application {app}")