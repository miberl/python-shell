import unittest

from exceptions.unexpected_argument_error import UnexpectedArgumentError


class TestUnexpectedArgumentError(unittest.TestCase):
    def test_raises_error(self):
        with self.assertRaises(UnexpectedArgumentError) as err:
            raise UnexpectedArgumentError('bad things')

        assert str(err.exception) == 'Unexpected argument: bad things'
