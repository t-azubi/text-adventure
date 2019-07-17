import items


class Character:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock(1)]
        self.hp = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

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
                if i.dmg > max_dmg:
                    max_dmg = i.dmg
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        dmg = best_weapon.dmg - enemy.armor
        if dmg > 0:
            enemy.hp -= dmg
        else:
            print(">You can't break the armor of {}, you should flee".format(enemy.name))
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            self.hp -= enemy.damage
            print("{} HP is {}. Your HP is {}".format(enemy.name, enemy.hp, self.hp))

    def flee(self):
        """Moves the player randomly to an adjacent tile"""
        print("> You ran down a random path, hopefully the next room will be safer")
