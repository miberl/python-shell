import sys
from collections import deque

from application import Application
from apps import cat, cd, echo, grep, head, ls, pwd, tail, uniq, cut, sort, find, wc

from inputparser.command import Instruction


class EvalInstructions:
    """
    NAME
        EvalInstructions
    DESCRIPTION
        Takes a list of instructions and returns the string that those instructions evaluate to.
    METHODS
        EvalInstructions.eval()
            Evaluates each of the provided instructions and returns a deque() object
    """
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
            "wc": wc.Wc()
        }

    def eval(self, instructions: [Instruction]) -> deque:
        """
        Evaluates instructions to a string

        :param instructions: List of instructions to be evaluated
        :return: deque object representing result of execution of instructions
        """
        if not instructions:
            return deque()

        outp = deque()
        for instruction in instructions:
            outp += self._run_one_instruction(instruction)

        return outp

    def _run_one_instruction(self, instruction: Instruction) -> deque:
        inp = sys.stdin
        while instruction.has_next():
            inp = self._run_command(inp, instruction)
        if inp == sys.stdin:
            return deque()
        return inp

    def _run_command(self, inp, instruction):
        command = instruction.get_next_command()
        r_in, r_out = command.get_redirs()
        inp = self._handle_input_redirection(inp, r_in)
        outp = self._eval_cmd(command, inp)
        outp = self._handle_output_redirection(outp, r_out)
        return outp

    @staticmethod
    def _handle_input_redirection(inp, r_in):
        for r in r_in:
            if inp == sys.stdin:
                inp = Application.read_lines(r)
            else:
                inp += Application.read_lines(r)
        return inp

    @staticmethod
    def _handle_output_redirection(outp, r_out):
        for r in r_out:
            Application.write_lines(r, list(outp))
            outp = deque()
        return outp

    def _eval_cmd(self, command, inp):
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
