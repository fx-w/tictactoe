
import Board

def make_move(player):

    success = False

    while not success:

        if player == 1:

            place = int(input("Where would you like to place X ? \n1 - 9: "))

            if 1 <= place <= 9 and Board.board[place - 1] == "E":

                Board.board[place -1] = "X"
                success = True

            else:
                success = False

        else:

            place = int(input("Where would you like to place O ? \n1 - 9: "))

            if 1 <= place <= 9 and Board.board[place - 1] == "E":

                Board.board[place - 1] = "O"
                success = True

            else:
                success = False

# TODO: catch data type errors
