class Chess:

    def _is_straight_line(self, from_cell, to_cell):

        return from_cell[0] == to_cell[0] or from_cell[1] == to_cell[1]

    def _is_diagonal_line(self, from_cell, to_cell):

        return abs(from_cell[0] - to_cell[0]) == abs(from_cell[1] - to_cell[1])

    def is_king_can_move(self, from_cell, to_cell):
        return abs(from_cell[0] - to_cell[0]) == 1 or abs(from_cell[1] - to_cell[1]) == 1

    def is_rook_can_move(self, from_cell, to_cell):
        return self._is_straight_line(from_cell, to_cell)

    def is_elephant_can_move(self, from_cell, to_cell):
        return self._is_diagonal_line(from_cell, to_cell)

    def is_queen_can_move(self, from_cell, to_cell):
        return self._is_straight_line(from_cell, to_cell) or \
               self._is_diagonal_line(from_cell, to_cell)

    def is_horse_can_move(self, from_cell, to_cell):
        x_diff = abs(from_cell[0] - to_cell[0])
        y_diff = abs(from_cell[1] - to_cell[1])

        return (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)
