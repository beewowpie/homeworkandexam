class Robot:
    def __init__(self, name, weapone, armor):
        self.name = name
        self.weapone = weapone
        self.armor = armor

    def __repr__(self):
        return f"A robot name {self.name}, with {self.weapone} and {self.armor}"