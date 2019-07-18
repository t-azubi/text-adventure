import items


class Merchant:
    """A base class for the merchant"""

    def __init__(self):
        self.gold = items.Gold(100)
        self.items = [items.Axe(1), items.Sword(1)]

    def has_gold(self):
        return self.gold.amount > 0
    def sell( merchant, the_player):
        if merchant.gold.amount < 150:
            print("You can sell items to the merchant.")
            for item in the_player.inventory:
                print("\nItem: {} , Amount: {}, base Value: {}\n".format(item.name, item.amount, item.base))
            bool = False
            item = (input("Which items do you want to sell? "))
            for items in the_player.inventory:
                if items.name.upper() == item.upper():
                    if items.amount > 0:
                        the_player.inventory[0].amount += items.value
                        items.amount -= 1
                        for mitems in merchant.items:
                            if mitems.name == items.name:
                                mitems.amount += item.amount
                                mitems.value = mitems.base * mitems.amount
                                bool = True
                        if bool == False:
                            merchant.items.append(item)
                        print("\n>You sold {} for {} golden coins.".format(items.name, items.base))

        elif merchant.gold.amount > 150:
            print("You cant sell items to the merchant.")

        else:
            print("> Invalid input")

    def buy(merchant, the_player):
        x = items.Gold(1)
        bool = False
        for item in merchant.items:
            print("\nItem: {} , Amount: {}, base Value: {}\n".format(item.name, item.amount, item.base))
        what = input(str(">What would you like to buy?"))
        for mitems in merchant.items:
            if mitems.name.upper() == what.upper() and not what.upper() == "GOLD":
                if mitems.base > the_player.inventory[0].amount:
                    print("> You do not have enough gold")
                else:
                    if mitems.amount > 0:
                        mitems.amount -= 1
                        mitems.value = mitems.base * mitems.amount
                        the_player.inventory[0].amount -= mitems.base
                        the_player.inventory[0].value = the_player.inventory[0].amount * the_player.inventory[0].base
                        for pitems in the_player.inventory:
                            if pitems.name.upper() == what.upper():
                                pitems.amount += 1
                                pitems.value = pitems.amount * pitems.base
                                bool = True
                        if bool == False:
                            mitems.amount = 1
                            mitems.value = mitems.amount * mitems.base
                            the_player.inventory.append(mitems)
                    else:
                        merchant.items.remove(item)
                    bool2 = True
        if bool2 == False:
            print(">The Merchant does not sell this.")

