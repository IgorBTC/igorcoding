from datetime import datetime as dt
from datetime import timedelta as td

#переменные для функций
final_sum_with_op = 0
final_sum = 0
percent_stake = 0


date1 = str(input("Введите дату начала вклада (например 20.03.2003): "))
date1 = dt.strptime(date1, '%d.%m.%Y')
date2 = str(input("Введите дату окончания вклада (например 20.03.2010): "))
date2 = dt.strptime(date2, '%d.%m.%Y')




sum_contribution = float(input("Введите сумму вклада: "))
new_client = str(input("Являетесь ли вы новым клиентом? (True - да, любое другое - нет): "))
banker = str(input("Являетесь ли вы сотрудником? (True - да, любое другое - нет): "))
retiree = str(input("Являетесь ли вы пенсионером? (True - да, любое другое - нет): "))
optional_param = str(input("Сложный процент(True - да, любое другое - нет): "))
metod_calculation = str(input("Выберите метод расчета: точные проценты или обыкновенные проценты: "))
capitalisation = str(input("Выберите схему капитализации: ежедневная, ежемесячная, ежеквартальная, ежегодная: "))
days = int(input("Введите кол-во дней вклада: "))

year = 0
year = days/365

def solution_with_OP(sum_contribution, percent_stake, year, optional_param): 
    return sum_contribution * (1 + percent_stake/n)**(year*n)

def solution(sum_contribution, percent_stake, year):
    return sum_contribution * percent_stake * year

if capitalisation == "ежедневная":
    n = 365
if capitalisation == "ежемесячная":
    n = 12
if capitalisation == "ежеквартальная":
    n = 4
if capitalisation == "ежегодная":
    n = 1
if capitalisation == "ежедневная" and metod_calculation == "Обыкновенные":
    n = 360


if new_client == "True":
    percent_stake += 0.03
if banker == "True" or retiree == "True": 
    percent_stake += 0.05

if sum_contribution <= 100000:
    percent_stake += 0.05
elif sum_contribution >= 100001 and sum_contribution <= 500000:
    percent_stake += 0.06
else:
    percent_stake += 0.07

'''if metod_calculation == "Точные":
    while date1 <= date2:
        if date1.month!=previous1:
            percent_stake += 0.015
            previous1 = date1.month
        if date1.month!=previous2:
            percent_stake += 0.015
            previous2 = date1.month
        date1+= td.timedelta(days=1)
    
if metod_calculation == "Обыкновенные":
    for i in range(0, term+1):
'''
        

if optional_param == "True":
    final_sum_with_op = solution_with_OP(sum_contribution, percent_stake, year, optional_param)
else:
    final_sum = solution(sum_contribution, percent_stake, year)



if optional_param == "True":
    print(f"Итоговая сумма со сложным процентом: {final_sum_with_op}")
else:
    print(f"Итоговая сумма без сложного процента: {final_sum + sum_contribution}")
