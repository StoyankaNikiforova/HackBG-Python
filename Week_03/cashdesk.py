import math
import time
import collections
import re


class Bill:
    def __init__(self, amount):
        self.amount = int(amount)
        if type(amount) != int:
            raise TypeError('Amount must be number!')
        if amount < 0:
            raise ValueError('Amount must be positive number!')

    def __str__(self):
        return "A {0}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return abs((self.amount**235*int(time.ctime()[23]))//389)


class BatchBill:
    def __init__(self, bills):
        self.bills = [Bill(int(value)) for value in bills]

    def __len__(self):
        count = 0
        for val in bills:
            count += 1
        return count

    def total(self):
        total = 0
        for val in self.bills:
            total += int(val)
        return total

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.cash = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            bill = money
            if bill in self.cash:
                self.cash[bill] += 1
            else:
                self.cash[bill] = 1
        if isinstance(money, BatchBill):
            for bill in money:
                if bill in self.cash:
                    self.cash[bill] += 1
                else:
                    self.cash[bill] = 1

    def sort_cash(self):
        temp_cash = {}
        cash = []
        for bill in self.cash:
            key_temp = int(re.findall('\d+', str(bill))[0])
            temp_cash[key_temp] = self.cash[bill]
        list_keys = sorted(temp_cash.keys())
        for value in list_keys:
            cash.append([value, temp_cash[value]])
        return cash

    def total(self):
        total = 0
        for value in self.cash:
            total += int(self.cash[value]) * int(value)
        return total

    def inspect(self):
        result = "We have a total of {0}$ in the desk".format(self.total())
        result += "\nWe have the following count of bills, sorted in ascending order:"
        for bill in self.sort_cash():
            count = bill[1]
            result += ("\n{0}$ bills - {1}".format(bill[0], count))
        return result
