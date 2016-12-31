class Reservation:
    def __init__(self, user_id, projection_id, row, col):
        self.user_id = user_id
        self.projection_id = projection_id
        self.row = row
        self.col = col

    @staticmethod
    def empty_hall():
        hall = [['.' for x in range(11)] for y in range(11)]
        hall[0][0] = ' '
        row = 0
        col = 1
        for i in range(10):
            hall[row][col] = str(col)
            col += 1

        row = 1
        col = 0
        for i in range(10):
            hall[row][col] = str(row)
            row += 1

        return hall
