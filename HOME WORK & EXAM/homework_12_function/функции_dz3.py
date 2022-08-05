# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров.
# При шифровании каждый символ заменяется другим,
# Отстоящим от него в алфавите на фиксированное число позиций.
# См. картинку шифр цезаря
# Примеры:
#         hello world! -> khoor zruog!    !!! ЗДЕСЬ КЛЮЧ ЦИФРА 3 !!!
#         this is a test string -> ymnx nx f yjxy xywnsl
# Сайт для проверки шифра Цезаря https://ciox.ru/caesar-cipher
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.

key = int(input('Введите число для шифрования в диапазоне (1 - 25):  '))


def encode(s):
    global key

    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    s1 = s.lower()
    s_encrypted = ''
    for letter in s1:
        newPos = alphabet.find(letter) + key
        if letter in alphabet:
            s_encrypted += alphabet[newPos]
        else:
            s_encrypted += letter
    return s_encrypted


print(encode(input("Введите текст для шифрования: ")))


def decode(s):
    global key

    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    s1 = s.lower()
    s_encrypted = ''
    for letter in s1:
        newPos = alphabet.find(letter) - key
        if letter in alphabet:
            s_encrypted += alphabet[newPos]
        else:
            s_encrypted += letter
    return s_encrypted


print(decode(input("Введите текст для дешифрования: ")))