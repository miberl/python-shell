from abc import ABC, abstractmethod
from exceptions.unexpected_argument_error import UnexpectedArgumentError
from exceptions.unknown_option_error import UnknownFlagError

class Application(ABC):
    def __init__(self) -> None:
        self.options = dict()

    @abstractmethod
    def run(self, args, inpt, out):
        pass

    @classmethod
    def read_lines(cls, filename):
        with open(filename) as f:
            return f.readlines()

    @classmethod
    def read_file(cls, filename):
        with open(filename) as f:
            return f.read()

    @classmethod
    def write_lines(cls, file, lines):
        with open(file, 'w') as f:
            f.writelines(lines)
    

    # parses provided arguments, returns a tuple of (command_args, options)
    # where command args is a list of leading and trailing arguments that are not options
    def parse_args(self, args):
        command_args = []
        options = dict()
        i = 0 

        # leading command options
        while i < len(args):
            if self.is_option_flag(args[i]):
                break 
            command_args.append(args[i])
            i += 1
        
        while i < len(args):
            if args[i] in self.options:
                options[args[i]] = Application.check_no_flags(
                    args[i + 1:i + self.options[args[i]] + 1])
                i += self.options[args[i]] + 1
            elif self.is_option_flag(args[i]):
                raise UnknownFlagError(args[i])
            else:
                #trailing command options, if available.
                command_args.extend(self.check_no_flags(args[i:]))
                break

        return (command_args, options)

    @classmethod
    def is_option_flag(cls, arg):
        return arg[0] == '-'

    @classmethod
    def check_no_flags(cls, args):
        for arg in args:
            if Application.is_option_flag(arg):
                raise UnexpectedArgumentError(arg)
        return args