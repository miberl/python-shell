from src.parser.antlr.CommandsParser import CommandsParser
from src.parser.antlr.CommandsLexer import CommandsLexer
from src.parser.antlr.CommandsListener import CommandsListener
from antlr4 import ParseTreeWalker, InputStream, CommonTokenStream;


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
