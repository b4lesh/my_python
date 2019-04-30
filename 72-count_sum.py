num = input('Введите число: ')
summ = 0
for i in num:
   if int(i) % 2 != 0:
       summ = int(i)**2 + summ
print(summ)
    
