with open ('moby.txt', 'r') as chapter:
    moby = [line.lower().strip() for line in chapter.readlines()]

with open('moby_clear.txt', 'w') as new_moby:
    for line in moby:
        symbols = list(line)
        new_line = [symbol for symbol in symbols if symbol.isalpha() or symbol == ' ']
        new_line = ''.join(new_line)
        words = new_line.split(' ')
        for word in words:
            if word != '':
                moby_clear.write(word + '\n')
        print(new_line)
