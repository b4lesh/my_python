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
        text = input('Сформулируйте задачу: ')
        category = input('Категория задачи: ')
        time = input('Время выполнения: ')
        TODO.append({'text': text, 'category': category, 'date': time})

    if command == 2:
        for i in TODO:
            print(f"Задача: {i['text']} | Категория: {i['category']} | Число: {i['date']}")

    if command == 3:
        print('Выход из программы.')
        break
    
