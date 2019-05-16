import histogram_v2

def moby_clean(file_name):
    with open (file_name, 'r') as file:
        words = [line.strip() for line in file.readlines()]
        dict = histogram_v2.histogram(words)
        list_dict = list(dict.items())
        list_dict.sort(key=lambda x: x[1])
        print(list_dict[:5])
        print(list_dict[-5:])

moby_clean('moby_clean.txt')
