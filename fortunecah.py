# import libraries
import os.path
import random
import json
import argparse


def random_card(deck_json):
    # error message in case JSON does not exist
    error404 = "404: The JSON file does not exist. \n" \
               "Download the Compact JSON from https://crhallberg.com/cah/ and " \
               "ensure it exists in the same directory as the executable script"

    # checks to make sure JSON exists
    if not os.path.exists(deck_json):
        return "ERROR " + error404

    # loads JSON file
    with open(deck_json) as json_file:
        deck = json.load(json_file)

    # pick random black card
    black = random.choice(deck["black"])

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
        white.append(random.choice(deck["white"]).rstrip(".").replace(r"\n", "\n"))

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, default="cah-cards-compact.json")
    args = parser.parse_args()
    print(random_card(deck_json=args.json))


if __name__ == "__main__":
    main()
