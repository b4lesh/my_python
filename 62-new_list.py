import math
lst = [2, 4, 9, 16, 25]
new_lst = []
for i in lst:
    new_lst.append(math.sqrt(i))
print(new_lst)

new_list2 = list(map(math.sqrt, lst))
print(new_list2)

new_list3 = [math.sqrt(i) for i in lst]
print(new_list3)
