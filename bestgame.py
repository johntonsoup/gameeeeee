print("Welcome to Tic-Tac-Toe!")

board = [
    [ '1','2','3'],
    [ '4','5','6'],
    [ '7','8','9']
    ]

def print_board():
    for g in board:
        print(g)

def big_dubs():
    pass

print_board()

p1 = "x"
p2 = "o"
while True:
    p1 = input("Player 1 choose position: ")
    if p1 == "1":
        board[0][0] = 'x'
        print_board()
    elif p1 == "2":
        board[0][1] = 'x'
        print_board()
    elif p1 == "3":
        board[0][2] = 'x'
        print_board()
    elif p1 == "4":
        board[1][0] = 'x'
        print_board()
    elif p1 == "5":
        board[1][1] = 'x'
        print_board()
    elif p1 == "6":
        board[1][2] = 'x'
        print_board()
    elif p1 == "7":
        board[2][0] = 'x'
        print_board()
    elif p1 == "8":
        board[2][1] = 'x'
        print_board()
    elif p1 == "9":
        board[2][2] = 'x'
        print_board()
    p2 = input("Player 2 choose position: ")
    if p2 == "1":
        board[0][0] = 'o'
        print_board()
    elif p2 == "2":
        board[0][1] = 'o'
        print_board()
    elif p2 == "3":
        board[0][2] = 'o'
        print_board()
    elif p2 == "4":
        board[1][0] = 'o'
        print_board()
    elif p2 == "5":
        board[1][1] = 'o'
        print_board()
    elif p2 == "6":
        board[1][2] = 'o'
        print_board()
    elif p2 == "7":
        board[2][0] = 'o'
        print_board()
    elif p2 == "8":
        board[2][1] = 'o'
        print_board()
    elif p2 == "9":
        board[2][2] = 'o'
        print_board()
        


    









