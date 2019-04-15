def func_sinus(x):
    import math

    
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1
    

x = float(input("Введите число: "))
print(func_sinus(x))
