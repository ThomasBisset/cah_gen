# import libraries
import random
import re

# read text files
black_file = open("black.txt", "r")
white_file = open("white.txt", "r")

# convert text files to Python lists
all_black_cards = black_file.read().split("\n")
all_white_cards = white_file.read().split("\n")

# remove full stops from end of all white cards


# pick a random black card
black_card = random.choice(all_black_cards)

# search black card for number of blanks (underscores) and it's location in the string
blank_spaces = []
for underscore in re.finditer("_", black_card):
    blank_spaces = blank_spaces + [underscore.start()]

# pick n white cards depending on number of blanks above
white_card = []
if len(blank_spaces) < 1:
    print(black_card, random.choice(all_white_cards))
else:
    for _i in blank_spaces:
        white_card = white_card + [random.choice(all_white_cards)]

# combine into a string to output
if len(blank_spaces) >= 1:
    black_card = black_card.replace("_", "{}")
    print(black_card.format(*white_card))

# debug shit
print("----")
print(black_card)
print(white_card)

# TODO: Haiku specific case
# TODO: _[SAME CARD]_ specific case
# TODO: Punctuation and capitalisation correction
# TODO: Respect newlines
