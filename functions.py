def input_board():
    board = []
    count = 1
    for _ in range(9):
        row = []
        print(f'----------------- {count} -----------------')
        for _ in range(9):
            number = input("Number(If it's empty, type nothing and press enter): ")
            if number == '':
                row.append(int(-1))
            else:
                row.append(int(number))
        board.append(row)
        count += 1
    return board

def format_answer(answer_board):
    for row in answer_board:
        print(row)
        print("\n")

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True 
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False