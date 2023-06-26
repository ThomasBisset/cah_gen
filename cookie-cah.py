# import libraries
import random
import json


def random_card(deck, colour, n):
    output = []
    for _i in range(n):
        n_sets = len(deck) - 1
        pack = random.randint(0, n_sets)
        output.append(random.choice(deck[pack][colour])["text"])
    return output


with open("cah-cards-full.json") as json_file:
    full_deck = json.load(json_file)


# format = cards[index of set][card colour][card index][text, pack kvp]


print(random_card(full_deck, "white", 3))