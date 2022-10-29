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
        4,1,13,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,3,1,35,8,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,1,1,1,1,3,1,45,8,1,1,2,1,2,3,2,49,8,2,1,2,1,2,3,2,53,8,2,1,3,
        3,3,56,8,3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,3,3,66,8,3,1,
        4,1,4,3,4,70,8,4,1,4,1,4,3,4,74,8,4,1,5,3,5,77,8,5,1,5,1,5,3,5,81,
        8,5,1,5,1,5,3,5,85,8,5,1,5,1,5,3,5,89,8,5,1,5,3,5,92,8,5,1,6,1,6,
        1,7,3,7,97,8,7,1,7,1,7,3,7,101,8,7,1,7,4,7,104,8,7,11,7,12,7,105,
        3,7,108,8,7,1,7,3,7,111,8,7,4,7,113,8,7,11,7,12,7,114,1,7,4,7,118,
        8,7,11,7,12,7,119,3,7,122,8,7,1,8,1,8,1,8,3,8,127,8,8,1,9,1,9,1,
        9,1,9,3,9,133,8,9,1,10,1,10,3,10,137,8,10,1,10,1,10,1,11,1,11,3,
        11,143,8,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,154,
        8,13,1,13,1,13,3,13,158,8,13,3,13,160,8,13,1,13,1,13,1,13,3,13,165,
        8,13,1,13,1,13,1,13,3,13,170,8,13,5,13,172,8,13,10,13,12,13,175,
        9,13,1,14,1,14,1,14,1,14,1,14,1,39,1,26,15,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,0,1,1,1,1,1,201,0,30,1,0,0,0,2,34,1,0,0,0,4,46,
        1,0,0,0,6,55,1,0,0,0,8,67,1,0,0,0,10,76,1,0,0,0,12,93,1,0,0,0,14,
        121,1,0,0,0,16,123,1,0,0,0,18,132,1,0,0,0,20,134,1,0,0,0,22,140,
        1,0,0,0,24,146,1,0,0,0,26,159,1,0,0,0,28,176,1,0,0,0,30,31,3,2,1,
        0,31,32,7,0,0,0,32,1,1,0,0,0,33,35,5,11,0,0,34,33,1,0,0,0,34,35,
        1,0,0,0,35,39,1,0,0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,
        39,40,1,0,0,0,39,37,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,44,3,
        6,3,0,43,45,5,11,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,
        48,3,6,3,0,47,49,5,11,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,
        0,0,50,52,5,2,0,0,51,53,5,11,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,
        5,1,0,0,0,54,56,5,11,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,60,1,0,0,
        0,57,59,3,8,4,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,
        1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,65,3,10,5,0,64,66,5,11,0,
        0,65,64,1,0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,69,3,10,5,0,68,70,
        5,11,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,3,0,0,
        72,74,5,11,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,77,5,
        11,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,80,3,12,6,0,
        79,81,3,14,7,0,80,79,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,82,83,5,
        11,0,0,83,85,3,20,10,0,84,82,1,0,0,0,84,85,1,0,0,0,85,88,1,0,0,0,
        86,87,5,11,0,0,87,89,3,22,11,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,
        1,0,0,0,90,92,5,11,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,
        93,94,3,26,13,0,94,13,1,0,0,0,95,97,5,11,0,0,96,95,1,0,0,0,96,97,
        1,0,0,0,97,98,1,0,0,0,98,107,3,18,9,0,99,101,5,11,0,0,100,99,1,0,
        0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,104,3,16,8,0,103,102,1,0,
        0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,
        0,0,107,100,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,11,
        0,0,110,109,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,96,1,0,0,
        0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,122,1,0,0,
        0,116,118,3,16,8,0,117,116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,
        0,119,120,1,0,0,0,120,122,1,0,0,0,121,112,1,0,0,0,121,117,1,0,0,
        0,122,15,1,0,0,0,123,126,5,11,0,0,124,127,3,26,13,0,125,127,3,24,
        12,0,126,124,1,0,0,0,126,125,1,0,0,0,127,17,1,0,0,0,128,129,5,4,
        0,0,129,133,3,26,13,0,130,131,5,5,0,0,131,133,3,26,13,0,132,128,
        1,0,0,0,132,130,1,0,0,0,133,19,1,0,0,0,134,136,5,6,0,0,135,137,5,
        11,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,139,3,
        26,13,0,139,21,1,0,0,0,140,142,5,7,0,0,141,143,5,11,0,0,142,141,
        1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,3,26,13,0,145,23,
        1,0,0,0,146,147,5,8,0,0,147,25,1,0,0,0,148,149,6,13,-1,0,149,160,
        5,10,0,0,150,160,5,12,0,0,151,153,3,28,14,0,152,154,3,26,13,0,153,
        152,1,0,0,0,153,154,1,0,0,0,154,160,1,0,0,0,155,157,3,24,12,0,156,
        158,3,26,13,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,
        148,1,0,0,0,159,150,1,0,0,0,159,151,1,0,0,0,159,155,1,0,0,0,160,
        173,1,0,0,0,161,162,10,4,0,0,162,164,3,28,14,0,163,165,3,26,13,0,
        164,163,1,0,0,0,164,165,1,0,0,0,165,172,1,0,0,0,166,167,10,2,0,0,
        167,169,3,24,12,0,168,170,3,26,13,0,169,168,1,0,0,0,169,170,1,0,
        0,0,170,172,1,0,0,0,171,161,1,0,0,0,171,166,1,0,0,0,172,175,1,0,
        0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,27,1,0,0,0,175,173,1,0,0,
        0,176,177,5,9,0,0,177,178,3,2,1,0,178,179,5,9,0,0,179,29,1,0,0,0,
        34,34,39,44,48,52,55,60,65,69,73,76,80,84,88,91,96,100,105,107,110,
        114,119,121,126,132,136,142,153,157,159,164,169,171,173
    ]

class CommandsParser ( Parser ):

    grammarFileName = "Commands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "';'", "'|'", "'-'", "'--'", 
                     "'<'", "'>'", "'*'", "'`'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WORD", "WHITESPACE", "QUOTEDTEXT", 
                      "OTHER" ]

    RULE_prog = 0
    RULE_terminal = 1
    RULE_combine = 2
    RULE_instuctions = 3
    RULE_pipe = 4
    RULE_command = 5
    RULE_app = 6
    RULE_args = 7
    RULE_arg = 8
    RULE_flag = 9
    RULE_redir_in = 10
    RULE_redir_out = 11
    RULE_globbed = 12
    RULE_atom = 13
    RULE_substituted = 14

    ruleNames =  [ "prog", "terminal", "combine", "instuctions", "pipe", 
                   "command", "app", "args", "arg", "flag", "redir_in", 
                   "redir_out", "globbed", "atom", "substituted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    WORD=10
    WHITESPACE=11
    QUOTEDTEXT=12
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
            self.state = 30
            self.terminal()
            self.state = 31
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

        def instuctions(self):
            return self.getTypedRuleContext(CommandsParser.InstuctionsContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def combine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.CombineContext)
            else:
                return self.getTypedRuleContext(CommandsParser.CombineContext,i)


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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 33
                self.match(CommandsParser.WHITESPACE)


            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 36
                    self.combine() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 42
            self.instuctions()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 43
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instuctions(self):
            return self.getTypedRuleContext(CommandsParser.InstuctionsContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_combine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombine" ):
                listener.enterCombine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombine" ):
                listener.exitCombine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombine" ):
                return visitor.visitCombine(self)
            else:
                return visitor.visitChildren(self)




    def combine(self):

        localctx = CommandsParser.CombineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_combine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.instuctions()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 47
                self.match(CommandsParser.WHITESPACE)


            self.state = 50
            self.match(CommandsParser.T__1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstuctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(CommandsParser.CommandContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.PipeContext)
            else:
                return self.getTypedRuleContext(CommandsParser.PipeContext,i)


        def getRuleIndex(self):
            return CommandsParser.RULE_instuctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstuctions" ):
                listener.enterInstuctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstuctions" ):
                listener.exitInstuctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstuctions" ):
                return visitor.visitInstuctions(self)
            else:
                return visitor.visitChildren(self)




    def instuctions(self):

        localctx = CommandsParser.InstuctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instuctions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 54
                self.match(CommandsParser.WHITESPACE)


            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.pipe() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 63
            self.command()
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(CommandsParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(CommandsParser.CommandContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)




    def pipe(self):

        localctx = CommandsParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.command()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 68
                self.match(CommandsParser.WHITESPACE)


            self.state = 71
            self.match(CommandsParser.T__2)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 72
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

        def args(self):
            return self.getTypedRuleContext(CommandsParser.ArgsContext,0)


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
        self.enterRule(localctx, 10, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 75
                self.match(CommandsParser.WHITESPACE)


            self.state = 78
            self.app()
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 79
                self.args()


            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(CommandsParser.WHITESPACE)
                self.state = 83
                self.redir_in()


            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(CommandsParser.WHITESPACE)
                self.state = 87
                self.redir_out()


            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 90
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
        self.enterRule(localctx, 12, self.RULE_app)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.atom(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.FlagContext)
            else:
                return self.getTypedRuleContext(CommandsParser.FlagContext,i)


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


        def getRuleIndex(self):
            return CommandsParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = CommandsParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 96
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==11:
                            self.state = 95
                            self.match(CommandsParser.WHITESPACE)


                        self.state = 98
                        self.flag()
                        self.state = 107
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                        if la_ == 1:
                            self.state = 100
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                            if la_ == 1:
                                self.state = 99
                                self.match(CommandsParser.WHITESPACE)


                            self.state = 103 
                            self._errHandler.sync(self)
                            _alt = 1
                            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt == 1:
                                    self.state = 102
                                    self.arg()

                                else:
                                    raise NoViableAltException(self)
                                self.state = 105 
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)



                        self.state = 110
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                        if la_ == 1:
                            self.state = 109
                            self.match(CommandsParser.WHITESPACE)



                    else:
                        raise NoViableAltException(self)
                    self.state = 114 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 116
                        self.arg()

                    else:
                        raise NoViableAltException(self)
                    self.state = 119 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass


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
        self.enterRule(localctx, 16, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CommandsParser.WHITESPACE)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 124
                self.atom(0)
                pass

            elif la_ == 2:
                self.state = 125
                self.globbed()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CommandsParser.AtomContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlag" ):
                listener.enterFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlag" ):
                listener.exitFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlag" ):
                return visitor.visitFlag(self)
            else:
                return visitor.visitChildren(self)




    def flag(self):

        localctx = CommandsParser.FlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_flag)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(CommandsParser.T__3)
                self.state = 129
                self.atom(0)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(CommandsParser.T__4)
                self.state = 131
                self.atom(0)
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
        self.enterRule(localctx, 20, self.RULE_redir_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CommandsParser.T__5)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 135
                self.match(CommandsParser.WHITESPACE)


            self.state = 138
            self.atom(0)
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
        self.enterRule(localctx, 22, self.RULE_redir_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CommandsParser.T__6)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 141
                self.match(CommandsParser.WHITESPACE)


            self.state = 144
            self.atom(0)
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
        self.enterRule(localctx, 24, self.RULE_globbed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CommandsParser.T__7)
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

        def WORD(self):
            return self.getToken(CommandsParser.WORD, 0)

        def QUOTEDTEXT(self):
            return self.getToken(CommandsParser.QUOTEDTEXT, 0)

        def substituted(self):
            return self.getTypedRuleContext(CommandsParser.SubstitutedContext,0)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.AtomContext)
            else:
                return self.getTypedRuleContext(CommandsParser.AtomContext,i)


        def globbed(self):
            return self.getTypedRuleContext(CommandsParser.GlobbedContext,0)


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



    def atom(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandsParser.AtomContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_atom, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 149
                self.match(CommandsParser.WORD)
                pass
            elif token in [12]:
                self.state = 150
                self.match(CommandsParser.QUOTEDTEXT)
                pass
            elif token in [9]:
                self.state = 151
                self.substituted()
                self.state = 153
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 152
                    self.atom(0)


                pass
            elif token in [8]:
                self.state = 155
                self.globbed()
                self.state = 157
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 156
                    self.atom(0)


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 171
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = CommandsParser.AtomContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atom)
                        self.state = 161
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 162
                        self.substituted()
                        self.state = 164
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                        if la_ == 1:
                            self.state = 163
                            self.atom(0)


                        pass

                    elif la_ == 2:
                        localctx = CommandsParser.AtomContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atom)
                        self.state = 166
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 167
                        self.globbed()
                        self.state = 169
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                        if la_ == 1:
                            self.state = 168
                            self.atom(0)


                        pass

             
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 28, self.RULE_substituted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(CommandsParser.T__8)
            self.state = 177
            self.terminal()
            self.state = 178
            self.match(CommandsParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.atom_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def atom_sempred(self, localctx:AtomContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




