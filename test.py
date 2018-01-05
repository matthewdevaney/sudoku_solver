import logging
from sudoku import Sudoku
import time

logging.basicConfig(filename='sudoku_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# create a list of puzzles to test
puzzle_test_string = ['790000300000006900800030076000005002005418700400700000610090008002300000009000054',
                      '005090001000002073760008200012009004000203000300100960001900058970500000500030700',
                      '000080050083060002670000001500820100006000800008041005800000039100090260030050000',
                      '007400090013000600000000043100000270900501004064000001520000000006000980080002700',
                      '200010050305042000018009002032100800001020300009003260100700980000260507060080003']

# solve each puzzle in the list
for puzzle in puzzle_test_string:

    # start the timer
    start_time = time.time()

    # create a new instance of the sudoku object
    s = Sudoku(puzzle)

    # display the unsolved puzzle
    logging.info('\nSudoku Puzzle:\n{}'.format(s))

    # display the solution or inform user no solution was found
    if s.solve():
        logging.info('Sudoku was solved in {}s :)\n{}'.format(round(time.time() - start_time, 2), s))
    else:
        logging.info('Sudoku was not solved :(\n{}'.format(round(time.time() - start_time, 2), s))
