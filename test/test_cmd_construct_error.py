from exceptions.command_construct_error import CommandConstructError
from setup_test import TestSetup


class TestInvalidSyntax(TestSetup):
    # Minimal testing as this is largely done by the parser
    # Should never really be thrown manually like this
    def test_throw_formatted_message(self):
        try:
            raise CommandConstructError("Bad Symbol with pipe")
        except CommandConstructError as e:
            self.assertEqual(str(e), "Error while constructing command after parsing, Bad Symbol with pipe")
