# Класс Tomato:
# Создайте класс Tomato
# Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# Создайте метод init(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
# Класс TomatoBush
# Создайте класс TomatoBush
# Определите метод init(), который будет принимать в качестве параметра количество томатов
# и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
#
# Класс Gardener
# Создайте класс Gardener
# Создайте метод init(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и
# 2) _plant - принимает объект класса Tomato, является protected
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

# Тесты:
# Вызовите справку по садоводству
# Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами
# Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними
# Соберите урожай

class Tomato:

    # Стадии созревания помидора
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def init(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def init(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def init(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')


# Тесты
if name == 'main':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()