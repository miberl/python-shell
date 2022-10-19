from collections import deque

from parser.antlr.CommandsParser import CommandsParser
from parser.antlr.CommandsListener import CommandsListener


class CustomParserListener(CommandsListener):
    def __init__(self):
        super().__init__()
        self.out = deque()

    # Enter a antlr tree produced by CommandsParser#combine.
    def enterCombine(self, ctx: CommandsParser.CombineContext):
        self.out.append("combine(")

    def exitCombine(self, ctx:CommandsParser.CombineContext):
        self.out.append(")")

    # Enter an antlr tree produced by CommandsParser#instuctions.
    def enterInstuctions(self, ctx: CommandsParser.InstuctionsContext):
        self.out.append("instruction(")

    def exitInstuctions(self, ctx:CommandsParser.InstuctionsContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#pipe.
    def enterPipe(self, ctx: CommandsParser.PipeContext):
        self.out.append("pipe(")

    def exitPipe(self, ctx:CommandsParser.PipeContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#command.
    def enterCommand(self, ctx: CommandsParser.CommandContext):
        self.out.append("command(")

    def exitCommand(self, ctx:CommandsParser.CommandContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#app.
    def enterApp(self, ctx: CommandsParser.AppContext):
        self.out.append("app(")

    def exitApp(self, ctx:CommandsParser.AppContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#args.
    def enterArgs(self, ctx: CommandsParser.ArgsContext):
        self.out.append("args(")

    def exitArgs(self, ctx:CommandsParser.ArgsContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#redir_in.
    def enterRedir_in(self, ctx: CommandsParser.Redir_inContext):
        self.out.append("file_in(")

    def exitRedir_in(self, ctx:CommandsParser.Redir_inContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#redir_out.
    def enterRedir_out(self, ctx: CommandsParser.Redir_outContext):
        self.out.append("file_out(")

    def exitRedir_out(self, ctx:CommandsParser.Redir_outContext):
        self.out.append(")")

    # Enter a antlr tree produced by CommandsParser#globbed.
    def enterGlobbed(self, ctx: CommandsParser.GlobbedContext):
        self.out.append("glob(")

    def exitGlobbed(self, ctx:CommandsParser.GlobbedContext):
        self.out.append(")")

    def enterAtom(self, ctx:CommandsParser.AtomContext):
        self.out.append("atom(")

    def exitAtom(self, ctx:CommandsParser.AtomContext):
        self.out.append(")")

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Oh no!! 1")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def enterSubstituted(self, ctx:CommandsParser.SubstitutedContext):
        self.out.append("substituted(")

    def exitSubstituted(self, ctx:CommandsParser.SubstitutedContext):
        self.out.append(")")
