from unittest import TestCase

from exceptions.command_construct_error import CommandConstructError
from inputparser.command import Command, Pipe


class TestHead(TestCase):
    def setUp(self) -> None:
        self.app_only = Command('cmd')
        self.single_flag = Command('cmd_1')
        self.single_flag.add_flag('f')

    def test_constructor(self):
        sut = Command("cmd")
        self.assertEqual("cmd", sut.get_app())

    def test_add_arg_no_flag(self):
        self.app_only.add_arg('hello')

        self.assertEqual(self.app_only.get_flags_and_args(), [(None, ['hello'])])

    def test_many_args_no_flags(self):
        self.app_only.add_arg('hello')
        self.app_only.add_arg('there')
        self.app_only.add_arg('mate')

        self.assertEqual(self.app_only.get_flags_and_args(),
                         [(None, ['hello', 'there', 'mate'])])

    def test_add_flag(self):
        self.app_only.add_flag('f')

        self.assertEqual(self.app_only.get_flags_and_args(), [('f', [])])

    def test_add_arg_after_flag(self):
        self.single_flag.add_arg('hello')
        self.assertEqual(self.single_flag.get_flags_and_args(),
                         [('f', ['hello'])])

    def test_add_second_flag_after_arg(self):
        self.single_flag.add_flag('g')
        self.assertEqual(self.single_flag.get_flags_and_args(),
                         [('f', []), ('g', [])])

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


class TestPipe(TestCase):
    def setUp(self) -> None:
        self.empty_pipe = Pipe()
        self.example_command = Command('cmd_1')
        self.example_command_two = Command('cmd_2')
        self.populated_pipe = Pipe()
        self.populated_pipe.set_left(self.example_command)
        self.populated_pipe.set_right(self.example_command_two)

    def test_construct(self):
        sut = Pipe()

    def test_raises_if_pipe_not_populated(self):
        with self.assertRaises(CommandConstructError):
            self.empty_pipe.get_piped_commands()

    def test_raises_if_not_pass_cmd_obj(self):
        with self.assertRaises(CommandConstructError):
            self.empty_pipe.set_left('hello')

    def test_create_pipe_with_left_and_right(self):
        self.empty_pipe.set_left(self.example_command)
        self.empty_pipe.set_right(self.example_command_two)
        self.assertEqual(self.empty_pipe.get_piped_commands(), (self.example_command, self.example_command_two))

    def test_access_commands_in_populated_pipe(self):
        self.assertEqual(self.populated_pipe.get_piped_commands(),
                         (self.example_command, self.example_command_two))
