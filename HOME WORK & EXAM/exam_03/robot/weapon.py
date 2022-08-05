class Weapon:
    def __init__(self, name, damage, durability):

        self.name = name
        self.damage = damage
        self.durability = durability

    def __repr__(self):
        return f"{self.name} deals {self.damage} damage to the head, but his durability is {self.durability}"
