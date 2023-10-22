board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

#define a function to print the current board state
def print_board():
    print("---------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("---------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("---------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("---------------")

#define a function to check if a player has won
def check_win(player):
    #check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    #check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    #check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    #no winner
    return False

#define the main game loop
def play_game():
    print("Welcome to tic-tac-toe!!")
    print_board()
    player = "X"
    while True:
        #get input from the current player
        move = int(input("Player " + player + ", enter your move (1-9): ")) - 1
        #check if the move is valid

        if 0 <= move < 9 and board[move] == " ":
            board[move] = player
        else:
            print("Invalid move. Try again.")
            continue

        #check if the current player has won
        if check_win(player):
            print("Congratulations! Player", player, "wins!")
            break

        #check if the board is full
        if " " not in board:
            print("It's a tie!")
            break
        
        #switch to the other player
        if player == "X":
            player = "O"
        else:
            player = "X"
        #print the updated board
        print_board()

#start the game
play_game()
