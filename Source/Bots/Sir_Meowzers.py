import random
import Validity, ManipulateBoard
"""
Sir Meowzers is a devious bot that plays random moves to overwhelm and confuse his opponents.
"""

def generate_move():
    meowzers_move = []

    for _ in range(2):
        meowzers_move.append(random.randint(0, 7))

    meowzers_move.append("x")

    for _ in range(2):
        meowzers_move.append(random.randint(0, 7))

    return meowzers_move

def meowzers_trashtalk():
    quotes = ["You're going to lose you pleb.", "How dare the likes of you play against the great sir meowzers.",
              "I've seen your future, You die sad and alone.", "Man, You're boring at least act like you're trying to win.",
              "Going out for some tuna later wanna join?", "Honestly ever one of your moves mesmerizes me.", "I hate you.",
              "I swear if you take one piece from me ill scratch you", "I heard you hate cats... Hope I heard wrong.",
              "At least we cats don't work for the cops.", "Running out of quotes.", "I may have slipped some fur in your tea.. Hope you're not allergic.",
              "You know it would suck if i got up and scratched you.. Consider surrender.", "Got some cat nip? Heard you've got some of the good stuff.",
              "Intrest rates are through the roof these days i applied for a mortgage and apparently \"Me being a cat and being wanted for fraud\" makes my intrest higher.",
              "Fun fact! I'm wanted by 12 government agencies."
        ]
    return quotes[random.randint(0, len(quotes) - 1)]

def meowzers_play(board, orientation):
    meowzers_move = []
    piece = ""
    while not Validity.is_valid(piece=piece, board=board, orientation=orientation,move=meowzers_move):
        meowzers_move = generate_move()
        piece = ManipulateBoard.get_piece(board=board, row=meowzers_move[0], col=meowzers_move[1])
    return {
        "move": meowzers_move,
        "quote": meowzers_trashtalk()
    }
