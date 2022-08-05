# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class TheExample:
    def __init__(self):
        self.h = 0
        self.d = 0
        self.g = 0
        self.gl = []
        self.sgl = []

    def func(self, a):
        if type(a) is str:
            for i in a:
                if i in 'aeoiu':
                    self.h += 1
                    self.gl.append(i)
                else:
                    self.d += 1
                    self.sgl.append(i)
            print('Кол-во гласных', self.h)
            print('Кол-во согласных', self.d)
            print('Длина слова', self.func1(a))
            if (self.h * self.d) <= self.func1(a):
                print('Гласные: ', self.gl)
            else:
                print('Согласные: ', self.sgl)
        elif type(a) is int:
            for i in str(a):
                i = int(i)
                if (i % 2) == 0:
                    self.g += i
            print('Произведение: ', self.g * self.func1(a))

    def func1(selfself, a):
        return len(str(a))


example = TheExample()
c = input()
if c.isalpha():
    example.func(c)
elif c.isdigit():
    example.func(int(c))