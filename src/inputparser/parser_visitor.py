from antlr4 import TerminalNode
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.command import Command, Instruction
from inputparser.globbing import Globbing
from shell_runner.eval_instructions import EvalInstructions
from inputparser.antlr.CommandsLexer import CommandsLexer


class ParseVisitor(CommandsVisitor):
    def __init__(self):
        self.instructions = []

    def get_instructions(self):
        return self.instructions

    def visitProg(self, ctx: CommandsParser.ProgContext):
        terminal = ctx.getChild(0, CommandsParser.TerminalContext)
        self.instructions = self.get_terminal(terminal)

    def get_terminal(self, ctx):
        instructions = ctx.getTypedRuleContexts(CommandsParser.InstructionContext)
        instruction_objs = []
        for instruction in instructions:
            instruction_objs.append(self.get_instruction(instruction))

        return instruction_objs

    def get_instruction(self, instruction):
        commands = instruction.getTypedRuleContexts(CommandsParser.CommandContext)
        instr = Instruction()

        for command in commands:
            instr.add(self.get_command(command))

        return instr

    def get_command(self, command: CommandsParser.CommandContext):
        cmd_args = self.get_command_args(command)
        cmd = Command(cmd_args[0])
        for arg in cmd_args[1:]:
            cmd.add_arg(arg)

        self.get_command_redirs(cmd, command)
        return cmd

    def get_command_args(self, command: CommandsParser.CommandContext) -> [str]:
        args = command.getTypedRuleContexts(CommandsParser.ArgContext)
        arg_list = []
        for arg in args:
            arg_text = self.eval_atom(arg)
            arg_list += arg_text
        return arg_list

    def get_command_redirs(self, cmd: Command, command: CommandsParser.CommandContext) -> (str, str):
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
        out = ''
        needs_glob = False

        for child in atom.getChildren():
            if isinstance(child, CommandsParser.SubstitutedContext):
                out += self.process_substituted(child)
            elif isinstance(child, CommandsParser.GlobbedContext):
                out += '*'
                needs_glob = True
            elif isinstance(child, CommandsParser.Quoted_textContext):
                for quote_child in child.children[1:-1]:
                    if isinstance(quote_child, CommandsParser.SubstitutedContext):
                        out += self.process_substituted(quote_child)
                    else:
                        out += quote_child.symbol.text
            else:
                assert isinstance(child, TerminalNode) and child.symbol.type == CommandsLexer.WORD
                out += child.symbol.text

        if needs_glob:
            return Globbing().glob(out)

        return [out]

    def process_substituted(self, child):
        terminal = child.getChild(0, CommandsParser.TerminalContext)
        instructions = self.get_terminal(terminal)
        return self.eval_substituted(instructions)

    def eval_substituted(self, instructions):
        out = ''
        for line in EvalInstructions().eval(instructions):
            out += line
        return out.strip('\n').replace('\n', ' ')
