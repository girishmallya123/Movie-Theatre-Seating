from setup_logging import logger

class Theater():
    def __init__(self, num_rows = 10, num_cols = 20):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.create_empty_theater()
        
    def create_empty_theater(self):
        self.theater_layout = [[ False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.availability = [ self.num_cols for _ in range(self.num_rows)]

    def is_valid_cell(self, x, y):
        return ((x>=0 and x< self.num_rows) and (y>=0 and y< self.num_cols))

    def calculate_free_seats(self, r_no, c_no, seats):
        free_seats = 0 
        if c_no == 0:
            free_seats = 3

        window_left, window_right =  c_no - 3, c_no + seats + 3
        for i in range(window_left, window_right):
            if self.is_valid_cell(r_no,i) and (not self.theater_layout[r_no][i]):
                free_seats+=1

            if i == self.num_cols -1 :
                free_seats += 3

        return free_seats - seats

    def update_theater_layout(self, row_n, col_n, n_seats):
        for i in range(col_n, col_n + n_seats):
            self.theater_layout[row_n][i] = True

    def convert_to_seat_nums(self, row_num, col_num, num_seats):
        row_identifier = chr(ord('A') + row_num)
        seats = [ "{}{}".format(row_identifier,str(i)) for i in range(col_num, col_num+num_seats)]
        return ",".join(seats)

    def check_row_spacing(self, row_num, col_num, num_seats):
        for i in [row_num - 1, row_num+1]:
            for j in range(col_num, col_num+num_seats):
                if self.is_valid_cell(i, j):
                    if self.theater_layout[i][j]:
                        return False
        return True

    def print_theater_layout(self):
        print(self.theater_layout)

    def allocate_seats(self, num_seats):
        logger.info("theater.allocate_seats: attempting to allocate {} seats".format(num_seats))
        num_seats = int(num_seats)
        row_num = self.num_rows // 2
        col_num = 0 
        row_flip_flag = 1
        counter = 1

        while row_num > 0 and row_num < self.num_rows:
            free_seats = self.calculate_free_seats(row_num, col_num, num_seats)
            if free_seats == 6:
                row_spacing = self.check_row_spacing(row_num, col_num, num_seats)
                if row_spacing:
                    logger.info("Allocating {} seats on row {}".format(num_seats, chr(ord('A') + row_num)))
                    self.update_theater_layout(row_num, col_num, num_seats)
                    return self.convert_to_seat_nums(row_num, col_num, num_seats)
            col_num +=1

            if col_num == self.num_cols-1:
                col_num = 0
                row_num = row_num + (row_flip_flag*counter)
                counter += 1
                row_flip_flag*=-1

