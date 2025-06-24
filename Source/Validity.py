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
        return is_valid_knight(move=move, orientation=orientation, board=board)
    elif piece.lower() == "r":
        return is_valid_rook(move=move, orientation=orientation, board=board)
    elif piece.lower() == "b":
        return is_valid_bishop(move=move, orientation=orientation, board=board)
    elif piece.lower() == "k":
        return is_valid_king(move=move, orientation=orientation, board=board)
    elif piece.lower() == "q":
        return is_valid_queen(move=move, orientation=orientation, board=board)
    return False

"""
 Checks if pawn is eligible for promotion upon next movement.
 Returns a boolean. 
"""
def is_promotable(move):
    if move[4] == "8":
        return True
    return False
"""
 Promotes the pawn.
 Returns the board or False.
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
Returns a boolean.
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
                if get_piece(row=5, col=end_pos[1], board=board) == "#" and get_piece(row=4, col=end_pos[1], board=board) == "#":
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
                if get_piece(row=2, col=end_pos[1], board=board) == "#" and get_piece(row=3, col=end_pos[1], board=board) == "#":
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

"""
Uses a helper function to map all valid vertical and horizontal moves then compares the user desired move against said list.
Returns a boolean.
"""
def is_valid_rook(move, orientation, board):
    valid_moves = []
    is_valid_vertical(move=move, orientation=orientation, board=board, valid_moves=valid_moves),
    is_valid_horizontal(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    if Converter.to_number(move[3:5]) in valid_moves:
        return True
    return False
"""
Maps all valid horizontal moves.
Returns a list of valid moves.
"""
def is_valid_horizontal(move, orientation, board, valid_moves):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    side_to_move = 1
    for i in range(2):
        holder = start_pos
        side_to_move *= -1
        holder = (holder[0], holder[1] + side_to_move)
        captured = get_piece(board=board, row=holder[0], col=holder[1])
        while captured is not None:
            if holder[1] < 0 or holder[1] > 7:
                break
            if holder != start_pos:
                if orientation == "White":
                    if captured.upper() == captured and captured != "#":
                        break
                    elif captured != "#":
                        valid_moves.append(holder)
                        break
                    valid_moves.append(holder)
                elif orientation == "Black":
                    if holder == start_pos:
                        if captured.upper() != captured and captured != "#":
                            break
                        elif captured != "#":
                            valid_moves.append(holder)
                            break
                        valid_moves.append(holder)
            holder = (holder[0], holder[1]+side_to_move)
            captured = get_piece(board=board, row=holder[0], col=holder[1])
    return valid_moves

"""
Maps all vertical valid moves.
Returns a list of valid moves.
"""
def is_valid_vertical(move, orientation, board, valid_moves):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    direction_to_move = 1
    for i in range(2):
        holder = start_pos
        direction_to_move *= -1
        holder = (holder[0]+ direction_to_move, holder[1])
        captured = get_piece(board=board, row=holder[0], col=holder[1])
        while captured is not None:
            if holder[0] < 0 or holder[0] > 7:
                break
            if holder != start_pos:
                if orientation == "White":
                    if captured.upper() == captured and captured != "#":
                        break
                    elif captured != "#":
                        valid_moves.append(holder)
                        break
                    valid_moves.append(holder)
                elif orientation == "Black":
                    if captured.upper() != captured and captured != "#":
                        break
                    elif captured != "#":
                        valid_moves.append(holder)
                        break
                    valid_moves.append(holder)
            holder = (holder[0] + direction_to_move, holder[1])
            captured = get_piece(board=board, row=holder[0], col=holder[1])
    return valid_moves
"""
Uses a helper function to map all diagonal valid moves and checks against it.
Returns a bool.
"""
def is_valid_bishop(move, orientation, board):
    valid_moves = is_valid_diagonal(move=move, orientation=orientation, board=board, valid_moves=[])
    if to_number(move[3:5]) in valid_moves:
        return True
    return False
"""
Maps all valid moves diagonally.
Returns a list of all valid moves.
"""
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
            while captured is not None:
                if holder[0] < 0 or holder[0] > 7 or holder[1] < 0 or holder[1] > 7:
                    break
                if holder != start_pos:
                    if orientation == "White":
                        if captured.upper() == captured and captured != "#":
                            break
                        if captured != "#":
                            valid_moves.append(holder)
                            break
                        valid_moves.append(holder)
                    elif orientation == "Black":
                        if captured.upper() == captured and captured != "#":
                            valid_moves.append(holder)
                            break
                        elif captured.islower():
                            break
                        valid_moves.append(holder)
                holder = (holder[0] + direction_to_move, holder[1] + side_to_move)
                captured = get_piece(board=board, row=holder[0], col=holder[1])
    return valid_moves

"""
Uses helper functions that were used in bishop and rook mapping to determine all valid moves and checks against those to see if the user's desired move is valid.
"""
def is_valid_queen(move, orientation, board):
    valid_moves = is_valid_diagonal(move=move, orientation=orientation, board=board, valid_moves=[])
    valid_moves = is_valid_vertical(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    valid_moves = is_valid_horizontal(move=move, orientation=orientation, board=board, valid_moves=valid_moves)
    if to_number(move[3:5], orientation=orientation) in valid_moves:
        return True
    return False
"""
 Uses a helper function to map all valid moves of the knight and checks if the desired move in inside the for mentioned map.
 Returns a boolean.
"""
def is_valid_knight(move, orientation, board):
    end_pos = Converter.to_number(move=move[3:5], orientation=orientation)
    valid_moves = knight_moves(valid_moves=[], orientation=orientation, board=board, move=move)
    if end_pos in valid_moves:
        return True
    return False
"""
 Maps all valid knight moves.
 Returns a list of all valid moves.
"""
def knight_moves(valid_moves, orientation, board, move):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    valid_modifiers = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)
    ]
    for modifier in valid_modifiers:
        holder = (start_pos[0] + modifier[0], start_pos[1] + modifier[1])
        if orientation == "White":
            captured = get_piece(board=board, row=holder[0], col=holder[1])
            if 0 <= holder[0] <= 7 and 0 <= holder[1] <= 7:
                if captured == "#" or captured.upper() != captured:
                    valid_moves.append(holder)
        elif orientation == "Black":
            captured = get_piece(board=board, row=holder[0], col=holder[1])
            if captured is not None:
                if captured == "#" or captured.upper() == captured:
                    if 0 <= holder[0] <= 7 and 0 <= holder[1] <= 7:
                        valid_moves.append(holder)
    return valid_moves

def is_valid_king(move, orientation, board):
    end_pos = Converter.to_number(move=move[3:5], orientation=orientation)
    valid_moves = king_moves(valid_moves=[], orientation=orientation, board=board, move=move)
    if end_pos in valid_moves:
        return True
    return False

def king_moves(valid_moves, orientation, board, move):
    from Source.ManipulateBoard import get_piece
    start_pos = Converter.to_number(move=move[0:2], orientation=orientation)
    valid_modifiers = [
        (1, 0), (1, 1), (0, 1), (-1, 1),
        (-1, 0), (-1, -1), (0, -1), (1, -1)
    ]
    for modifier in valid_modifiers:
        holder = (start_pos[0] + modifier[0], start_pos[1] + modifier[1])
        captured = get_piece(board=board, row=holder[0], col=holder[1])
        if 0 <= holder[0] <= 7 and 0 <= holder[1] <= 7:
            if orientation == "White":
                if captured.upper() != captured or captured == "#":
                    valid_moves.append(holder)
            elif orientation == "Black":
                if captured.upper() == captured or captured == "#":
                    valid_moves.append(holder)
    return valid_moves

def is_pawn_checked(pos, orientation, checked_squares):
    modifiers = (
    (1, 1), (1, -1)
    )
    if orientation == "Black":
        for modifier in modifiers:
            holder = (pos[0] + modifier[0], pos[1] + modifier[1])
            if 0 <= holder[0] <= 7 and 0 <= holder[1] <= 7:
                checked_squares.append(holder)
    elif orientation == "White":
        for modifier in modifiers:
            holder = (pos[0] - modifier[0], pos[1] + modifier[1])
            if 0 <= holder[0] <= 7 and 0 <= holder[1] <= 7:
                checked_squares.append(holder)
    return list(checked_squares)