from exceptions.command_construct_error import CommandConstructError


class Command:
    def __init__(self, app: str):
        self.app = app
        self.args = []
        self.redir_in = None
        self.redir_out = None

    def add_arg(self, arg: str) -> None:
        if self.no_existing_flags():
            self.add_arg_to_end(arg)
        else:
            self.add_arg_to_flag_args(arg)

    def add_arg_to_end(self, arg: str) -> None:
        self.args.append((None, [arg]))

    def add_arg_to_flag_args(self, arg: str) -> None:
        self.args[-1][1].append(arg)

    def no_existing_flags(self) -> bool:
        return len(self.args) == 0

    def add_flag(self, flag: str) -> None:
        self.args.append((flag, []))

    def add_redir_in(self, file: str) -> None:
        self.redir_in = file

    def add_redir_out(self, file: str) -> None:
        self.redir_out = file

    def get_flags_and_args(self) -> list[tuple[str, list[str]]]:
        return self.args

    def get_redirs(self) -> list[str, str]:
        return self.redir_in, self.redir_out

    def get_app(self) -> str:
        return self.app


class Pipe:
    def __init__(self):
        self.left = None
        self.right = None

    def set_left(self, left: Command) -> None:
        self.throw_if_not_command(left)
        self.left = left

    def set_right(self, right: Command) -> None:
        self.throw_if_not_command(right)
        self.right = right

    @staticmethod
    def throw_if_not_command(pipe_obj: Command) -> None:
        if type(pipe_obj) is not Command:
            raise CommandConstructError("Bad object in pipe")

    def get_piped_commands(self) -> tuple[Command, Command]:
        self.throw_if_either_is_none()
        return self.left, self.right

    def throw_if_either_is_none(self) -> None:
        if self.left is None or self.right is None:
            raise CommandConstructError("Pipe accessed before commands populated")
