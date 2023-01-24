size = int(input())

chess_board = [list(input()) for _ in range(size)]

moves = (
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2)
)

knight_attacks = []
top_knight = 0
position_of_top_knight = tuple()
count = 0

def valid_move(position):
    all_valid_moves = []
    for move in moves:
        possible_moves = position[0] + move[0], position[1] + move[1]
        if 0 <= possible_moves[0] < size and 0 <= possible_moves[1] < size:
            all_valid_moves.append(possible_moves)
    return all_valid_moves


while True:
    for row in range(size):
        for colum in range(size):

            if chess_board[row][colum] == 'K':
                position = row, colum
                attacks = 0

                for current_move in valid_move(position):
                    r = current_move[0]
                    c = current_move[1]

                    if chess_board[r][c] == 'K':
                        attacks += 1

                if attacks > top_knight:
                    top_knight = attacks
                    position_of_top_knight = row, colum
    if position_of_top_knight:
        row = position_of_top_knight[0]
        col = position_of_top_knight[1]
        chess_board[row][col] = '0'
        count += 1
        position_of_top_knight = tuple()
        top_knight = 0
    else:
        print(count)
        break