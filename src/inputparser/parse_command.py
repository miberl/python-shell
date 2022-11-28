from inputparser.antlr.CommandsListener import CommandsListener
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsLexer import CommandsLexer
from antlr4 import ParseTreeWalker, InputStream, CommonTokenStream
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.parser_error_listner import ParserErrorListener


class ParseCommands:
    def parse_listen(self, cmd: str, listener: CommandsListener) -> None:
        """
        Parses a string and processes it using a listener object.

        :param cmd: String to be parsed
        :param listener: Listener object that listens to the produced parse tree
        :return: None
        """
        tree = self._get_tree(cmd)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def parse_visitor(self, cmd: str, visitor: CommandsVisitor) -> None:
        """
        Parses a string and processes it using a visitor object.

        :param cmd: String to be parsed
        :param visitor: Listener object that visits nodes in the produced parse tree
        :return: None
        """
        tree = self._get_tree(cmd)
        visitor.visit(tree)

    @staticmethod
    def _get_tree(cmd: str) -> CommandsParser.ProgContext:
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
