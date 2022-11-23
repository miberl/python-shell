import os
from abc import ABC, abstractmethod
from exceptions.unexpected_argument_error import UnexpectedArgumentError
from exceptions.unknown_option_error import UnknownFlagError


class Application(ABC):
    """
    NAME Application DESCRIPTION Encapsulate common application interface and
    provide common utility methods that engage with external components,
    such as the file system.
    """

    def __init__(self) -> None:
        self.options = dict()

    @abstractmethod
    def run(self, args, inpt, out):  # pragma: no cover
        """
        Runs an app. Out parameter is overwritten, essentially acts as output.

        :param args: string list of arguments provided to the application
        :param inpt: queue drawn from stdin or from input redirection
        :param out: output queue, populated in running of an app.
        :return: None
        """
        pass

    def run_unsafe(self, args, inpt, out):
        """Runs the unsafe version of an app, see run()"""
        try:
            self.run(args, inpt, out)
        except Exception as e:
            out.append(str(e))

    @classmethod
    def read_lines(cls, filename):
        with open(filename) as f:
            return f.readlines()

    @classmethod
    def write_lines(cls, file, lines):
        with open(file, "w") as f:
            f.writelines(lines)

    @classmethod
    def get_dir_contents(cls, top: str):
        return next(os.walk(top))

    def parse_args(self, args):
        """
        parses provided arguments, returns a tuple of (command_args, options)
        where command args is a list of leading and trailing arguments that
        are not options
        """
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
                # trailing command options, if available.
                command_args.extend(self.check_no_flags(args[i:]))
                break

        return command_args, options

    @classmethod
    def is_option_flag(cls, arg):
        return arg[0] == '-'

    @classmethod
    def check_no_flags(cls, args):
        for arg in args:
            if Application.is_option_flag(arg):
                raise UnexpectedArgumentError(arg)
        return args
