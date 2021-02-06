# Runs the application in a loop
xox = True
while xox:

    # ASCII format of a picture
    xox_asxii = [
        f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'##::::'##::'#######::'##::::'##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
        f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. ##::'##::'##.... ##:. ##::'##::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
        f":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::. ##'##::: ##:::: ##::. ##'##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
        f"::::':::::::::::::::::::::::#######:'#######:'#######:'#######:'#######:::. ###:::: ##:::: ##:::. ###::::'#######:'#######:'#######:'#######:'#######::::::::::::::::::::::::::::",
        f"........:........:........:........:........:........:........:........::: ## ##::: ##:::: ##::: ## ##:::........:........:........:........:........:........:........:.........",
        f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ##:. ##:: ##:::: ##:: ##:. ##::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
        f":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ##:::. ##:. #######:: ##:::. ##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
        f"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::..:::.......:::..:::::..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
    ]
    for i in xox_asxii: print(i)

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    game_still_going = True

    winner = None

    current_player = "X"


    # Main function that runs the game
    def play_game():
        display_board()

        while game_still_going:
            handle_turn(current_player)

            check_if_game_over()

            flip_player()

        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner is None:
            print("Tie! \_0_/ || \_0_/")


    # Displays board
    def display_board():
        print("\n")
        print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
        print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
        print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
        print("\n")


    def handle_turn(player):
        if current_player == "X":
            print("Turn of " + player)
        elif current_player == "O":
            print("Turn of " + player)
        position = input("Choose a number between 1 and 9 : ")

        valid = False
        while not valid:
            while position not in numbers:
                position = input("Choose a number between 1 and 9 : ")
            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("You can't choose there, choose again!")
        board[position] = player

        display_board()


    # If player is X, make the name of player O; else, X
    def flip_player():
        global current_player

        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"


    def check_if_game_over():
        check_for_winner()
        check_for_tie()


    def check_for_winner():
        global winner

        row_winner = check_rows()
        column_winner = check_columns()
        diagonal_winner = check_diagonals()

        if row_winner:
            winner = row_winner
        elif column_winner:
            winner = column_winner
        elif diagonal_winner:
            winner = diagonal_winner
        else:
            winner = None


    def check_rows():
        global game_still_going

        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"

        if row_1 or row_2 or row_3:
            game_still_going = False

        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        else:
            return None


    def check_columns():
        global game_still_going

        columns_1 = board[0] == board[3] == board[6] != "-"
        columns_2 = board[1] == board[4] == board[7] != "-"
        columns_3 = board[2] == board[5] == board[8] != "-"

        if columns_1 or columns_2 or columns_3:
            game_still_going = False

        if columns_1:
            return board[0]
        elif columns_2:
            return board[1]
        elif columns_3:
            return board[2]
        else:
            return None


    def check_diagonals():
        global game_still_going

        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"

        if diagonal_1 or diagonal_2:
            game_still_going = False

        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[1]
        else:
            return None


    def check_for_tie():
        global game_still_going

        if "-" not in board:
            game_still_going = False
            return True
        else:
            return False


    play_game()

    # Asks to player for a new game
    loop = True
    while loop:
        print()
        yes_no = input("Do you want to play one more game ? Yes : y / No : n ")
        if yes_no == "y":
            loop = False
            xox = True
        elif yes_no == "n":
            loop = False
            xox = False
            print("Game Over!")
        else:
            loop = True
