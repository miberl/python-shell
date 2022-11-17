from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from apps import cat, echo, ls, cd, pwd, head, grep, tail, uniq, sort, cut, history
from shell_runner.shell_history import ShellHistory
from shell_runner.eval_instructions import EvalInstructions

class ShellExec:
    def __init__(self):
        self.history = ShellHistory()

    def run_instructions(self, instruction: str):
        self.history.add_to_history(instruction)
        instructions = self.get_instructions(instruction)
        
        return EvalInstructions().eval(instructions)

    def get_instructions(self, instruction) -> [(str, [str])]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(instruction, visitor)
        instructions = visitor.get_instructions()
        return instructions
