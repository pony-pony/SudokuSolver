from functions import ( input_board, 
                        find_next_empty,
                        is_valid,
                        solve_sudoku,
                        format_answer )

if __name__ == '__main__':
    board = input_board()
    solve_sudoku(board)
    print(format_answer(board))
    