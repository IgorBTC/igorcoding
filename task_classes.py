import random as rd

class BankAccount:
    def __init__(self, balance = 0, amount = 0, operation):
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
        self.balance += self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = amount
        return self.balance, self.transaction
    
    def withdraw(self):
        self.balance -= self.amount
        if self.operation in self.transaction:
            self.transaction[self.operation] = amount
        return self.balance, self.transaction
    
    def get_transaction_history(self):
        print(self.transaction)
        
choice = int(input("Выберите действие: 1 - добавить владельца, 2 - удалить владельца, 3 - выход: "))
amount = float(input("Введите сумму для пополнения/снятия: "))
