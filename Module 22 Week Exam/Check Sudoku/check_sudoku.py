'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_row(sudoku):
    '''function for checking the rules for row'''
    for row in sudoku:
        if sum([int(ele) for ele in row]) != 45:#Sum of numbers in a row should be equal to 45
            return False
    return True
def check_column(sudoku):
    '''function for checking the rules for column'''
    for row, list_ in enumerate(sudoku):
        sum_res = 0
        for column in range(len(list_)):
            sum_res += int(sudoku[column][row])
        if sum_res != 45:
            return False
    return True
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if check_row(sudoku) and check_column(sudoku):
        return True
    return False
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for row in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
