def my_str(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s 


s = str(input('Введите строку: '))
n = int(input('Введите число: '))

print(my_str(s, n))
