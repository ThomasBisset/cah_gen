# import libraries
import random
import json


# load json
# download compact JSON from https://crhallberg.com/cah/
with open("cah-cards-compact.json") as json_file:
    deck = json.load(json_file)


def random_card(full_deck):

    # pick random black card
    black = random.choice(full_deck["black"])

    # formatting black cards
    black["text"] = black["text"].replace("_", "[{}]")
    black["text"] = black["text"].replace(r"\n", "\n")

    # special cases
    black["text"] = black["text"].replace("_(SAME CARD AGAIN)_", "[{}]")
    black["text"] = black["text"].replace("_[SAME CARD AGAIN]_", "[{}]")
    if black["text"] == "What are the 3 secrets for a long and happy marriage?":
        black["pick"] = 3

    # pick random white card(s) and formatting them
    white = []
    for i in range(black["pick"]):
        white.append(random.choice(full_deck["white"]).rstrip(".").replace(r"\n", "\n"))

    # print to screen if card does not have blank spaces
    if black["text"].find("[{}]") == -1:
        answer = []
        prompt = black["text"]
        for i in white:
            answer.append(i)
        output = prompt + "\n" + "[" + str(*answer) + "]"
    # print to screen if there are blank spaces
    else:
        output = black["text"].format(*white)

    return output


print(random_card(deck))
