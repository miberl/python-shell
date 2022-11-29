import unittest
import subprocess


class TestSetup(unittest.TestCase):
    SHELL_IMAGE = "comp0010-test"
    TEST_VOLUME = "comp0010-test-volume"
    TEST_IMAGE = "comp0010-test-image"
    TEST_DIR = "/test"

    @classmethod
    def eval(cls, cmdline, shell="/comp0010/sh"):
        volume = cls.TEST_VOLUME + ":" + cls.TEST_DIR + ":"
        args = [
            "docker",
            "run",
            "--rm",
            "-v",
            volume,
            cls.TEST_IMAGE,
            shell,
            "-c",
            cmdline,
        ]
        p = subprocess.run(args, capture_output=True)
        return p.stdout.decode()

    @classmethod
    def setUpClass(cls):
        dockerfile = ("FROM " + cls.SHELL_IMAGE + "\nWORKDIR " + cls.TEST_DIR).encode()
        args = ["docker", "build", "-t", cls.TEST_IMAGE, "-"]
        p = subprocess.run(args, input=dockerfile, stdout=subprocess.DEVNULL)
        if p.returncode != 0:
            print("error: failed to build test image")
            exit(1)

    def setUp(self):
        p = subprocess.run(
            ["docker", "volume", "create", self.TEST_VOLUME], stdout=subprocess.DEVNULL
        )
        if p.returncode != 0:
            print("error: failed to create test volume")
            exit(1)

        # Do not change -> Base setup used by provided system tests
        base_setup = [
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
            "touch dir1/subdir/.hidden",  # Note: this command fails
        ]
        # Custom files & directories
        custom_setup = [
            "echo AAA > dir1/file3.txt",
            "echo AAA >> dir1/file3.txt",
            "echo BBB >> dir1/file3.txt",
            "echo CCC >> dir1/file3.txt",
            "echo CCC >> dir1/file3.txt",
            "echo CCC >> dir1/file3.txt",
            "echo AAA > dir1/file4.txt",
            "echo AAA >> dir1/file4.txt",
            "echo secret >> dir2/subdir/.hidden",
            "echo secret >> dir2/subdir/normal",
            "echo Andhra Pradesh > dir1/cutTest.txt",
            "echo Arunachal Pradesh >> dir1/cutTest.txt",
            "echo Assam >> dir1/cutTest.txt",
            "echo Bihar >> dir1/cutTest.txt",
            "echo Chhattisgarh >> dir1/cutTest.txt",
        ]

        filesystem_setup = ";".join(base_setup + custom_setup)
        self.eval(filesystem_setup, shell="/bin/bash")

    def tearDown(self):
        p = subprocess.run(
            ["docker", "volume", "rm", self.TEST_VOLUME], stdout=subprocess.DEVNULL
        )
        if p.returncode != 0:
            print("error: failed to remove test volume")
            exit(1)

    def run_test(self, cmd, result):
        stdout = self.eval(cmd)
        res = stdout.rstrip().split("\n")
        self.assertEqual(res, result)

    def run_test_expect_exception(self, cmd, exception=RuntimeError):
        self.assertRaises(exception, self.eval(cmd))

    def run_test_no_order(self, cmd, result):
        stdout = self.eval(cmd)
        res = stdout.rstrip().split("\n")
        self.assertEqual(sorted(res), sorted(result))
