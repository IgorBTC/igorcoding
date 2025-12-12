import random as rd

class BankAccount():
    def __init__(self, balance = 0, amount = 0, operation = ""):
        self.balance = balance
        self.user = {}
        self.transaction = {}
        self.amount = amount
        self.operation = operation
        
        
    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")
    
    
    def add_owner(self, owner, account_number):
        owner = str(input("Введите владельца: "))
        account_number = rd.random(1000,9999)
        if choice == 1: 
            if owner in self.user:
                self.owner = str(input("Введите нового владельца: "))
                self.user[owner] = account_number
                print("Владелец успешно сменился!")
    
    def del_owner(self, owner, account_number):
        if owner in self.user:
            del self.user[owner]
            print(f"Удален: {account_number}")
        else:
            print(f"Владелец {account_number} не найден")
    
    def transactions(self):
        print("Список всех операций: пополнение, снятие, история операций")
    
    def show_balance(self, balance):
        print(f"Текущий баланс: {balance}")
    
    def deposit(self):
        self.amount = float(input("Введите сумму для пополнения: "))
        self.balance += self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    
    def withdraw(self):
        self.amount = float(input("Введите сумму для снятия: "))
        self.balance -= self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    
    def get_transaction_history(self):
        print(self.transaction)
    
    def validate_amount(self):
        if self.balance < 0:
            print("Сумма отрицательная")
        else: 
            print("Сумма положительная")
    
    
        
choice = int(input("Выберите действие: 1 - добавить владельца, 2 - удалить владельца, 3 - выход: "))


class SavingAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__(self.balance, self.amount, self.operation)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        self.balance *= self.interest_rate
        return self.balance
    def withdraw(self):
        super().withdraw(self)
        while self.amount > 500000:
            print("Ошибка! Попробуйте другую сумму")
            self.amount = float(input("Введите сумму для снятия: "))
        self.balance -= self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    def __mul__(self, other = 1.1):
        self.other = other
        self.interest_rate *= self.other
        return self.interest_rate

class CreditAccout(BankAccount):
    def __init__(self, credit_limit = 300000, debt = 0):
        super().__init__(self.balance, self.amount, self.operation)
        self.credit_limit = credit_limit
        self.debt = debt
    def withdraw(self):
        super().withdraw(self)
        while (self.balance - self.amount + self.credit_limit) < 0:
            print("Ошибка! Попробуйте другую сумму")
            self.amount = float(input("Введите сумму для снятия: "))
            self.debt = self.balance - self.amount + self.credit_limit
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    
    def pay_debt(self):
        print(f"Погашение задолжности: {self.debt} ")
        self.balance -= self.debt
        return self.balance
    
    def available_balance(self):
        print(f"Доступный баланс: {self.balance + self.credit_limit}")
    
class StudentAccount(BankAccount):
    def __init__(self, university = "", adult, grant):
        super().__init__(self.balance, self.amount, self.operation)
        self.university = university
        self.adult = adult
        self.grant = grant
    
    def deposit(self):
        super().deposit(self)
        self.adult = int(input("Вы являетесь родителем? 1 - да, другое - нет: "))
        self.amount = float(input("Введите сумму для пополнения: "))
        if self.adult == 1:
            self.balance += self.amount * 1.05
        else:
            self.balance += self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    
    def withdraw(self):
        super().withdraw(self)
        while self.amount > 100000:
            print("Ошибка! Сумма не должна превышать 100000")
            self.amount = float(input("Введите сумму для снятия: "))
        self.balance -= self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = self.amount
        return self.balance, self.transaction
    

    def apply_for_grant(self):
        self.grant = int(input("Подаёте заявку на стипендию(1 - да, 2 - нет): "))
        return self.grant
    
