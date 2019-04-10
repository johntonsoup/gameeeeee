print("Welcome to Tic-Tac-Toe!")

board = [
    [ '7','8','9'],
    [ '4','5','6'],
    [ '1','2','3']
    ]

def print_board():
    for g in board:
        print(g)

def big_dubs():
    
    if board[0][0]=='x' and board[0][1]== 'x' and board[0][2] == 'x':  # across top
        print("Player 1 Wins")
        
    elif board[1][0]=='x' and board[1][1]=='x' and board[1][2] == 'x': # across middle
        print("Player 1 Wins")
        
    elif board[2][0]=='x' and board[2][1]=='x' and board[2][2] == 'x': # across bottom
        print("Player 1 Wins")
        
    elif board[0][0]=='x' and board[1][0]=='x' and board[2][0] =='x': # left row
        print("Player 1 Wins")
        
    elif board[0][1]=='x' and board[1][1]=='x' and board[2][1] =='x': # middle row
        print("Player 1 Wins")
        
    elif board[0][2]=='x' and board[1][2]=='x' and board[2][2] =='x': # right row
        print("Player 1 Wins")
        
    elif board[0][0]=='x' and board[1][1]=='x' and board[2][2] =='x': # right diagonal
        print("Player 1 Wins")
        
    elif board[0][2]=='x' and board[1][1]=='x' and board[2][0] =='x': # left diagonal
        print("Player 1 Wins")
        
    elif board[0][0]=='o' and board[0][1]=='o' and board[0][2] == 'o': # across top
        print("Player 2 Wins")
        
    elif board[1][0]=='o' and board[1][1]=='o' and board[1][2] == 'o': # across middle
        print("Player 2 Wins")
        
    elif board[2][0]=='o' and board[2][1]=='o' and board[2][2] == 'o': # across bottom
        print("Player 2 Wins")
        
    elif board[0][0]=='o' and board[1][0]=='o' and board[2][0] == 'o': # left row
        print("Player 2 Wins")
        
    elif board[0][1]=='o' and board[1][1]=='o' and board[2][1] == 'o': # middle row
        print("Player 2 Wins")
        
    elif board[0][2]=='o' and board[1][2]=='o' and board[2][2] == 'o': # right row
        print("Player 2 Wins")
        
    elif board[0][0]=='o' and board[1][1]=='o' and board[2][2] == 'o': # L to R diagonal
        print("Player 2 Wins")
        
    elif board[0][2]=='o' and board[1][1]=='o' and board[2][0] == 'o': # R to L diagonal
        print("Player 2 Wins")
        
print_board()

p1 = "x"
p2 = "o"
while True:
    p1 = input("Player 1 choose position: ")
    if p1 == "7":
        board[0][0] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "8":
        board[0][1] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "9":
        board[0][2] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "4":
        board[1][0] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "5":
        board[1][1] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "6":
        board[1][2] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "1":
        board[2][0] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "2":
        board[2][1] = 'x'
        print_board()
        big_dubs()
        
    elif p1 == "3":
        board[2][2] = 'x'
        print_board()
        big_dubs()
        
    p2 = input("Player 2 choose position: ")
    if p2 == "7":
        board[0][0] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "8":
        board[0][1] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "9":
        board[0][2] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "4":
        board[1][0] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "5":
        board[1][1] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "6":
        board[1][2] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "1":
        board[2][0] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "2":
        board[2][1] = 'o'
        print_board()
        big_dubs()
        
    elif p2 == "3":
        board[2][2] = 'o'
        print_board()
        big_dubs()
        





    

    









