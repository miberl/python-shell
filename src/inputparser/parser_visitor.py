from antlr4 import TerminalNode
from exceptions.command_construct_error import InstructionConstructError
from inputparser.antlr.CommandsParser import CommandsParser
from inputparser.antlr.CommandsVisitor import CommandsVisitor
from inputparser.command import Command, Instruction
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
        cmd = self.get_command_app(command)
        self.get_command_args(cmd, command)
        self.get_command_redirs(cmd, command)
        return cmd

    def get_command_app(self, command: CommandsParser.CommandContext) -> Command:
        app = command.getChild(0, CommandsParser.AppContext)
        self.throw_if_none(app, 'app')
        app_text = self.eval_atom(app)
        cmd = Command(app_text)
        return cmd

    def get_command_args(self, cmd: Command, command: CommandsParser.CommandContext):
        args = command.getTypedRuleContexts(CommandsParser.ArgContext)
        for arg in args:
            arg_text = self.eval_atom(arg)
            cmd.add_arg(arg_text)

    def get_command_redirs(self, cmd: Command, command: CommandsParser.CommandContext):
        file_in = command.getChild(0, CommandsParser.Redir_inContext)
        file_out = command.getChild(0, CommandsParser.Redir_outContext)

        if file_in is not None:
            file_in_text = self.eval_atom(file_in)
            cmd.add_redir_in(file_in_text)
        if file_out is not None:
            file_out_text = self.eval_atom(file_out)
            cmd.add_redir_out(file_out_text)

    @staticmethod
    def throw_if_none(elem, err):
        if elem is None:
            raise InstructionConstructError(f'Expected {err}, got none while parsing')

    def eval_atom(self, atom_container) -> str:
        atom = atom_container.getChild(0, CommandsParser.AtomContext)
        self.throw_if_none(atom, 'atom')

        out = []

        for child in atom.getChildren():
            if isinstance(child, CommandsParser.SubstitutedContext):
                terminal = child.getChild(0, CommandsParser.TerminalContext)
                instructions = self.get_terminal(terminal)
                out.append(self.eval_substituted(instructions))
            elif isinstance(child, CommandsParser.GlobbedContext):
                out.append(None)
            elif isinstance(child, CommandsParser.Quoted_textContext):
                text_words = list(child.getChildren())
                for word in text_words[1:-1]:
                    out.append(word.symbol.text)
            elif isinstance(child, TerminalNode) and child.symbol.type == CommandsLexer.WORD:
                out.append(child.symbol.text)

        result = self.globbed_results(out)

        return result

    def eval_substituted(self, instructions):
        out = ''
        for line in EvalInstructions().eval(instructions):
            out += line
        return out

    def globbed_results(self, out):
        if None not in out:
            return self.combined_str(out)

        poss = self.get_list_of_items_in_current_dir()

        result = ''
        for pos in poss:
            if self.pos_satisfies_out(out, pos):
                result += pos + ' '

        if result == '':
            raise InstructionConstructError('No Globbing match found')
        return result[:-1]

    @staticmethod
    def get_list_of_items_in_current_dir():
        i = Instruction()
        i.add(Command('ls'))
        poss = EvalInstructions().eval([i])
        for i, pos in enumerate(poss):
            poss[i] = pos[:-1]
        return poss

    @staticmethod
    def combined_str(out) -> str:
        result = ''
        for word in out:
            result += word
        return result

    def pos_satisfies_out(self, out, pos, i=0):
        if not out and len(pos) == i:
            return True
        elif not out or i >= len(pos) or (out[0] is not None and i + len(out[0]) > len(pos)):
            return False

        if out[0] is None:
            return self.pos_satisfies_out(out[1:], pos, i) or self.pos_satisfies_out(out, pos, i + 1)
        else:
            l = len(out[0])
            return pos[i: i + l] == out[0] and self.pos_satisfies_out(out[1:], pos, i + l)
