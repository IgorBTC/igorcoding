import random as rd

class BankAccount:
    def __init__(self, balance = 0, user = {}):
        self.balance = balance
        self.user = user
        
        
    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")
    def get_owner(self):
        self.owner = str(input("Введите нового владельца: "))
        
    def del_owner(self):
        self.owner = ""
        print("Владелец удалён!")
    
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
            

choice = int(input("Выберите действие: 1 - добавить владельца, 2 - удалить владельца, 3 - выход: "))