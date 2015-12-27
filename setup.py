from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

# import io, codecs, os

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='python-app-template',
    version='0.0.1',
    description='Simple project description',
    author='German A. Rivera',
    author_email='garivera89@gmail.com',
    url='https://github.com/gerrive/python-app-template.git',
    platforms='any',
    test_require=['tox'],
    cmdclass={'test': Tox},
    extras_require={'testing': ['pytest']},
    packages=['pyapp']
)
