board = [" "] * 9



# PRINT BOARD

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")



# CHECK WINNER

def check_winner(board):

    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 4, 8],
        [2, 4, 6],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8]
    ]

    for combination in win_combinations:

        if (
            board[combination[0]]
            == board[combination[1]]
            == board[combination[2]]
            and board[combination[0]] != " "
        ):
            return board[combination[0]]

    return None



# GET EMPTY POSITIONS

def get_empty_positions(board):

    empty_positions = []

    for i in range(9):

        if board[i] == " ":
            empty_positions.append(i)

    return empty_positions



# MAKE A HYPOTHETICAL MOVE

def make_move(board, position, player):

    temp_board = list(board)

    temp_board[position] = player

    return temp_board


# MINIMAX

def minimax(board, maximizing):

    # 1. Check whether this board is already a finished game
    result = check_winner(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    # 2. Get available moves
    empty_positions = get_empty_positions(board)

    # 3. No moves left = draw
    if not empty_positions:
        return 0



    # O = MAXIMIZING PLAYER
  
    if maximizing:

        best_score = -float("inf")

        for position in empty_positions:

            # Pretend O makes a move
            new_board = make_move(board, position, "O")

            # Now it's X's turn
            score = minimax(new_board, False)

            if score > best_score:
                best_score = score

        return best_score

    # X = MINIMIZING PLAYER
    
    else:

        best_score = float("inf")

        for position in empty_positions:

            # Pretend X makes a move
            new_board = make_move(board, position, "X")

            # Now it's O's turn
            score = minimax(new_board, True)

            if score < best_score:
                best_score = score

        return best_score



# FIND BEST AI MOVE

def ai_move(board):

    best_score = -float("inf")
    best_position = None

    empty_positions = get_empty_positions(board)

    for position in empty_positions:

        # Pretend O plays here
        new_board = make_move(board, position, "O")

        # Ask Minimax how good this move eventually becomes
        score = minimax(new_board, False)

        if score > best_score:
            best_score = score
            best_position = position

    return best_position

# MAIN GAME

def play_game():

    while True:

    
        # HUMAN TURN - X

        print_board(board)

        try:
            ask_user = int(input("Choose your position (1-9): "))
        except ValueError:
            print("Please enter a number.")
            continue

        ask_user -= 1

        if ask_user < 0 or ask_user > 8:
            print("Invalid position.")
            continue

        if board[ask_user] != " ":
            print("That grid is occupied.")
            continue

        board[ask_user] = "X"


        # Check X win
        result = check_winner(board)

        if result == "X":
            print_board(board)
            print("Player X wins!")
            break


        # Check draw
        if not get_empty_positions(board):
            print_board(board)
            print("Draw!")
            break



        # AI TURN - O
  
        position = ai_move(board)

        board[position] = "O"

        print(f"AI chooses position {position + 1}")


        # Check O win
        result = check_winner(board)

        if result == "O":
            print_board(board)
            print("AI wins!")
            break


        # Check draw
        if not get_empty_positions(board):
            print_board(board)
            print("Draw!")
            break



# START GAME

play_game()