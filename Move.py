import Board
from Bcolors import bcolors


def make_move(player):
    success = False

    while not success:

        if player == 1:

            try:
                place = int(input("Where would you like to place X ? \n1 - 9: "))
                if 1 <= place <= 9 and Board.board[place - 1] == "E":
                    Board.board[place - 1] = f"{bcolors.OKBLUE}X{bcolors.ENDC}"
                    success = True

            except:
                success = False


        else:

            try:

                place = int(input("Where would you like to place O ? \n1 - 9: "))
                if 1 <= place <= 9 and Board.board[place - 1] == "E":
                    Board.board[place - 1] = f"{bcolors.OKGREEN}O{bcolors.ENDC}"
                    success = True

            except:
                success = False
