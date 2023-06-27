# import libraries
import random
import json


# load json
with open("cah-cards-compact.json") as json_file:
    full_deck = json.load(json_file)


# pick random black card
black = random.choice(full_deck["black"])
black["text"] = black["text"].replace("_(SAME CARD AGAIN)_", "[{}]")
black["text"] = black["text"].replace("_[SAME CARD AGAIN]_", "[{}]")
black["text"] = black["text"].replace("_", "[{}]")


# pick random white card(s)
white = []
for i in range(black["pick"]):
    white.append(random.choice(full_deck["white"]).rstrip("."))


# print output strings
if black["text"].find("[{}]") == -1:
    print(black["text"])
    for i in white:
        print("[", end="")
        print(i, end=".]\n")
else:
    print(black["text"].format(*white))
