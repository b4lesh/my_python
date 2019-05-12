with open('text.txt', 'r') as aero:
    temps = [float(line) for line in aero.readlines()]

print(max(temps))
print(min(temps))
print(sum(temps)/ len(temps))
print(len(set(temps)))
