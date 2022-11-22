import readline
from os import getcwd
from os import listdir
import platform
from shell_runner.eval_instructions import EvalInstructions

complete_options = []


def get_apps_from_eval():
    return EvalInstructions().appList.keys()


def get_files_and_directories():
    return listdir()


def get_complete_options():
    complete_options = []
    for app in get_apps_from_eval():
        complete_options.append(app)
    for file in get_files_and_directories():
        complete_options.append(file)
    return complete_options


# rus when user presses tab
def completer(text, state):
    options = [x for x in complete_options if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None


def take_input():
    # does not work on windows
    if platform.system() != "Windows":
        global complete_options
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")
        complete_options = get_complete_options()
    # no autocompletion on windows
    code = input(getcwd() + "> ")
    return code
