data = {'пятница': {12: 250, 16: 350, 20: 450},
    'чемпионы':{10: 250, 13: 350, 16: 350},
    'пернатая банда': {10: 350, 14: 450, 18: 450}}

film = input("Выберете фильм: ").lower()
time_price = int(input("Выберете время: "))
date = input("Выберете дату: ").lower()
num = int(input("Введите количество билетов: "))

price = data[film][time_price]*num

if date == "завтра":
    price = price * 0.95
        
if num >= 20:
    price = price * 0.80

print(price)
    
