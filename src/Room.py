import Enemies
import actions
import items
import merchant


class Room:
    """The base class for a tile within the world space"""

    def __init__(self, size):
        self.size = size

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()


class StartingRoom(Room):

    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class EmptyCavePath(Room):
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

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.GiantSpider()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if self.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, enemy=Enemies.Ogre()):
        self.enemy = enemy
        super().__init__(self.enemy)

    def intro_text(self):
        if self.is_alive():
            return """
            An ogre is blocking your path!
            """
        else:
            return """
            A dead ogre reminds you of your triumph.
            """


import random


class Gen_Current_Room():
    def gen():
        rand = random.randint(6, 6)
        if rand == 1:
            return EmptyCavePath
        elif rand == 2:
            return Find5GoldRoom
        elif rand == 3:
            return FindDaggerRoom
        elif rand == 4:
            return OgreRoom
        elif rand == 5:
            return GiantSpiderRoom
        elif rand == 6:
            return MerchantRoom
        else:
            return EmptyCavePath
