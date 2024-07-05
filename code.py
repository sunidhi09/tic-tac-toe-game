def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the player has won."""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for _ in range(9):
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, or 2) separated by a space: ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter row and column as 0, 1, or 2.")
    
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
