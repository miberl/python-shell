from inputparser.antlr.commands_parser import CommandsParser
from inputparser.antlr.commands_lexer import CommandsLexer
from antlr4 import ParseTreeWalker, InputStream, CommonTokenStream


class ParseCommands:
    @staticmethod
    def parse_listen(cmd: str, listener):
        input_stream = InputStream(cmd)
        lexer = CommandsLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CommandsParser(stream)
        parser.addErrorListener(listener)
        tree = parser.prog()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    @staticmethod
    def parse_visitor(cmd: str, visitor):
        input_stream = InputStream(cmd)
        lexer = CommandsLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CommandsParser(stream)
        tree = parser.prog()
        visitor.visit(tree)
