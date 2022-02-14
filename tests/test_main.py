import unittest
import main 
import os
from exceptions import InvalidCommandLineExecution, InvalidInputFileException

class TestArgumentParse(unittest.TestCase):

    def setUp(self):
        filename = 'input_file.txt'
        if not os.path.exists(filename):
            open(filename, 'w').close()

    def tearDown(self):
        filenames = ['input_file.txt', "input_file2.txt", "output_file.txt"]
        
        for f in filenames: 
            if os.path.exists(f):
                os.remove(f)

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


    '''
        Test for invalid input file_contents
    '''
    def test_invalid_file_contents(self):
        args = ["main.py", "input_file2.txt", "output_file.txt"]
        f = open(args[1], "w")
        f.write("abc")
        f.close()

        self.assertRaises(InvalidInputFileException,
                      main.book_seats, args[1], args[2])

    '''
        Test for valid file_contents and valid output file generation
    '''
    def test_valid_contents(self):
        args = ["main.py", "input_file2.txt", "output_file.txt"]
        
        f = open(args[1], "w")
        f.write("R001 3")
        f.close()
        
        main.book_seats(args[1], args[2])
        self.assertTrue(os.path.isfile(args[2])) 
