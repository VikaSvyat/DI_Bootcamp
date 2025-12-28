import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    print('    1 | 2 | 3  ')
    print("  *************")
    for i, line in enumerate(board):
        print(f"{i+1} * {line[0]} | {line[1]} | {line[2]} *")
        if i < len(board) - 1:
            print("- *---|---|---*")
    print("  *************")

def player_input(board, player):
    print (f"Player {player}'s' turn... ")
    accepted = False
    while not accepted:
        try: 
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            
            if not (1<= row <=3 and 1<= col <=3):
                print('Out of range')
            elif board[row-1][col-1] != " ":
                print('Occupied')
            else:
                accepted = True
                board[row-1][col-1] = player.upper()
        except ValueError:
            print("TypeError")
    
def check_win(board, player):
    if (board[0][0]==board[1][1]==board[2][2]==player) or (board[0][2]==board[1][1]==board[2][0]==player):
        return 1 
    for i in range (0,3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return 1 
        elif board[0][i]==board[1][i]==board[2][i]==player:
            return 1 
    return 0

def check_tie(board, win):
    if all(" " not in line for line in board) and win == 0:
        return 1 
    else:
        return 0
        
# print(f"check_tie = {check_tie()}")
def next_player(player):
    if player == 'X':
        return '0'
    else:
        return 'X'

def play():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    player = '0'
    clear_terminal()
    display_board(board) 
    while player in ('X','0'):
        if check_win(board, player) == 1:
            message = "Game is over: "+player+" win!!"
            player = ' '
        elif check_tie(board, 0) == 1:
            message = "Game is over: tie, nobody win"
            player = ' '
        else:
            player = next_player(player)
            player_input(board, player)
            clear_terminal()
            display_board(board)
    print (message)

play()
        