import random


from enum import Enum

class Quotes:
    def invalid_input():
        return ">Your input was invalid"


class GenPaths:
    def __init__(self, counter, action, quote):
        self.counter = counter
        self.action = action
        self.quote = quote

    def path_gen():
        counter = random.randint(1, 3)
        if counter == 1:
            print(">There is only one path that leads you out of this room")
        else:
            action = GenPaths.path_handling(counter)
            GenPaths.make_cool_quote(action)

    def path_handling(counter):
        if counter == 2:
            action = str(input(">There are two ways you can go, which will you choose. Enter 1 or 2 to choose your path!\n"))
        elif counter == 3:
            action = str(input(">There are three ways you can go, choose wisely. Enter 1, 2 or 3 to choose your path!\n"))



        return action

    def make_cool_quote(action):
        if int(action) == 1:
            quote = (">You choose the first path,")
        elif int(action) == 2:
            quote = (">You choose the second path,")
        elif int(action) == 3:
            quote = (">You choose the third path,")

        rand = random.randint(1, 5)
        if rand == 1:
            quote += " let's see where this path will lead you."
        elif rand == 2:
            quote += " hopefully your decision was the right one."
        elif rand == 3:
            quote += " we'll see if it was the right one."
        elif rand == 4:
            quote += " "
        elif rand == 5:
            quote += " "

        print(quote)


class Actions(Enum):
    ATTACK = 1,
    LOOK = 2,
    TAKE = 3

