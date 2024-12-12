'''
prepare board
counter = 0
while board is not full (counter!= 9) and there is no win:
    X player, play
    input location (valid, free scape )
    counter +=1
    put X on board
    draw board
    check if won:
        row of X
        column of X
        diagonal of x
    if not won:
        check if board is full (counter == 9), tie
    O player, play
    input location (valid, free scape )
     counter +=1
    put O on board
    draw board
    check if won:
        row of O
        column of O
        diagonal of O
    if not won:
        check if board is full (counter == 9), tie
'''


def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],  # could be better board[1, 1]
        'turn': 'X',
        'counter': 0
    }


def draw_board(game):
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()


def input_square(game, x_or_o):
    row: int = int(input(f'Enter row for {x_or_o}: '))
    column: int = int(input(f'Enter column for {x_or_o}: '))
    while game['board'][row][column] != "_":
        print("try again")
        row: int = int(input(f'Enter row for {x_or_o}: '))
        column: int = int(input(f'Enter column for {x_or_o}: '))
    else:
        game['board'][row][column] = game['turn']
        game['counter'] += 1


def change_player(game):
    if game['turn'] == 'X':
        game['turn'] = 'O'
    else:
        game['turn'] = 'X'


def check_win(game, X_O: str) -> bool:
    # rows
    for row in game['board']:
        if row[0] == row[1] == row[2] == X_O:
            return True
    # diagonals
    if game['board'][0][0] == game['board'][1][1] == game['board'][2][2] == X_O:
        return True
    elif game['board'][0][2] == game['board'][1][1] == game['board'][2][0] == X_O:
        return True
    # columns
    elif game['board'][0][0] == game['board'][1][0] == game['board'][2][0] == X_O:
        return True
    elif game['board'][0][1] == game['board'][1][1] == game['board'][2][1] == X_O:
        return True
    elif game['board'][0][2] == game['board'][1][2] == game['board'][2][2] == X_O:
        return True
    else:
        return False


def check_tie(game) -> bool:
    return game['counter'] >= 9


def lets_play():
    # prepare game
    game = create_game()
    draw_board(game)
    while not check_tie(game) and not check_win(game, game['turn']):
        input_square(game, game['turn'])
        draw_board(game)
        if check_tie(game):
            break

        if check_win(game, game['turn']):
            break
        change_player(game)
    if check_win(game, game['turn']):
        print(f"the winner is {game['turn']}")
    if check_tie(game):
        print("we have a tie")


if __name__ == '__main__':
    lets_play()
