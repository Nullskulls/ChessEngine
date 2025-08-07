import os
import Draw, ManipulateBoard
import copy
from Bots.Sir_Meowzers import meowzers_play
from Bots.Miss_Whiskers import whiskers_play
from Bots.Count_Catstien import catstein_play


def main():
    user_choice = input("[1] Continue last game.\n[2] New Game.\n$ ")
    if int(user_choice) == 2:
        ManipulateBoard.create_board()

    user_choice = input("[1] Pass and play\n[2] Bots.\n$ ")
    match user_choice:
        case "1":
            pass_and_play()
        case "2":
            bot = input("Which bot would you like to play?\n[1] Sir Meowzers.\n[2] Miss Whiskers.\n[3] Count Catstein\n$ ")
            play_against_bot(bot)

def pass_and_play():
    board = ManipulateBoard.read_board()
    x = 1
    while True:
        if x == 1:
            orientation = "White"
        elif x == -1:
            orientation = "Black"
        else:
            raise Exception("Unexpected error occurred please try again")
        Draw.draw(board, orientation)
        move = input("Please enter a move.\nExample: e2xe4.\n$ ")
        old_board = copy.deepcopy(board)
        new_board = ManipulateBoard.move_piece(board=board, move=move, orientation=orientation)
        if old_board != new_board:
            board = new_board
            os.system("cls" if os.name == "nt" else "clear")
            x *= -1
        ManipulateBoard.saver(data=board)


def play_against_bot(bot):
    user_choice = input("Play White or black?\n[1] White\n[2] Black\n$ ")
    bypass = True if int(bot) == 2 or 3 else False
    match user_choice:
        case "1":
            user_orientation = "White"
        case "2":
            user_orientation = "Black"
    turn =  1
    board = ManipulateBoard.read_board()
    bot_move = {
        "quote": "",
        "move": ""
    }
    while True:
        playing = "White" if turn == 1 else "Black"
        Draw.draw(board=board, orientation=user_orientation)
        if playing == user_orientation:
            bypass = False
            print(bot_move["quote"])
            move = input("Please enter a move.\nExample: e2xe4.\n$ ")
        else:
            bypass = True if int(bot) == 2 or 3 else False
            if bot == "1":
                bot_move = meowzers_play(orientation=playing, board=board)
            elif bot == "2":
                bot_move = whiskers_play()
            elif bot == "3":
                bot_move = catstein_play(board=board, orientation=playing)
            move = bot_move["move"]
        old_board = copy.deepcopy(board)
        new_board = ManipulateBoard.move_piece(board=board, move=move, orientation=playing, bypass=bypass)
        if old_board != new_board:
            board = new_board
            os.system("cls" if os.name == "nt" else "clear")
            turn *= -1
        ManipulateBoard.saver(data=board)

if __name__ == "__main__":
    main()