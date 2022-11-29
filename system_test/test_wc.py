from setup_test import TestSetup


class TestWc(TestSetup):
    def test_reads_from_file(self):
        self.run_test('wc dir1/file1.txt',
                      ['    3    3    12 dir1/file1.txt'])

    def test_reads_multiple_files(self):
        self.run_test('wc dir1/file1.txt dir1/file2.txt',
                      ['    3    3    12 dir1/file1.txt',
                       '    1    1     4 dir1/file2.txt',
                       '    4    4    16 total'])

    def test_l_option(self):
        self.run_test('wc -l dir1/file1.txt',
                      ['    3 dir1/file1.txt'])

    def test_w_option(self):
        self.run_test('wc -w dir1/file1.txt',
                      ['    3 dir1/file1.txt'])

    def test_c_option(self):
        self.run_test('wc -c dir1/file1.txt',
                      ['    12 dir1/file1.txt'])

    def test_m_option(self):
        self.run_test('wc -m dir1/file1.txt',
                      ['    12 dir1/file1.txt'])

    def test_tabs_as_word_delimiter(self):
        self.run_test('wc -l dir1/file1.txt',
                      ['    3 dir1/file1.txt'])
