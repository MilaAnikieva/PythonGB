# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = equation.split()
k = int(equation[2][:-1])
b = float(equation[4])
y = k * x + b
print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date = input('Введите дату рождения ').split('.')
month_day = {'1': 31, '2': 30, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

if 1 <= int(date[2]) <= 9999 and len(date[2]) == 4:
    if 1 <= int(date[1]) <= 12:
        if 1 <= int(date[0]) <= month_day.get(str(int(date[1]))):
            print('Дата введена корректно.')
        else:
            print('День введен некоррекнто!')
    else:
        print('Месяц введен некорректно!')
else:
    print('Год введен некорректно!')

print('.'.join(date))