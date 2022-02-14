import sys
from exceptions import InvalidCommandLineExecution, InvalidInputFileException
from setup_logging import logger
import os.path
from theater import Theater

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

'''
    This function converts the allocations into the desired output format
    to be written in the file.
'''
def store_allocations(op_file_contents, customer, allocations):
    if customer in op_file_contents:
        new_allocation = op_file_contents[customer]+ "," + allocations
        op_file_contents[customer] = new_allocation
    else:
        op_file_contents[customer] = allocations

    return op_file_contents

'''
    This function writes to the output file passed in the command line
    argument.
'''
def write_to_file(op_file_contents, output_file):
    with open(output_file, 'w') as f: 
        for key, value in op_file_contents.items(): 
            f.write('%s %s\n' % (key, value))

def book_seats(input_file, output_file): 
    with open(input_file, 'r') as f:
        lines = f.readlines()

    theater = Theater()
    output_file_contents = {}

    for line in lines:
        attr = line.split(' ')
        if not len(attr) == 2:
            raise InvalidInputFileException

        num_seats = int(attr[1])
        customer = attr[0]

        while num_seats > 20:
            allocations = theater.allocate_seats(20)
            if not allocations:
                logger.info("customer {} could not be allocated because of unavailable spaces".format(customer))
                break
            num_seats -= 20
            logger.info("customer {} has been allocated {}".format(customer, allocations))
            output_file_contents = store_allocations(output_file_contents, customer, allocations)
        
        allocations = theater.allocate_seats(num_seats)

        if not allocations:
            logger.info("customer {} could not be allocated because of unavailable spaces".format(customer))
            continue

        output_file_contents = store_allocations(output_file_contents, customer, allocations)
        logger.info("customer {} has been allocated {}".format(customer, allocations))

    write_to_file(output_file_contents, output_file)

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

    try:
        ret = book_seats(input_file, output_file)
    except InvalidInputFileException:
        logger.error("main: input file is invalid")
