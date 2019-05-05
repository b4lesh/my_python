uncle = "Мой дядя самых честных правил, Когда не в шутку занемог, \
    Он уважать себя заставил И лучше выдумать не мог"
lst = [i for i in uncle.split() if not i.startswith('м')]
string = ' '.join(lst)
print(string)
