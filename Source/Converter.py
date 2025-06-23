"""
    This function converts chess notation to row, col coordinates. (custom chess notation)

"""
def to_number(move, orientation = "White"):
    if type(move) == list:
        return tuple(move)
    if orientation == "White":
        return 8 - int(move[1]), ord(move[0].lower()) - ord("a")
    elif orientation == "Black":
        return int(move[1]) - 1, ord(move[0].lower()) - ord("a")
    raise ValueError("Invalid orientation. Use 'White' or 'Black'.")

if __name__ == "__main__":
    #quick test
    print(to_number([7,0], "White"))  # [7, 0]
    print(to_number("h8", "White"))  # [0, 7]
    print(to_number("a1", "Black"))  # [0, 0]
    print(to_number("h8", "Black"))  # [7, 7]