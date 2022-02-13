import sys
from exceptions import InvalidCommandLineExecution
from setup_logging import logger
import os.path

def parse_command_line_args(args):
    n = len(args)

    '''
        The program will be executed with the program name, input file path and
        output file path as its 3 arguments, we will raise an exception if
        the number of args is not eq to 3.
    '''

    if not (n == 3):
        raise InvalidCommandLineExecution

    input_file = args[1]
    output_file = args[2]

    if not (os.path.isfile(input_file)):
        raise FileNotFoundError

    return input_file, output_file

if __name__ == "__main__":
    cmd_line_args = sys.argv

    try:
        input_file, output_file = parse_command_line_args(cmd_line_args)
    except InvalidCommandLineExecution:
        logger.error("main: Invalid command line execution")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("main: The input file does not exist")
        sys.exit(1)
