def max_num(x, y):
    if x >= y:
        return x
    else:
        return y


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

print(max_num(x, y))
