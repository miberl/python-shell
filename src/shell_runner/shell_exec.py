from inputparser.command import Instruction
from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from shell_runner.shell_history import ShellHistory
from shell_runner.eval_instructions import EvalInstructions

class ShellExec:
    def __init__(self):
        self.history = ShellHistory()

    def run_instructions(self, cmdline: str):
        self.history.add_to_history(cmdline)
        instructions = self.get_instructions_object_from_string(cmdline)
        
        return EvalInstructions().eval(instructions)

    def get_instructions_object_from_string(self, cmdline: str) -> [Instruction]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(cmdline, visitor)
        instructions = visitor.get_instructions()
        return instructions
