import Validity
from Source.Debuggers import Mapper
from Source.Validity import is_valid_vertical, is_valid_horizontal


def is_checkmate(board):
    move = 1
    white_king_pos = []
    black_king_pos = []
    white_checked_squares = []
    black_checked_squares = []
    white_king_moves = []
    black_king_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            match board[i][j].lower():
                case "p":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    checked_spaces = Validity.is_pawn_checked(pos=[i,j], orientation=orientation, checked_squares=[])
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_checked_squares.append(tuple(checked_space))
                case "n":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    checked_spaces = Validity.knight_moves(move=[i,j], orientation=orientation, valid_moves=[], board=board)
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_checked_squares.append(tuple(checked_space))
                case "q":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    checked_spaces = Validity.is_valid_vertical(move=[i,j], orientation=orientation, board=board, valid_moves=[])
                    checked_spaces = Validity.is_valid_horizontal(move=[i, j], orientation=orientation, board=board,valid_moves=checked_spaces)
                    checked_spaces = Validity.is_valid_diagonal(move=[i,j], orientation=orientation, board=board, valid_moves=checked_spaces)
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_checked_squares.append(tuple(checked_space))
                case "k":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                        white_king_pos = tuple([i, j])
                    else:
                        orientation = "Black"
                        black_king_pos = tuple([i, j])
                    checked_spaces = Validity.king_moves(move=[i,j], orientation=orientation, valid_moves=[], board=board)
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_king_moves.append(tuple(checked_space))
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_king_moves.append(tuple(checked_space))
                            white_checked_squares.append(tuple(checked_space))
                case "b":
                    if board[i][j].upper() == board[i][j]:
                        orientation = "White"
                    else:
                        orientation = "Black"
                    checked_spaces = Validity.is_valid_diagonal(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_checked_squares.append(tuple(checked_space))
                case "r":
                    if board[i][j].upper() == board[i][j]:
                      orientation = "White"
                    else:
                      orientation = "Black"
                    checked_spaces = is_valid_vertical(move=[i, j], orientation=orientation, board=board, valid_moves=[])
                    checked_spaces = is_valid_horizontal(move=[i, j], orientation=orientation, board=board, valid_moves=checked_spaces)
                    if orientation == "Black":
                        for checked_space in checked_spaces:
                            black_checked_squares.append(tuple(checked_space))
                    elif orientation == "White":
                        for checked_space in checked_spaces:
                            white_checked_squares.append(tuple(checked_space))

    if white_king_pos in black_checked_squares and all(move in black_checked_squares for move in white_king_moves):
        return "Black Wins."
    elif white_king_pos in black_checked_squares:
        return "Check"
    elif black_king_pos in white_checked_squares and all(move in white_checked_squares for move in black_king_moves):
        return "White Wins."
    elif black_king_pos in white_checked_squares:
        return "Check"
    else:
        return False


