import random

lst =[random.randint(-500, 500)for x in range(1000)]
print(lst)

max_num = max(lst)
min_num = min(lst)
max_i = lst.index(max_num)
min_i = lst.index(min_num)
print(min_i, max_i)

if min_i < max_i:
    slice = lst[min_i:max_i + 1]
else:
    slice = lst[max_i:min_i + 1]


result = len([num for num in slice if num < 0])
print(result)
