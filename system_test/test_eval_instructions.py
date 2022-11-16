from application import Application
from setup_test import TestSetup


class TestApp(Application):
    def run(self, args, inpt, out):
        return args, inpt


class TestEvalInstruction(TestSetup):
    def test_simple_command(self):
        pass
