from antlr4.error.ErrorListener import ErrorListener

from exceptions.invalid_syntax_error import InvalidSyntaxError


class ParserErrorListener(ErrorListener):
    # Only interested in catching syntax errors at this stage

    def __init__(self):
        super(ParserErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise InvalidSyntaxError(msg)

    def reportAmbiguity(self, *kwargs):
        return

    def reportAttemptingFullContext(self, *kwargs):
        return

    def reportContextSensitivity(self, *kwargs):
        return
