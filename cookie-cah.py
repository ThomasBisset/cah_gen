# import libraries
import random
import json


# load json
# download compact JSON from https://crhallberg.com/cah/
with open("cah-cards-compact.json") as json_file:
    full_deck = json.load(json_file)


# pick random black card
black = random.choice(full_deck["black"])


# formatting black cards
black["text"] = black["text"].replace("_(SAME CARD AGAIN)_", "[{}]")
black["text"] = black["text"].replace("_[SAME CARD AGAIN]_", "[{}]")
black["text"] = black["text"].replace("_", "[{}]")
black["text"] = black["text"].replace(r"\n", "\n")


# pick random white card(s) and formatting them
white = []
for i in range(black["pick"]):
    white.append(random.choice(full_deck["white"]).rstrip(".").replace(r"\n", "\n"))


# print to screen if card does not have blank spaces
if black["text"].find("[{}]") == -1:
    print(black["text"])
    for i in white:
        print("[", end="")
        print(i, end=".]\n")
# print to screen if there are blank spaces
else:
    print(black["text"].format(*white))
