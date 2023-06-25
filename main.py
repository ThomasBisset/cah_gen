# import libraries
import random


def pick_random_card(file, n):
    stack = file.read().split("\n")
    pick = []
    for _loop in range(n):
        pick.append(random.choice(stack))
    return pick


# read text files
black_stack = open("black.txt", "r")
white_stack = open("white.txt", "r")


# draw a black card
black_pick = pick_random_card(black_stack, 1)[0]
black_pick = black_pick.strip("\n")


flag = black_pick.count("_")
if "SAME CARD AGAIN" in black_pick:
    flag = "same"
if "Make a haiku." in black_pick:
    flag = "haiku"


if flag == "haiku":
    print(black_pick)
    white_pick = pick_random_card(white_stack, 3)
    for i in white_pick:
        print("[" + i + "]")
elif flag == "same":
    white_pick = pick_random_card(white_stack, 1)
    white_pick = [i.rstrip(".") for i in white_pick]
    black_pick = black_pick.replace("_[SAME CARD AGAIN]_", "[{}]")
    black_pick = black_pick.replace("_(SAME CARD AGAIN)_", "[{}]")
    black_pick = black_pick.replace("_", "[{}]")
    print(black_pick.format(*white_pick, *white_pick))
elif flag == 0:
    white_pick = "[" + str(*pick_random_card(white_stack, 1)) + "]"
    print(black_pick)
    print(white_pick)
elif flag > 0:
    white_pick = pick_random_card(white_stack, flag)
    white_pick = [i.rstrip(".") for i in white_pick]
    white_pick = [i.strip("\n") for i in white_pick]
    black_pick = black_pick.replace("_", "[{}]")
    print(black_pick.format(*white_pick))


# TODO: Capitalisation correction?
# TODO: Colours?
