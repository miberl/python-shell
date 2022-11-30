from inputparser.command import Instruction
from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from shell_runner.eval_instructions import EvalInstructions


class ShellExec:
    """
    NAME
        ShellExec
    DESCRIPTION
        Runs parser on provided cli and evaluates generated objects
    METHODS
        ShellExec().run_instructions(cmdline)
        Takes a cli and runs the parser on it, calls evaluation methods
    """

    def run_instructions(self, cmdline: str):
        """
        Takes a cli string and runs the parser, calls evaluation methods

        :param cmdline: Command line as a string (eg. 'ls -a dir1/')
        :return: type(deque) - Result of evaluation of command line objects
        """
        instructions = self._get_instructions_object_from_string(cmdline)

        return EvalInstructions().eval(instructions)

    @staticmethod
    def _get_instructions_object_from_string(cmdline: str) -> [Instruction]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(cmdline, visitor)
        instructions = visitor.get_instructions()
        return instructions
