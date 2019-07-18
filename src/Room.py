import Enemies
import actions
import items


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

    def __init__(self, item, name):
        self.item = item
        self.name = name
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
        super().__init__(item, "daggerroom")

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class MerchantRoom(Room):
    def __init__(self):
        super().__init__()

    def intro_text(self):
        return """
        It seems you found a Merchant just ask him what he have to offer you
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, item=items.Gold(5)):
        self.item = item
        super().__init__(item, "goldroom")

    def intro_text(self):
        return """
        Someone dropped a 5 golden coins. You pick it up.
        """


class EnemyRoom(Room):
    def __init__(self, enemy):
        self.enemy = enemy
        self.name = enemy.name.lower() + "room"

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(), actions.Attack(enemy=self.enemy)]


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.GiantSpider()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        return """
            A giant spider jumps down from its web in front of you!
            """


class OgreRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Ogre()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        return """
            An ogre is blocking your path!
            """


import random


class Gen_Current_Room():
    def gen():
        rand = random.randint(0, 6)
        if rand == 1:
            return EmptyCavePath()
        elif rand == 2:
            return Find5GoldRoom()
        elif rand == 3:
            return FindDaggerRoom()
        elif rand == 4:
            return OgreRoom()
        elif rand == 5:
            return GiantSpiderRoom()
        else:
            return EmptyCavePath()
