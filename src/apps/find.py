from application import Application
from exceptions.invalid_syntax_error import InvalidSyntaxError
import os
from re import match


class Find(Application):
    def __init__(self):
        super().__init__()
        self.options = {
            "-name" : 1 
        }

    def run(self, args, inpt, out) -> None:
        command_args, options = self.parse_args(args)
        
        directory = command_args[0] if len(command_args) > 0 else '.'
        file_name_pattern = options.get("-name")[0] if options.get("-name") is not None else None

        if file_name_pattern:
            self.find_with_name(directory, file_name_pattern, out)
        else:
            self.find(directory, out)

                
    def find(self, path, out):
        for root, dirs, files in os.walk(path):
            for file in files:
                out.append(os.path.join(root, file) + "\n")

    def find_with_name(self, path, file_pattern, out):
        file_pattern = file_pattern.replace("*", ".*")
        for root, dirs, files in os.walk(path):
            for file in files:
                if match(file_pattern.rstrip(), file.rstrip()):
                    out.append(os.path.join(root, file) + "\n")