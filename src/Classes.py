import random


from enum import Enum

class Quotes:
    def invalid_input():
        return ">Your input was invalid"


class GenPaths:
    def path_gen(self):
        counter = random.randint(1, 3)
        if counter == 1:
            print(">There is only one path that leads you out of this room")
        else:
            action = self.path_handling(counter)
            self.make_cool_quote(action)

    def path_handling(self,counter):
        a = GenPaths
        if counter == 2:
            action = str(input(">There are two ways you can go, which will you choose. Enter 1 or 2 to choose your path!\n"))
        elif counter == 3:
            action = str(input(">There are three ways you can go, choose wisely. Enter 1, 2 or 3 to choose your path!\n"))
        while not action.isdigit():
            action = str(input(">Please enter a number from 1 to {}".format(counter)))

        while (int(action) > counter or int(action) < 1):
            action = str(input("> You have to chosen a valid path!"))

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

