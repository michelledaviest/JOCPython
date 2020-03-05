import numpy as np

board = np.array([['-']*3]*3)
board = np.array(['-']*9).reshape((3,3))
play = "x"
playX = True
player1 = [0]*8
player2 = [0]*8
num_plays = 9

def check_win():
    if 3 in player1: return 1
    if -3 in player2: return -1
    else: return 0

def add_scores(score, row, col, point):
    score[row] += point #row point
    score[3 + col] += point #col point
    if row == col: score[6] += point #diagonal1
    if (2-col) == row: score[7] += point #diagonal2

def print_board():
    for row in board:
        print("{} {} {}".format(row[0],row[1],row[2]))

while num_plays != 0:
    num_plays -= 1
    print_board()

    i = int(input("Enter row position of "+play+": "))
    j = int(input("Enter column position of "+play+": "))

    while(True):
        if (i>0 and j>0) and (i<4 and j<4) and (board[i-1][j-1] == '-'): 
            board[i-1][j-1] = play
            break
        else: print("Invalid row and column")

    if playX: #player 1 - add +1's
        add_scores(player1, i-1, j-1, 1)
        playX = False
        play = "o"
    else: #player 2
        add_scores(player2, i-1, j-1, -1)
        playX = True
        play = "x"

    winner = check_win()
    if winner != 0:
        if winner == 1: print("Player 1 has won!")
        elif winner == 2: print("Player 2 has won!")
        print_board()
        break
        
if num_plays == 0: 
    print("It's a draw!")
    print_board()
