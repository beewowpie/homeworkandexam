# Задание №1
# Найти самое длинное слово в строке.
# "Первый способ через функции"

# def find_longest_word(word_list):
#     longest_word = ''
#     for word in word_list:
#         if len(word) > len(longest_word):
#             longest_word = word
#     print(longest_word)
#
# words = input('Please enter a few words')
# word_list = words.split()
# find_longest_word(word_list)
#
# # "Второй способ через sorted(сортируем список по длине)"
# #
# string = "java javascript python"
# string_split = string.split(" ")
# list_sort = sorted(string_split, key=len)
# print(list_sort[-1])
#
# "Третий способ"
#
# string_with_words = "python javascript cucumberstaffff java cucumberstaff"
# list_with_words = string_with_words.split(" ")
# long_word_len = len(list_with_words[0])
# current_word = 0
# print(long_word_len)
# for word in list_with_words:
#     word_len = len(word)
#     if word_len > long_word_len:
#         long_word_len = word_len
#         current_word = word
# print(f"Longest word {current_word}")
# print(f"longest len {long_word_len}")


