def sudoku_solved(sudoku):
    result = True
    sum_first_line = sum(sudoku[0])
    # check horizontal lines
    horizontal_cheker = [False for line in sudoku if sum(line) != sum_first_line]
    if horizontal_cheker:
        result = False
    # check vertical lines
    for i in range(len(sudoku)):
        sum_current_line = 0
        for j in range(len(sudoku)):
            sum_current_line += sudoku[j][i]
        if sum_current_line != sum_first_line:
            result = False
    # check 3X3 squareс
    for big_row in range(0, len(sudoku), 3):
        for coll in range(0, len(sudoku), 3):
            cuurent_sum = 0
            for row in range(big_row + 0,  big_row + 3):
                cuurent_sum += sum(sudoku[row][coll: coll + 3])
            if cuurent_sum != sum_first_line:
                result = False
    return result
# print(sudoku_solved([[4, 5, 2, 3, 8, 9, 7, 1, 6],
#                     [3, 8, 7, 4, 6, 1, 2, 9, 5],
#                     [6, 1, 9, 2, 5, 7, 3, 4, 8],
#                     [9, 3, 5, 1, 2, 6, 8, 7, 4],
#                     [7, 6, 4, 9, 3, 8, 5, 2, 1],
#                     [1, 2, 8, 5, 7, 4, 6, 3, 9],
#                     [5, 7, 1, 8, 9, 2, 4, 6, 3],
#                     [8, 9, 6, 7, 4, 3, 1, 5, 2],
#                     [2, 4, 3, 6, 1, 5, 9, 8, 7]]))
# print(sudoku_solved([
#             [1, 2, 3, 1, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
