from orange import Orange
from apple import Apple
from tangerine import Tangerine
from banana import Banana

orange = Orange("Verna", ["a, b1, c, b2"], 100, "Orange")
apple = Apple("Antonovka", ["a, b, c, e"], 120, "Apple")
tangerine = Tangerine("Klementin", ["a, d , k"], 110, "Tangerine")
banana = Banana("Baby", ["b, b1, b2"], 130, "Banana", 358)
apple.cut()
orange.clear()
tangerine.clear()
banana.clear()

print(orange)
print(apple)
print(tangerine)
print(banana)


