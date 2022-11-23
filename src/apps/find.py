from application import Application
import os
from re import match


class Find(Application):
    def __init__(self):
        super().__init__()
        self.options = {"-name": 1}

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)

        directory = command_args[0] if len(command_args) > 0 else "."
        file_name_pattern = (
            options.get("-name")[0] if options.get("-name") is not None else None
        )

        self.find(directory, file_name_pattern, out)

    def find(self, path, file_pattern, out):
        file_pattern = (
            file_pattern.replace("*", ".*").rstrip() if file_pattern else None
        )

        for root, dirs, files in os.walk(path):
            for file in files:
                if not file_pattern or match(file_pattern, file.rstrip()):
                    out.append(os.path.join(root, file) + "\n")
