class  BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError("balance must be positive number")
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = []
        self.history.append("Account was created")

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            (self.history).append("Deposited {0}$".format(amount))
        else:
            raise ValueError("Amount must be positive number")

    def balanse(self):
        (self.history).append("Balance check -> {0}$".format(self.balance))
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            (self.history).append("{0}$ was withdrawed".format(amount))
            return True
        else:
            (self.history).append("Withdraw for {0}$ failed".format(amount))
            return False

    def __str__(self):
        return str.format("Bank account for {0} with balance of {1}{2}", self.name, self.balance, self.currency)

    def __int__(self):
        (self.history).append("__int__check -> {0}$".format(self.balance))
        return self.balance

    def historyes(self):
        return self.history


def main():
    account = BankAccount("Rado", 0, "$")
    print(account)
    account.deposit(1000)
    print(account.balanse())
    print(str(account))
    print(int(account))
    print(account.historyes())
    print(account.withdraw(500))
    print(account.balanse())
    print(account.historyes())
    print(account.withdraw(1000))
    print(account.balanse())
    print(account.historyes())

if __name__ == '__main__':
    main()
