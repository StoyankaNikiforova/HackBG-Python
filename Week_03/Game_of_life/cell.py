class Cell:
    _live = '■'
    _dead = '□'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _get_neighbor(self, neigh):
        list_neighs = [[-1, -1], [-1, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, 1]]
        coorX = self.x + list_neighs[neigh][0]
        coorY = self.y + list_neighs[neigh][1]
        return [coorX, coorY]

    def _is_in_matrix(self, matrix):
        if self.x < 0 or self.x >= matrix.width:
            return False
        if self.y < 0 or self.y >= matrix.height:
            return False
        return True

    def _is_alive(self, matrix):
        if matrix.fild[self.x][self.y] == self._live:
            return True
        else:
            return False

    def is_to_be_alive(self, matrix):
        count_live_neighs = 0
        for index in range(8):
            neight_coord = self._get_neighbor(index)
            neigh = Cell(neight_coord[0], neight_coord[1])
            if neigh._is_in_matrix(matrix) and neigh._is_alive(matrix):
                    count_live_neighs += 1
        if self._is_alive(matrix):
            if count_live_neighs == 2 or count_live_neighs == 3:
                return True
            else:
                return False
        else:
            if count_live_neighs == 3:
                return True
            else:
                return False
