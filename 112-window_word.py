import tkinter

words = {'dog':'собака', 'cat':'кот', 'human':'человек', 'table':'стол', 'door':'дверь'}

def random_text(words):
    import random
    return random.choice(words)

def translate():
    eng_word = label_word.get()
    ru_word = entry.get()
    if words.get(ru_word) == eng_word:
        return label_result.config(text='Угадали!')
    else:
        return label_result.config(text='Не правильно.')


window = tkinter.Tk()

label = tkinter.Label(window, text = 'Случайное слово: ')
label.pack()

label_word = tkinter.Label(window, text=random(words))
label_word.pack()

label_translate = tkinter.Label(window, text = 'Укажите перевод слова: ')
label_translate.pack()

entry = tkinter.Entry(window)
entry.pack()

label_result = tkinter.Label(window)
label_result.pack()

button_next = tkinter.Button(window, text='Готово!', command = translate)
button_next.pack()

button_exit = tkinter.Button(window, text='Выход', command = window.destroy)
button_exit.pack()

window.mainloop()
