def add_task():
    text = input('Сформулируйте задачу: ')
    category = input('Категория задачи: ')
    time = input('Время выполнения: ')
    TODO.append([text, category, time])

def show_all_tasks():
    for task in TODO:
        text, category, time = task
        print(f'Задача: {text} | Категория: {category} | Время выполнения: {time}')
    print('')

TODO = []

while True:
    hello_text = '''Простой todo:
        1. Добавить задачу
        2. Вывести список задач.
        3. Выход. '''
    print(hello_text)
    try:
        command = int(input('Выберите команду: '))
    except:
        print('Неверный ввод!')
        continue
    if command == 1:
        add_task()
    elif command == 2:
        show_all_tasks()
    elif command == 3:
        print('Выход из программы.')
        break
    else:
         print('Неверная команда! ')
