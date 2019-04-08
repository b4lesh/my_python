def get_parity(x):
    if x % 2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'


num = int(input("Введите число: "))
print(get_parity(num))
