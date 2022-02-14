import unittest
import main 
import os
from exceptions import InvalidCommandLineExecution

class TestArgumentParse(unittest.TestCase):

    def setUp(self):
        filename = 'input_file.txt'
        if not os.path.exists(filename):
            open(filename, 'w').close()

    def tearDown(self):
        filename = 'input_file.txt'
        os.remove(filename)

    '''
        Test for valid parameters. (n=3)
    '''
    def test_valid_number_of_args(self):
        valid_args = ["main.py", "input_file.txt", "output_file.txt"] 
        try:
            main.parse_command_line_args(valid_args)
        except:
            self.fail("parse_command_line_args raised Exception unexpectedly!")

    '''
        Test for invalid params (n>3)
    '''
    def test_invalid_number_of_args(self):
        args = ["main.py", "input_file.txt", "output_file.txt", "random"] 
        self.assertRaises(InvalidCommandLineExecution,
                          main.parse_command_line_args, args)

    '''
        Test for invalid params (n<3)
    '''
    def test_invalid_number_of_args_2(self):
        args = ["main.py", "input_file.txt"] 
        self.assertRaises(InvalidCommandLineExecution,
                      main.parse_command_line_args, args)


    '''
        Test for invalid input file
    '''
    def test_invalid_number_of_args_2(self):
        args = ["main.py", "non-existent-file.txt", "output_file.txt"] 
        self.assertRaises(FileNotFoundError,
                      main.parse_command_line_args, args)


