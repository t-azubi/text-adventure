import Enemies
import actions
import items
import merchant


class Room:
    def __init__(self, name):
        self.name = name
    """The base class for a tile within the world space"""
    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()


class StartingRoom(Room):
    def __init__(self):
        super().__init__("startingroom")
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class EmptyCavePath(Room):

    def __init__(self):
        super().__init__("emptyroom")
    def intro_text(self):
        return """
        Just an empty Room there is nothing. You must forge onwards.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class LootRoom(Room):
    """A room that adds something to the player's inventory"""

    def __init__(self, item):
        self.item = item
        self.name = "lootroom"
        super().__init__("lootroom")

    def add_loot(self, the_player):
        bool = False
        for items in the_player.inventory:
            if items.name == self.item.name:
                items.amount += self.item.amount
                items.value = items.base * items.amount
                bool = True
        if bool == False:
            the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self, item=items.Dagger(1)):
        self.item = item
        super().__init__(item)

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class MerchantRoom(Room):
    def __init__(self):
        self.merchant = merchant
        super().__init__("merchantroom")

    def intro_text(self):
        return """
        It seems you found a Merchant just ask him what he have to offer you
        """
    def modify_player(self, the_player):
        print("\n>You leave the merchant")

class Find5GoldRoom(LootRoom):
    def __init__(self, item=items.Gold(5)):
        self.item = item
        super().__init__(item)

    def intro_text(self):
        return """
        Someone dropped a 5 golden coins. You pick it up.
        """


class EnemyRoom(Room):
    def __init__(self, enemy):
        self.enemy = enemy
        self.name = "enemyroom"

    def modify_player(self, the_player):
        mult = the_player.exp[0]
        multi = 1 + (mult/10) + the_player.roomcounter/10
        self.enemy.hp *= multi
        self.enemy.hp =round(self.enemy.hp, 1)
        self.enemy.damage *= multi
        self.enemy.damage = round(self.enemy.damage, 1)
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            the_player.hp = round(the_player.hp, 1)
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(), actions.Attack(enemy=self.enemy)]


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.GiantSpider()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.GiantSpider()
        return """
            A giant spider jumps down from its web in front of you!
            """
class SpiderRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Spider()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Spider()
        return """
            A dog-sized spider crawls out of a corner of the room towards you, what do you want to do?
            """

class TrollRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Troll()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Troll()
        return """
            You come into the room and just manage to save yourself from a table flying towards you.
            A troll comes towards you.
            """

class WolfRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Wolf()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Wolve()
        return """
            You see a wolf standing over a dead body. He growls at you.
            """

class GhostRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Ghost()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Ghost()
        return """
            From a skeleton in the corner of the room rises a grey foul spirit with a homicidal look at you
            """

class OgreRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Ogre()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Ogre()
        return """
            An ogre is blocking your path!
            """


class BatRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Bat()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if not self.enemy.is_alive:
            self.enemy = Enemies.Bat()
        return """
            A bat tries to reach your neck and taste your blood.
            """



import random


class Gen_Current_Room():

    def get_enemyroom(self):
        rand = random.randint(0,7)
        if rand == 1:
            return SpiderRoom()
        elif rand == 2:
            return GiantSpiderRoom()
        elif rand == 3:
            return WolfRoom()
        elif rand == 4:
            return TrollRoom()
        elif rand == 5:
            return OgreRoom()
        elif rand == 6:
            return BatRoom()
        elif rand == 7:
            return GhostRoom()
        else :
            return SpiderRoom()

    def get_lootroom(self):
        rand = random.randint(1, 3)
        if rand == 1:
            return FindDaggerRoom()
        elif rand == 2:
           return Find5GoldRoom()
        elif rand == 3:
            return MerchantRoom()
        else:
            return Find5GoldRoom()

    def gen(self):
        rand = random.randint(1, 5)
        if  rand % 3 == 0:
            return self.get_lootroom()
        elif rand % 3 == 1:
            return self.get_enemyroom()
        else:
            return EmptyCavePath()


