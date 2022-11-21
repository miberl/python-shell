from os import getcwd
from os.path import exists
from shell_runner.eval_instructions import EvalInstructions


class shell_colours:
    APP = "\u001b[36m"  # dark blue
    FLAG = "\u001b[35;1m"  # magenta
    PIPE = "\033[96m"
    REDIR_IN = "\033[96m"
    REDIR_OUT = "\033[96m"
    DIR = "\033[92m"  # green
    FAIL = "\u001b[31m"  # red
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"

    LINE_CLEAR = "\x1b[2K"
    LINE_UP = "\033[1A"


class syntax_highlighter:
    def take_input(self):
        cwd = getcwd()
        print(cwd + "> ", end="")
        code = input()
        print(shell_colours.LINE_UP, end=shell_colours.LINE_CLEAR)
        print(cwd + "> " + self.highlight_code(code))
        return code

    def highlight_code(self, code) -> str:
        has_space = code.endswith(" ")
        apps = self.get_apps_from_eval(EvalInstructions())
        words = code.split()
        new_code = ""
        for word in words:
            if word in apps:
                new_code += self.highlight_app(word)
            elif exists(word) and ("/" in word or "\\" in word or word == "."):
                new_code += self.highlight_directory(word)
            elif word.startswith("-"):
                new_code += self.highlight_flag(word)
            elif word.startswith("|"):
                new_code += self.highlight_pipe(word)
            elif word.startswith("<"):
                new_code += self.highlight_redir_in(word)
            elif word.startswith(">"):
                new_code += self.highlight_redir_out(word)
            else:
                new_code += word + " "
        if new_code.endswith(" ") and not has_space:
            new_code = new_code[:-1]
        return new_code

    def get_apps_from_eval(self, eval):
        return eval.appList.keys()

    def highlight_app(self, word):
        return shell_colours.APP + word + shell_colours.ENDC + " "

    def highlight_directory(self, word):
        return (
            shell_colours.UNDERLINE
            + shell_colours.DIR
            + word
            + shell_colours.ENDC
            + " "
        )

    def highlight_flag(self, word):
        return shell_colours.FLAG + word + shell_colours.ENDC + " "

    def highlight_pipe(self, word):
        return shell_colours.PIPE + word + shell_colours.ENDC + " "

    def highlight_redir_in(self, word):
        return shell_colours.REDIR_IN + word + shell_colours.ENDC + " "

    def highlight_redir_out(self, word):
        return shell_colours.REDIR_OUT + word + shell_colours.ENDC + " "
