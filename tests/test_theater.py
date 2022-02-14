import unittest
import theater
import os
from exceptions import InvalidCommandLineExecution, InvalidInputFileException

class TestTheater(unittest.TestCase):

    '''
        Test for valid cells
    '''
    def test_valid_cells(self):
        t = theater.Theater(2, 4)
        self.assertTrue(t.is_valid_cell(0, 0))

    
    def test_valid_cells_2(self):
        t = theater.Theater(2, 4)
        self.assertTrue(t.is_valid_cell(1, 3))

    
    def test_valid_cells_3(self):
        t = theater.Theater(2, 4)
        self.assertFalse(t.is_valid_cell(5, 5))


    def test_valid_cells_4(self):
        t = theater.Theater(2, 4)
        self.assertFalse(t.is_valid_cell(5, 5))

    
    '''
        Test for free seats calculator
    '''
    def test_calc_free_seats(self):
        t = theater.Theater(5, 10)
        self.assertEqual(t.calculate_free_seats(0, 0, 20), 0)
    
    def test_calc_free_seats_2(self):
        t = theater.Theater(5, 10)

        # Create a scenario where the first row has 6 available seats
        t.theater_layout[0] = [True, True, True, True, False, False, False, False, False, False]
        self.assertEqual(t.calculate_free_seats(0, 0, 1), 2)
        self.assertEqual(t.calculate_free_seats(0, 1, 1), 0)
        self.assertEqual(t.calculate_free_seats(0, 4, 1), 3)
        self.assertEqual(t.calculate_free_seats(0, 9, 1), 6)
    
    '''
        Test for update theater layout
    '''
    def test_update_theater(self):
        t = theater.Theater(5, 10)

        r_no = 3
        c_no = 3
        num_seats = 2

        t.update_theater_layout(r_no, c_no, num_seats)
        for i in range(c_no, c_no + num_seats):
            self.assertTrue(t.theater_layout[r_no][i])
    
    
    '''
        Test to check the algorithm that converts alloted seat numbers in grid
        to the format specified in the problem description.
    '''
    def test_convert_to_seat_nums(self):
        t = theater.Theater(5, 10)

        r_no = 3
        c_no = 3
        num_seats = 2

        seat_nums = t.convert_to_seat_nums(r_no, c_no, num_seats)
        self.assertEqual(seat_nums, "D3,D4")


    def test_convert_to_seat_nums_2(self):
        t = theater.Theater(5, 10)

        r_no = 0
        c_no = 0
        num_seats = 5

        seat_nums = t.convert_to_seat_nums(r_no, c_no, num_seats)
        self.assertEqual(seat_nums, "A0,A1,A2,A3,A4")
    
    '''
        Tests for the seat allocation algorithm
    '''

    '''
        Test1: Algorithm must start allocating from the middle most row for
        "best customer experience".

        The middle most rows when there are 5, would be the 2nd one, which is
        B.
    '''

    def test_allocate_seats(self):
        t = theater.Theater(5, 10)
        num_seats = 3

        allocations = t.allocate_seats(3)
        self.assertEqual(allocations, "B0,B1,B2")

        '''
            If 3 more seats are requested by the next customer at this point,
            it must allocate seats with 3 empty seats between them, so it must
            be seats B6, B7, B8.
        '''

        allocations = t.allocate_seats(3)
        self.assertEqual(allocations, "B7,B8,B9")

        '''
            Assume 5 more seats are to be booked now, now that row 'B' cannot
            accomodate these seats, it will now go to row 'D'. Since 'A' and
            'C' do not have a block of 5 empty seats without breaking the
            distancing condition in the front/back row.
        '''

        allocations = t.allocate_seats(5)
        self.assertEqual(allocations, "D0,D1,D2,D3,D4")


    '''
        Test2: The allocaiton algorithm returns an empty string if it cannot
        find enough seats to allocate.

        Let the theater have just a single row with 10 seats,
        Let it allocate 3 seats first, now it cannot.
        And now when we request for 7 more seats it must fail.
    '''
    def test_allocate_seats_2(self):
        t = theater.Theater(1, 10)

        allocations = t.allocate_seats(3)
        self.assertEqual(allocations, "A0,A1,A2")

        allocations = t.allocate_seats(9)
        self.assertEqual(allocations, "")
