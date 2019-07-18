import items


class Character:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock(1)]
        self.exp = [1, 0]
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

    def get_needed_exp(self):
        lvl = self.exp[0]
        max = 100.0
        for x in range(0, lvl):
            max += x * 1.2
        exp = max - self.exp[1]
        return exp

    def print_exp(self):
        exp = self.get_needed_exp()
        if exp < 1:
            self.exp[0] += 1
            exp = self.get_needed_exp()
        else:
            print("#################################################\n")
            print("> You are lvl {}. You need {} Exp to reach the next lvl.".format(self.exp[0], exp))
            print("\n#################################################\n")

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
