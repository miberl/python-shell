from unittest import TestCase

from exceptions.command_construct_error import InstructionConstructError
from inputparser.command import Command, Instruction


class TestHead(TestCase):
    def setUp(self) -> None:
        self.app_only = Command('cmd')
        self.single_flag = Command('cmd_1')
        self.single_flag.add_arg('-f')

    def test_constructor(self):
        sut = Command("cmd")
        self.assertEqual("cmd", sut.get_app())

    def test_add_arg_no_flag(self):
        self.app_only.add_arg('hello')

        self.assertEqual(self.app_only.get_args(), ['hello'])

    def test_many_args_no_flags(self):
        self.app_only.add_arg('hello')
        self.app_only.add_arg('there')
        self.app_only.add_arg('mate')

        self.assertEqual(self.app_only.get_args(),
                         ['hello', 'there', 'mate'])

    def test_add_flag(self):
        self.app_only.add_arg('-f')

        self.assertEqual(self.app_only.get_args(), ['-f'])

    def test_add_arg_after_flag(self):
        self.single_flag.add_arg('hello')
        self.assertEqual(self.single_flag.get_args(),
                         ['-f', 'hello'])

    def test_add_second_flag_after_arg(self):
        self.single_flag.add_arg('-g')
        self.assertEqual(self.single_flag.get_args(),
                         ['-f', '-g'])

    def test_add_file_in(self):
        self.app_only.add_redir_in('file_one.txt')
        self.assertEqual(self.app_only.get_redirs(), ('file_one.txt', None))

    def test_add_file_out(self):
        self.app_only.add_redir_out('file_two.txt')
        self.assertEqual(self.app_only.get_redirs(), (None, 'file_two.txt'))

    def test_add_redir_in_and_out(self):
        self.app_only.add_redir_in('file_one.txt')
        self.app_only.add_redir_out('file_two.txt')

        self.assertEqual(self.app_only.get_redirs()
                         , ('file_one.txt', 'file_two.txt'))


class TestInstruction(TestCase):
    def setUp(self) -> None:
        self.empty_instruction = Instruction()
        self.example_command = Command('cmd_1')
        self.example_command_two = Command('cmd_2')
        self.example_command_three = Command('cmd_3')
        self.populated_instruction = Instruction()
        self.populated_instruction.add(self.example_command)
        self.populated_instruction.add(self.example_command_two)
        self.populated_instruction.add(self.example_command_three)

    def test_construct(self):
        sut = Instruction()

    def test_empty_not_has_next(self):
        assert not self.empty_instruction.has_next()

    def test_empty_if_get_will_throw(self):
        try:
            self.empty_instruction.get_next_command()
            assert False
        except InstructionConstructError as e:
            assert str(e) == 'Error while constructing command after parsing, No command in instruction'

    def test_empty_throw_if_add_bad_obj(self):
        try:
            self.empty_instruction.add('hello')
        except InstructionConstructError as e:
            assert str(e) == 'Error while constructing command after parsing, ' \
                             'Expected command when adding to instruction'

    def test_add_to_empty_has_next(self):
        self.empty_instruction.add(self.example_command)
        assert self.empty_instruction.has_next()

    def test_add_to_empty_get_next(self):
        self.empty_instruction.add(self.example_command)
        assert self.example_command == self.empty_instruction.get_next_command()

    def test_get_many_commands(self):
        commands = []
        while self.populated_instruction.has_next():
            commands.append(self.populated_instruction.get_next_command())

        assert commands == [self.example_command, self.example_command_two, self.example_command_three]
