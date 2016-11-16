import os
import time

from matrix import Matrix


class Game:
    def get_inputs(self):
        n = int(input("Enter size of Matrix: "))
        self.width = n
        self.height = n
        count_living = int(input("Count of living: "))
        list_liv_sell = []
        for indx in range(count_living):
            input_line = input("Cell: {0}: ".format(indx))
            line = input_line.split(' ')
            numbers = []
            numbers.append(int(line[0]))
            numbers.append(int(line[1]))
            list_liv_sell.append(numbers)
        self.list_living = list_liv_sell

    def start(self):
        list_living = self.list_living
        # first_list = list_living
        # first_matrix = Matrix(self.width, self.height, first_list)
        while True:
            matrix = Matrix(self.width, self.height, list_living)
            matrix.set_living()
            # if matrix.list_living == first_matrix.list_living:
            #     self.stop()
            os.system('clear')
            matrix.print_matrix()
            time.sleep(0.2)
            list_living = matrix.new_list_living()

    def stop(self):
        print("Game over!")
        print(exit())
