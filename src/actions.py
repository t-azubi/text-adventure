from Player import Character as Player


class Action():
    """The base class for all actions"""

    def __init__(self, method, name, **kwargs):
        """Creates a new action
        :param method: the function object to execute
        :param name: the name of the action
        :param ends_turn: True if the player is expected to move after this action else False
        """
        self.method = method
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}".format(self.name)


class ViewInventory(Action):
    """Prints the player's inventory"""

    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", enemy=enemy)


class Flee(Action):
    def __init__(self):
        super().__init__(method=Player.flee, name="Flee")
