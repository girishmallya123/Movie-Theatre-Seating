### Movie Theater Seating Challenge

**Implemented in:**  Python 3.9
**Requirements**: Python3.9, pip

**Problem Description**:
Implement an algorithm for assigning seats within a movie theater to
fulfill reservation requests. The assignment should maximize both customer satisfaction and customer safety. For the purpose of public safety, assume that a buffer of three seats and/or one row is required.

**Assumptions**:
1) The size of the input file is not too large, say less than 1000 lines. 
2) A group of people that make a reservation cannot be "fragmented". They must be seated together, with the only exception being if the number of seats reserved is over 20. In which case, seat allotment will happen in groups of 20 at a time.
For example, if a reservation request is made by R001 for 26 seats, the algorithm treats it as two requests for 20 seats and 6 seats.
3) Since the problem description has specified that the algorithm should maximize customer safety, we have assumed the distancing norms to include:
	- Buffer of 3 seats on either side. (left & right)
			**AND** 
	- One row on either side. (front & back)
4) Since the problem description has also specified that the algorithm should maximize customer satisfaction, I have assumed that the customers would prefer to be allotted seats near the middle rows as much as possible. 

**Algorithm**
1) Read a line from the input file.
2) Scan the theater layout to look for the number of seats requested. The scanning follows a simple nested for loop as shown below in the pseudocode.
	```python
		for row in num_rows:
			for col in num_cols:
				search seats which satisfy row and column buffer
	```
3) If we cannot find seats that can satisfy the distancing norms, we return and inform the customer that the request could not be satisfied.

**Instructions to run the code**
1) clone the repo by running 
```bash
git clone https://github.com/girishmallya123/Movie-Theatre-Seating.git
```

2) Enter the project directory, 
```bash
cd Movie-Theatre-Seating/
```
3) To run unit tests, run the following command,
```bash
python3.9 -m unittest discover tests
```
4) To run the program, 
```bash
python3.9 main.py input_file.txt output_file.txt
```

***Sample Input file***
```
R001 3

R002 4

R003 12

R004 3

R005 5

R006 2

R007 1

R008 2

R009 4

R010 5
```

***Sample Output File***
```
R001 E1,E2,E3

R002 E7,E8,E9,E10

R003 G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12

R004 E14,E15,E16

R005 G13,G14,G15,G16,G17

R006 E16,E17

R007 D4

R008 F19,F20

R009 C5,C6,C7,C8

R010 C12,C13,C14,C15,C16
```
