def add_task():
    text = input('Сформулируйте задачу: ')
    category = input()
    time = input()
    TODO.append([text, category, time])

def show_all_tasks():
    for task in TODO:
        text, category, time = task
        print(f'Задача: {text} Категория: {category} Дата: {time}')
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
        сontinue
    if command == 1:
        add_task()
    elif command == 2:
        show_all_tasks()
    elif command == 3:
        break
    else:
         print('Неверная команда! ')
