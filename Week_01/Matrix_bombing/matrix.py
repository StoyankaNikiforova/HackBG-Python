from point import Point


class Matrix:
    def __init__(self, rows, cols):
        self.rows = int(rows)
        self.cols = int(cols)
        self.full = self.full_matrix()

    def full_matrix(self):
        matrix = []
        for i in range(self.rows):
            input_row = input("Enter matrix row: ").split(' ')
            for j in range(self.cols):
                point = Point(i, j, int(input_row[j]))
                matrix.append(point)
        return matrix

    def get_point_by_poss(self, x, y):
        for value in self.full:
            if value.x == x and value.y == y:
                return value

    def sum_of_weight(self):
        s = 0
        for point in self.full:
            s += point.weight
        return s
