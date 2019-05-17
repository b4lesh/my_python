import tkinter
import json

FILE_NAME = 'task.json'

def read_file():
    try:
        with open(FILE_NAME, 'r') as file:
            text = file.readline()
            result = json.loads(text)
            return result
    except:
        print('Файла нет!')
        return []


def write_file(x):
    with open(FILE_NAME, 'w') as file:
        text = json.dumps(x)
        file.write(text)



def add_task():
    text = entry_task.get()
    category = entry_category.get()
    time = entry_time.get()

    tasks.append({'text': text, 'category': category, 'date': time})
    print('Задача добавлена')
    write_file(tasks)

    entry_task.delete(0, tkinter.END)
    entry_category.delete(0, tkinter.END)
    entry_time.delete(0, tkinter.END)

def show_list():
    for i in tasks:
         print(f"Задача: {i['text']} | Категория: {i['category']} | Время: {i['date']}")
        


tasks = read_file()




window = tkinter.Tk()
window.title('Менеджер задач')
window.resizable(False, False)
window.geometry('300x160')
frame_global_wrap = tkinter.Frame(window)
frame_global_wrap.pack()

frame_wrap_input = tkinter.Frame(frame_global_wrap)
frame_wrap_input.pack(side='top')

frame_label = tkinter.Frame(frame_wrap_input)
frame_label.pack(side='left')

label_task = tkinter.Label(frame_label, text = 'Задача: ')
label_task.pack()

label_category = tkinter.Label(frame_label, text = 'Категория: ')
label_category.pack()

label_time = tkinter.Label(frame_label, text = 'Время: ')
label_time.pack()



frame_entry = tkinter.Frame(frame_wrap_input)
frame_entry.pack(side='right')

entry_task = tkinter.Entry(frame_entry)
entry_task.pack()

entry_category = tkinter.Entry(frame_entry)
entry_category.pack()

entry_time = tkinter.Entry(frame_entry)
entry_time.pack()




frame_button = tkinter.Frame(window)
frame_button.pack(side='bottom')

button_add = tkinter.Button(frame_button, text = 'Добавить', width = '25', command = add_task)
button_add.pack()

button_list = tkinter.Button(frame_button, text = 'Список задач', width = '25', command = show_list)
button_list.pack()

button_exit = tkinter.Button(frame_button, text = 'Выход', width = '25', command = window.destroy)
button_exit.pack()

window.mainloop()
