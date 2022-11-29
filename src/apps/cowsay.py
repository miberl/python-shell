from application import Application

MAX_LINE_LENGTH = 39


class Cowsay(Application):
    def __init__(self) -> None:
        super().__init__()
        self.cow = [
            "        \   ^__^\n",
            "         \  (oo)\_______\n",
            "            (__)\       )\/\\\n",
            "                ||----w |\n",
            "                ||     ||\n",
        ]

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        lines = []
        if len(command_args) > 0:
            lines.extend(command_args)
        else:
            for line in inpt:
                lines.append(line)
        text_bubble = self.get_text_bubble(lines)
        out.extend(text_bubble)
        out.extend(self.cow)

    @staticmethod
    def get_text_bubble(lines):
        text_bubble = []
        wrapped_lines = Cowsay.wrap_lines(lines)
        max_line_length = Cowsay.max_line_length(wrapped_lines)
        line_separator = f" {'-' * (max_line_length+1)}"
        # print bubble
        text_bubble.append(line_separator)
        for i, line in enumerate(wrapped_lines):
            b1, b2 = Cowsay.get_border_brackets(i, len(wrapped_lines))
            text_bubble.append(f"{b1} {line}{' '*(max_line_length - len(line))}{b2}")
        text_bubble.append(line_separator)
        return [f"{line}\n" for line in text_bubble]

    @staticmethod
    def get_border_brackets(index, length):
        if length == 1:
            return "<", ">"
        if index == 0:
            return "/", "\\"
        if index == length - 1:
            return "\\", "/"
        return "|", "|"

    @staticmethod
    def max_line_length(lines):
        return max([len(line) for line in lines]) + 1

    @staticmethod
    def wrap_oversized_word(word):
        for i in range(0, len(word), MAX_LINE_LENGTH):
            yield word[i : i + MAX_LINE_LENGTH]

    @staticmethod
    def wrap_lines(lines):
        words = [word for l in lines for word in l.rstrip().split()]
        wrapped_lines, current_line = [], None

        for word in words:
            if len(word) > MAX_LINE_LENGTH:
                # word is too long
                for w in Cowsay.wrap_oversized_word(word):
                    if current_line:
                        wrapped_lines.append(current_line)
                    current_line = w
            elif current_line and len(current_line) + len(word) > MAX_LINE_LENGTH:
                # word is too long for current line
                wrapped_lines.append(current_line)
                current_line = word
            else:
                current_line = " ".join([current_line, word]) if current_line else word

        wrapped_lines.append(current_line)
        return wrapped_lines
