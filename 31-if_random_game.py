def if_random_game(x):
    if x == random_num:
        return 'Победа!'
    else:
        return 'Повторите еще раз!'


import random
random_num = random.randit(1, 4)

num = int(input("Введите число: "))
print(if_random_game(num))

    
