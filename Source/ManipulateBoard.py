import json
import sys
from copy import deepcopy
import Converter
import Checkmate
from Validity import is_valid
"""
    Function to save moves to persistent storage.
"""
def saver(data, file_name = "board.json"):
    #open file.
    with open(file_name, "w") as file:
        #overwrite existing data and save new data to file.
        file.write(json.dumps(data))


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
            #write to file using json dumps
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
                #try reading the file again
                with open(file_name, "r") as file:
                    return json.loads(file.read())

            except Exception as error:
                #if it fails return the error and exit
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
"""
    this function simply writes the piece to the board at the given coordinates
"""
def set_piece(move, board, piece):
    #Check if args are present
    if move is not None and board is not None and piece is not None:
        board[move[0]][move[1]] = piece
        return board
    else:
        raise Exception("Invalid arguments")


"""
    Handles piece movement a1xa3
"""
def move_piece(move, board, orientation, bypass = False):
    #check if all arguments are present
    if move is not None and board is not None and orientation is not None:
        #initialze all values
        starting_position = Converter.to_number(move[0:2], orientation)
        ending_position = Converter.to_number(move[3:5], orientation)
        piece = get_piece(board, starting_position[0], starting_position[1])
        validity = is_valid(move=move, piece=piece, orientation=orientation, board=board, bypass=bypass)
        #if not in checkmate
        if not Checkmate.is_checkmate(board=board, bypass=bypass):
            #if valid is valid or not none
            if validity:
                #if validation not true or false (only happens when a pawn promotes it returns a new board)
                if validity not in [True, False]:
                    #set the board to the returned board
                    board = validity
                    #update the variable piece so it isn't undone
                    piece = get_piece(board, starting_position[0], starting_position[1])
                #make a copy of the board
                temp_board = set_piece(starting_position, deepcopy(board), '#')
                temp_board = set_piece(ending_position, temp_board, piece)
                #if not now in checkmate
                if not Checkmate.is_checked(board=temp_board) and not Checkmate.is_checkmate(board=temp_board, bypass=bypass):
                    #finalize by saving temporary board to board
                    board = temp_board
                    return board
                #if is checked and not checkmated return the board without the prev move
                elif not Checkmate.is_checkmate(board=temp_board, bypass=bypass) and Checkmate.is_checked(board=temp_board) and (Checkmate.find_checker(board=temp_board)['orientation'] != orientation):
                    print("Piece is checked. ")
                    return board
                #else (has to be checkmate) exit the program
                elif not Checkmate.is_checkmate(board=temp_board, bypass=bypass) and Checkmate.is_checked(board=temp_board) and (Checkmate.find_checker(board=temp_board)['orientation'] == orientation):
                    board = temp_board
                    return board
                else:
                    sys.exit("Checkmate.")
        #if move is invalid ignore it
        else:
            print("Invalid move")
            return board
    #if everything is skipped throw an error
    else:
        raise Exception("Invalid arguments")
    raise Exception("Unexpected errors")


if __name__ == "__main__":
    #quick test
    if create_board():
        print("Board created")
    print(read_board())
    print(get_piece(read_board(), 0, 0))