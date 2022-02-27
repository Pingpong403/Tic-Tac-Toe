# Tic-Tac-Toe
# by Josh Hamilton

def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board = create_board(grid)
    print(board)

    print('\nPlayer 1 is "X", Player 2 is "O".')

    turn = 0
    game_won = False
    game_state = 'Clean'
    while not game_won:
        # Turn 0 is player 1, turn 1 is player 2.
        # This loop goes from player one to player two until
        # a win condition is met or they draw.

        # Input
        if turn == 0:
            player = 'X'
            print('Player 1 where would you like to place an X?')
            while True:
                try:
                    space = int(input())
                    if space not in grid:
                        print('That is not an available space. Try again.')
                    else:
                        break
                except ValueError:
                    print('Try entering a number.')
        else:
            player = 'O'
            print('Player 2 where would you like to place an O?')
            while True:
                try:
                    space = int(input())
                    if space not in grid:
                        print('That is not an available space. Try again.')
                    else:
                        break
                except ValueError:
                    print('Try entering a number.')

        # Update & display board
        grid = modify_grid(grid, space, player)
        board = create_board(grid)
        print(board)

        # Check for win or draw, update turn
        winner = check_win(grid)
        if winner != None:
            game_won = True
            game_state = 'Won'
        elif 1 not in grid and 2 not in grid and 3 not in grid and 4 not in grid and 5 not in grid and 6 not in grid and 7 not in grid and 8 not in grid and 9 not in grid:
            game_won = True
            game_state = 'Draw'
        else:
            if turn == 0:
                turn += 1
            else:
                turn -= 1
            print()
    
    if game_state == 'Won':
        if winner == 'X':
            print('Player 1 won the game!')
        else:
            print('Player 2 won the game!')
    else:
        print('Draw!')

def create_board(grid):
    board = f'''{grid[0]}|{grid[1]}|{grid[2]}
-+-+-
{grid[3]}|{grid[4]}|{grid[5]}
-+-+-
{grid[6]}|{grid[7]}|{grid[8]}'''
    return board

def modify_grid(grid, space, player):
    space -= 1
    player = player.capitalize()
    replace_index = grid.pop(space) - 1
    grid.insert(replace_index, player)
    return grid

def check_win(grid):
    winner = None
    players = ['X', 'O']
    for player in players:
        if grid[0] == player and grid[1] == player and grid[2] == player:
            winner = player
        if grid[3] == player and grid[4] == player and grid[5] == player:
            winner = player
        if grid[6] == player and grid[7] == player and grid[8] == player:
            winner = player
        if grid[0] == player and grid[3] == player and grid[6] == player:
            winner = player
        if grid[1] == player and grid[4] == player and grid[7] == player:
            winner = player
        if grid[2] == player and grid[5] == player and grid[8] == player:
            winner = player
        if grid[0] == player and grid[4] == player and grid[8] == player:
            winner = player
        if grid[2] == player and grid[4] == player and grid[6] == player:
            winner = player
    return winner


if __name__ == '__main__':
    main()