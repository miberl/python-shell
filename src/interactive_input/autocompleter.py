from os import getcwd

# from os import listdir
import os
import platform
from shell_runner.eval_instructions import EvalInstructions

successful_import = True


def supported_platform():
    return platform.system() == "Darwin" or platform.system() == "Linux"


if supported_platform():  # pragma: no cover
    try:
        import readline
    except ImportError:
        successful_import = False

complete_options = []


def get_apps_from_eval():  # pragma: no cover
    return EvalInstructions().appList.keys()


def get_path_with_no_last_word(path):
    # example: /home/user -> /home/
    if "/" in path:
        dirs = path.split("/")
        complete_dir = ""
        for i in range(0, len(dirs) - 1):
            complete_dir += dirs[i] + "/"
        return complete_dir
    else:
        return path


def is_unfinished_path(path):
    # example: /home/us -> where /home is a valid directory
    if "/" in path:
        if os.path.isdir(get_path_with_no_last_word(path)):
            return True
    return False


def last_word_is_path(code):
    # example: /home/user would return user is a path
    if code == "":
        return False
    if not code.endswith(" "):
        if is_unfinished_path(code.split()[-1]):
            return True
    return False


def get_last_word_in_code(code):
    # example: echo aa bb -> bb or cd ./aa/bb -> bb
    if code.endswith(" "):
        return ""
    if code == "":
        return ""
    if "/" in code.split()[-1]:
        return code.split()[-1].split("/")[-1]
    else:
        return code.split()[-1]


def get_complete_options(code):
    complete_options = []

    # try to add files and directories
    if last_word_is_path(code):
        last_word = code.split()[-1]
        for file in os.listdir(get_path_with_no_last_word(last_word)):
            if os.path.isdir(get_path_with_no_last_word(last_word) + file):
                complete_options.append(file + "/")
            else:
                complete_options.append(file)
    else:
        # apps should always be if there is no path
        for app in get_apps_from_eval():
            complete_options.append(app)

        for file in os.listdir():
            if os.path.isdir(file):
                complete_options.append(file + "/")
            else:
                complete_options.append(file)

    return complete_options


# rus when user presses tab
def completer(text, state):
    complete_options = get_complete_options(readline.get_line_buffer())
    last_word = get_last_word_in_code(readline.get_line_buffer())
    options = [x for x in complete_options if x.startswith(last_word)]
    try:
        return options[state]
    except IndexError:  # pragma: no cover
        return None


def take_input():  # pragma: no cover
    # does not work on windows
    if successful_import and (
        platform.system() == "Darwin" or platform.system() == "Linux"
    ):
        global complete_options
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")
    # no autocompletion on windows
    code = input(getcwd() + "> ")
    return code
