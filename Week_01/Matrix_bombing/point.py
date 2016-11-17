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
