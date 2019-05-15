with open('text_temp.txt', 'r') as aero:
    temps = [float(line) for line in aero.readlines()]

print('Максимальная температура: ', max(temps))
print('Минимальная температура: ', min(temps))
print('Средняя температура: ', sum(temps)/ len(temps))
print('Уникальных значений в файле: ', len(set(temps)))

