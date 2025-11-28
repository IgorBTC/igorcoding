import random
# Начальные условия

hare = 0
wolf = 0

# Параметры модели
capacity_environment = 5000  # Максимальная популяция зайцев
birthday_hare = 0.3  # В месяц
death_hare = 0.1   # В месяц

birthday_wolf = 0.15
death_wolf = 0.2
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] #месяц
year = 0

# Коэффициенты взаимодействия
coef_eating = 0.001  # Вероятность встречи и поедания
efficiency_conversion = 0.1  # Насколько эффективно волки превращают зайцев в потомство

# Встречи и поедание
meeting = coef_eating * hare * wolf
eating_hare = min(meeting, hare * 0.3)  # Не более 30% зайцев

# Рост популяции зайцев (логистическое уравнение)
growth_hare = hare * birthday_hare * (1 - hare/capacity_environment)
death_hare_natural = hare * death_hare

# Рост популяции волков
growth_wolf = wolf * birthday_wolf + eating_hare * efficiency_conversion
death_wolf_natural = wolf * death_wolf

# Обновление популяций
hare = hare + growth_hare - death_hare_natural - eating_hare
wolf = wolf + growth_wolf - death_wolf_natural




for x in range (0, 10):
    # Эпизодические события (раз в 2-3 года)
    if year % random.randint(2, 3) == 0:
        events = random.choice(['эпидемия', 'пожар', 'обильный_корм'])
        if events == 'эпидемия':
            hare *= 0.7
            wolf *= 0.8
        elif events == 'пожар':
            hare *= 0.6
            wolf *= 0.5
        elif events == 'обильный_корм':
            hare *= 1.4
    
    hare_counter = []
    wolf_counter = []
    print(f"=== Год {year+1} ===")
    print(f"Текущие популяции зайцев и волков: {hare}, {wolf}")
    year += 1
    
    
    for i in range(len(month)):
        hare = random.randint(1000,5000)
        wolf = random.randint(10,100)
        # Зима: сложные условия
        if month[i] in ['December', 'January', 'February']:  # Декабрь, Январь, Февраль
            birthday_hare *= 0.5
            death_hare *= 1.5
            coef_eating *= 1.2  # Волкам легче найти зайцев
            
        # Весна: благоприятные условия  
        elif month[i] in ['March', 'April', 'May']:
            birthday_hare *= 1.3
            death_hare *= 0.8
        
        hare_counter.append(hare)
        wolf_counter.append(wolf)
    print(f"Максимум: Зайцы = {max(hare_counter)}, Волки= {max(wolf_counter)}")
    print(f"Минимум: Зайцы = {min(hare_counter)}, Волки= {min(wolf_counter)}")
    increase_hare = round(((hare_counter[11]/hare_counter[0]) * 100),2)
    increase_wolf = round(((wolf_counter[11]/wolf_counter[0]) * 100),2)
    
    print(f"Зайцы: {hare_counter[11]}, ({increase_hare}%)  | Волки: {wolf_counter[11]}, ({increase_wolf}%)\n")
    
    




