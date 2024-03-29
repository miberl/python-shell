from exceptions.command_construct_error import InstructionConstructError
from setup_test import TestSetup


class TestInvalidSyntax(TestSetup):
    # Minimal testing as this is largely done by the parser
    # Should never really be thrown manually like this
    def test_throw_formatted_message(self):
        try:
            raise InstructionConstructError("Bad Symbol with pipe")
        except InstructionConstructError as e:
            msg = "Error while constructing command after parsing"
            arg = "Bad Symbol with pipe"
            assert msg in str(e) and arg in str(e)
