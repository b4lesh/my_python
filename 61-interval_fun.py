def interval_fun(x):
    return x**2 + 3
summ = 0
for i in range(10, 30, 2):
    summ = summ + interval_fun(i)
print(summ)
    
