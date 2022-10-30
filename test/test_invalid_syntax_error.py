from exceptions.invalid_syntax_error import InvalidSyntaxError
from setup_test import TestSetup


class TestInvalidSyntax(TestSetup):
    # Minimal testing as this is largely done by the parser
    # Should never really be thrown manually like this
    def test_throw_formatted_message(self):
        try:
            raise InvalidSyntaxError("ls -a `a'")
        except InvalidSyntaxError as e:
            self.assertEqual(str(e), "Invalid syntax, see 'ls -a `a\'', stopping!")
