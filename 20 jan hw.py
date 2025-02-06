class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.__account_number = account_number #private member
        self.__balance = initial_balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: ${amount:.2f}. New balance: ${self.__balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def add_interest(self, rate):
        if rate > 0:
            interest = self.__balance * (rate / 100)
            self.__balance += interest
            print(f"Interest added: ${interest:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Interest rate must be positive.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


if __name__ == "__main__":
    account = BankAccount("123456789", 1000.0)
    account.deposit(500)
    account.withdraw(200)
    account.add_interest(5)  
    print(f"Final balance: ${account.get_balance():.2f}")
