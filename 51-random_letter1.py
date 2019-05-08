import random
lst = ['самовар', 'весна', 'лето']
print('Задан список слов: ',lst)
random_w = random.choice(lst)
a = random.randint(0, len(random_w)-1)
random_l = random_w[a]
print(random_w[0:a]+'?'+random_w[a+1:])
l = input('Угадайте букву: ')
if l == random_l:
    print('Победа! Слово: ', random_w)
else:
    print('Увы! Попробуйте в другой раз. Слово: ', random_w)
    
