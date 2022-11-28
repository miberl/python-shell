from os import getcwd
from os import listdir
from os.path import isdir
import platform
from shell_runner.eval_instructions import EvalInstructions

successfull_import = True

if platform.system() == "Darwin" or platform.system() == "Linux":
    try:
        import readline
    except ImportError:
        successfull_import = False

complete_options = []


def get_apps_from_eval():
    return EvalInstructions().appList.keys()


def get_path_with_no_last_word(path):
    if "/" in path:
        dirs = path.split("/")
        complete_dir = ""
        for i in range(0, len(dirs) - 1):
            complete_dir += dirs[i] + "/"
        return complete_dir
    else:
        return path


def is_unfinished_path(path):
    if "/" in path:
        if isdir(get_path_with_no_last_word(path)):
            return True
    return False


def last_word_is_path(code):
    if code == "":
        return False
    if not code.endswith(" "):
        if is_unfinished_path(code.split()[-1]):
            return True
    return False


def get_complete_options(code):
    complete_options = []

    # try to add files and directories
    if last_word_is_path(code):
        last_word = code.split()[-1]
        for file in listdir(get_path_with_no_last_word(last_word)):
            if isdir(get_path_with_no_last_word(last_word) + file):
                complete_options.append(file + "/")
            else:
                complete_options.append(file)
    else:
        # apps should always be if there is no path
        for app in get_apps_from_eval():
            complete_options.append(app)

        for file in listdir():
            if isdir(file):
                complete_options.append(file + "/")
            else:
                complete_options.append(file)

    return complete_options


def get_last_word_in_code(code):
    if code.endswith(" "):
        return ""
    if code == "":
        return ""
    if "/" in code.split()[-1]:
        return code.split()[-1].split("/")[-1]
    else:
        return code.split()[-1]


# rus when user presses tab
def completer(text, state):
    complete_options = get_complete_options(readline.get_line_buffer())
    new_text = get_last_word_in_code(readline.get_line_buffer())
    options = [x for x in complete_options if x.startswith(new_text)]
    try:
        return options[state]
    except IndexError:
        return None


def take_input():
    # does not work on windows
    if successfull_import and (
        platform.system() == "Darwin" or platform.system() == "Linux"
    ):
        global complete_options
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")
    # no autocompletion on windows
    code = input(getcwd() + "> ")
    return code
