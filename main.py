# validations

def is_valid(board, row, col, num):
    '''
    :param board: The game board
    :param row: The row being tested
    :param col: The column being tested
    :param num: The number we want to place
    :return: if num be placed in the position received as a parameter or not
    '''

    # check if num is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False
    # check if num is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    # check if num is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# solve the board

def solve_sudoku(board):
    '''
    The function passes the game board received as a parameter and tries to complete it
    :param board: The game board
    :return: if all cells are filled and valid
    '''
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # An empty cell is represented by 0
                # Try placing digits 1 to 9 in the empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place num if it's valid
                        if solve_sudoku(board):  # Recursively solve for next empty cell
                            return True
                        board[row][col] = 0  # Backtrack if num leads to no solution
                return False  # Return False if no number fits in this cell
    return True  # Return True if all cells are filled and valid


# print board
def print_sudoku_board(board):
    '''
    print the game board
    :param board: The game board
    '''
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()


# Let's play
# example board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if solve_sudoku(sudoku_board):
    print_sudoku_board(sudoku_board)
else:
    print('No solution to this board game...')


