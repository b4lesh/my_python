def call_tel(time, code):
    if code == 343:
        return 15 * time
    elif code == 381:
        return 18 * time
    elif code == 473:
        return 13 * time
    elif code == 485:
        return 11 * time
    else:
        return "Введённый код города не верный."


code = int(input("Введите код города: "))
time = int(input("Введите минуты: "))
print(call_tel(time, code))
