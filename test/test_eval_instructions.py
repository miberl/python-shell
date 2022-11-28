from inputparser.command import Instruction, Command
from setup_test import TestSetup
from shell_runner.eval_instructions import EvalInstructions


class TestEvalInstructions(TestSetup):
    def code_under_test(self, args):
        result = EvalInstructions().eval(args)

        self.out = list(result)

    def setUp(self):
        self.instruction = Instruction()
        self.command = Command('echo')
        self.command.add_arg('hello')
        self.instruction.add(self.command)
        self.instruction2 = Instruction()
        self.command2 = Command('echo')
        self.command2.add_arg('there')
        self.instruction2.add(self.command2)

        self.redirected_output_instruction = Instruction()
        self.redir_out_cmd = Command('echo')
        self.redir_out_cmd.add_arg('hello')
        self.redir_out_cmd.add_redir_out('file_out.txt')
        self.redirected_output_instruction.add(self.redir_out_cmd)

        self.redirected_input_instruction = Instruction()
        self.redir_in_cmd = Command('cat')
        self.redir_in_cmd.add_redir_in('dir1/file2.txt')
        self.redirected_input_instruction.add(self.redir_in_cmd)

    def test_eval_no_instructions(self):
        self.run_test([], [])

    def test_eval_simple_instruction(self):
        self.run_test([self.instruction], ['hello\n'])

    def test_eval_many_instructions(self):
        self.run_test([self.instruction, self.instruction2], ['hello\n', 'there\n'])

    def test_input_redirection(self):
        self.run_test([self.redirected_input_instruction], ['CCC\n'],
                      'application.Application.read_lines', TestSetup.mock_read_lines)

    def test_output_redirection(self):
        TestSetup.lines_written = None
        self.run_test([self.redirected_output_instruction], [],
                      'application.Application.write_lines', TestSetup.mock_write_lines)
        result = TestSetup.lines_written
        assert result == ('file_out.txt', ['hello\n'])

    def test_unsafe_app_run(self):
        instr = Instruction()
        instr.add(Command('_echo'))

        self.run_test([instr], ['\n'])

    def test_instruction_no_command(self):
        instr = Instruction()

        self.run_test([instr], [])

    def test_multiple_files_redir_in(self):
        self.redir_in_cmd.add_redir_in('dir1/file4.txt')

        self.run_test([self.redirected_input_instruction], ['CCC\n', 'AAA\n', 'AAA\n'],
                      'application.Application.read_lines', TestSetup.mock_read_lines)

    def test_bad_app(self):
        bad_cmd = Command('foo')
        instruction = Instruction()
        instruction.add(bad_cmd)

        with self.assertRaises(ValueError) as err:
            self.run_test([instruction], [])

        assert 'unsupported application foo' in str(err.exception)
