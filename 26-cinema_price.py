def cinema(film, date, time, num):
    if film == "пятница":
        if time == 12:
            price = 250 * num
        elif time == 16:
            price = 350 * num
        elif time == 20:
            price = 450 * num
    elif film == "чемпионы":
        if time == 10:
            price = 250 * num
        elif time == 13:
            price = 350 * num
        elif time == 16:
            price = 350 * num
    elif film == "пернатая банда":
        if time == 10:
            price = 350 * num
        elif time == 14:
            price = 450 * num
        elif time == 18:
            price = 450 * num

    if date == "завтра":
        price = price * 0.95
        
    if num >= 20:
        price = price * 0.80
    return price


film = input("Выберете фильм: ").lower()
date = input("Выберете дату: ").lower()
time = int(input("Выберете время: "))
num = int(input("Введите количество билетов: "))
print(cinema(film, date, time, num))
          
