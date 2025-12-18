count_attack_heroes = int(input("Введите кол-во аттак: "))

class Heroes():
    def __init__(self, hp_hero = 250, attack = 20, hp = 300, post_of_flame = 40):
        self.hp_hero = hp_hero
        self.attack = attack
        self.hp = hp
        self.post_of_flame = post_of_flame
    
class Goblin(Heroes):
    def __init__(self):
        super().__init__()
    def spawn_goblin(self):
        print(f"Гоблин с {self.hp}HP появился в мире!")
    def attack_goblin(self):
        self.hp_hero -= self.attack
        print(f"Гоблин атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {self.hp_hero} здоровья.")
        return self.hp_hero

class Skeleton(Heroes):
    def __init__(self):
        super().__init__()
    def spawn_skeleton(self):
        print(f"Скелет с {self.hp}HP появился в мире!")
    def attack_skeleton(self):
        self.hp_hero -= self.attack
        print(f"Скелет атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {self.hp_hero} здоровья.")
        return self.hp_hero
    
class Drakon(Heroes):
    def __init__(self):
        super().__init__()
    def spawn_drakon(self):
        print(f"Игнис с {self.hp}HP появился в мире!")
    def attack_drakon_common(self):
        self.hp_hero -= self.attack
        print(f"Игнис атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {self.hp_hero} здоровья.")
        return self.hp_hero
    def attack_drakon_breath(self):
        self.hp_hero -= self.attack
        print(f"Вдобавок 'Игнис' опаляет Рыцарь своим дыханием, нанося ещё {self.attack} урона! У Рыцарь осталось {self.hp_hero} здоровья.")
        return self.hp_hero
    def attack_drakon_flame(self):
        self.hp_hero -= self.post_of_flame
        print(f"Игнис выдыхает столб пламени на Рыцарь, нанося {self.post_of_flame} урона! У Рыцарь осталось {self.hp_hero} здоровья.")
        return self.hp_hero