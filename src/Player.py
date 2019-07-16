import items


class Character:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock(1)]
        self.hp = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        print("#################################################")
        print("\nINVENTORY: \n")
        for item in self.inventory:
            print(item)
        print("#################################################\n")

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self):
        """Moves the player randomly to an adjacent tile"""
        print("> You ran down a random path hopefully the next room will be safer")
