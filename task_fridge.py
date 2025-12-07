class my_fridge:
    def __init__(self, temperature=4):
        
        self.products = {'сыр':2, 'манго':0, 'пиво':3, 'минералка': 10}
        self.temperature = temperature
    
    def show_temperature(self):
        print(f"Температура холодильника: {self.temperature} {chr(176)}C")
    
    def change_temperature(self):
        self.temperature = int(input("Введите температуру: "))
        if self.temperature < 4 or self.temperature > 10:
            print("Ошибка! Попробуйте ещё раз: ")
            self.temperature = int(input("Введите температуру: "))
        

    def add_products(self):
        product = str(input("Введите продукт: "))
        quantity = int(input("Введите кол-во: "))
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
    
    def del_products(self):
        product = str(input("Введите продукт который хотите удалить: "))
        product = product.strip()
        if product in self.products:
            del self.products[product]
            print(f"Удален: {product}")
        else:
            print(f"Продукт {product} не найден")

    def show_products(self):
        print(f"Содержимое холодильника: {self.products}")


        
fridge = my_fridge()

while True:
    choice = int(input("Выберите действие (1-посмотреть холодильник, 2-добавить в холодильник, 3-удалить продукт из холодильника, 4-выход): "))
    if choice == 1:
        fridge.show_products()

    if choice == 2:
        fridge.add_products()

    if choice == 3:
        fridge.del_products()

    if choice == 4:
        break
    
while True:
    temp = int(input("Выберите действие (1 - посмотреть температуру, 2 - изменить температуру, 3 - выход): "))
    if temp == 1:
        fridge.show_temperature()
    if temp == 2:
        fridge.change_temperature()
    if temp == 3:
        break