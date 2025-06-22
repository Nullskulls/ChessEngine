import os
import Draw, ManipulateBoard
import copy

def main():
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
        move = input("Please enter a move: ")
        old_board = copy.deepcopy(board)
        new_board = ManipulateBoard.move_piece(board=board, move=move, orientation=orientation)
        if old_board != new_board:
            board = new_board
            os.system("cls" if os.name == "nt" else "clear")
            x *= -1

if __name__ == "__main__":
    main()