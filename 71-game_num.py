import random
game = 3
n = random.randint(1, 4)
for i in range(game):
    num = input("Введите число: ")
    if num == 'выход':
        break
    
    num = int(num)
    if num == n:
        print('Победа!')
        break 
    elif num > n:
        print('Число больше.')
    else:
        print('Число меньше.')
        

