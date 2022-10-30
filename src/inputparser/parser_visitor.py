from exceptions.command_construct_error import CommandConstructError
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.command import Command, Pipe
from antlr4.tree import Tree


class ParseVisitor(CommandsVisitor):
    def __init__(self):
        self.instructions = []

    def get_commands(self) -> [(str, [])]:
        commands = []

        for instruction in self.instructions:
            if type(instruction) is Command:
                app, args = self.construct_new_command_pair(instruction)
                commands.append((app, args))
            else:
                raise NotImplementedError()

        return commands

    def construct_new_command_pair(self, instruction) -> (str, []):
        app = instruction.get_app()
        flags = instruction.get_flags_and_args()
        args = self.expand_flags_to_flat_arr(flags)

        return app, args

    @staticmethod
    def expand_flags_to_flat_arr(flags) -> []:
        args = []
        for flag, flag_args in flags:
            if flag is not None:
                args.append('-' + flag)
            args += flag_args

        return args

    def get_instructions(self) -> []:
        return self.instructions

    def visitInstuctions(self, ctx: CommandsParser.InstuctionsContext) -> None:
        # Instruction has one or zero children; a pipe or two commands

        if len(ctx.children) == 2:
            new_instruction = self.try_for_pipe(ctx.children)
        elif len(ctx.children) == 1:
            new_instruction = self.try_for_command(ctx.children)
        else:
            raise CommandConstructError("Bad number of children for instruction")

        self.instructions.append(new_instruction)

    def try_for_pipe(self, children) -> Pipe:
        # Create a new pipe object with two commands as children

        new_pipe = Pipe()
        self.try_set_left_pipe(children[0], new_pipe)
        new_pipe.set_right(self.try_for_command([children[1]]))

        return new_pipe

    def try_set_left_pipe(self, ctx, new_pipe) -> None:
        # If command on left branch, add this to the new pipe object

        if type(ctx) is CommandsParser.PipeContext:
            new_pipe.set_left(self.try_for_command(ctx.children))
        else:
            self.check_terminator_or_error(ctx, "Expected pipe for instruction with two children")

    def try_for_command(self, children: []) -> Command:
        # Expecting command in the provided list of children

        for child in children:
            if type(child) is CommandsParser.CommandContext:
                return self.get_command(children[0])
            else:
                self.check_terminator_or_error(child, "Expected command after instruction or pipe")

        raise CommandConstructError("Expected command after instruction or pipe")

    def get_command(self, ctx) -> Command:
        # CTX is a command node, should create command object from this

        cmd = self.try_init_command_with_name(ctx)

        for child in ctx.children[1:]:
            self.enumerate_possible_children_following_name(child, cmd)

        return cmd

    def enumerate_possible_children_following_name(self, ctx, cmd) -> None:
        # Given a command object, with just a name, populate the
        # remaining fields of the command object (args, redir etc)

        if type(ctx) is CommandsParser.ArgsContext:
            self.get_args(ctx, cmd)
        else:
            self.check_for_redir_command(ctx, cmd)

    def check_for_redir_command(self, ctx, cmd) -> None:
        # While constructing a command object, check for redirs at a node

        if type(ctx) is CommandsParser.Redir_inContext:
            cmd.add_redir_in(self.search_for_atom(ctx))
        elif type(ctx) is CommandsParser.Redir_outContext:
            cmd.add_redir_out(self.search_for_atom(ctx))
        else:
            self.check_terminator_or_error(ctx, "Unexpected child of command")

    def try_init_command_with_name(self, ctx) -> Command:
        # Check if the ctx node is a command node
        cmd = None

        if type(ctx.children[0]) is CommandsParser.AppContext:
            cmd = Command(self.get_app_name(ctx.children[0]))
        else:
            self.check_terminator_or_error(ctx.childen[0], "No command could be constructed")
        return cmd

    def get_app_name(self, ctx) -> str:
        if len(ctx.children) != 1:
            raise CommandConstructError("Bad app name node, expected single atom")

        return self.search_for_atom(ctx)

    def get_args(self, ctx, cmd) -> None:
        # From an args node, add all subsequent flags and arguments to a command object

        for child in ctx.children:
            if type(child) is CommandsParser.ArgContext:
                arg = self.search_for_atom(child)
                cmd.add_arg(arg)
            elif type(child) is CommandsParser.FlagContext:
                flag = self.search_for_atom(child)
                cmd.add_flag(flag)
            else:
                self.check_terminator_or_error(child, "Unexpected child of args")

    @staticmethod
    def check_terminator_or_error(ctx, err_msg) -> None:
        # Very common pattern, check if the current node is either whitespace, or otherwise throw an error

        if type(ctx) is not Tree.TerminalNodeImpl:
            raise CommandConstructError(err_msg)

    def search_for_atom(self, ctx) -> str:
        # We think there is an atom (text) in ctx.children

        arg = None
        for child in ctx.children:
            if type(child) is CommandsParser.AtomContext:
                arg = self.set_arg(arg, child)
            else:
                self.check_terminator_or_error(child, "Unexpected node while searching for atom")

        self.error_if_arg_not_assigned(arg)

        return arg

    @staticmethod
    def error_if_arg_not_assigned(arg) -> None:
        if arg is None:
            raise CommandConstructError("®Expected atom, found none")

    def set_arg(self, arg, child) -> str:
        if arg is not None:
            raise CommandConstructError("Expected single atom at search, got multiple")
        arg = self.process_atom(child)
        return arg

    def process_atom(self, ctx) -> str:
        # Get string from atom object

        if type(ctx.children[0]) is Tree.TerminalNodeImpl:
            return ctx.children[0].symbol.text
        else:
            raise NotImplementedError()
