import json
import sys

"""
    This function initializes the chess board and saves it to a desired file
"""
def create_board(file_name = "board.json"):
    #initizalize the board
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
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
        #if board is created returns the board
        if create_board():
            try:
                with open(file_name, "r") as file:
                    return json.loads(file.read())

            except Exception as error:
                print(f"Unexpected error occurred whilst creating your board: {error}")
                sys.exit()
        else:
            #otherwise raise an exception to avoid recursive loop
            raise Exception("Failed to create board")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")
        sys.exit()


"""
        This function returns the piece at the given coordinates
"""
def get_piece(board, row, col):
    #check if board and coordinates are present
    if board is not None and row is not None and col is not None:
        #check if coordinates are valid
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return None
        return board[row][col]
    else:
        raise Exception("Invalid coordinates")


if __name__ == "__main__":
    #quick test
    if create_board():
        print("Board created")
    print(read_board())
    print(get_piece(read_board(), 0, 0))