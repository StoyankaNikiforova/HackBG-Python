from cell import Cell


class Matrix:
    def __init__(self, width, height, list_living):
        self.width = width
        self.height = height
        self.fild = self.empty()
        self.list_living = list_living

    def empty(self):
        matrix = []
        for index1 in range(self.height):
            line = []
            for index2 in range(self.width):
                line.append(Cell._dead)
            matrix.append(line)
        return matrix

    def set_living(self):
        for live_cell in self.list_living:
            self.fild[live_cell[0]][live_cell[1]] = Cell._live

    def new_list_living(self):
        new_list = []
        for index1 in range(self.width):
            for index2 in range(self.height):
                cell = Cell(index1, index2)
                if cell.is_to_be_alive(self):
                    new_list.append([cell.x, cell.y])
        return new_list

    def print_matrix(self):
        result = []
        for list_sells in self.fild:
            item = " ".join(list_sells)
            result.append(item)
            print(item)
        return result
