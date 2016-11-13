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
