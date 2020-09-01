
board = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]               # all fields are stored in a list


def print_board():                                                  # prints out the board nicely formatted
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n"
          )


def print_help():                                                   # prints out a board map for the user
    print("1" + " | " + "2" + " | " + "3" + "\n" +
          "4" + " | " + "5" + " | " + "6" + "\n" +
          "7" + " | " + "8" + " | " + "9" + "\n"
          )
