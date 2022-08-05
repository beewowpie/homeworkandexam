# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков
# (как в Facebook)
# Примеры:
# likes() -> "no one likes this"
# likes("Ann") -> "Ann likes this"
# likes("Ann", "Alex") -> "Ann and Alex like this"
# likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
# likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"

def likes(*args):
    if len(args) == 0:
        print("Нет лайков")
    elif len(args) == 1:
        print(f"{args[0]} нравится этот пост")
    elif len(args) == 2:
        print(f"{args[0]},{args[1]} нравится этот пост")
    elif len(args) > 2:
        print(f"{args[0]},{args[1]} и {len(args) - 2} нравится этот пост")


args = input("Введите имя")
likes(args)