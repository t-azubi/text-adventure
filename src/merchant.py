import items


class Merchant:
    """A base class for the merchant"""

    def __init__(self):
        self.gold = items.Gold(100)
        self.items = [items.Axe(1), items.Sword(1), items.Hammer(1)]

    def has_gold(self):
        return self.gold.amount > 0

#hammer should be added to the items class

##player selling items
def sell(self, merchant, the_player):
    if Merchant.gold == 0:
        print("You can sell items to the merchant.")
        for item in the_player.inventory:
            print("\nItem: {} , Ammount: {}, base Value: {}\n".format(item.name,item.ammount, item.base))
            bool = False
            item = (input("Which items do you want to sell? "))
            for items in the_player.inventory:
                if items.name.upper == item.upper():
                    if items.amount > 0:
                        the_player.inventory[0].amount += items.value
                        items.amount -= 1
                        for mitems in merchant.items:
                            if mitems.name == item.name:
                                mitems.amount += item.amount
                                mitems.value = mitems.base * mitems.amount
                                bool = True
                        if bool == False:
                            merchant.items.append(item)
    elif Merchant.gold > 100:
        print("You cant sell items to the merchant.")


##player buying items
def buy(self, merchant, the_player):
    x = items.Gold(1)
    for item in merchant.items:
        print("\nItem: {} , Ammount: {}, base Value: {}\n".format(item.name, item.ammount, item.base))
        what = input(str(">What would you like to buy?"))
    for mitems in merchant.items:
       if mitems.name == what.name and not what.name.upper() == "GOLD":
           if mitems.amount == 0:
               merchant.items.remove(item)
           else:
             mitems.amount -= 1
             mitems.value = mitems.base * mitems.amount
             the_player.inventory[0] -= mitems.base
             for pitems in the_player.inventory:
                 if pitems.name.upper == what.upper():
                         pitems.amount += 1
                         pitems.value = pitems.amount * pitems.base
                         bool = True
             if bool == False:
                 the_player.inventory.append(mitems(1))
            bool2 = True
    if bool2 == False:
       print(">The Merchant does not sell this.")


