import unittest

from exceptions.unknown_option_error import UnknownFlagError


class TestUnexpectedArgumentError(unittest.TestCase):
    def test_raises_error(self):
        with self.assertRaises(UnknownFlagError) as err:
            raise UnknownFlagError('bad things')

        assert str(err.exception) == 'Unknown option flag: bad things'
