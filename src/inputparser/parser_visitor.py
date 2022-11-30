from antlr4 import TerminalNode
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.command import Command, Instruction
from inputparser.globbing import Globbing
from shell_runner.eval_instructions import EvalInstructions
from inputparser.antlr.CommandsLexer import CommandsLexer


class ParseVisitor(CommandsVisitor):
    """
    NAME
        ParseVisitor
    DESCRIPTION
        Class used to traverse produced parse tree. Used in combination
        with ParseCommand.
        Generates set of Instruction objects that can be gotten.
    METHODS
        get_instructions()
            Returns list of instruction objects built from parse tree
        internal visitor methods
            Used to traverse tree
    """

    def __init__(self):
        self.instructions = []

    def get_instructions(self) -> [Instruction]:
        """
        Returns list of instruction objects built from parse tree, encoding
        information in command

        :return: List of instruction objects
        """
        return self.instructions

    def visitProg(self, ctx: CommandsParser.ProgContext):
        terminal = ctx.getChild(0, CommandsParser.TerminalContext)
        if terminal is not None:
            self.instructions = self.get_terminal(terminal)

    def get_terminal(self, ctx):
        instructs = ctx.getTypedRuleContexts(CommandsParser.InstructionContext)
        instruction_objs = []
        for instruction in instructs:
            instruction_objs.append(self.get_instruction(instruction))

        return instruction_objs

    def get_instruction(self, instruction):
        cmds = instruction.getTypedRuleContexts(CommandsParser.CommandContext)
        instr = Instruction()

        for cmd in cmds:
            instr.add(self.get_command(cmd))

        return instr

    def get_command(self, cmd: CommandsParser.CommandContext):
        cmd_args = self.get_command_args(cmd)
        command = Command(cmd_args[0])
        for arg in cmd_args[1:]:
            command.add_arg(arg)

        self.get_command_redirs(command, cmd)
        return command

    def get_command_args(self, cmd: CommandsParser.CommandContext) -> [str]:
        args = cmd.getTypedRuleContexts(CommandsParser.ArgContext)
        arg_list = []
        for arg in args:
            arg_text = self.eval_atom(arg)
            arg_list += arg_text
        return arg_list

    def get_command_redirs(
        self, cmd: Command, command: CommandsParser.CommandContext
    ) -> (str, str):
        file_in = command.getChild(0, CommandsParser.Redir_inContext)
        i = 1
        while file_in is not None:
            file_in_text = self.eval_atom(file_in)[-1]
            cmd.add_redir_in(file_in_text)
            file_in = command.getChild(i, CommandsParser.Redir_outContext)
            i += 1

        file_out = command.getChild(0, CommandsParser.Redir_outContext)
        while file_out is not None:
            file_out_text = self.eval_atom(file_out)[-1]
            cmd.add_redir_out(file_out_text)
            file_out = command.getChild(i, CommandsParser.Redir_outContext)
            i += 1

    def eval_atom(self, atom_container) -> [str]:
        atom = atom_container.getChild(0, CommandsParser.AtomContext)
        assert atom is not None
        out = ""
        needs_glob = False

        for child in atom.getChildren():
            if isinstance(child, CommandsParser.SubstitutedContext):
                out += self.process_substituted(child)
            elif isinstance(child, CommandsParser.GlobbedContext):
                out += "*"
                needs_glob = True
            elif isinstance(child, CommandsParser.Quoted_textContext):
                out = self._eval_quoted_text(child, out)
            else:
                assert (
                    isinstance(child, TerminalNode)
                    and child.symbol.type == CommandsLexer.WORD
                )
                out += child.symbol.text

        if needs_glob:
            return Globbing().glob(out)

        return [out]

    def _eval_quoted_text(self, child, out):
        for quote_node in child.children[1:-1]:
            if isinstance(quote_node, CommandsParser.SubstitutedContext):
                out += self.process_substituted(quote_node)
            else:
                out += quote_node.symbol.text
        return out

    def process_substituted(self, child):
        terminal = child.getChild(0, CommandsParser.TerminalContext)
        instructions = self.get_terminal(terminal)
        return self.eval_substituted(instructions)

    @staticmethod
    def eval_substituted(instructions):
        out = ""
        for line in EvalInstructions().eval(instructions):
            out += line
        return out.strip("\n").replace("\n", " ")
