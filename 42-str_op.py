s = "У лукоморья 123 дуб зеленый 456"
if 'я' in s:
    print('"я" находится на позиции ', s.index('я'))
print(f'"у" встречается в строке {s.count("у")} раза ')
if not s.isalpha():
    print(s.upper())
if len(s) > 4:
    print(s.lower())

print('О' + s[1:])
