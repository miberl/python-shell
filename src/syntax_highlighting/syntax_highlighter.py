from os import getcwd


class shell_colours:
    APP = "\u001b[34;1m"
    FLAG = "\033[96m"
    PIPE = "\033[96m"
    REDIR_IN = "\033[96m"
    REDIR_OUT = "\033[96m"
    DIR = "\033[96m"
    FAIL = "\033[91m"
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
        words = code.split()
        new_code = ""
        previous_word = ""
        for word in words:
            if word.startswith("-"):
                new_code += shell_colours.FLAG + word + shell_colours.ENDC + " "
            elif word.startswith("|"):
                new_code += shell_colours.PIPE + word + shell_colours.ENDC + " "
            elif word.startswith("<"):
                new_code += shell_colours.REDIR_IN + word + shell_colours.ENDC + " "
            elif word.startswith(">"):
                new_code += shell_colours.REDIR_OUT + word + shell_colours.ENDC + " "
            else:
                new_code += shell_colours.ARG + word + shell_colours.ENDC + " "
            previous_word = word

        return new_code
