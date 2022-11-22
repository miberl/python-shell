import sys
from collections import deque

from shell_runner.shell_exec import ShellExec
from syntax_highlighting.syntax_highlighter import syntax_highlighter
from interactive_input.autocompleter import take_input


class Shell:
    def __init__(self) -> None:
        self.shell = ShellExec()

    def eval(self, cmdline: str) -> deque:
        return self.shell.run_instructions(cmdline)

    def main(self, argv):

        args_num = len(argv) - 1
        if args_num > 0:
            if args_num != 2:
                raise ValueError("wrong number of command line arguments")
            if argv[1] != "-c":
                raise ValueError(f"unexpected command line argument {argv[1]}")
            out = self.eval(argv[2])
            while len(out) > 0:
                print(out.popleft(), end="")
        else:
            while True:
                sh = syntax_highlighter()
                cmdline = take_input()
                sh.highlight_and_print_code(cmdline)
                out = self.eval(cmdline)
                while len(out) > 0:
                    print(out.popleft(), end="")


if __name__ == "__main__":
    shell = Shell()
    shell.main(sys.argv)
