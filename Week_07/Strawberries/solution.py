from copy import deepcopy


def strawberries(rows, cols, days, deads):
    if rows < 0 or cols < 0:
        raise ValueError

    matrix = []

    for i in range(rows):
        matrix.append([1 for x in range(cols)])
    if not deads:
        sum_of_weight = 0
        for value in matrix:
            sum_of_weight += sum(value)
        return sum_of_weight

    dead_1 = deads[0]
    dead_2 = deads[1]
    matrix[dead_1[0]][dead_1[1]] = 0
    matrix[dead_2[0]][dead_2[1]] = 0
    for x in range(days):
        matrix1 = deepcopy(matrix)
        for i in range(rows):
            for j in range(cols):
                if matrix1[i][j] == 0:
                    if i - 1 >= 0:
                        matrix[i-1][j] = 0
                        # deads.append()
                        if i + 1 < rows:
                            matrix[i+1][j] = 0
                            if j - 1 >= 0:
                                matrix[i][j-1] = 0
                                if j+1 < cols:
                                    matrix[i][j+1] = 0
    sum_of_weight = 0
    for value in matrix:
        sum_of_weight += sum(value)
    return sum_of_weight



def main():
    print(strawberries(8, 10, 2, [(4, 8), (2, 7)]))


if __name__ == '__main__':
    main()
