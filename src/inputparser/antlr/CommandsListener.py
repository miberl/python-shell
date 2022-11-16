# Generated from Commands.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete listener for a parse tree produced by CommandsParser.
class CommandsListener(ParseTreeListener):

    # Enter a parse tree produced by CommandsParser#prog.
    def enterProg(self, ctx:CommandsParser.ProgContext):
        pass

    # Exit a parse tree produced by CommandsParser#prog.
    def exitProg(self, ctx:CommandsParser.ProgContext):
        pass


    # Enter a parse tree produced by CommandsParser#terminal.
    def enterTerminal(self, ctx:CommandsParser.TerminalContext):
        pass

    # Exit a parse tree produced by CommandsParser#terminal.
    def exitTerminal(self, ctx:CommandsParser.TerminalContext):
        pass


    # Enter a parse tree produced by CommandsParser#instruction.
    def enterInstruction(self, ctx:CommandsParser.InstructionContext):
        pass

    # Exit a parse tree produced by CommandsParser#instruction.
    def exitInstruction(self, ctx:CommandsParser.InstructionContext):
        pass


    # Enter a parse tree produced by CommandsParser#command.
    def enterCommand(self, ctx:CommandsParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#command.
    def exitCommand(self, ctx:CommandsParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#app.
    def enterApp(self, ctx:CommandsParser.AppContext):
        pass

    # Exit a parse tree produced by CommandsParser#app.
    def exitApp(self, ctx:CommandsParser.AppContext):
        pass


    # Enter a parse tree produced by CommandsParser#arg.
    def enterArg(self, ctx:CommandsParser.ArgContext):
        pass

    # Exit a parse tree produced by CommandsParser#arg.
    def exitArg(self, ctx:CommandsParser.ArgContext):
        pass


    # Enter a parse tree produced by CommandsParser#redir_in.
    def enterRedir_in(self, ctx:CommandsParser.Redir_inContext):
        pass

    # Exit a parse tree produced by CommandsParser#redir_in.
    def exitRedir_in(self, ctx:CommandsParser.Redir_inContext):
        pass


    # Enter a parse tree produced by CommandsParser#redir_out.
    def enterRedir_out(self, ctx:CommandsParser.Redir_outContext):
        pass

    # Exit a parse tree produced by CommandsParser#redir_out.
    def exitRedir_out(self, ctx:CommandsParser.Redir_outContext):
        pass


    # Enter a parse tree produced by CommandsParser#globbed.
    def enterGlobbed(self, ctx:CommandsParser.GlobbedContext):
        pass

    # Exit a parse tree produced by CommandsParser#globbed.
    def exitGlobbed(self, ctx:CommandsParser.GlobbedContext):
        pass


    # Enter a parse tree produced by CommandsParser#atom.
    def enterAtom(self, ctx:CommandsParser.AtomContext):
        pass

    # Exit a parse tree produced by CommandsParser#atom.
    def exitAtom(self, ctx:CommandsParser.AtomContext):
        pass


    # Enter a parse tree produced by CommandsParser#substituted.
    def enterSubstituted(self, ctx:CommandsParser.SubstitutedContext):
        pass

    # Exit a parse tree produced by CommandsParser#substituted.
    def exitSubstituted(self, ctx:CommandsParser.SubstitutedContext):
        pass


    # Enter a parse tree produced by CommandsParser#quoted_text.
    def enterQuoted_text(self, ctx:CommandsParser.Quoted_textContext):
        pass

    # Exit a parse tree produced by CommandsParser#quoted_text.
    def exitQuoted_text(self, ctx:CommandsParser.Quoted_textContext):
        pass



del CommandsParser