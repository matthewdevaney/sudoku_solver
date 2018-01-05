class Sudoku(object):

    def __init__(self, puzzle_string):

        # create an empty dictionary to store puzzle information
        self.puzzle = {}

        # load a dictionary with puzzle information: x/y grid co-ordinates, value, locked
        for i in range(len(puzzle_string)):

            # map each value to x/y grid co-ordinates
            puzzle_sub_dict = {
                'x': int(i / 3),
                'y': i % 3,
                'value': int(puzzle_string[i])
            }
            
            # determine if the value can be changed while attempting to solve the puzzle
            if puzzle_sub_dict['value'] == 0:
                puzzle_sub_dict['locked'] = False
            else:
                puzzle_sub_dict['locked'] = True

            # add all values in the sub-dictionary to sudoku puzzle dictionary
            self.puzzle[i] = puzzle_sub_dict
            
    def __str__(self):
        display= """
{} {} {}
{} {} {}
{} {} {}
        """.format(self.puzzle[0]['value'], self.puzzle[1]['value'], self.puzzle[2]['value'],
                   self.puzzle[3]['value'], self.puzzle[4]['value'], self.puzzle[5]['value'],
                   self.puzzle[6]['value'], self.puzzle[7]['value'], self.puzzle[8]['value'])

        return display

    def is_valid(self, check_position):

        # create a set of possible answers to assist with checking that no duplicates appear in the same row column
        numbers_set_x = set(range(1, 4))
        numbers_set_y = set(range(1, 4))

        for i in range(len(self.puzzle.keys())):
            if self.puzzle[i]['value'] != 0:
                # check the x co-ordinate to ensure all values in a row are unique
                if self.puzzle[check_position]['x'] == int(i / 3):
                    if self.puzzle[i]['value'] in numbers_set_x:
                        # remove a number from the set if it appears the same row as the value being checked
                        numbers_set_x.remove(self.puzzle[i]['value'])
                    else:
                        return False
                # check the y co-ordinate to ensure all values in a column are unique
                if self.puzzle[check_position]['y'] == i % 3:
                    if self.puzzle[i]['value'] in numbers_set_y:
                        # remove a number from the set if it appears in the same column as the value being checked
                        numbers_set_y.remove(self.puzzle[i]['value'])
                    else:
                        return False
        return True

    def solve(self, start_pos=0):

        # the sudoku has been solved if the program has filled in every cell with a valid number
        if start_pos == len(self.puzzle.keys()):
            return True

        for i in range(start_pos, len(self.puzzle.keys())):
            if self.puzzle[i]['locked']:
                # the sudoku has been fully solved if all cells have been validated and the last cell is locked
                if start_pos == len(self.puzzle.keys()) - 1:
                    return True
                continue
            else:
                for j in set(range(1, 4)):
                    # load a new value into the current sudoku cell
                    self.puzzle[i]['value'] = j
                    # check if the value is valid and recursively solve the Sudoku
                    if self.is_valid(i) and self.solve(i + 1):
                        return True
                # backtracking
                self.puzzle[i]['value'] = 0
                return False
        return False

# puzzle
sudoku_string = '003021000'

# create a new instance of the sudoku
s = Sudoku(sudoku_string)

# display the unsolved puzzle
print('\nSudoku Puzzle:\n{}'.format(s))

if s.solve():
    print('Sudoku was solved :)\n{}'.format(s))
else:
    print('Sudoku was not solved :(\n{}'.format(s))
