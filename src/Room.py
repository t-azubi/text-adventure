import Enemies
import actions
import items


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
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self):
        super().__init__(items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class MerchantRoom(LootRoom):
    def __init__(self):
        super().__init__(items.Dagger())

    def intro_text(self):
        return """
        It seems you found a Merchant just ask him what he have to offer you
        """


class Find5GoldRoom(LootRoom):
    def __init__(self):
        super().__init__(items.Gold(5))

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
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
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self):
        super().__init__(Enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self):
        super().__init__(Enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
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
        rand = random.randint(1, 5)
        if rand == 1:
            return EmptyCavePath
        elif rand == 2:
            return Find5GoldRoom
        elif rand == 3:
            return FindDaggerRoom
        elif random == 4:
            return OgreRoom
        elif random == 5:
            return GiantSpiderRoom
        else:
            return EmptyCavePath
