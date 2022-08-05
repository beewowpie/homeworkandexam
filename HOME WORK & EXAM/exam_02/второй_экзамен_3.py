
# 3.Напишите программу, демонстрирующую работу try\except\finally.
# #encoding='utf-8'

# try:
#     f = open('my_file.txt', 'r')
#     try:
#         s = f.readlines()
#         print(s)
#     finally:
#         f.close()
# except FileNotFoundError:
#     print('невозможно открыть файл')
# except:
#     print('ошибка при работе с файлом')
# --------------------------------------------------------
# можно более компактно с помощью менеджера контекста

# try:
#     with open('my_file1.txt', 'r') as f:
#         s = f.readlines()
#         print(s)
# except FileNotFoundError:
#     print('невозможно открыть файл')
# except:
#     print('ошибка при работе с файлом')
# finally:
#     print('файл закрыт? ',f.closed)

