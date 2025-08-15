letters = ['no','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
pieces = {
    "K": "♔",  # White King
    "Q": "♕",  # White Queen
    "R": "♖",  # White Rook
    "B": "♗",  # White Bishop
    "N": "♘",  # White Knight
    "P": "♙",  # White Pawn

    "k": "♚",  # Black King
    "q": "♛",  # Black Queen
    "r": "♜",  # Black Rook
    "b": "♝",  # Black Bishop
    "n": "♞",  # Black Knight
    "p": "♟"   # Black Pawn
}

def draw(board="None", orientation="White"):
    if board == "None":
        raise TypeError("Board cannot be None")
    i = 8
    j = 0
    if orientation == "White":
        for row in board:
            print(f"{i}  ", end='')
            for col in row:
                if col == '#':
                    print("#", end="　   ")
                else:
                    print(pieces[col], end="    ")
            print(end="\n \n")
            i-=1
    if orientation == "Black":
        for row in board[::-1]:
            print(f"{i}  ", end='')
            for col in row:
                print(col, end="    ")
            print(end="\n \n")
            i -= 1
    draw_bottom_border()
    print(f"{orientation} is playing.")

def draw_bottom_border():
    for i in range(9):
        if i == 0:
            print("*　 ", end='')
            continue
        print(f"{letters[i]}   　", end='')
    print()


if __name__ == "__main__":
    board_demo = [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ]
    draw(board_demo, orientation="Black")

