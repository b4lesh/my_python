import csv

def write_file(file, lst):
    try:
        with open(file, 'w') as out_file:
            csv_out = csv.writer(out_file)
            csv_out.writerow(['name','address','age'])
            for row in lst:
                csv_out.writerow(row)
        print(data)

    except Exception as expt:
        print(expt)


data = [('Георгий', 'Невский проспект', '22'), ('Иван', 'пр. Ветеранов', '21')]


write_file('new_cvs.csv', data)
