def read_file(file):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as expt:
        return expt


def write_file(file, lst):
    try:
        with open(file, 'w') as out_file:
            for i, line in enumerate(lst):
                line = f'{i + 1} ' + line
                out_file.write(line)
        print('Готово')
    except Exception as expt:
        return expt


def f(a, b):
    lst = read_file(a)

    new_file = write_file(b, lst)
    return new_file


f('text.txt', 'update_text.txt')
