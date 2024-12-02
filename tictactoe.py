class Player:
    def __init__(self, name, token):
        
        # Initialize a player with a name, token (X or O), and winning status.
        self.name = name
        self.token = token
        self.winner = False

    def set_winning_status(self, status):

        # Set the player's winning status.
        self.winner = status

    def __str__(self):
        return f"{self.name} ({self.token})"


class GameBoard:
    def __init__(self):
        
        # Initialize the game board with a 3x3 grid.
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.last_move_by = None

    def display_board(self):
        # Display the current state of the game board.
        print("\n")
        for i in range(3):
            print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:  
                print("---+---+---")
        print("\n")

    def set_move(self, player, x, y):
        
        # Set a player's move on the board.
        if x < 0 or x > 2 or y < 0 or y > 2 or self.board[x][y] != " ":
            return False
        self.board[x][y] = player.token
        self.last_move_by = player
        return True

    def check_winner(self):

        # Check if there is a winner based on the current board state
        # Check rows, columns, and diagonals
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_tie(self):

        # Check if the game is a tie
        return all(self.board[x][y] != " " for x in range(3) for y in range(3)) and self.check_winner() is None

    def reset_board(self):

        # Reset the game board for a new game.
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.last_move_by = None


def main():
    print("Welcome to Tic Tac Toe!")
    # Create players
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")

    # Initialize the game board
    board = GameBoard()

    # Game loop
    current_player = player1
    board.display_board()

    while True:
        try:
            move = input(f"{current_player}, enter your move as x,y (e.g., 0,1): ").strip()
            x, y = map(int, move.split(","))
            if not board.set_move(current_player, x, y):
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter coordinates in the form x,y (e.g., 0,1).")
            continue

        board.display_board()
        winner_token = board.check_winner()

        if winner_token:
            winner = player1 if winner_token == player1.token else player2
            winner.set_winning_status(True)
            print(f"Congratulations! {winner.name} wins!")
            break

        if board.is_tie():
            print("It's a tie!")
            break

        current_player = player2 if current_player == player1 else player1

    print("Game over!")


if __name__ == "__main__":
    main()