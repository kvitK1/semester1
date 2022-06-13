def generate_chess_board():
    return {(col, row) for col in range(1, 9) for row in range(1, 9)}


def generate_positions(pos, directs):
    positions = set()
    for direct in directs:
        col = pos[0]
        row = pos[1]
        positions.add(col, row)
        while col in range(1, 9) and row in range(1, 9):
            positions.add(col, row)
            col += direct[0]
            row += direct[1]
    return positions


def find_allowed_positions(pos1, pos2):
    chess_board = generate_chess_board()
    chess_letters_inversed... 

tura = [(0, -1) (0, 1), (-1, 0), (1, 0)]
# ferz = [(0, -1) (0, 1), (-1, 0), (1, 0), (1, 1), (-1, 1), (-1, 1), (-1, -1)]
slon = [(1, 1), (-1, 1), (-1, 1), (-1, -1)]
ferz = tura + slon