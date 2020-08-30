
# import other files

import Board
import Player
import Win
import Move

player = 2                                                          # this player starts not

print("Hello! This is a TicTacToe Game! Have Fun!")                 # dialog at start of game

while not Win.check_win():                                          # game will run until someone wins

    player = Player.switch_player(player)

    turn_dialog = "\n\nPlayer " + str(player) + " its your turn!\n"     # generating the dialog before each turn

    # Players turn

    print(turn_dialog)
    Board.print_board()
    Board.print_help()

    # Make MOVE

    Move.make_move(player)


print("\nYou won player " + str(player) + "! Congrats!\n")                            # winning dialog

Board.print_board()                                                                 # show winning Board
