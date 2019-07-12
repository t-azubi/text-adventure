import random

from enum import Enum


class Actions(Enum):
    ATTACK = 1,
    LOOK = 2,
    TAKE = 3


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
        GenPaths.path_handling(counter)

    def path_handling(counter):

        if counter == 1:
            action = "1"
            print(">There is only one way to go.")
        elif counter == 2:
            action = str(input(">There are two ways you can go, which will you choose. 1 | 2 :"))
        elif counter == 3:
            action = str(input(">There are three ways you can go, choose wisely. 1 | 2 | 3 :"))

        if int(action) > counter or int(action) < 1:
            print("> You have to choose a valied path!")
            GenPaths.path_Handling(counter)

        if int(action) == 1:
            quote = (">You choose the first path,")
            GenPaths.make_cool_quote(quote)
        elif int(action) == 2:
            quote = (">You choose the second path,")
            GenPaths.make_cool_quote(quote)
        elif int(action) == 3:
            quote = (">You choose the third path,")
            GenPaths.make_cool_quote(quote)

    def make_cool_quote(quote):
        rand = random.randint(1, 5)
        if rand == 1:
            quote += " let's see where this path will leads you."
        elif rand == 2:
            quote += " hopefully your decision was the right one."
        elif rand == 3:
            quote += " we'll see if it was the right one."
        elif rand == 4:
            quote += " "
        elif rand == 5:
            quote += " "

class Weapon:

    def __init__(self, name, kind, dmg, worth, broken):
        self.name = name
        self.kind = kind
        self.dmg = dmg
        self.worth = worth
        self.broken = broken

    def can_attack(self):
        if self.broken == False:
            return True
        else:
            return False

class Character:

    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def can_do_action(self):
        if self.hp > 0:
            print("Choose how you want to continue!")
        else:
            print("You can't do anything, your character is dead!")


class Item:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

class Room:

    def __init__(self, size, props, loot, enemies):
        self.size = size
        self.props = props
        self.loot = loot
        self.enemies = enemies

    def gen_room():
        if random.randint

class BigRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="chairs", loot="gold", enemies="spiders")

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass