
import Board                                                                # import other files
import Player
import Win
import Move
from Bcolors import bcolors

player = 2                                                                  # this player starts not

print("Hello! This is a TicTacToe Game! Have Fun!")                         # dialog at start of game

while not Win.check_win() and not Win.check_tie():                          # game will run until someone wins or ties

    player = Player.switch_player(player)                                   # switch the active player

    turn_dialog = "\n\nPlayer " + str(player) + " its your turn!\n"         # generating the dialog before each turn

    print(turn_dialog)                                                      # tell the player that it is his turn
    Board.print_board()                                                     # show the current state of the board
    Board.print_help()                                                      # print out the board map as help
    Move.make_move(player)                                                  # let the player choose a field

if Win.check_win():                                                                             # check if sm1 won
    print(f"{bcolors.BOLD}\nYou won player " + str(player) + f"! Congrats!\n{bcolors.ENDC}")    # winning dialog
    Board.print_board()                                                                         # show winning Board

elif Win.check_tie():                                                                           # check if tie
    print(f"{bcolors.BOLD}It's a tie!{bcolors.ENDC}")                                           # tie dialog
    Board.print_board()                                                                         # show tie Board
