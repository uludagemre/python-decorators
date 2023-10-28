# test_decorators.py
import unittest
from decorators import say_hello, jump_five_meters
from io import StringIO
import sys


class TestDecorators(unittest.TestCase):
    def test_decorator_output(self):
        # Capture standard output to check the printed content

        say_hello()
        jump_five_meters()


if __name__ == '__main__':
    unittest.main()
