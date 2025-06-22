import  Converter
import ManipulateBoard


"""
This function is a general handler for all piece validity checks.
It passes it to helper functions to actually deal with the validation.
returns a simple Bool value.
"""
def is_valid(piece, move, orientation, board):
    if piece.lower() == "p":
        return is_valid_pawn(move=move, orientation=orientation, board=board, piece=piece)
    elif piece == "n":
        return True
    elif piece == "r":
        return True
    elif piece == "b":
        return True
    return True


"""
Helper function to handle pawn move validity.
"""
def is_valid_pawn(move, orientation, board, piece):
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    end_pos = Converter.to_number(move=move[3:5], orientation=orientation)
    if orientation == "White":
        if end_pos[0] >= start_pos[0]:
            return False
        elif end_pos[0] != start_pos[0]-1:
            return False
        else:
            if end_pos == (start_pos[0]-1, start_pos[1]+1) or end_pos == (start_pos[0]-1, start_pos[1]-1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and piece.upper() != piece:
                    return True
                else:
                    return False
            if end_pos == (start_pos[0]-1, start_pos[1]) and ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) == "#":
                return True
            else:
                return False
    elif orientation == "Black":
        if end_pos[0] <= start_pos[0]:
            return False
        elif end_pos[0] != start_pos[0]+1:
            return False
        else:
            if end_pos == (start_pos[0]+1, start_pos[1]+1) or end_pos == (start_pos[0]+1, start_pos[1]-1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and piece.upper() != piece:
                    return True
                else:
                    return False
            if end_pos == (start_pos[0]+1, start_pos[1]) and ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) == "#":
                return True
            else:
                return False
    return False
