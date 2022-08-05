# 1.Реализовать калькулятор с 4 методами: Сумма, вычитаниеб ,
# умножение, деление. Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны

class calculator:
    def valdate_numbers(self, first_number, second_number):
        is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
        is_valid_second_number = isinstance(second_number, int) or isinstance(second_number, float)
        if is_valid_first_number and  is_valid_second_number:
            print("Valid")
        else:
            raise Exception(" Not Valid")

    def summ(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        sum = first_number + second_number
        return sum

    def difference(self, first_number, second_number):
        self.valdate_numbers(first_number,second_number)
        diff = first_number - second_number
        return diff

    def multiplication(self, first_number, second_number):
        self.valdate_numbers(first_number,second_number)
        multip = first_number * second_number
        return multip

    def division(self, first_number, second_number):
        self.valdate_numbers(first_number,second_number)

        if second_number == 0:
            print("it cannot be divided by 0")
        else:
            div = first_number / second_number
            print(div)
        return

my_calc = calculator()
my_calc.summ(1,2)
my_calc.difference(1,2)
my_calc.multiplication(1,2)
my_calc.division(1,0)