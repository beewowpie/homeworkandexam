# Задание №2
# Преобразовать текст в список слов с удалением знаков препинания.

string = input('Write down a text:\n')
singns = ['.', ',', ':', ';', '!', '?', '(', ')']
words = string.split()
i = 0

for word in words:
    if word[-1] in singns:
        words[i] = word[:-1]
        word = words[i]
    if word[0] in singns:
        words[i] = word[1:]
    i += 1
for i in words:
    print(i, end= ' ')
print()