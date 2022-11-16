import unittest
from shell import eval


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = eval("echo foo")
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
