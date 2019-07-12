
class quotes :
   def invaildCommand(self):
     return "> Pleas enter a valid command! "
    
   
 class actions(Enum) :
     ATTACK = 1,
     LOOK = 2,
     TAKE = 3

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