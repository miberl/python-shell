from inputparser.parser_visitor import ParseVisitor

from inputparser.parse_command import ParseCommands

from apps import cat, echo, ls, cd, pwd, head, grep, tail, uniq, sort, cut
from shell_runner.eval_instructions import EvalInstructions


class Shell:

    def run_instructions(self, instruction: str):
        instructions = self.get_instructions(instruction)

        return EvalInstructions().eval(instructions)

    def get_instructions(self, instruction) -> [(str, [str])]:
        visitor = ParseVisitor()
        parser = ParseCommands()
        parser.parse_visitor(instruction, visitor)
        instructions = visitor.get_instructions()
        return instructions
