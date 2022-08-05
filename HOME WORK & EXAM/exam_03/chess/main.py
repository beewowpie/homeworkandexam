from chess import Chess

game_1 = Chess()
print("========КОРОЛЬ========")
print(game_1.is_king_can_move([2, 2], [2, 3]))  # YES
print(game_1.is_king_can_move([2, 2], [3, 2]))  # YES
print(game_1.is_king_can_move([2, 2], [3, 3]))  # YES
print(game_1.is_king_can_move([2, 2], [1, 1]))  # YES
print(game_1.is_king_can_move([2, 2], [2, 4]))  # NO
print(game_1.is_king_can_move([2, 2], [4, 4]))  # NO
print("========ЛАДЬЯ========")
print(game_1.is_rook_can_move([2, 2], [2, 5]))  # YES
print(game_1.is_rook_can_move([2, 2], [4, 2]))  # YES
print(game_1.is_rook_can_move([2, 2], [3, 3]))  # NO
print(game_1.is_rook_can_move([2, 2], [1, 4]))  # NO
print("========СЛОН========")
print(game_1.is_elephant_can_move([2, 2], [4, 4]))  # YES
print(game_1.is_elephant_can_move([2, 4], [3, 3]))  # YES
print(game_1.is_elephant_can_move([2, 3], [4, 1]))  # YES
print(game_1.is_elephant_can_move([2, 4], [4, 4]))  # NO
print(game_1.is_elephant_can_move([2, 2], [2, 5]))  # NO
print("========ФЕРЗЬ========")
print(game_1.is_queen_can_move([2, 3], [4, 5]))  # YES
print(game_1.is_queen_can_move([1, 3], [1, 1]))  # YES
print(game_1.is_queen_can_move([4, 4], [1, 4]))  # YES
print(game_1.is_queen_can_move([2, 2], [4, 3]))  # NO
print("========КОНЬ========")
print(game_1.is_horse_can_move([1, 2], [3, 3]))  # YES
print(game_1.is_horse_can_move([4, 4], [2, 3]))  # YES
print(game_1.is_horse_can_move([3, 1], [1, 2]))  # YES
print(game_1.is_horse_can_move([4, 4], [2, 1]))  # NO
print(game_1.is_horse_can_move([3, 1], [1, 5]))  # NO
