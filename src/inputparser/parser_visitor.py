from exceptions.command_construct_error import CommandConstructError
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.command import Command, Pipe
from antlr4.tree import Tree


class ParseVisitor(CommandsVisitor):
    def __init__(self):
        self.instructions = []

    def get_commands(self):
        commands = []

        for instruction in self.instructions:
            match instruction:
                case Command():
                    app = instruction.get_app()
                    flags = instruction.get_flags_and_args()
                    args = []
                    for flag, flag_args in flags:
                        if flag is not None:
                            args.append('-' + flag)
                        args += flag_args
                    commands.append((app, args))
                case _:
                    raise NotImplementedError()

        return commands

    def get_instructions(self):
        return self.instructions

    def visitInstuctions(self, ctx: CommandsParser.InstuctionsContext):
        # Instruction has one or zero children; a pipe or two commands

        if len(ctx.children) == 2:
            new_instruction = self.try_for_pipe(ctx.children)
        elif len(ctx.children) == 1:
            new_instruction = self.try_for_command(ctx.children)
        else:
            raise CommandConstructError("Bad number of children for instruction")

        self.instructions.append(new_instruction)

    def try_for_pipe(self, children):
        new_pipe = Pipe()

        match children[0]:
            case CommandsParser.PipeContext():
                new_pipe.set_left(self.try_for_command(children[0].children))
            case Tree.TerminalNodeImpl():
                pass
            case _:
                raise CommandConstructError("Expected pipe for instruction with two children")
        new_pipe.set_right(self.try_for_command([children[1]]))

        return new_pipe

    def try_for_command(self, children):
        for child in children:
            match child:
                case CommandsParser.CommandContext():
                    return self.get_command(children[0])
                case Tree.TerminalNodeImpl():
                    pass
                case _:
                    raise CommandConstructError("Expected command after instruction or pipe")

    def get_command(self, ctx) -> Command:
        cmd = None
        match ctx.children[0]:
            case CommandsParser.AppContext():
                cmd = Command(self.get_app_name(ctx.children[0]))
            case Tree.TerminalNodeImpl():
                pass
            case _:
                raise CommandConstructError("No command could be constructed")

        for child in ctx.children[1:]:
            match child:
                case CommandsParser.ArgsContext():
                    self.get_args(child, cmd)
                case CommandsParser.Redir_inContext():
                    re_in = self.search_for_atom(child)
                    cmd.add_redir_in(re_in)
                case CommandsParser.Redir_outContext():
                    re_out = self.search_for_atom(child)
                    cmd.add_redir_out(re_out)
                case Tree.TerminalNodeImpl():
                    pass
                case _:
                    raise CommandConstructError("Unexpected child of command")

        return cmd

    def get_app_name(self, ctx) -> str:
        if len(ctx.children) != 1:
            raise CommandConstructError("Bad app name node, expected single atom")
        return self.search_for_atom(ctx)

    def get_args(self, ctx, cmd):
        for child in ctx.children:
            match child:
                case CommandsParser.ArgContext():
                    arg = self.search_for_atom(child)
                    cmd.add_arg(arg)
                case CommandsParser.FlagContext():
                    flag = self.search_for_atom(child)
                    cmd.add_flag(flag)
                case Tree.TerminalNodeImpl():
                    pass
                case _:
                    raise CommandConstructError("Unexpected child of args")

    def search_for_atom(self, ctx) -> str:
        arg = None
        for child in ctx.children:
            match child:
                case CommandsParser.AtomContext():
                    if arg is not None:
                        raise CommandConstructError("Expected single atom at search, got multiple")
                    arg = self.process_atom(child)
                case Tree.TerminalNodeImpl():
                    pass
                case _:
                    raise CommandConstructError("Unexpected node while searching for atom")

        if arg is None:
            raise CommandConstructError("Expected atom, found none")

        return arg

    def process_atom(self, ctx):
        match ctx.children[0]:
            case Tree.TerminalNodeImpl():
                return ctx.children[0].symbol.text
            case _:
                raise NotImplementedError()
