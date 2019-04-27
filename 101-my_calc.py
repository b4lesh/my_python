x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = input('Введите действие: ')
if z == '+':
    result = x + y
elif z == '-':
    result = x - y
elif z == '*':
    result = x * y
elif z == '/':
    resulr = x / y
try:
    y == '0'
except ZeroDivisionError:
    print("Ошибка деления на нуль")    


print('Результат: ', result)
