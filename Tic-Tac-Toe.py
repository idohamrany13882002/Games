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
    '''
    create a dict containing the board, turn order and counter for checking a tie
    :return:
    '''
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
    '''
    printing the game board with markers for the rows and columns.
    :param game:
    :return:
    '''
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()


def input_square(game, x_or_o):
    '''
    Receives input regarding where to put the players and validating if the space exist on the board and not occupied.
    id valid placing the mark on the board
    :param game:
    :param x_or_o:
    :return:
    '''
    while True:
        row: int = int(input(f'Enter row for {x_or_o}: '))
        if 0<=row<=2:
            break
    while True:
        column: int = int(input(f'Enter column for {x_or_o}: '))
        if 0<= column<=2:
            break
    while game['board'][row][column] != "_":
        print("try again")
        row: int = int(input(f'Enter row for {x_or_o}: '))
        column: int = int(input(f'Enter column for {x_or_o}: '))
    else:
        game['board'][row][column] = game['turn']
        game['counter'] += 1


def change_player(game):
    '''
    checking which player just made a move and assigning the next turn to the other player.
    :param game:
    :return:
    '''
    if game['turn'] == 'X':
        game['turn'] = 'O'
    else:
        game['turn'] = 'X'


def check_win(game, X_O: str) -> bool:
    '''
    checking if a player had won the game.
    :param game:
    :param X_O:
    :return:
    '''
    # rows
    for row in game['board']:
        if row[0] == row[1] == row[2] == X_O:
            return True
    # columns
    for i in range(3):
        if game['board'][0][i] == game['board'][1][i] == game['board'][2][i] == X_O:
            return True
    # diagonals
    if game['board'][0][0] == game['board'][1][1] == game['board'][2][2] == X_O:
        return True
    elif game['board'][0][2] == game['board'][1][1] == game['board'][2][0] == X_O:
        return True
    else:
        return False


def check_tie(game) -> bool:
    '''
    checking if the turn counter had reached 9.
    :param game:
    :return:
    '''
    return game['counter'] >= 9


def lets_play():
    '''
    Combines all of the functions togther to create the game
    :return:
    '''
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
