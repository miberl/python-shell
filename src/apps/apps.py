import os
from os import listdir


def pwd(args, out) -> None:
    out.append(os.getcwd())


def cd(args, out) -> None:
    if len(args) == 0 or len(args) > 1:
        raise ValueError("wrong number of command line arguments")
    os.chdir(args[0])


def echo(args, out) -> None:
    out.append(" ".join(args) + "\n")


def ls(args, out) -> None:
    if len(args) == 0:
        ls_dir = os.getcwd()
    elif len(args) > 1:
        raise ValueError("wrong number of command line arguments")
    else:
        ls_dir = args[0]
    for f in listdir(ls_dir):
        if not f.startswith("."):
            out.append(f + "\n")


def cat(args, out) -> None:
    for a in args:
        with open(a) as f:
            out.append(f.read())


def head(args, out) -> None:
    if len(args) != 1 and len(args) != 3:
        raise ValueError("wrong number of command line arguments")
    if len(args) == 1:
        num_lines = 10
        file = args[0]
    if len(args) == 3:
        if args[0] != "-n":
            raise ValueError("wrong flags")
        else:
            num_lines = int(args[1])
            file = args[2]
    with open(file) as f:
        lines = f.readlines()
        for i in range(0, min(len(lines), num_lines)):
            out.append(lines[i])


def tail(args, out) -> None:
    if len(args) != 1 and len(args) != 3:
        raise ValueError("wrong number of command line arguments")
    if len(args) == 1:
        num_lines = 10
        file = args[0]
    if len(args) == 3:
        if args[0] != "-n":
            raise ValueError("wrong flags")
        else:
            num_lines = int(args[1])
            file = args[2]
    with open(file) as f:
        lines = f.readlines()
        display_length = min(len(lines), num_lines)
        for i in range(0, display_length):
            out.append(lines[len(lines) - display_length + i])


def grep(args, out) -> None:
    if len(args) < 2:
        raise ValueError("wrong number of command line arguments")
    pattern = args[0]
    files = args[1:]
    for file in files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if re.match(pattern, line):
                    if len(files) > 1:
                        out.append(f"{file}:{line}")
                    else:
                        out.append(line)
