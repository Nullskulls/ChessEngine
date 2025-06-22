import  Converter
import ManipulateBoard
from Source.Converter import to_number

"""
This function is a general handler for all piece validity checks.
It passes it to helper functions to actually deal with the validation.
returns a simple Bool value.
"""
def is_valid(piece, move, orientation, board):
    if piece.lower() == "p":
        if is_valid_pawn(move=move, orientation=orientation, board=board) and is_promotable(move=move):
            return promote(move=move, orientation=orientation, board=board)
        else:
            return is_valid_pawn(move=move, orientation=orientation, board=board)

    elif piece.lower() == "n":
        return True
    elif piece.lower() == "r":
        return is_valid_rook(move=move, orientation=orientation, board=board)
    elif piece.lower() == "b":
        if is_valid_bishop(move=move, orientation=orientation, board=board):
            return True
    return False

"""
Checks if pawn is eligible for promotion upon next movement. 
"""
def is_promotable(move):
    if move[4] == "8":
        return True
    return False
"""
 Promotes the pawn.
"""
def promote(move, orientation, board):
    if orientation == "White":
        promoting_choice = input("Promote pawn!\n[1] Queen\n[2] Knight\n[3] Bishop\n[4] Rook\n$ ")
        holder = to_number(move=move[0:2], orientation=orientation)
        match promoting_choice:
            case "1":
                return ManipulateBoard.set_piece(move=holder, board=board, piece="Q")
            case "2":
                return ManipulateBoard.set_piece(move=holder, board=board, piece="N")
            case "3":
                return ManipulateBoard.set_piece(move=holder, board=board, piece="B")
            case "4":
                return ManipulateBoard.set_piece(move=holder, board=board, piece="R")
    if orientation == "Black":
        promoting_choice = input("Promote pawn!\n[1] Queen\n[2] Knight\n[3] Bishop\n[4] Rook\n$ ")
        holder = to_number(move=move[0:2], orientation=orientation)
        match promoting_choice:
            case "1":
                ManipulateBoard.set_piece(move=holder, board=board, piece="q")
            case "2":
                ManipulateBoard.set_piece(move=holder, board=board, piece="n")
            case "3":
                ManipulateBoard.set_piece(move=holder, board=board, piece="b")
            case "4":
                ManipulateBoard.set_piece(move=holder, board=board, piece="r")
    return False


"""
Helper function to handle pawn move validity.
"""
def is_valid_pawn(move, orientation, board):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    end_pos = Converter.to_number(move=move[3:5], orientation=orientation)
    captured_piece = get_piece(row=end_pos[0], col=end_pos[1], board=board)
    if orientation == "White":
        if end_pos[0] >= start_pos[0]:
            return False
        elif end_pos[0] != start_pos[0]-1:
            if start_pos[0] == 6 and end_pos[0] == 4:
                if start_pos[1] == end_pos[1]:
                    return True
            return False
        else:
            if end_pos == (start_pos[0]-1, start_pos[1]+1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and captured_piece.upper() != captured_piece:
                    return True
            elif  end_pos == (start_pos[0]-1, start_pos[1]-1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and captured_piece.upper() != captured_piece:
                    return True
                else:
                    return False
            elif end_pos == (start_pos[0]-1, start_pos[1]) and ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) == "#":
                return True
            else:
                return False
    elif orientation == "Black":
        if end_pos[0] <= start_pos[0]:
            return False
        elif end_pos[0] != start_pos[0]+1:
            if start_pos[0] == 1 and end_pos[0] == 3:
                if start_pos[1] == end_pos[1]:
                    return True
            return False
        else:
            if end_pos == (start_pos[0]+1, start_pos[1]+1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and captured_piece.upper() == captured_piece:
                    return True
            elif end_pos == (start_pos[0] + 1, start_pos[1] - 1):
                if ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) != "#" and captured_piece.upper() == captured_piece:
                    return True
            elif end_pos == (start_pos[0]+1, start_pos[1]) and ManipulateBoard.get_piece(board=board, row=end_pos[0], col=end_pos[1]) == "#":
                return True
            else:
                return False
    return False


def is_valid_rook(move, orientation, board):
    valid_moves = []
    is_valid_vertical(move=move, orientation=orientation, board=board, valid_moves=valid_moves),
    is_valid_horizontal(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    if Converter.to_number(move[3:5]) in valid_moves:
        return True
    return False

def is_valid_horizontal(move, orientation, board, valid_moves):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    side_to_move = 1
    for i in range(2):
        holder = start_pos
        side_to_move *= -1
        holder = (holder[0], holder[1] + side_to_move)
        captured = get_piece(board=board, row=holder[0], col=holder[1])
        if captured is not None:
            while captured.upper() != captured or captured == "#":
                if holder[1] < 0 or holder[1] > 7:
                    break
                if holder != start_pos:
                    if orientation == "White":
                        if captured.upper() == captured and captured != "#":
                            break
                        valid_moves.append(holder)
                    elif orientation == "Black":
                        if holder == start_pos:
                            if captured.upper() != captured and captured != "#":
                                break
                            valid_moves.append(holder)
                holder = (holder[0], holder[1]+side_to_move)
    return valid_moves


def is_valid_vertical(move, orientation, board, valid_moves):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    direction_to_move = 1
    for i in range(2):
        holder = start_pos
        direction_to_move *= -1
        holder = (holder[0]+ direction_to_move, holder[1])
        captured = get_piece(board=board, row=holder[0], col=holder[1])
        if captured is not None:
            while captured.upper() != captured or captured == "#":
                if holder[0] < 0 or holder[0] > 7:
                    break
                if holder != start_pos:
                    if orientation == "White":
                        if captured.upper() == captured and captured != "#":
                            break
                        valid_moves.append(holder)
                    elif orientation == "Black":
                        if holder == start_pos:
                            if captured.upper() == captured and captured != "#":
                                break
                            valid_moves.append(holder)
                holder = (holder[0] + direction_to_move, holder[1])
    return valid_moves

def is_valid_bishop(move, orientation, board):
    valid_moves = is_valid_diagonal(move=move, orientation=orientation, board=board, valid_moves=[])
    if to_number(move[3:5]) in valid_moves:
        return True
    return False

def is_valid_diagonal(move, orientation, board, valid_moves):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    direction_to_move = 1
    side_to_move = 1
    for _ in range(2):
        side_to_move *= -1
        for _ in range(2):
            holder = start_pos
            direction_to_move *= -1
            holder = (holder[0] + direction_to_move, holder[1]+side_to_move)
            captured = get_piece(board=board, row=holder[0], col=holder[1])
            if captured is not None:
                while captured.upper() != captured or captured == "#":
                    if holder[0] < 0 or holder[0] > 7 or holder[1] < 0 or holder[1] > 7:
                        break
                    if holder != start_pos:
                        if orientation == "White":
                            if captured.upper() == captured and captured != "#":
                                break
                            valid_moves.append(holder)
                        elif orientation == "Black":
                            if holder == start_pos:
                                if captured.upper() == captured and captured != "#":
                                    break
                                valid_moves.append(holder)
                    holder = (holder[0] + direction_to_move, holder[1] + side_to_move)
    return valid_moves


def is_valid_queen(move, orientation, board):
    valid_moves = is_valid_diagonal(move=move, orientation=orientation, board=board, valid_moves=[])
    valid_moves = is_valid_vertical(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    valid_moves = is_valid_horizontal(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    if to_number(move[3:5]) in valid_moves:
        return True
    return False