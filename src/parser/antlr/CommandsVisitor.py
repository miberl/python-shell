# Generated from Commands.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete generic visitor for a parse tree produced by CommandsParser.

class CommandsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandsParser#prog.
    def visitProg(self, ctx:CommandsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#terminal.
    def visitTerminal(self, ctx:CommandsParser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#combine.
    def visitCombine(self, ctx:CommandsParser.CombineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#instuctions.
    def visitInstuctions(self, ctx:CommandsParser.InstuctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#pipe.
    def visitPipe(self, ctx:CommandsParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#command.
    def visitCommand(self, ctx:CommandsParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#app.
    def visitApp(self, ctx:CommandsParser.AppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#args.
    def visitArgs(self, ctx:CommandsParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#redir_in.
    def visitRedir_in(self, ctx:CommandsParser.Redir_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#redir_out.
    def visitRedir_out(self, ctx:CommandsParser.Redir_outContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#globbed.
    def visitGlobbed(self, ctx:CommandsParser.GlobbedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#atom.
    def visitAtom(self, ctx:CommandsParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#substituted.
    def visitSubstituted(self, ctx:CommandsParser.SubstitutedContext):
        return self.visitChildren(ctx)



del CommandsParser