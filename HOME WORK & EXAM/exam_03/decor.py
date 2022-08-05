# 3.метод sum(a,b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку если переданы нечисловые параметры(например строка)

def validate_numbers_decorator(function):
    def wrapper_arguments(arg1, arg2):
        print(f"Аргументы для проверки: {arg1}, {arg2}")

        is_arg1_valid = isinstance(arg1, int) or isinstance(arg1, float)
        is_arg2_valid = isinstance(arg2, int) or isinstance(arg1, float)

        if is_arg1_valid and is_arg2_valid:
            print("Агрументы валидны")
        else:
            raise Exception("Not valid")

        function(arg1, arg2)

    return wrapper_arguments


@validate_numbers_decorator
def sum(a, b):
    return a + b


@validate_numbers_decorator
def multiply(a, b):
    return a * b


sum(1, 2)
# sum(3, "4")
multiply(3, 5)
