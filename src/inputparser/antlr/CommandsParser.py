# Generated from Commands.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,3,0,27,8,
        0,1,0,1,0,1,1,3,1,32,8,1,1,1,1,1,3,1,36,8,1,1,1,1,1,3,1,40,8,1,5,
        1,42,8,1,10,1,12,1,45,9,1,1,1,1,1,3,1,49,8,1,1,2,3,2,52,8,2,1,2,
        1,2,3,2,56,8,2,1,2,1,2,3,2,60,8,2,1,2,5,2,63,8,2,10,2,12,2,66,9,
        2,1,2,3,2,69,8,2,1,3,1,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,1,3,
        1,3,1,3,1,3,1,3,5,3,85,8,3,10,3,12,3,88,9,3,1,4,1,4,3,4,92,8,4,1,
        5,1,5,3,5,96,8,5,1,5,1,5,1,6,1,6,3,6,102,8,6,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,1,8,4,8,112,8,8,11,8,12,8,113,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,131,8,10,10,10,
        12,10,134,9,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,5,10,149,8,10,10,10,12,10,152,9,10,1,10,3,10,155,
        8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,1,1,1,193,0,23,
        1,0,0,0,2,31,1,0,0,0,4,51,1,0,0,0,6,75,1,0,0,0,8,91,1,0,0,0,10,93,
        1,0,0,0,12,99,1,0,0,0,14,105,1,0,0,0,16,111,1,0,0,0,18,115,1,0,0,
        0,20,154,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,23,24,1,0,0,0,24,26,
        1,0,0,0,25,27,5,9,0,0,26,25,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,
        28,29,7,0,0,0,29,1,1,0,0,0,30,32,5,9,0,0,31,30,1,0,0,0,31,32,1,0,
        0,0,32,43,1,0,0,0,33,35,3,4,2,0,34,36,5,9,0,0,35,34,1,0,0,0,35,36,
        1,0,0,0,36,37,1,0,0,0,37,39,5,2,0,0,38,40,5,9,0,0,39,38,1,0,0,0,
        39,40,1,0,0,0,40,42,1,0,0,0,41,33,1,0,0,0,42,45,1,0,0,0,43,41,1,
        0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,48,3,4,2,0,47,
        49,5,9,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,3,1,0,0,0,50,52,5,9,0,
        0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,64,3,6,3,0,54,56,
        5,9,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,59,5,3,0,0,
        58,60,5,9,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,63,3,
        6,3,0,62,55,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        68,1,0,0,0,66,64,1,0,0,0,67,69,5,9,0,0,68,67,1,0,0,0,68,69,1,0,0,
        0,69,5,1,0,0,0,70,74,3,10,5,0,71,74,3,12,6,0,72,74,5,9,0,0,73,70,
        1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,
        75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,86,3,8,4,0,79,80,5,
        9,0,0,80,85,3,8,4,0,81,85,3,10,5,0,82,85,3,12,6,0,83,85,5,9,0,0,
        84,79,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,88,1,
        0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,7,1,0,0,0,88,86,1,0,0,0,89,
        92,3,16,8,0,90,92,3,14,7,0,91,89,1,0,0,0,91,90,1,0,0,0,92,9,1,0,
        0,0,93,95,5,4,0,0,94,96,5,9,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,
        1,0,0,0,97,98,3,16,8,0,98,11,1,0,0,0,99,101,5,5,0,0,100,102,5,9,
        0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,3,16,
        8,0,104,13,1,0,0,0,105,106,5,6,0,0,106,15,1,0,0,0,107,112,5,8,0,
        0,108,112,3,18,9,0,109,112,3,14,7,0,110,112,3,20,10,0,111,107,1,
        0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,113,1,
        0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,17,1,0,0,0,115,116,5,7,
        0,0,116,117,3,2,1,0,117,118,5,7,0,0,118,19,1,0,0,0,119,132,5,10,
        0,0,120,131,5,11,0,0,121,131,5,6,0,0,122,131,5,3,0,0,123,131,5,2,
        0,0,124,131,5,4,0,0,125,131,5,5,0,0,126,131,5,12,0,0,127,131,5,8,
        0,0,128,131,3,18,9,0,129,131,5,9,0,0,130,120,1,0,0,0,130,121,1,0,
        0,0,130,122,1,0,0,0,130,123,1,0,0,0,130,124,1,0,0,0,130,125,1,0,
        0,0,130,126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,
        0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,
        0,0,134,132,1,0,0,0,135,155,5,10,0,0,136,150,5,11,0,0,137,149,5,
        10,0,0,138,149,5,2,0,0,139,149,5,6,0,0,140,149,5,2,0,0,141,149,5,
        6,0,0,142,149,5,4,0,0,143,149,5,5,0,0,144,149,5,12,0,0,145,149,5,
        8,0,0,146,149,3,18,9,0,147,149,5,9,0,0,148,137,1,0,0,0,148,138,1,
        0,0,0,148,139,1,0,0,0,148,140,1,0,0,0,148,141,1,0,0,0,148,142,1,
        0,0,0,148,143,1,0,0,0,148,144,1,0,0,0,148,145,1,0,0,0,148,146,1,
        0,0,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,
        0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,155,5,11,0,0,154,119,1,
        0,0,0,154,136,1,0,0,0,155,21,1,0,0,0,26,23,26,31,35,39,43,48,51,
        55,59,64,68,73,75,84,86,91,95,101,111,113,130,132,148,150,154
    ]

class CommandsParser ( Parser ):

    grammarFileName = "Commands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "';'", "'|'", "'<'", "'>'", "'*'", 
                     "'`'", "<INVALID>", "<INVALID>", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WORD", "WHITESPACE", "SINGLEQUOTE", "DOUBLEQUOTE", 
                      "QUOTEWORD", "OTHER" ]

    RULE_prog = 0
    RULE_terminal = 1
    RULE_instruction = 2
    RULE_command = 3
    RULE_arg = 4
    RULE_redir_in = 5
    RULE_redir_out = 6
    RULE_globbed = 7
    RULE_atom = 8
    RULE_substituted = 9
    RULE_quoted_text = 10

    ruleNames =  [ "prog", "terminal", "instruction", "command", "arg", 
                   "redir_in", "redir_out", "globbed", "atom", "substituted", 
                   "quoted_text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    WORD=8
    WHITESPACE=9
    SINGLEQUOTE=10
    DOUBLEQUOTE=11
    QUOTEWORD=12
    OTHER=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandsParser.EOF, 0)

        def terminal(self):
            return self.getTypedRuleContext(CommandsParser.TerminalContext,0)


        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CommandsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                self.terminal()


            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 25
                self.match(CommandsParser.WHITESPACE)


            self.state = 28
            _la = self._input.LA(1)
            if not(_la==-1 or _la==1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.InstructionContext)
            else:
                return self.getTypedRuleContext(CommandsParser.InstructionContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)




    def terminal(self):

        localctx = CommandsParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.match(CommandsParser.WHITESPACE)


            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    self.instruction()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 34
                        self.match(CommandsParser.WHITESPACE)


                    self.state = 37
                    self.match(CommandsParser.T__1)
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 38
                        self.match(CommandsParser.WHITESPACE)

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 46
            self.instruction()
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 47
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.CommandContext)
            else:
                return self.getTypedRuleContext(CommandsParser.CommandContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = CommandsParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(CommandsParser.WHITESPACE)


            self.state = 53
            self.command()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 54
                        self.match(CommandsParser.WHITESPACE)


                    self.state = 57
                    self.match(CommandsParser.T__2)
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 58
                        self.match(CommandsParser.WHITESPACE)


                    self.state = 61
                    self.command() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 67
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.ArgContext)
            else:
                return self.getTypedRuleContext(CommandsParser.ArgContext,i)


        def redir_in(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.Redir_inContext)
            else:
                return self.getTypedRuleContext(CommandsParser.Redir_inContext,i)


        def redir_out(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.Redir_outContext)
            else:
                return self.getTypedRuleContext(CommandsParser.Redir_outContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CommandsParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 560) != 0:
                self.state = 73
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 70
                    self.redir_in()
                    pass
                elif token in [5]:
                    self.state = 71
                    self.redir_out()
                    pass
                elif token in [9]:
                    self.state = 72
                    self.match(CommandsParser.WHITESPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.arg()
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        self.state = 79
                        self.match(CommandsParser.WHITESPACE)
                        self.state = 80
                        self.arg()
                        pass

                    elif la_ == 2:
                        self.state = 81
                        self.redir_in()
                        pass

                    elif la_ == 3:
                        self.state = 82
                        self.redir_out()
                        pass

                    elif la_ == 4:
                        self.state = 83
                        self.match(CommandsParser.WHITESPACE)
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CommandsParser.AtomContext,0)


        def globbed(self):
            return self.getTypedRuleContext(CommandsParser.GlobbedContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = CommandsParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 89
                self.atom()
                pass

            elif la_ == 2:
                self.state = 90
                self.globbed()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Redir_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CommandsParser.AtomContext,0)


        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_redir_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedir_in" ):
                listener.enterRedir_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedir_in" ):
                listener.exitRedir_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedir_in" ):
                return visitor.visitRedir_in(self)
            else:
                return visitor.visitChildren(self)




    def redir_in(self):

        localctx = CommandsParser.Redir_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_redir_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(CommandsParser.T__3)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 94
                self.match(CommandsParser.WHITESPACE)


            self.state = 97
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Redir_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CommandsParser.AtomContext,0)


        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_redir_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedir_out" ):
                listener.enterRedir_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedir_out" ):
                listener.exitRedir_out(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedir_out" ):
                return visitor.visitRedir_out(self)
            else:
                return visitor.visitChildren(self)




    def redir_out(self):

        localctx = CommandsParser.Redir_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_redir_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CommandsParser.T__4)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 100
                self.match(CommandsParser.WHITESPACE)


            self.state = 103
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobbedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_globbed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobbed" ):
                listener.enterGlobbed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobbed" ):
                listener.exitGlobbed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobbed" ):
                return visitor.visitGlobbed(self)
            else:
                return visitor.visitChildren(self)




    def globbed(self):

        localctx = CommandsParser.GlobbedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_globbed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(CommandsParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WORD)
            else:
                return self.getToken(CommandsParser.WORD, i)

        def substituted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.SubstitutedContext)
            else:
                return self.getTypedRuleContext(CommandsParser.SubstitutedContext,i)


        def globbed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.GlobbedContext)
            else:
                return self.getTypedRuleContext(CommandsParser.GlobbedContext,i)


        def quoted_text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.Quoted_textContext)
            else:
                return self.getTypedRuleContext(CommandsParser.Quoted_textContext,i)


        def getRuleIndex(self):
            return CommandsParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CommandsParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 111
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 107
                        self.match(CommandsParser.WORD)
                        pass
                    elif token in [7]:
                        self.state = 108
                        self.substituted()
                        pass
                    elif token in [6]:
                        self.state = 109
                        self.globbed()
                        pass
                    elif token in [10, 11]:
                        self.state = 110
                        self.quoted_text()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 113 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubstitutedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminal(self):
            return self.getTypedRuleContext(CommandsParser.TerminalContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_substituted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstituted" ):
                listener.enterSubstituted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstituted" ):
                listener.exitSubstituted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstituted" ):
                return visitor.visitSubstituted(self)
            else:
                return visitor.visitChildren(self)




    def substituted(self):

        localctx = CommandsParser.SubstitutedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_substituted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CommandsParser.T__6)
            self.state = 116
            self.terminal()
            self.state = 117
            self.match(CommandsParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Quoted_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLEQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.SINGLEQUOTE)
            else:
                return self.getToken(CommandsParser.SINGLEQUOTE, i)

        def DOUBLEQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.DOUBLEQUOTE)
            else:
                return self.getToken(CommandsParser.DOUBLEQUOTE, i)

        def QUOTEWORD(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.QUOTEWORD)
            else:
                return self.getToken(CommandsParser.QUOTEWORD, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WORD)
            else:
                return self.getToken(CommandsParser.WORD, i)

        def substituted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.SubstitutedContext)
            else:
                return self.getTypedRuleContext(CommandsParser.SubstitutedContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_quoted_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted_text" ):
                listener.enterQuoted_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted_text" ):
                listener.exitQuoted_text(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted_text" ):
                return visitor.visitQuoted_text(self)
            else:
                return visitor.visitChildren(self)




    def quoted_text(self):

        localctx = CommandsParser.Quoted_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quoted_text)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(CommandsParser.SINGLEQUOTE)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 7164) != 0:
                    self.state = 130
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [11]:
                        self.state = 120
                        self.match(CommandsParser.DOUBLEQUOTE)
                        pass
                    elif token in [6]:
                        self.state = 121
                        self.match(CommandsParser.T__5)
                        pass
                    elif token in [3]:
                        self.state = 122
                        self.match(CommandsParser.T__2)
                        pass
                    elif token in [2]:
                        self.state = 123
                        self.match(CommandsParser.T__1)
                        pass
                    elif token in [4]:
                        self.state = 124
                        self.match(CommandsParser.T__3)
                        pass
                    elif token in [5]:
                        self.state = 125
                        self.match(CommandsParser.T__4)
                        pass
                    elif token in [12]:
                        self.state = 126
                        self.match(CommandsParser.QUOTEWORD)
                        pass
                    elif token in [8]:
                        self.state = 127
                        self.match(CommandsParser.WORD)
                        pass
                    elif token in [7]:
                        self.state = 128
                        self.substituted()
                        pass
                    elif token in [9]:
                        self.state = 129
                        self.match(CommandsParser.WHITESPACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 135
                self.match(CommandsParser.SINGLEQUOTE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(CommandsParser.DOUBLEQUOTE)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 6132) != 0:
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        self.state = 137
                        self.match(CommandsParser.SINGLEQUOTE)
                        pass

                    elif la_ == 2:
                        self.state = 138
                        self.match(CommandsParser.T__1)
                        pass

                    elif la_ == 3:
                        self.state = 139
                        self.match(CommandsParser.T__5)
                        pass

                    elif la_ == 4:
                        self.state = 140
                        self.match(CommandsParser.T__1)
                        pass

                    elif la_ == 5:
                        self.state = 141
                        self.match(CommandsParser.T__5)
                        pass

                    elif la_ == 6:
                        self.state = 142
                        self.match(CommandsParser.T__3)
                        pass

                    elif la_ == 7:
                        self.state = 143
                        self.match(CommandsParser.T__4)
                        pass

                    elif la_ == 8:
                        self.state = 144
                        self.match(CommandsParser.QUOTEWORD)
                        pass

                    elif la_ == 9:
                        self.state = 145
                        self.match(CommandsParser.WORD)
                        pass

                    elif la_ == 10:
                        self.state = 146
                        self.substituted()
                        pass

                    elif la_ == 11:
                        self.state = 147
                        self.match(CommandsParser.WHITESPACE)
                        pass


                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 153
                self.match(CommandsParser.DOUBLEQUOTE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





