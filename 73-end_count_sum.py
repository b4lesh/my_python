
summ = 0
while True:
    num = input('Введите число или Стоп для выхода: ')
    if num == 'стоп':
        print('Выход из программы! До встречи')
        break
    else:
        try:
            summ = int(num) + summ
        except:
            print('Ошибка ввода.')
            continue
print('Cумма: ', summ)
