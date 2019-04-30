game = 3
import random
n = random.randint(1, 4)
for i in range(game):
    num = input("Введите число: ")

    if num == 'выход':
        break
    else:
        num = int(num)
        if num == n:
            print('Победа!')
            break 
        else:
            if num > n:
                print('Число больше.')
            else:
                print('Число меньше.')
        

