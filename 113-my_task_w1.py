import tkinter
import json



def read_file():
    try:
        with open(FILE_NAME, 'r') as file:
            text = file.readline()
            result = json.loads(text)
            return result
    except:
        print('Файла нет!')
        return []

tasks = read('my_task.json')

window = tkinter.Tk()


frame_task = tkinter.Frame(window)
frame_task.pack()


label_task = tkinter.Label(frame_task, text = 'Задача: ')
label_task.pack(side='left')

entry_task = tkinter.Entry(frame_task)
entry_task.pack(side = 'right')

frame_category = tkinter.Frame(window)
frame_category.pack()

label_category = tkinter.Label(frame_category, text = 'Категория: ')
label_category.pack(side = 'left')

entry_category = tkinter.Entry(frame_category)
entry_category.pack(side = 'right')

frame_time = tkinter.Frame(window)
frame_time.pack()


label_time = tkinter.Label(frame_time, text = 'Время: ')
label_time.pack(side = 'left')

entry_time = tkinter.Entry(frame_time)
entry_time.pack(side = 'right')

frame_button = tkinter.Frame(window)
frame_button.pack()

button_next = tkinter.Button(frame_button, text = 'Заказать')
button_next.pack()

button_next = tkinter.Button(frame_button, text = 'Список задач')
button_next.pack()

button_next = tkinter.Button(frame_button, text = 'Выход', command = window.destroy)
button_next.pack()
