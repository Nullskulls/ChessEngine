import os
import Converter, Draw, ManipulateBoard

def main():
    board = ManipulateBoard.read_board()
    x = 1
    while True:
        if x == 1:
            orientation = "White"
        elif x == -1:
            orientation = "Black"
        else:
            raise Exception("Unexpected error occured please try again")
        Draw.draw(board, orientation)
        move = input("Please enter a move: ")
        board = ManipulateBoard.move_piece(move ,board, orientation)
        os.system("cls" if os.name == "nt" else "clear")
        Draw.draw(board, orientation)
        x = x*-1

if __name__ == "__main__":
    main()