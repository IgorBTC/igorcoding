class Heroes():
    def __init__(self, attack = 20, hp = 300, post_of_flame = 40):
        self.attack = attack
        self.hp = hp
        self.post_of_flame = post_of_flame
    
class Goblin(Heroes):
    def spawn_goblin(self):
        print(f"Гоблин с {self.hp}HP появился в мире!")
    def attack_goblin(self):
        global hp_hero
        hp_hero -= self.attack
        print(f"Гоблин атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {hp_hero} здоровья.")
        return hp_hero

class Skeleton(Heroes):
    def spawn_skeleton(self):
        print(f"Скелет с {self.hp}HP появился в мире!")
    def attack_skeleton(self):
        global hp_hero
        hp_hero -= self.attack
        print(f"Скелет атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {hp_hero} здоровья.")
        return hp_hero
    
class Dragon(Heroes):
    def spawn_dragon(self):
        print(f"Игнис с {self.hp}HP появился в мире!")
    def attack_dragon_common(self):
        global hp_hero
        hp_hero -= self.attack
        print(f"Игнис атакует Рыцарь и наносит {self.attack} урона! У Рыцарь осталось {hp_hero} здоровья.")
        return hp_hero
    def attack_dragon_breath(self):
        global hp_hero
        hp_hero -= self.attack
        print(f"Вдобавок 'Игнис' опаляет Рыцарь своим дыханием, нанося ещё {self.attack} урона! У Рыцарь осталось {hp_hero} здоровья.")
        return hp_hero
    def attack_dragon_flame(self):
        global hp_hero
        hp_hero -= self.post_of_flame
        print(f"Игнис выдыхает столб пламени на Рыцарь, нанося {self.post_of_flame} урона! У Рыцарь осталось {hp_hero} здоровья.")
        return hp_hero

hp_hero = 250
class_heroes = Heroes()
class_goblin = Goblin()
class_skeleton = Skeleton()
class_dragon = Dragon()
    
while True:
    choice = int(input("Выберите какой персонаж будет атаковать 1-гоблин, 2-скелет, 3-дракон, 4-выход: "))
    if choice == 1:
        class_goblin.spawn_goblin()
        class_goblin.attack_goblin()
    if choice == 2:
        class_skeleton.spawn_skeleton()
        class_skeleton.attack_skeleton()
    if choice == 3:
        class_dragon.spawn_dragon()
        class_dragon.attack_dragon_common()
        class_dragon.attack_dragon_breath()
        class_dragon.attack_dragon_flame()
    if choice == 4:
        break
    continue