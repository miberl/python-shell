from inputparser.globbing import Globbing
from setup_test import TestSetup


class TestGlobbing(TestSetup):
    def code_under_test(self, pattern: str):
        self.out = Globbing().glob(pattern)

    def test_basic_glob(self):
        self.run_test('*', ['dir1', 'dir2', 'test.txt'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glob_thing_before(self):
        self.run_test('di*', ['dir1', 'dir2'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_surrounded_glob(self):
        self.run_test('d*2', ['dir2'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_globbing_looks_into_directories(self):
        self.run_test('dir1/*', ['dir1/cutTest.txt', 'dir1/file1.txt', 'dir1/file2.txt',
                                 'dir1/file3.txt', 'dir1/file4.txt', 'dir1/longfile.txt'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glob_on_directory(self):
        self.run_test('*/*', ['dir1/cutTest.txt', 'dir1/file1.txt', 'dir1/file2.txt',
                      'dir1/file3.txt', 'dir1/file4.txt', 'dir1/longfile.txt', 'dir2/subdir'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glob_not_show_hidden(self):
        self.run_test('dir2/subdir/*', ['dir2/subdir/file.txt', 'dir2/subdir/normal'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glob_absolute_path(self):
        self.run_test('/*', ['/dir1', '/dir2', '/test.txt'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glob_only_dir(self):
        self.run_test('/*/', ['/dir1/', '/dir2/'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)

    def test_glop_prepend_dot(self):
        self.run_test('./*', ['dir1', 'dir2', 'test.txt'],
                      'application.Application.get_dir_contents', TestSetup.mock_os_walk)
