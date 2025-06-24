import copy

import Validity
from ManipulateBoard import move_piece


def find_king_pos(board):
    kings_pos = {
        "white_king": [],
        "black_king": [],
    }
    for i in range(len(board)):
        for j in range(len(board[i])):
            match board[i][j].lower():
                case "k":
                    if board[i][j].upper() == board[i][j]:
                        kings_pos["white_king"] = [i, j]
                    else:
                        kings_pos["black_king"] = [i, j]
    return kings_pos

def find_checker(board):
    kings_pos = find_king_pos(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            match board[i][j].lower():
                case "k":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.king_moves(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                                "position": [i, j],
                                "orientation": orientation,
                                "moves" : space_taken
                            }
                case "p":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.is_pawn_checked(pos=[i, j], orientation=orientation, checked_squares=[])
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                            "position": [i, j],
                            "orientation": orientation,
                            "moves" : space_taken
                        }
                case "q":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.is_valid_diagonal(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    space_taken = Validity.is_valid_vertical(move=[i, j], orientation=orientation, board=board, valid_moves=space_taken)
                    space_taken = Validity.is_valid_horizontal(move=[i, j], orientation=orientation, board=board, valid_moves=space_taken)
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                            "position": [i, j],
                            "orientation": orientation,
                            "moves" : space_taken
                        }
                case "r":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.is_valid_horizontal(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    space_taken = Validity.is_valid_vertical(move=[i, j], orientation=orientation, board=board, valid_moves=space_taken)
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                            "position": [i, j],
                            "orientation": orientation,
                            "moves" : space_taken
                    }
                case "b":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.is_valid_diagonal(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                            "position": [i, j],
                            "orientation": orientation,
                            "moves" : space_taken
                        }
                case "n":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    space_taken = Validity.knight_moves(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    if tuple(kings_pos["white_king"]) in space_taken or tuple(kings_pos["black_king"]) in space_taken:
                        return {
                            "position": [i, j],
                            "orientation": orientation,
                            "moves" : space_taken
                        }
    return None

def number_of_playable(board):
    number_of_pieces = {
        "White": 0,
        "Black": 0,
    }
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].lower() != "k" and board[i][j] != "#":
                if board[i][j].upper() == board[i][j]:
                    orientation = "White"
                else:
                    orientation = "Black"
                number_of_pieces[orientation] += 1
    return number_of_pieces


def is_checked(board):
    if find_checker(board) is None:
        return False
    else:
        return True

def is_checkmate(board):
    if not is_checked(board):
        return False

    checked = find_checker(board)
    if checked is None:
        return False  # failsafe — should never happen here

    attacking_side = checked["orientation"]
    defending_side = "Black" if attacking_side == "White" else "White"
    king_pos = find_king_pos(board)["white_king" if defending_side == "White" else "black_king"]

    # 1. Try every piece on defending side
    for i in range(len(board)):
        for j in range(len(board[i])):
            piece = board[i][j]

            # Skip empty squares
            if piece == "#":
                continue

            # Skip opponent's pieces
            if (piece.isupper() and defending_side != "White") or (piece.islower() and defending_side != "Black"):
                continue

            for r in range(8):
                for c in range(8):
                    move = [i, j, "x", r, c]
                    if Validity.is_valid(move=move, board=board, orientation=defending_side, piece=piece):
                        simulated = simulate_board(copy.deepcopy(board), move, defending_side)
                        if not is_checked(simulated):
                            return False

    # 2. Try moving the king
    king_moves = Validity.king_moves(valid_moves=[], move=king_pos, board=board, orientation=defending_side)
    for dest in king_moves:
        move = [king_pos[0], king_pos[1], "x", dest[0], dest[1]]
        if Validity.is_valid(move=move, board=board, orientation=defending_side, piece='K' if defending_side == "White" else 'k'):
            simulated = simulate_board(board, move, defending_side)
            if not is_checked(simulated):
                return False

    return True  # No legal moves = checkmate




def simulate_board(board, move, orientation):
    temp_board = copy.deepcopy(board)
    temp_board = move_piece(move=move, board=temp_board, orientation=orientation)
    return temp_board