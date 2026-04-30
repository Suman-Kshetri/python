# Encapsulation = binding data (variables) + methods together
# Restricts direct access to data
# Achieved using:
# Private variables (__var)
# Getter & Setter methods

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# Usage
acc = BankAccount(1000)

print(acc.get_balance())   # Access via method
acc.deposit(500)
print(acc.get_balance())

# Direct access (not recommended)
# print(acc.__balance) ❌ Error