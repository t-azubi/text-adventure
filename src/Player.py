import items


class Character:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock(1), items.SmallPotion(1)]
        self.exp = [1, 0]
        self.hp = 100
        self.hpmax = 100
        self.victory = False
        self.roomcounter = 0
        self.slayedEnemies = 0
        self.fledFromRoom = 0

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
        max = 100
        for x in range(1, lvl):
            max += max * 1.2
        exp = max - self.exp[1]
        return exp

    def update_lvl(self):
        exp = self.get_needed_exp()
        if exp < 1:
            self.exp[0] += 1
            self.hpmax += 30
            exp = self.get_needed_exp()
        return self.exp
    def print_stats(self):
        exp = self.get_needed_exp()
        if exp < 1:
            self.exp[0] += 1
            exp = self.get_needed_exp()
        else:
            best_weapon = None
            max_dmg = 0
            armor = 0
            best_head = 0
            best_chest = 0
            best_shield = 0
            for i in self.inventory:
                if isinstance(i, items.Weapon):
                    if i.dmg > max_dmg:
                        max_dmg = i.dmg
                        best_weapon = i
                elif isinstance(i, items.Armor):
                        if i.part == "chest":
                            if i.armor > best_chest:
                                best_chest = i.armor
                        elif i.part == "head":
                            if i.armor > best_head:
                                best_head = i.armor
                        elif i.part == "shield":
                            if i.armor > best_shield:
                                best_shield = i.armor
            armor = best_chest + best_head + best_shield
            print("#################################################\n")
            print (">You passed {} rooms, slayed {} Enemies and fled from {} rooms.\n".format(self.roomcounter, self.slayedEnemies, self.fledFromRoom))
            print(">You have {} from max {} Hp, {} Armor and your best weapon does {} damage.\n".format(round(self.hp,1), self.hpmax, armor,best_weapon.dmg))
            print(">You are lvl {}. You need {} Exp to reach the next lvl.".format(self.exp[0], round(exp,1)))
            print("\n#################################################\n")


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        armor = 0
        best_head = 0
        best_chest = 0
        best_shield = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.dmg > max_dmg:
                    max_dmg = i.dmg
                    best_weapon = i
                elif isinstance(i, items.Armor):
                    if i.part == "chest":
                        if i.armor > best_chest:
                            best_chest = i.armor
                        elif i.part == "head":
                            if i.armor > best_head:
                                best_head = i.armor
                        elif i.part == "shield":
                            if i.armor > best_shield:
                                best_shield = i.armor
        armor = best_chest + best_head + best_shield
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        dmg = best_weapon.dmg - enemy.armor
        if dmg > 0:
            enemy.hp -= dmg
        else:
            print(">You can't break the armor of {}, you should flee".format(enemy.name))
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            edmg = enemy.damage - armor
            if edmg > 0:
                self.hp -= enemy.damage
                print("{} HP is {}. Your HP is {}".format(enemy.name, enemy.hp, self.hp))
            else:
                print("Your Armor blocked all damage from {}".format(enemy.name))


    def sell(self, merchant):
        if merchant.gold.amount < 150:
            print("You can sell items to the merchant.")
            for item in self.inventory:
                print("\nItem: {} , Amount: {}, Description: {},  base Value: {}\n".format(item.name, item.amount,item.description, item.base))
            bool = False
            item = (input("Which items do you want to sell or are you finish selling?"))
            if item.upper() == "FINISH":
                return merchant
            if item.upper() == "GOLD":
                print(">You can't sell gold to a merchant!")
                return merchant
            for items in self.inventory:
                if items.name.upper() == item.upper() and not item.lower() == "gold":
                    if items.amount > 0:
                        self.inventory[0].amount += items.value
                        items.amount -= 1
                        if items.amount == 0:
                            self.inventory.remove(items)
                        for mitems in merchant.items:
                            if mitems.name == items.name:
                                mitems.amount += item.amount
                                mitems.value = mitems.base * mitems.amount
                                bool = True
                        if bool == False:
                            merchant.items.append(items)
                        merchant.gold.amount -= mitems.base
                        print("\n>You sold {} for {} golden coins.".format(items.name, items.base))
                        return merchant
        else:
            print("You cant sell items to the merchant.")
            return merchant

    def buy(self, merchant):
        x = items.Gold(1)
        bool = False
        for item in merchant.items:
            print("\nItem: {} , Amount: {}, Description: {},  base Value: {}\n".format(item.name, item.amount,item.description, item.base))
        what = input(str(">You have {} Gold. What would you like to buy, or are you finished buying?".format(self.inventory[0].amount)))
        for mitems in merchant.items:
            if what.upper() == "FINISH":
                return merchant
            if mitems.name.upper() == what.upper() and not what.upper() == "GOLD":
                if mitems.base > self.inventory[0].amount:
                    print("> You do not have enough gold")
                    return merchant
                else:
                        mitems.amount -= 1
                        mitems.value = mitems.base * mitems.amount
                        merchant.gold.amount += mitems.base
                        self.inventory[0].amount -= mitems.base
                        self.inventory[0].value = self.inventory[0].amount * self.inventory[0].base
                        for pitems in self.inventory:
                            if pitems.name.upper() == what.upper():
                                pitems.amount += 1
                                pitems.value = pitems.amount * pitems.base
                                bool = True
                        if bool == False:
                            if mitems.amount == 0:
                                a = mitems
                                merchant.items.remove(mitems)
                                a.amount = 1
                                a.value = a.amount * a.base
                                self.inventory.append(a)
                                return merchant
                            else:
                                self.inventory.append(mitems)

        return merchant

    def flee(self):
        """Moves the player randomly to an adjacent tile"""
        print("> You ran down a random path, hopefully the next room will be safer")
