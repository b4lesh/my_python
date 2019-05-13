with open ('moby.txt', 'r') as chapter:
    moby = [line.lower() for line in chapter.readlines()]
for text in moby:
    print(text.strip())

