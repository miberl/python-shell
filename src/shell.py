import sys
from collections import deque
from os import getcwd

from shell_runner.shell_exec import ShellExec
from syntax_highlighting.syntax_highlighter import syntax_highlighter


class Shell:
    """
    NAME
        Shell
    DESCRIPTION
        Used to run the shell, either as a REPL or by providing arguments
    METHODS
        Shell().main
            Runs the shell, provided with commandline arguments
    """
    def __init__(self) -> None:
        self.shell = ShellExec()

    def _eval(self, cmdline: str) -> deque:
        return self.shell.run_instructions(cmdline)

    def main(self, argv: [str]) -> None:
        """
        Method used to run shell
        :param argv: Command line arguments, either empty (for REPL) or -c followed by a command string
        :return: Returns Noting, prints results
        """
        args_num = len(argv) - 1
        if args_num > 0:
            self._execute_from_args(args_num, argv)
        else:
            self._repl()

    def _execute_from_args(self, args_num: int, argv: [str]) -> None:
        self._check_args(args_num, argv)
        out = self._eval(argv[2])
        self._display(out)

    @staticmethod
    def _check_args(args_num, argv) -> None:
        """:raises ValueErorr:"""

        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {argv[1]}")

    def _repl(self) -> None:
        while True:
            cmdline = self._read()
            out = self._eval(cmdline)
            self._display(out)

    @staticmethod
    def _read() -> str:
        sh = syntax_highlighter()
        cmdline = sh.take_input()
        return cmdline

    @staticmethod
    def _display(out: deque) -> None:
        while len(out) > 0:
            print(out.popleft(), end="")


def main():
    shell = Shell()
    shell.main(sys.argv)


if __name__ == "__main__":
    main()
