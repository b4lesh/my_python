names = ['John', 'Paul', 'George', 'Ringo']
names1 = []
for name in names:
    if name in ['John', 'Paul']:
        names1.append(name)
print(names1)

names2 = list(filter((lambda name: name == 'John' or name == 'Paul'), names))
print(names2)
