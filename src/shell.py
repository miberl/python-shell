import sys
from os import getcwd
from collections import deque

from apps import cat, cd, echo, grep, head, ls, pwd, tail
from shell_runner.shell import Shell

appList = {'cat': cat.Cat(), 'cd': cd.Cd(), 'echo': echo.Echo(), 'grep': grep.Grep(
), 'head': head.Head(), 'ls': ls.Ls(), 'pwd': pwd.Pwd(), 'tail': tail.Tail()}


def eval(cmdline, out):
    shell = Shell()
    shell.run_instructions(cmdline, out)


def main(argv):

    args_num = len(argv) - 1
    if args_num > 0:
        out = deque()
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {argv[1]}")
        eval(argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
        while True:
            print(getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            eval(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")


if __name__ == "__main__":
    main(sys.argv)
