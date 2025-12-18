import random as rd
import json as js

class BankAccount():
    def __init__(self, balance = 0, amount = 0, operation = "", activity = 1, transaction_app = None):
        self.balance = balance
        self.user = {}
        self.transaction = {}
        self.amount = amount
        self.operation = operation
        self.activity = activity
        self.transaction_app = transaction_app
        
    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")
    
    def add_owner(self, owner = "", account_number = 9999):
        owner = str(input("Введите владельца: "))
        account_number = rd.randint(1000,9999)
        self.activity = int(input("Выберите действие: 1-сменить владельца, 2-удалить владельца, другое-выход)"))
        if self.activity == 1:
            if owner in self.user:
                self.owner = str(input("Введите нового владельца: "))
                self.user[owner] = account_number
                print("Владелец успешно сменился!")
        elif self.activity == 2:  
            if owner in self.user:
                del self.user[owner]
                print(f"Удален: {account_number}")
            else:
                print(f"Владелец {account_number} не найден")
        else:
            print("Вы успешно вышли")
    
    def transactions(self):
        print("Список всех операций: пополнение, снятие, история операций")
    
    def deposit(self):
        while True:
            try:
                self.amount = float(input("Введите сумму для пополнения: "))
                break
            except ValueError:
                print("Ошибка! Введите число!")
        self.balance += self.amount
        if "Пополнение" not in self.transaction:
            self.transaction["Пополнение"] = [] 
        self.transaction["Пополнение"].append(self.amount)
        return self.balance, self.transaction
    
    def withdraw(self):
        while True:
            try:
                self.amount = float(input("Введите сумму для снятия: "))
                break
            except ValueError:
                print("Ошибка! Введите число!")
        self.balance -= self.amount
        if "Снятие" not in self.transaction:
            self.transaction["Снятие"] = [] 
        self.transaction["Снятие"].append(self.amount)
        return self.balance, self.transaction
    
    def get_transaction_history(self):
        print(self.transaction)
    
    def validate_amount(self):
        if self.balance < 0:
            print("Сумма отрицательная")
        else: 
            print("Сумма положительная")
    
    
    def transaction_log(self):
        self.transaction = js.dumps(self.transaction, ensure_ascii=False)
        self.transaction_app = open('transaction.txt', 'a')
        self.transaction_app.write(self.transaction)
        self.transaction_app.close()
        return self.transaction_app

class SavingAccount(BankAccount):
    def __init__(self, interest_rate = 1.13):
        super().__init__()
        self.interest_rate = interest_rate
        
    def add_interest(self):
        self.balance *= self.interest_rate
        return self.balance
    def withdraw(self):
        super().withdraw()
        while self.amount > 500000:
            print("Ошибка! Попробуйте другую сумму")
            self.amount = float(input("Введите сумму для снятия: "))
            while True:
                try:
                    self.amount = float(input("Введите сумму для снятия ещё раз: "))
                    break
                except ValueError:
                    print("Ошибка! Введите число!")
        self.balance -= self.amount
        if "Снятие" not in self.transaction:
            self.transaction["Снятие"] = [] 
        self.transaction["Снятие"].append(self.amount)
        return self.balance, self.transaction
    def __mul__(self, other = 1.1):
        self.other = other
        self.interest_rate *= self.other
        return self.interest_rate

class CreditAccout(BankAccount):
    def __init__(self, credit_limit = 300000, debt = 0):
        super().__init__()
        self.credit_limit = credit_limit
        self.debt = debt
    def withdraw(self):
        super().withdraw()
        while (self.balance - self.amount + self.credit_limit) < 0:
            print("Ошибка! Попробуйте другую сумму")
            self.amount = float(input("Введите сумму для снятия: "))
            while True:
                try:
                    self.amount = float(input("Введите сумму для снятия: "))
                    break
                except ValueError:
                    print("Ошибка! Введите число!")
            self.debt = self.balance - self.amount + self.credit_limit
        if "Снятие" not in self.transaction:
            self.transaction["Снятие"] = [] 
        self.transaction["Снятие"].append(self.amount)
        return self.balance, self.transaction
    
    def pay_debt(self):
        print(f"Погашение задолжности: {self.debt} ")
        self.balance -= self.debt
        return self.balance
    
    def available_balance(self):
        print(f"Доступный баланс: {self.balance + self.credit_limit}")
    
class StudentAccount(BankAccount):
    def __init__(self, university = "",  adult = 0, grant = 0):
        super().__init__()
        self.university = university
        self.adult = adult
        self.grant = grant
    
    def deposit(self):
        super().deposit()
        self.adult = int(input("Вы являетесь родителем? 1 - да, другое - нет: "))
        self.amount = float(input("Введите сумму для пополнения: "))
        while True:
            try:
                self.amount = float(input("Введите сумму для пополнения: "))
                break
            except ValueError:
                print("Ошибка! Введите число!")
        if self.adult == 1:
            self.balance += self.amount * 1.05
        else:
            self.balance += self.amount
        if "Пополнение" not in self.transaction:
            self.transaction["Пополнение"] = [] 
        self.transaction["Пополнение"].append(self.amount)
        return self.balance, self.transaction
    
    def withdraw(self):
        super().withdraw()
        while self.amount > 100000:
            print("Ошибка! Сумма не должна превышать 100000")
            self.amount = float(input("Введите сумму для снятия: "))
            while True:
                try:
                    self.amount = float(input("Введите сумму для снятия: "))
                    break
                except ValueError:
                    print("Ошибка! Введите число!")
        self.balance -= self.amount
        if "Снятие" not in self.transaction:
            self.transaction["Снятие"] = [] 
        self.transaction["Снятие"].append(self.amount)
        return self.balance, self.transaction
    

    def apply_for_grant(self):
        self.grant = int(input("Подаёте заявку на стипендию(1 - да, 2 - нет): "))
        return self.grant
    
bank_account = BankAccount()
saving_account = SavingAccount()
credit_account = CreditAccout()
student_account = StudentAccount()

while True:
    choice_BankAccount = int(input("Выберите действие (1-посмотреть баланс, 2-добавить/удалить владельца, 3-список всех операций, \n 4-депозит, 5-вывод, 6-список транзакций, 7-проверка баланса, 8 - записать все транзакции в файл \n 9 -переход к следующему раздела: "))
    if choice_BankAccount == 1:
        bank_account.show_balance()

    if choice_BankAccount == 2:
        bank_account.add_owner()
        
    if choice_BankAccount == 3:
        bank_account.transactions()
    
    if choice_BankAccount == 4:
        bank_account.deposit()
    
    if choice_BankAccount == 5:
        bank_account.withdraw()
    
    if choice_BankAccount == 6:
        bank_account.get_transaction_history()

    if choice_BankAccount == 7:
        bank_account.validate_amount()
    
    if choice_BankAccount == 8:
        bank_account.transaction_log()
        
    if choice_BankAccount == 9:
        while True:
            choice_SavingAccount = int(input("Выберите действие (1-начислить проценты, 2-вывод, 3-увеличить % годовых, \n 4-перейти к следующему разделу, 5-вернутся к предыдущему разделу: "))
            
            if choice_SavingAccount == 1:
                saving_account.add_interest()
                continue
            if choice_SavingAccount == 2:
                saving_account.withdraw()
                continue
            if choice_SavingAccount == 3:
                saving_account.__mul__()
                continue
            if choice_SavingAccount == 5:
                break
              
            if choice_SavingAccount == 4:
                while True:
                    choice_CreditAccount = int(input("Выберите действие (1-вывод, 2- выплата задолжности, 3-доступный баланс, \n 4-перейти к следующему разделу, 5-вернутся к предыдущему разделу: "))

                    if choice_CreditAccount == 1:
                        credit_account.withdraw()
                
                    if choice_CreditAccount == 2:
                        credit_account.pay_debt()
                    
                    if choice_CreditAccount == 3:
                        credit_account.available_balance()
                        
                    if choice_CreditAccount == 5:
                        break
                    
                    if choice_CreditAccount == 4:
                        while True:
                            choice_StudentAccount = int(input("Выберите действие (1-депозит, 2- вывод, 3- подать заявку на стипендию, \n 4- выход, 5-вернутся к предыдущему разделу "))
                            
                            if choice_StudentAccount == 1:
                                student_account.deposit()
                    
                            if choice_StudentAccount == 2:
                                student_account.withdraw()
                            
                            if choice_StudentAccount == 3:
                                student_account.apply_for_grant()
                                
                            if choice_StudentAccount == 5:
                                break
                            
                            if choice_StudentAccount == 4:
                                choice_BankAccount = 11
            break