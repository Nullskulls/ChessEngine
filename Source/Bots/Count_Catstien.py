import random, Validity, ManipulateBoard

"""
    Catstein is a Count, He knows the rules and how to play but he sometimes chooses to ignore them to spite the opponent,
    Because truly what can you do.
"""
def generate_move():
    catstein_move = []

    for _ in range(2):
        catstein_move.append(random.randint(0, 7))

    catstein_move.append("x")

    for _ in range(2):
        catstein_move.append(random.randint(0, 7))

    return catstein_move

def neutral_quote():
    quotes = [
        "I'll make you nobility if you win.", "Not bad not bad.", "You're better than the last person.",
        "Not to sound egotistical but im better than all grandmasters.", "I see you're seeking refuge in my lands pleb. Win and i may consider it or behead you...",
        "Fun Fact! You can port your own AI into this its easier than you expect."
    ]
    return quotes[random.randint(0, len(quotes) - 1)]


def devious_quote():
    quotes = [
        "Oops..", "Hand slipped..", "Must've been the wind.", "You didn't see that.", "Yes i cheated do something about it I dare you",
        "And that totally goes there.", "My mistake, No i'm not moving it back.", "I hope you break your leg if you move it back", "Hehehe.",
        "Who said i couldn't cheat.", "Gotcha.", "Guess what.. Chicken butt.", "Hey, Im taking a piece home.", "I'll play properly if you list all digits of pi.",
        "And that's why i never lose."

    ]
    return quotes[random.randint(0, len(quotes) - 1)]


def catstein_play(board, orientation):
    if random.random() < 0.15:  # 15% chance to break rules
        return {
            "move": generate_move(),
            "quote": devious_quote()
        }
    else:
        catstein_move = []
        piece = ""
        while not Validity.is_valid(piece=piece, board=board, orientation=orientation, move=catstein_move):
            catstein_move = generate_move()
            piece = ManipulateBoard.get_piece(board=board, row=catstein_move[0], col=catstein_move[1])
        return {
            "move": catstein_move,
            "quote": neutral_quote()
        }
