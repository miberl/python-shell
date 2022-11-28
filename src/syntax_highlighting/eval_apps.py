from os import getcwd
from os.path import exists
from shell_runner.eval_instructions import EvalInstructions
from re import findall


class ShellColours:
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


class SyntaxHighlighter:
    def highlight_input(self, code):  # pragma nocover
        print(ShellColours.LINE_UP, end=ShellColours.LINE_CLEAR)
        print(getcwd() + "> " + self._highlight_code(code))

    def _highlight_code(self, code) -> str:
        has_space = code.endswith(" ")
        apps = self._get_apps_from_eval(EvalInstructions())
        words = code.split()
        new_code = ""
        word_num = 0
        tokens = findall("\s+", code)
        spaces = [0]
        for token in tokens:
            spaces.append(len(token))
        for word in words:
            new_code += spaces[word_num] * " "
            word_num += 1
            new_code = self._highligh_words(apps, new_code, word)
        if new_code.endswith(" ") and not has_space:
            new_code = new_code[:-1]
        return new_code

    def _highligh_words(self, apps, new_code, word):
        if word in apps:
            new_code += self._highlight_app(word)
        elif exists(word) and ("/" in word or "\\" in word or word == "."):
            new_code += self._highlight_directory(word)
        elif word.startswith("-"):
            new_code += self._highlight_flag(word)
        elif word.startswith("|"):
            new_code += self._highlight_pipe(word)
        elif word.startswith("<"):
            new_code += self._highlight_redir_in(word)
        elif word.startswith(">"):
            new_code += self._highlight_redir_out(word)
        else:
            new_code += word
        return new_code

    @staticmethod
    def _get_apps_from_eval(eval_obj):
        return eval_obj.appList.keys()

    @staticmethod
    def _highlight_app(word):
        return ShellColours.APP + word + ShellColours.ENDC

    @staticmethod
    def _highlight_directory(word):
        return ShellColours.UNDERLINE + ShellColours.DIR + word + ShellColours.ENDC

    @staticmethod
    def _highlight_flag(word):
        return ShellColours.FLAG + word + ShellColours.ENDC

    @staticmethod
    def _highlight_pipe(word):
        return ShellColours.PIPE + word + ShellColours.ENDC

    @staticmethod
    def _highlight_redir_in(word):
        return ShellColours.REDIR_IN + word + ShellColours.ENDC

    @staticmethod
    def _highlight_redir_out(word):
        return ShellColours.REDIR_OUT + word + ShellColours.ENDC
