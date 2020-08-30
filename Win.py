
import Board

winner = 0

# Player 1 win conditions:

def check_win():
    if Board.board[0] == "O" and Board.board[1] == "O" and Board.board[2] == "O":
        return True

    elif Board.board[3] == "O" and Board.board[4] == "O" and Board.board[5] == "O":
        return True

    elif Board.board[6] == "O" and Board.board[7] == "O" and Board.board[8] == "O":
        return True

    elif Board.board[0] == "O" and Board.board[3] == "O" and Board.board[6] == "O":
        return True

    elif Board.board[1] == "O" and Board.board[4] == "O" and Board.board[7] == "O":
        return True

    elif Board.board[2] == "O" and Board.board[5] == "O" and Board.board[8] == "O":
        return True

    elif Board.board[0] == "O" and Board.board[4] == "O" and Board.board[8] == "O":
        return True

    elif Board.board[2] == "O" and Board.board[4] == "O" and Board.board[6] == "O":
        return True

    # Player 2 win conditions: 

    if Board.board[0] == "X" and Board.board[1] == "X" and Board.board[2] == "X":
        return True

    elif Board.board[3] == "X" and Board.board[4] == "X" and Board.board[5] == "X":
        return True

    elif Board.board[6] == "X" and Board.board[7] == "X" and Board.board[8] == "X":
        return True

    elif Board.board[0] == "X" and Board.board[3] == "X" and Board.board[6] == "X":
        return True

    elif Board.board[1] == "X" and Board.board[4] == "X" and Board.board[7] == "X":
        return True

    elif Board.board[2] == "X" and Board.board[5] == "X" and Board.board[8] == "X":
        return True

    elif Board.board[0] == "X" and Board.board[4] == "X" and Board.board[8] == "X":
        return True

    elif Board.board[2] == "X" and Board.board[4] == "X" and Board.board[6] == "X":
        return True

    else:
        return False
