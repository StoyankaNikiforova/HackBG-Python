import collections


class Point:
    AREA = 1

    def __init__(self, x, y, weight=0):
        self.x = x
        self.y = y
        self.weight = weight

    def __sub__(self, other):
        return self.weight - other.weight

    def __add__(self, other):
        return self.weight + other.weight

    def __str__(self):
        return "({0}, {1})".format(str(self.x), str(self.y))

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        if self.x > other.x:
            return self
        if self.x == other.x and self.y > other.y:
            return self

    def get_null_neighb(self):
        neighb = []
        for i in range(-self.AREA, self.AREA+1):
            for j in range(-self.AREA, self.AREA+1):
                if not (i == 0 and j == 0):
                    neighb.append(Point(i, j))
        return neighb

    def neighbours(self, m):
        neighb = []
        null_neighbours = self.get_null_neighb()
        for value in null_neighbours:
            x_pos = self.x + value.x
            y_pos = self.y + value.y
            if (x_pos >= 0 and x_pos < m.cols) and (y_pos >= 0 and y_pos < m.rows):
                n = m.get_point_by_poss(x_pos, y_pos)
                neighb.append(n)
        return neighb


class Matrix:
    def __init__(self, rows, cols, m):
        self.rows = int(rows)
        self.cols = int(cols)
        self.m = m
        self.full = self.full_matrix()

    def full_matrix(self):
        matrix = []
        for i in range(self.rows):
            input_row = self.m[i]
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


def sort_points(dict_points):
    sort_keys = sorted(dict_points.keys())
    result = "{"
    for value in sort_keys:
        result += "{}: {}, ".format(value, dict_points[value])
    result = result.strip(', ')
    result += "}"
    # result = {}
    # for value in sort_keys:
    #     result[value] = dict_points[value]

    return result


def matrix_bombing_plan(m):
    rows = len(m)
    cols = len(m[0])
    m = Matrix(rows, cols, m)
    start_weight = m.sum_of_weight()
    max_damage = 0
    matrix_damage = {}
    for point in m.full:
        damage = start_weight - damage_of(point, m)
        matrix_damage[point] = damage

    return sort_points(matrix_damage)


def damage_of(p, m):
    d = 0
    negh = p.neighbours(m)
    for n in negh:
        diff = n - p
        if diff > 0:
            d += p.weight
        else:
            d += n.weight
    return d

print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
