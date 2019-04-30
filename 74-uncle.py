uncle = "Мой дядя самых честных правил, Когда не в шутку занемог, \
    Он уважать себя заставил И лучше выдумать не мог"
lst = [i for i in uncle.lower().split() if not i.startswith('м')]
uncle=str(lst)
print(uncle)
