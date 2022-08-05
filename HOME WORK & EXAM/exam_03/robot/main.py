from weapon import Weapon
from armor import Armor
from robot import Robot

gun = Weapon("blaster", 100, 60)

armor = Armor("exoskeleton", 100, 30)

robot = Robot("bumblebee", gun, armor)

print(robot)