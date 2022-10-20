from parser.antlr.CommandsParser import CommandsParser
from parser.antlr.CommandsVisitor import CommandsVisitor


class ParseVisitor(CommandsVisitor):
    def __init__(self):
        self.commands = []

    def get_commands(self):
        return self.commands

    def visitCommand(self, ctx: CommandsParser.CommandContext):
        if len(ctx.children) == 0:
            raise Exception()

        app = self.get_app(ctx)

        args = self.get_args(ctx)

        self.commands.append((app, args))

    @staticmethod
    def get_app(ctx):
        return ctx.children[0].children[0].children[0].symbol.text

    @staticmethod
    def get_args(ctx):
        args = []
        if len(ctx.children) == 1:
            return []

        for arg in ctx.children[1].children:
            try:
                args.append(arg.children[0].symbol.text)
            except AttributeError:
                continue

        return args


