from exceptions.command_construct_error import InstructionConstructError


class Command:
    def __init__(self, app: str):
        self.app = app
        self.args = []
        self.redir_in = None
        self.redir_out = None

    def add_arg(self, arg: str) -> None:
       self.args.append(arg)

    def add_redir_in(self, file: str) -> None:
        self.redir_in = file

    def add_redir_out(self, file: str) -> None:
        self.redir_out = file

    def get_args(self) -> [str]:
        return self.args

    def get_redirs(self) -> (str, str):
        return self.redir_in, self.redir_out

    def get_app(self) -> str:
        return self.app


class Instruction:
    def __init__(self):
        self.commands = []

    def add(self, command: Command) -> None:
        if type(command) is not Command:
            raise InstructionConstructError("Expected command when adding to instruction")

        self.commands.append(command)

    def get_next_command(self) -> Command:
        self.throw_if_either_is_none()
        return self.commands.pop(0)

    def has_next(self) -> bool:
        return len(self.commands) != 0

    def throw_if_either_is_none(self) -> None:
        if not self.commands:
            raise InstructionConstructError("No command in instruction")
