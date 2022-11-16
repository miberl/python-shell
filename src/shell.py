import sys
from os import getcwd

from shell_runner.shell import Shell


def eval(cmdline):
    shell = Shell()
    return shell.run_instructions(cmdline)


def main(argv):

    args_num = len(argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {argv[1]}")
        out = eval(argv[2])
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
        while True:
            print(getcwd() + "> ", end="")
            cmdline = input()
            out = eval(cmdline)
            while len(out) > 0:
                print(out.popleft(), end="")


if __name__ == "__main__":
    main(sys.argv)
