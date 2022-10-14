import unittest

from collections import deque
from apps.echo import Echo
import subprocess


class TestCat(unittest.TestCase):
    def setUp(self):
        p = subprocess.run(
            ["docker", "volume", "create", self.TEST_VOLUME], stdout=subprocess.DEVNULL
        )
        if p.returncode != 0:
            print("error: failed to create test volume")
            exit(1)
        filesystem_setup = ";".join(
            [
                "echo \"''\" > test.txt",
                "mkdir dir1",
                "mkdir -p dir2/subdir",
                "echo AAA > dir1/file1.txt",
                "echo BBB >> dir1/file1.txt",
                "echo AAA >> dir1/file1.txt",
                "echo CCC > dir1/file2.txt",
                "for i in {1..20}; do echo $i >> dir1/longfile.txt; done",
                "echo AAA > dir2/subdir/file.txt",
                "echo aaa >> dir2/subdir/file.txt",
                "echo AAA >> dir2/subdir/file.txt",
                "touch dir1/subdir/.hidden",
            ]
        )
        self.eval(filesystem_setup, shell="/bin/bash")


if __name__ == "__main__":
    unittest.main()
