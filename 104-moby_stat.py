def moby_clean(x):
    with open ('moby_clean.txt', 'r') as file:
        text = file.read()
        text = moby_clean('moby_clean.txt')

        word_count = {}

        for word in text:
            word_count.setdefault(text, 0)
            word_count[text] += 1
        return word_count
print(text)
