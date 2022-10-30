from exceptions.command_construct_error import CommandConstructError


class Command:
    def __init__(self, app):
        self.app = app
        self.args = []
        self.redir_in = None
        self.redir_out = None

    def add_arg(self, arg):
        if len(self.args) == 0:
            self.args.append((None, [arg]))
        else:
            self.args[-1][1].append(arg)

    def add_flag(self, flag):
        self.args.append((flag, []))

    def add_redir_in(self, file):
        self.redir_in = file

    def add_redir_out(self, file):
        self.redir_out = file

    def get_flags_and_args(self):
        return self.args

    def get_redirs(self):
        return self.redir_in, self.redir_out

    def get_app(self):
        return self.app


class Pipe:
    def __init__(self):
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = self.check_pipe(left)

    def set_right(self, right):
        self.right = self.check_pipe(right)

    @staticmethod
    def check_pipe(pipe_obj):
        match  pipe_obj:
            case Command():
                return pipe_obj
            case _:
                raise CommandConstructError("Bad object in pipe")

    def get_piped_commands(self):
        if self.left is None or self.right is None:
            raise CommandConstructError("Pipe accessed before commands populated")
        return self.left, self.right
