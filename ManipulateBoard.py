import json

"""
    This function initializes the chess board and saves it to a desired file
"""
def create_board(file_name = "board.json"):
    #initizalize the board
    board = [
        "undecided"
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


if __name__ == "__main__":
    #quick test
    if create_board():
        print("Board created")
    print(read_board())