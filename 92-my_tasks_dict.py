task = {'text': '', 'category': '', 'date': ''}

lst = list()

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
        first = input('Сформулируйте задачу: ')
        task['text'] = first
        two = input('Категория задачи: ')
        task['category'] = two
        three = input('Время выполнения: ')
        task['date'] = three
        
        lst.append(task)

    if command == 2:
        for i in lst:
            print(f"Задача: {i['text']} | Категория: {i['category']} | Число: {i['date']}")

    if command == 3:
        print('Выход из программы.')
        break
    
