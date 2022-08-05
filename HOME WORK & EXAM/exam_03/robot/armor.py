class Armor:

    def __init__(self, name, strenghth, weight):
        self.name = name
        self.strength = strenghth
        self.weight = weight

    def __repr__(self):
        return f"{self.name} has strenght {self.strength} and its mass {self.weight} kg"
