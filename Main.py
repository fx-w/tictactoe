
# import other files

import Board
import Player
import Win
import Move
from Bcolors import bcolors

player = 2                                                                  # this player starts not

print("Hello! This is a TicTacToe Game! Have Fun!")                         # dialog at start of game

while not Win.check_win():                                                  # game will run until someone wins

    player = Player.switch_player(player)

    turn_dialog = "\n\nPlayer " + str(player) + " its your turn!\n"         # generating the dialog before each turn

    # Players turn

    print(turn_dialog)
    Board.print_board()
    Board.print_help()

    # Make MOVE

    Move.make_move(player)


print(f"˜{bcolors.BOLD}\nYou won player " + str(player) + f"! Congrats!\n{bcolors.ENDC}")                  # winning dialog

Board.print_board()                                                         # show winning Board

# TODO add ability to tie
