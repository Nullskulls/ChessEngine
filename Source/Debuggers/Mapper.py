def draw_debug_board(checked_squares):
    board = [["." for _ in range(8)] for _ in range(8)]

    # Flatten and clean up input — handles both [(x, y)] and [[(x, y), ...], ...]
    flat_squares = []
    for entry in checked_squares:
        if isinstance(entry, (list, tuple)) and len(entry) == 2 and isinstance(entry[0], int):
            flat_squares.append(entry)
        elif isinstance(entry, (list, tuple)):
            for sub in entry:
                if isinstance(sub, (list, tuple)) and len(sub) == 2 and isinstance(sub[0], int):
                    flat_squares.append(sub)

    # Mark the board
    for r, c in flat_squares:
        if 0 <= r < 8 and 0 <= c < 8:
            board[r][c] = "X"

    # Print it
    for row in board:
        print(" ".join(row))
