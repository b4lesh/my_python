def if_random_game(x):
    import random
    n = random.randint(1, 4)
    if x == n:
        return 'Победа!'
    else:
        if x > n:
            return 'Число больше.'
        else:
            return 'Число меньше.'



num = int(input("Введите число: "))
print(if_random_game(num))

    
