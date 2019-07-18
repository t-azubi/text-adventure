import items, random


class Merchant:
    """A base class for the merchant"""

    def __init__(self):
        self.gold = items.Gold(100)
        self.items = self.gen_listofitems()

    def gen_listofitems(self):
        quantity = random.randint(2, 5)
        list = []
        bool = False
        item = self.get_item()
        list.append(item)
        for x in range(1, quantity):
            item = self.get_item()
            bool = False
            for items in list:
                if items.name == item.name:
                    items.amount += item.amount
                    items.value = items.base * items.amount
                    bool = True
            if bool == False:
                list.append(item)

        return list

    def get_item(self):
        rand = random.randint(0, 8)
        if rand == 1:
            return items.Dagger(1)
        elif rand == 2:
            return items.Sword(1)
        elif rand == 3:
            return items.Bow(1)
        elif rand == 4:
            return items.Axe(1)
        elif rand == 5 :
            return items.Leather_ChestPlate(1)
        elif rand == 6:
            return items.Wooden_Shield(1)
        elif rand == 7:
            return items.Leather_Cap(1)
        else:
            return items.Dagger(1)


    def sell( merchant, the_player):
        if merchant.gold.amount < 150:
            print("You can sell items to the merchant.")
            for item in the_player.inventory:
                print("\nItem: {} , Amount: {}, base Value: {}\n".format(item.name, item.amount, item.base))
            bool = False
            item = (input("Which items do you want to sell or are you finish selling?"))
            if item.upper() == "FINISH":
                return
            if item.upper() == "GOLD":
                print(">You can't sell gold to a merchant!")
            for items in the_player.inventory:
                if items.name.upper() == item.upper() and not item.lower() == "gold":
                    if items.amount > 0:
                        the_player.inventory[0].amount += items.value
                        items.amount -= 1
                        if items.amount == 0:
                            the_player.inventory.remove(items)
                        for mitems in merchant.items:
                            if mitems.name == items.name:
                                mitems.amount += item.amount
                                mitems.value = mitems.base * mitems.amount
                                bool = True
                        if bool == False:
                            merchant.items.append(item)
                        print("\n>You sold {} for {} golden coins.".format(items.name, items.base))
        else:
            print("You cant sell items to the merchant.")

    def buy(merchant, the_player):
        x = items.Gold(1)
        bool = False
        for item in merchant.items:
            print("\nItem: {} , Amount: {}, base Value: {}\n".format(item.name, item.amount, item.base))
        what = input(str(">You have {} Gold. What would you like to buy, or are you finished buying?".format(the_player.inventory[0].amount)))
        for mitems in merchant.items:
            if what.upper() == "FINISH":
                return
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

