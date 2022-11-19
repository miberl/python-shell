from collections import deque

from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsListener import CommandsListener


class CustomParserListener(CommandsListener):
    def __init__(self):
        super().__init__()
        self.out = deque()

    # Enter an antlr tree produced by CommandsParser#instuctions.
    def enterInstruction(self, ctx: CommandsParser.InstructionContext):
        self.out.append("instruction(")

    def exitInstruction(self, ctx: CommandsParser.InstructionContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#command.
    def enterCommand(self, ctx: CommandsParser.CommandContext):
        self.out.append("command(")

    def exitCommand(self, ctx: CommandsParser.CommandContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#args.
    def enterArg(self, ctx: CommandsParser.ArgContext):
        self.out.append("arg(")

    def exitArg(self, ctx: CommandsParser.ArgContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#redir_in.
    def enterRedir_in(self, ctx: CommandsParser.Redir_inContext):
        self.out.append("file_in(")

    def exitRedir_in(self, ctx: CommandsParser.Redir_inContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#redir_out.
    def enterRedir_out(self, ctx: CommandsParser.Redir_outContext):
        self.out.append("file_out(")

    def exitRedir_out(self, ctx: CommandsParser.Redir_outContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#globbed.
    def enterGlobbed(self, ctx: CommandsParser.GlobbedContext):
        self.out.append("glob(")

    def exitGlobbed(self, ctx: CommandsParser.GlobbedContext):
        self.out.append(")")

    def enterAtom(self, ctx: CommandsParser.AtomContext):
        self.out.append("atom(")

    def exitAtom(self, ctx: CommandsParser.AtomContext):
        self.out.append(")")

    def enterSubstituted(self, ctx: CommandsParser.SubstitutedContext):
        self.out.append("substituted(")

    def exitSubstituted(self, ctx: CommandsParser.SubstitutedContext):
        self.out.append(")")
