# import libraries
import random
import json


def random_card(deck, colour, n):
    output = []
    for _i in range(n):
        n_sets = len(deck)
        pack = random.randint(0, n_sets)
        output.append(random.choice(deck[pack][colour]))
    return output


# load json
with open("cah-cards-full.json") as json_file:
    full_deck = json.load(json_file)


# pick random black card
black = random_card(full_deck, "black", 1)[0]
black_output = black["text"].replace("_", "[{}]")


# pick random white card(s)
white = random_card(full_deck, "white", black["pick"])
white_output = []
for i in white:
    white_output = i["text"].rstrip(".")

# output
print(black_output.format(white_output))
