from os import getcwd


class shell_colours:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    FLAG = "\033[96m"
    APP = "\033[96m"
    ARG = "\033[96m"
    PIPE = "\033[96m"
    REDIR_IN = "\033[96m"
    REDIR_OUT = "\033[96m"


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
        new_code = self.highlight_app(new_code)
        new_code = self.highlight_flags(code)
        return new_code

    def highlight_flags(self, code) -> str:
        words = code.split()
        new_code = ""
        for word in words:
            if word.startswith("-"):
                new_code += shell_colours.FLAG + word + shell_colours.ENDC + " "
            else:
                new_code += word + " "
        return new_code

    def highlight_app(self, code) -> str:
        words = code.split()
        new_code = ""
        words[0] = shell_colours.APP + words[0] + shell_colours.ENDC
        for word in words:
            new_code += word + " "
        return new_code
