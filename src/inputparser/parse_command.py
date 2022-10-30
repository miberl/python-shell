from inputparser.antlr.CommandsListener import CommandsListener
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsLexer import CommandsLexer
from antlr4 import ParseTreeWalker, InputStream, CommonTokenStream
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.parser_error_listner import ParserErrorListener


class ParseCommands:
    def parse_listen(self, cmd: str, listener: CommandsListener):
        tree = self.get_tree(cmd)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def parse_visitor(self, cmd: str, visitor: CommandsVisitor):
        tree = self.get_tree(cmd)
        visitor.visit(tree)

    @staticmethod
    def get_tree(cmd):
        input_stream = InputStream(cmd)

        # Lex and parse input
        lexer = CommandsLexer(input_stream)
        lexer.addErrorListener(ParserErrorListener())
        stream = CommonTokenStream(lexer)
        parser = CommandsParser(stream)

        # Check for errors and get parse tree
        parser.addErrorListener(ParserErrorListener())
        tree = parser.prog()
        return tree
