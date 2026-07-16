class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.__balance += amount
            print(amount, "Deposited")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print(amount, "Withdrawn")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount("Mukul", 5000)

account.deposit(1000)

account.withdraw(2000)

account.show_balance()

print("Owner:", account.owner)