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
        4,1,13,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,3,
        1,29,8,1,1,1,1,1,3,1,33,8,1,1,1,1,1,3,1,37,8,1,3,1,39,8,1,1,1,1,
        1,3,1,43,8,1,1,2,3,2,46,8,2,1,2,1,2,3,2,50,8,2,1,2,1,2,3,2,54,8,
        2,1,2,5,2,57,8,2,10,2,12,2,60,9,2,1,2,3,2,63,8,2,1,3,3,3,66,8,3,
        1,3,1,3,5,3,70,8,3,10,3,12,3,73,9,3,1,3,1,3,3,3,77,8,3,1,3,1,3,3,
        3,81,8,3,1,3,3,3,84,8,3,1,4,1,4,1,5,1,5,1,5,3,5,91,8,5,1,6,1,6,3,
        6,95,8,6,1,6,1,6,1,7,1,7,3,7,101,8,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,
        1,9,4,9,111,8,9,11,9,12,9,112,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,5,11,128,8,11,10,11,12,11,131,9,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,144,
        8,11,10,11,12,11,147,9,11,1,11,3,11,150,8,11,1,11,0,0,12,0,2,4,6,
        8,10,12,14,16,18,20,22,0,1,1,1,1,1,179,0,24,1,0,0,0,2,28,1,0,0,0,
        4,45,1,0,0,0,6,65,1,0,0,0,8,85,1,0,0,0,10,87,1,0,0,0,12,92,1,0,0,
        0,14,98,1,0,0,0,16,104,1,0,0,0,18,110,1,0,0,0,20,114,1,0,0,0,22,
        149,1,0,0,0,24,25,3,2,1,0,25,26,7,0,0,0,26,1,1,0,0,0,27,29,5,9,0,
        0,28,27,1,0,0,0,28,29,1,0,0,0,29,38,1,0,0,0,30,32,3,4,2,0,31,33,
        5,9,0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,36,5,2,0,0,
        35,37,5,9,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,30,1,
        0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,42,3,4,2,0,41,43,5,9,0,0,42,
        41,1,0,0,0,42,43,1,0,0,0,43,3,1,0,0,0,44,46,5,9,0,0,45,44,1,0,0,
        0,45,46,1,0,0,0,46,47,1,0,0,0,47,58,3,6,3,0,48,50,5,9,0,0,49,48,
        1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,53,5,3,0,0,52,54,5,9,0,0,
        53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,57,3,6,3,0,56,49,1,
        0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,62,1,0,0,0,60,
        58,1,0,0,0,61,63,5,9,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,5,1,0,0,
        0,64,66,5,9,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,71,
        3,8,4,0,68,70,3,10,5,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,76,1,0,0,0,73,71,1,0,0,0,74,75,5,9,0,0,75,77,3,
        12,6,0,76,74,1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,0,78,79,5,9,0,0,79,
        81,3,14,7,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,84,5,9,
        0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,86,3,18,9,0,86,9,
        1,0,0,0,87,90,5,9,0,0,88,91,3,18,9,0,89,91,3,16,8,0,90,88,1,0,0,
        0,90,89,1,0,0,0,91,11,1,0,0,0,92,94,5,4,0,0,93,95,5,9,0,0,94,93,
        1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,3,18,9,0,97,13,1,0,0,0,
        98,100,5,5,0,0,99,101,5,9,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
        102,1,0,0,0,102,103,3,18,9,0,103,15,1,0,0,0,104,105,5,6,0,0,105,
        17,1,0,0,0,106,111,5,8,0,0,107,111,3,20,10,0,108,111,3,16,8,0,109,
        111,3,22,11,0,110,106,1,0,0,0,110,107,1,0,0,0,110,108,1,0,0,0,110,
        109,1,0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        19,1,0,0,0,114,115,5,7,0,0,115,116,3,2,1,0,116,117,5,7,0,0,117,21,
        1,0,0,0,118,129,5,10,0,0,119,128,5,11,0,0,120,128,5,6,0,0,121,128,
        5,3,0,0,122,128,5,2,0,0,123,128,5,12,0,0,124,128,5,8,0,0,125,128,
        3,20,10,0,126,128,5,9,0,0,127,119,1,0,0,0,127,120,1,0,0,0,127,121,
        1,0,0,0,127,122,1,0,0,0,127,123,1,0,0,0,127,124,1,0,0,0,127,125,
        1,0,0,0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,
        1,0,0,0,130,132,1,0,0,0,131,129,1,0,0,0,132,150,5,10,0,0,133,145,
        5,11,0,0,134,144,5,10,0,0,135,144,5,2,0,0,136,144,5,6,0,0,137,144,
        5,2,0,0,138,144,5,6,0,0,139,144,5,12,0,0,140,144,5,8,0,0,141,144,
        3,20,10,0,142,144,5,9,0,0,143,134,1,0,0,0,143,135,1,0,0,0,143,136,
        1,0,0,0,143,137,1,0,0,0,143,138,1,0,0,0,143,139,1,0,0,0,143,140,
        1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,150,
        5,11,0,0,149,118,1,0,0,0,149,133,1,0,0,0,150,23,1,0,0,0,25,28,32,
        36,38,42,45,49,53,58,62,65,71,76,80,83,90,94,100,110,112,127,129,
        143,145,149
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
    RULE_app = 4
    RULE_arg = 5
    RULE_redir_in = 6
    RULE_redir_out = 7
    RULE_globbed = 8
    RULE_atom = 9
    RULE_substituted = 10
    RULE_quoted_text = 11

    ruleNames =  [ "prog", "terminal", "instruction", "command", "app", 
                   "arg", "redir_in", "redir_out", "globbed", "atom", "substituted", 
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

        def terminal(self):
            return self.getTypedRuleContext(CommandsParser.TerminalContext,0)


        def EOF(self):
            return self.getToken(CommandsParser.EOF, 0)

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
            self.state = 24
            self.terminal()
            self.state = 25
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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 27
                self.match(CommandsParser.WHITESPACE)


            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 30
                self.instruction()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 31
                    self.match(CommandsParser.WHITESPACE)


                self.state = 34
                self.match(CommandsParser.T__1)
                self.state = 36
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.match(CommandsParser.WHITESPACE)




            self.state = 40
            self.instruction()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 41
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 44
                self.match(CommandsParser.WHITESPACE)


            self.state = 47
            self.command()
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 48
                        self.match(CommandsParser.WHITESPACE)


                    self.state = 51
                    self.match(CommandsParser.T__2)
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 52
                        self.match(CommandsParser.WHITESPACE)


                    self.state = 55
                    self.command() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 61
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

        def app(self):
            return self.getTypedRuleContext(CommandsParser.AppContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.ArgContext)
            else:
                return self.getTypedRuleContext(CommandsParser.ArgContext,i)


        def redir_in(self):
            return self.getTypedRuleContext(CommandsParser.Redir_inContext,0)


        def redir_out(self):
            return self.getTypedRuleContext(CommandsParser.Redir_outContext,0)


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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 64
                self.match(CommandsParser.WHITESPACE)


            self.state = 67
            self.app()
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.arg() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(CommandsParser.WHITESPACE)
                self.state = 75
                self.redir_in()


            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(CommandsParser.WHITESPACE)
                self.state = 79
                self.redir_out()


            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AppContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CommandsParser.AtomContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_app

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApp" ):
                listener.enterApp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApp" ):
                listener.exitApp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp" ):
                return visitor.visitApp(self)
            else:
                return visitor.visitChildren(self)




    def app(self):

        localctx = CommandsParser.AppContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_app)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.atom()
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

        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

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
        self.enterRule(localctx, 10, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(CommandsParser.WHITESPACE)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 88
                self.atom()
                pass

            elif la_ == 2:
                self.state = 89
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
        self.enterRule(localctx, 12, self.RULE_redir_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CommandsParser.T__3)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 93
                self.match(CommandsParser.WHITESPACE)


            self.state = 96
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
        self.enterRule(localctx, 14, self.RULE_redir_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(CommandsParser.T__4)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 99
                self.match(CommandsParser.WHITESPACE)


            self.state = 102
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
        self.enterRule(localctx, 16, self.RULE_globbed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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
        self.enterRule(localctx, 18, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 110
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 106
                        self.match(CommandsParser.WORD)
                        pass
                    elif token in [7]:
                        self.state = 107
                        self.substituted()
                        pass
                    elif token in [6]:
                        self.state = 108
                        self.globbed()
                        pass
                    elif token in [10, 11]:
                        self.state = 109
                        self.quoted_text()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 112 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_substituted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(CommandsParser.T__6)
            self.state = 115
            self.terminal()
            self.state = 116
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
        self.enterRule(localctx, 22, self.RULE_quoted_text)
        self._la = 0 # Token type
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(CommandsParser.SINGLEQUOTE)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 7116) != 0:
                    self.state = 127
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [11]:
                        self.state = 119
                        self.match(CommandsParser.DOUBLEQUOTE)
                        pass
                    elif token in [6]:
                        self.state = 120
                        self.match(CommandsParser.T__5)
                        pass
                    elif token in [3]:
                        self.state = 121
                        self.match(CommandsParser.T__2)
                        pass
                    elif token in [2]:
                        self.state = 122
                        self.match(CommandsParser.T__1)
                        pass
                    elif token in [12]:
                        self.state = 123
                        self.match(CommandsParser.QUOTEWORD)
                        pass
                    elif token in [8]:
                        self.state = 124
                        self.match(CommandsParser.WORD)
                        pass
                    elif token in [7]:
                        self.state = 125
                        self.substituted()
                        pass
                    elif token in [9]:
                        self.state = 126
                        self.match(CommandsParser.WHITESPACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 132
                self.match(CommandsParser.SINGLEQUOTE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(CommandsParser.DOUBLEQUOTE)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 6084) != 0:
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 134
                        self.match(CommandsParser.SINGLEQUOTE)
                        pass

                    elif la_ == 2:
                        self.state = 135
                        self.match(CommandsParser.T__1)
                        pass

                    elif la_ == 3:
                        self.state = 136
                        self.match(CommandsParser.T__5)
                        pass

                    elif la_ == 4:
                        self.state = 137
                        self.match(CommandsParser.T__1)
                        pass

                    elif la_ == 5:
                        self.state = 138
                        self.match(CommandsParser.T__5)
                        pass

                    elif la_ == 6:
                        self.state = 139
                        self.match(CommandsParser.QUOTEWORD)
                        pass

                    elif la_ == 7:
                        self.state = 140
                        self.match(CommandsParser.WORD)
                        pass

                    elif la_ == 8:
                        self.state = 141
                        self.substituted()
                        pass

                    elif la_ == 9:
                        self.state = 142
                        self.match(CommandsParser.WHITESPACE)
                        pass


                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 148
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





