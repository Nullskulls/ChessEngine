import json

"""
    This function initializes the chess board and saves it to a desired file
"""
def create_board(file_name = "board.json"):
    #initizalize the board
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
    ]
    try:
        #open file
        with open(file_name, "w") as file:
            #write to file using json dumps for clarity
            file.write(json.dumps(board))
            return True
    except FileNotFoundError:
        return False


"""
    This function reads the chess board from a json file and returns it.
"""
def read_board(file_name = "board.json"):
    try:
        #try viewing file
        with open(file_name, "r") as file:
            #retreive file
            board = json.loads(file.read())
            return board
    except FileNotFoundError:
        #in case of failure creates board
        print("Board not found.")
        create_board()
        return read_board(file_name)


"""
        This function returns the piece at the given coordinates
"""
def get_piece(board, x, y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return None
    return board[x][y]


if __name__ == "__main__":
    #quick test
    if create_board():
        print("Board created")
    print(read_board())
    print(get_piece(read_board(), 0, 0))