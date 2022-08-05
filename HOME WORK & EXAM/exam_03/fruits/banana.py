from orange import Orange

class Banana(Orange):

    def __init__(self, sort, vitamins, price, name, num_of_kalium):
        super().__init__(sort, vitamins, price, name)
        self.num_of_kalium = num_of_kalium