import sys
from os import getcwd
from collections import deque

from shell_runner.shell_exec import ShellExec

class Shell:
    def __init__(self) -> None:
        self.shell = ShellExec()

    def eval(self, cmdline, out):
        self.shell.run_instructions(cmdline, out)

    def main(self, argv):

        args_num = len(argv) - 1
        if args_num > 0:
            out = deque()
            if args_num != 2:
                raise ValueError("wrong number of command line arguments")
            if argv[1] != "-c":
                raise ValueError(f"unexpected command line argument {argv[1]}")
            self.eval(argv[2], out)
            while len(out) > 0:
                print(out.popleft(), end="")
        else:
            while True:
                print(getcwd() + "> ", end="")
                cmdline = input()
                out = deque()
                self.eval(cmdline, out)
                while len(out) > 0:
                    print(out.popleft(), end="")


if __name__ == "__main__":
    shell = Shell()
    shell.main(sys.argv)

