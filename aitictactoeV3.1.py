import random
import datetime

def display_board(board):
    horizontal_line = " ---" * 3
    print("  a   b   c")
    print(horizontal_line)
    for i, row in enumerate(board):
        print(f"{i + 1}|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
        print(horizontal_line)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] for row in range(3)) and board[0][col] != ' ':
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] != ' ':
        return True
    if all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def make_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def parse_move(move):
    if len(move) == 2 and move[0].isalpha() and move[1].isdigit():
        col = ord(move[0].lower()) - ord('a')
        row = int(move[1]) - 1
        return row, col
    else:
        return None

def play_game():
    player_score = 0
    computer_score = 0
    name = 'Player 1'
    print(" what is your ccps username/email user?");   
    name=input("Enter name")
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = True  # True if player's turn, False if computer's turn

        while True:
            display_board(board)

            if player_turn:
                move = input("Enter your move (e.g., 'a1', 'b2'): ")
                parsed_move = parse_move(move)
                if parsed_move is not None:
                    row, col = parsed_move
                else:
                    print("Invalid move format. Try again.")
                    continue
            else:
                print("Computer's move:")
                row, col = make_computer_move(board)

            if board[row][col] == ' ':
                board[row][col] = 'X' if player_turn else 'O'
                if check_winner(board):
                    display_board(board)
                    print("Player wins!" if player_turn else "Computer wins!")
                    if player_turn:
                        player_score += 1
                    else:
                        computer_score += 1
                    break
                elif is_board_full(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    player_turn = not player_turn
            else:
                print("Cell already occupied. Try again.")
       


        #x = datetime.datetime.now()
        #print(x)

        if ((player_score > 1) and (player_score % 9)==0):
            #print(os.execl("date")+ " what is your ccps username/email user?")
            #name = input();
            print(datetime.datetime.now())
            print(name+" score is a multiple of 9 🤣")
        print(f"Player Score: {player_score}, Computer Score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
#    while True:
        play_game()
        print('bye '+ name) 
