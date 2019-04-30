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
    try:
        result = x / y
    except ZeroDivisionError:
        result = "Ошибка деления на ноль"    


print('Результат: ', result)
