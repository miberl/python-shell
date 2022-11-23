from exceptions.command_construct_error import InstructionConstructError


class Command:
    """
    NAME
        Command
    DESCRIPTION
        Object to store information related to a single command.
        Purely for data representation, no execution or evaluation.
    """
    def __init__(self, app: str):
        """
        Initialises a command object with an app of given name

        :param app: Name of the app to initialise the command object with
        """
        self.app = app
        self.args = []
        self.redir_in = []
        self.redir_out = []

    def add_arg(self, arg: str) -> None:
        """
        Adds an arg (or flag) to the command object, must be added in correct
        order

        :param arg: String of the argument, either a flag or an argument
        :return: None
        """
        self.args.append(arg)

    def add_redir_in(self, file: str) -> None:
        """
        Add a file for input redirection. May add multiple, but must be done
        in order.

        :param file: String defining the name/path of the file to be used as
        input
        :return: None
        """
        self.redir_in.append(file)

    def add_redir_out(self, file: str) -> None:
        """
        Add a file for output redirection. May add multiple. Output is not
        written to stdout if one or more included

        :param file: String defining the name/path of the file to be used as
        output
        :return: None
        """
        self.redir_out.append(file)

    def get_args(self) -> [str]:
        """
        Gives the ordered array of arguments. Note no distinction between
        flags and args is made here.

        :return: List of string arguments
        """
        return self.args

    def get_redirs(self) -> ([str], [str]):
        """
        Gives a tuple of a list file paths provided for input and output
        redirections.

        :return: Pair; First element -> list of input redirections, Second
        element -> list of output redirections
        """
        return self.redir_in, self.redir_out

    def get_app(self) -> str:
        """
        Returns the app assigned to the command at instantiation

        :return: String of the app name
        """
        return self.app


class Instruction:
    """
    NAME Instruction DESCRIPTION Holds one or more commands in an object,
    that are intended to be piped together.
    """
    def __init__(self):
        self.commands = []

    def add(self, command: Command) -> None:
        """
        Adds a command to the internal list of the instruction object

        :param command: Command object to be added, must be added in order
        :return: None
        """
        if type(command) is not Command:
            raise InstructionConstructError("Expected command when adding to "
                                            "instruction")

        self.commands.append(command)

    def get_next_command(self) -> Command:
        """
        Gets the next command in the internal list and removes it from that list

        :return: Command object, removed from list
        :raises InstructionConstructError: If internal command list is empty
        """
        self._throw_if_either_is_none()
        return self.commands.pop(0)

    def has_next(self) -> bool:
        """
        Returns true if the internal list has more command objects,
        false otherwise.

        :return: Boolean value indicating if more commands can be gotten
        """
        return len(self.commands) != 0

    def _throw_if_either_is_none(self) -> None:
        if not self.commands:
            raise InstructionConstructError("No command in instruction")
