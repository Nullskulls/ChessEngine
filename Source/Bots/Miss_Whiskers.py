import random

"""
Miss Whiskers is an AI bot that straight up does not know the rules of chess, She may or may not be able to movie your pieces
Kill your king or break game state. Rumor has it that she is Sir Meowzers' ex-wife
"""

def generate_move():
    meowzers_move = []

    for _ in range(2):
        meowzers_move.append(random.randint(0, 7))

    meowzers_move.append("x")

    for _ in range(2):
        meowzers_move.append(random.randint(0, 7))

    return meowzers_move

def trash_talk():
    quotes = [

        "She cant play He said, Tell that to your kids oh right you don't have custody.", "Sorry, I don't know what i'm doing.",
        "Man you're bad I don't know how to play yet here I am winning.",  "Wow you suck.",
        "Heyyy wanna go out after this..?", "Mind helping me move out tomorrow?", "Pathetic.", "Can we wrap this up i've places to be.",
        "Meow.",
    ]
    return quotes[random.randint(0, len(quotes) - 1)]

def whiskers_play():
    return {
        "move": generate_move(),
        "quote": trash_talk()
    }