class Sudoku(object):

    def __init__(self, puzzle_string):

        # create an empty dictionary to store puzzle information
        self.puzzle = {}

        # load a dictionary with puzzle information: x/y grid co-ordinates, value, locked
        for i in range(len(puzzle_string)):

            # map each value to x/y grid co-ordinates
            puzzle_sub_dict = {
                'x': int(i / 9),
                'y': i % 9,
                'z': str(int(int(i / 9) / 3)) + str(int(i % 9 / 3)),
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
        display = """
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
----------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
----------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
        """.format(self.puzzle[0]['value'], self.puzzle[1]['value'], self.puzzle[2]['value'],
                   self.puzzle[3]['value'], self.puzzle[4]['value'], self.puzzle[5]['value'],
                   self.puzzle[6]['value'], self.puzzle[7]['value'], self.puzzle[8]['value'],
                   self.puzzle[9]['value'], self.puzzle[10]['value'], self.puzzle[11]['value'],
                   self.puzzle[12]['value'], self.puzzle[13]['value'], self.puzzle[14]['value'],
                   self.puzzle[15]['value'], self.puzzle[16]['value'], self.puzzle[17]['value'],
                   self.puzzle[18]['value'], self.puzzle[19]['value'], self.puzzle[20]['value'],
                   self.puzzle[21]['value'], self.puzzle[22]['value'], self.puzzle[23]['value'],
                   self.puzzle[24]['value'], self.puzzle[25]['value'], self.puzzle[26]['value'],
                   self.puzzle[27]['value'], self.puzzle[28]['value'], self.puzzle[29]['value'],
                   self.puzzle[30]['value'], self.puzzle[31]['value'], self.puzzle[32]['value'],
                   self.puzzle[33]['value'], self.puzzle[34]['value'], self.puzzle[35]['value'],
                   self.puzzle[36]['value'], self.puzzle[37]['value'], self.puzzle[38]['value'],
                   self.puzzle[39]['value'], self.puzzle[40]['value'], self.puzzle[41]['value'],
                   self.puzzle[42]['value'], self.puzzle[43]['value'], self.puzzle[44]['value'],
                   self.puzzle[45]['value'], self.puzzle[46]['value'], self.puzzle[47]['value'],
                   self.puzzle[48]['value'], self.puzzle[49]['value'], self.puzzle[50]['value'],
                   self.puzzle[51]['value'], self.puzzle[52]['value'], self.puzzle[53]['value'],
                   self.puzzle[54]['value'], self.puzzle[55]['value'], self.puzzle[56]['value'],
                   self.puzzle[57]['value'], self.puzzle[58]['value'], self.puzzle[59]['value'],
                   self.puzzle[60]['value'], self.puzzle[61]['value'], self.puzzle[62]['value'],
                   self.puzzle[63]['value'], self.puzzle[64]['value'], self.puzzle[65]['value'],
                   self.puzzle[66]['value'], self.puzzle[67]['value'], self.puzzle[68]['value'],
                   self.puzzle[69]['value'], self.puzzle[70]['value'], self.puzzle[71]['value'],
                   self.puzzle[72]['value'], self.puzzle[73]['value'], self.puzzle[74]['value'],
                   self.puzzle[75]['value'], self.puzzle[76]['value'], self.puzzle[77]['value'],
                   self.puzzle[78]['value'], self.puzzle[79]['value'], self.puzzle[80]['value']
                   )

        return display

    def is_valid(self, check_position):

        # create a set of possible answers to assist with checking that no duplicates appear in the same row column
        numbers_set_x = set(range(1, 10))
        numbers_set_y = set(range(1, 10))
        numbers_set_z = set(range(1, 10))

        for i in range(len(self.puzzle.keys())):
            if self.puzzle[i]['value'] != 0:
                # check the x co-ordinate to ensure all values in a row are unique
                if self.puzzle[check_position]['x'] == int(i / 9):
                    if self.puzzle[i]['value'] in numbers_set_x:
                        # remove a number from the set if it appears the same row as the value being checked
                        numbers_set_x.remove(self.puzzle[i]['value'])
                    else:
                        return False
                # check the y co-ordinate to ensure all values in a column are unique
                if self.puzzle[check_position]['y'] == i % 9:
                    if self.puzzle[i]['value'] in numbers_set_y:
                        # remove a number from the set if it appears in the same column as the value being checked
                        numbers_set_y.remove(self.puzzle[i]['value'])
                    else:
                        return False
                if self.puzzle[check_position]['z'] == str(int(int(i / 9) / 3)) + str(int(i % 9 / 3)):
                    if self.puzzle[i]['value'] in numbers_set_z:
                        # remove a number from the set if it appears in the same box as the value being checked
                        numbers_set_z.remove(self.puzzle[i]['value'])
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
                if i == len(self.puzzle.keys()) - 1:
                    return True
                continue
            else:
                for j in set(range(1, 10)):
                    # load a new value into the current sudoku cell
                    self.puzzle[i]['value'] = j
                    # check if the value is valid and recursively solve the Sudoku
                    if self.is_valid(i) and self.solve(i + 1):
                        return True
                # backtracking
                self.puzzle[i]['value'] = 0
                return False
        return False
