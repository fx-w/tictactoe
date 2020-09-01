import Board

# Tie

def check_tie():
    if "E" not in Board.board:
        return True
    else:
        return False


# Player 1 win conditions:

def check_win():
    if "O" in Board.board[0] and "O" in Board.board[1] and "O" in Board.board[2]:
        return True

    elif "O" in Board.board[3] and "O" in Board.board[4] and "O" in Board.board[5]:
        return True

    elif "O" in Board.board[6] and "O" in Board.board[7] and "O" in Board.board[8]:
        return True

    elif "O" in Board.board[0] and "O" in Board.board[3] and "O" in Board.board[6]:
        return True

    elif "O" in Board.board[1] and "O" in Board.board[4] and "O" in Board.board[7]:
        return True

    elif "O" in Board.board[2] and "O" in Board.board[5] and "O" in Board.board[8]:
        return True

    elif "O" in Board.board[0] and "O" in Board.board[4] and "O" in Board.board[8]:
        return True

    elif "O" in Board.board[2] and "O" in Board.board[4] and "O" in Board.board[6]:
        return True

# Player 2 win conditions:

    if "X" in Board.board[0] and "X" in Board.board[1] and "X" in Board.board[2]:
        return True

    elif "X" in Board.board[3] and "X" in Board.board[4] and "X" in Board.board[5]:
        return True

    elif "X" in Board.board[6] and "X" in Board.board[7] and "X" in Board.board[8]:
        return True

    elif "X" in Board.board[0] and "X" in Board.board[3] and "X" in Board.board[6]:
        return True

    elif "X" in Board.board[1] and "X" in Board.board[4] and "X" in Board.board[7]:
        return True

    elif "X" in Board.board[2] and "X" in Board.board[5] and "X" in Board.board[8]:
        return True

    elif "X" in Board.board[0] and "X" in Board.board[4] and "X" in Board.board[8]:
        return True

    elif "X" in Board.board[2] and "X" in Board.board[4] and "X" in Board.board[6]:
        return True

    else:
        return False
