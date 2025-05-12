def draw(board="None", orientation="White"):
    if board == "None":
        raise TypeError("Board cannot be None")
    if orientation == "White":
        for row in board:
            for col in row:
                print(col, end="  ")
            print(end="\n \n")
    if orientation == "Black":
        for row in board[::-1]:
            for col in row:
                print(col, end="  ")
            print(end="\n \n")


if __name__ == "__main__":
    board_demo = [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ]
    draw(board_demo, orientation="Black")

