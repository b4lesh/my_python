
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
def max_num(num1, num2):
    if num1 < num2:
        return print("Большее число: ", num2)
    if num1 > num2:
        return print("Большее число: ", num1)
    elif num1 == num2:
        return print("Большее число: ", num1)
    
